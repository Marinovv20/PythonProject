import csv

def load_addresses_from_csv(path, limit=5000):
    addresses = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            number = row.get("NUMBER", "").strip()
            street = row.get("STREET", "").strip()
            city = row.get("CITY", "").strip()
            region = row.get("REGION", "").strip()
            postcode = row.get("POSTCODE", "").strip()
            country = row.get("COUNTRY", "").strip()

            parts = [number, street, city, region, postcode, country]
            address = ", ".join([p for p in parts if p])
            if address:
                addresses.append(address)
            if len(addresses) >= limit:
                break
    return addresses
