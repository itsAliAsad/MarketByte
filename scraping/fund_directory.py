# scrape_fund_directory.py

import requests
from bs4 import BeautifulSoup
import csv
import re
import time

BASE_URL = "https://www.mufap.com.pk"
DIRECTORY_URL = f"{BASE_URL}/FundProfile/FundDirectory"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Fetching fund directory page...")
response = requests.get(DIRECTORY_URL, headers=headers, timeout=30)
response.raise_for_status()
print(f"Status: {response.status_code}, Content length: {len(response.text)}")

soup = BeautifulSoup(response.text, "html.parser")

# Find all "View Details" links — each one = one fund
detail_links = soup.find_all("a", href=re.compile(r"/FundProfile/FundDetail\?FundID=\d+"))
print(f"Found {len(detail_links)} fund detail links")

# Now we need to extract fund data from each card.
# The structure from the page shows each fund is in a table row
# with the fund info in the first cell and metadata in other cells.
# Let's find all table rows that contain fund data.

funds = []
rows = soup.find_all("tr")

for row in rows:
    # Look for rows that have a View Details link
    link = row.find("a", href=re.compile(r"/FundProfile/FundDetail\?FundID=\d+"))
    if not link:
        continue
    
    # Extract FundID from link
    href = link.get("href", "")
    fund_id_match = re.search(r"FundID=(\d+)", href)
    if not fund_id_match:
        continue
    fund_id = fund_id_match.group(1)
    
    # Get all text content from the row
    cells = row.find_all("td")
    if len(cells) < 4:
        continue
    
    # Cell 0: Contains fund name, AMC, NAV, offer price, category, risk
    card_text = cells[0].get_text(separator="|", strip=True)
    
    # Cell 1: Sector (Open-End Funds, VPS, etc.)
    sector = cells[1].get_text(strip=True) if len(cells) > 1 else ""
    
    # Cell 2: AMC Name
    amc_name = cells[2].get_text(strip=True) if len(cells) > 2 else ""
    
    # Cell 3: Category
    category = cells[3].get_text(strip=True) if len(cells) > 3 else ""
    
    # Parse the card text to extract structured fields
    # Pattern: "Logo|FundName|AMCName|NAV_value|NAV|OfferPrice_value|Offer Price|Category_value|Category|RiskProfile|Risk Profile|View Details"
    parts = [p.strip() for p in card_text.split("|") if p.strip()]
    
    # Extract fund name - it's typically the first meaningful text after "Logo"
    fund_name = ""
    nav = ""
    offer_price = ""
    risk_profile = ""
    
    # Strategy: find the text segments
    for i, part in enumerate(parts):
        if part == "NAV" and i > 0:
            nav = parts[i-1]
        if part == "Offer Price" and i > 0:
            offer_price = parts[i-1]
        if part == "Risk Profile" and i > 0:
            risk_profile = parts[i-1]
        if part == "Category" and i > 0:
            # The category from the card (redundant with cell[3] but useful as backup)
            pass
    
    # Fund name: usually parts[1] if parts[0] is "Logo", 
    # but could also be parts[0] if no logo text
    if parts:
        if parts[0] == "Logo" and len(parts) > 1:
            fund_name = parts[1]
        elif parts[0] != "Logo":
            fund_name = parts[0]
    
    # Clean AMC from fund name if it got concatenated
    if amc_name and fund_name.endswith(amc_name):
        fund_name = fund_name[:-len(amc_name)].strip()
    
    funds.append({
        "fund_id": fund_id,
        "fund_name": fund_name,
        "amc_name": amc_name,
        "sector": sector,
        "category_mufap": category,
        "risk_profile": risk_profile,
        "nav": nav,
        "offer_price": offer_price,
    })

print(f"\nExtracted {len(funds)} funds")

# Preview first 5
for f in funds[:5]:
    print(f"  {f['fund_id']}: {f['fund_name']} | {f['category_mufap']} | NAV: {f['nav']}")

# Save to CSV
output_file = "data/fund_directory.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "fund_id", "fund_name", "amc_name", "sector", 
        "category_mufap", "risk_profile", "nav", "offer_price"
    ])
    writer.writeheader()
    writer.writerows(funds)

print(f"\nSaved to {output_file}")
print(f"Total funds: {len(funds)}")

# Print category breakdown
from collections import Counter
cats = Counter(f["category_mufap"] for f in funds)
print("\nCategory breakdown:")
for cat, count in cats.most_common():
    print(f"  {cat}: {count}")