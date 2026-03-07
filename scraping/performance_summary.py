# scrape_performance_summary.py

import requests
from bs4 import BeautifulSoup
import csv
import re

URL = "https://www.mufap.com.pk/Industry/IndustryStatDaily?tab=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Fetching performance summary...")
response = requests.get(URL, headers=headers, timeout=60)
response.raise_for_status()
print(f"Status: {response.status_code}, Length: {len(response.text)}")

soup = BeautifulSoup(response.text, "html.parser")

# Find the main data table — look for the table with the expected headers
tables = soup.find_all("table")
print(f"Found {len(tables)} tables on page")

data_table = None
for table in tables:
    header_row = table.find("tr")
    if header_row and "Sector" in header_row.get_text() and "365 Days" in header_row.get_text():
        data_table = table
        break

if not data_table:
    print("ERROR: Could not find the performance data table!")
    print("Dumping all table headers for debugging:")
    for i, t in enumerate(tables):
        first_row = t.find("tr")
        if first_row:
            print(f"  Table {i}: {first_row.get_text()[:100]}")
    exit(1)

print("Found performance data table")

# Parse all rows
rows = data_table.find_all("tr")
print(f"Total rows in table: {len(rows)}")

funds = []
for row in rows[1:]:  # Skip header row
    cells = row.find_all("td")
    if len(cells) < 18:
        continue

    # Extract text from each cell, strip whitespace
    cell_texts = [c.get_text(strip=True) for c in cells]

    # Cell 0: Sector
    # Cell 1: Category
    # Cell 2: Fund Name (contains link with FundID)
    # Cell 3: Rating
    # Cell 4: Benchmark
    # Cell 5: Validity Date
    # Cell 6: NAV
    # Cell 7-17: Returns (YTD, MTD, 1D, 15D, 30D, 90D, 180D, 270D, 365D, 2Y, 3Y)

    # Extract FundID from the link in the fund name cell
    link = cells[2].find("a", href=re.compile(r"FundID=\d+"))
    fund_id = ""
    if link:
        match = re.search(r"FundID=(\d+)", link.get("href", ""))
        if match:
            fund_id = match.group(1)

    # Clean category — MUFAP appends "(Annualized Return )" to some categories
    category = cell_texts[1]
    category = re.sub(r"\s*\(Annualized Return\s*\)\s*", "", category).strip()
    category = re.sub(r"\s*\(Absolute Return\s*\)\s*", "", category).strip()

    # Clean return values — replace N/A with empty, handle commas
    def clean_number(val):
        val = val.strip()
        if val in ("N/A", "n/a", "-", "", "Nil"):
            return ""
        val = val.replace(",", "")
        try:
            float(val)
            return val
        except ValueError:
            return ""

    fund = {
        "fund_id": fund_id,
        "fund_name": cell_texts[2],
        "sector": cell_texts[0],
        "category_mufap": category,
        "rating": cell_texts[3] if cell_texts[3] not in ("N/A", "-") else "",
        "benchmark": cell_texts[4] if cell_texts[4] not in ("N/A", "Nil", "-") else "",
        "validity_date": cell_texts[5],
        "nav": clean_number(cell_texts[6]),
        "return_ytd_pct": clean_number(cell_texts[7]),
        "return_mtd_pct": clean_number(cell_texts[8]),
        "return_1d_pct": clean_number(cell_texts[9]),
        "return_15d_pct": clean_number(cell_texts[10]),
        "return_30d_pct": clean_number(cell_texts[11]),
        "return_90d_pct": clean_number(cell_texts[12]),
        "return_180d_pct": clean_number(cell_texts[13]),
        "return_270d_pct": clean_number(cell_texts[14]),
        "return_365d_pct": clean_number(cell_texts[15]),
        "return_2y_pct": clean_number(cell_texts[16]),
        "return_3y_pct": clean_number(cell_texts[17]),
    }

    funds.append(fund)

print(f"\nExtracted {len(funds)} funds")

# Preview
for f in funds[:3]:
    print(f"  {f['fund_id']}: {f['fund_name']} | {f['category_mufap']} | 1Y: {f['return_365d_pct']}%")

# Save
output_file = "data/performance_summary.csv"
fieldnames = [
    "fund_id", "fund_name", "sector", "category_mufap", "rating", "benchmark",
    "validity_date", "nav", "return_ytd_pct", "return_mtd_pct", "return_1d_pct",
    "return_15d_pct", "return_30d_pct", "return_90d_pct", "return_180d_pct",
    "return_270d_pct", "return_365d_pct", "return_2y_pct", "return_3y_pct"
]

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(funds)

print(f"\nSaved to {output_file}")
print(f"Total funds: {len(funds)}")

# Quick stats
non_empty_1y = sum(1 for f in funds if f["return_365d_pct"])
non_empty_3y = sum(1 for f in funds if f["return_3y_pct"])
print(f"Funds with 1Y return: {non_empty_1y}")
print(f"Funds with 3Y return: {non_empty_3y}")