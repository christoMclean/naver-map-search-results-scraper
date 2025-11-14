import logging

class NaverMapParser:
    """Simulated parser representing business listing extraction."""

    def parse_listing(self, keyword: str) -> dict:
        logging.info(f"Simulating listing parse for keyword: {keyword}")
        return {
            "Name": f"Sample Business for {keyword}",
            "Category": "Restaurant",
            "BusinessStatus": "Open",
            "OverallRating": 4.5,
            "ReviewCount": 10,
            "Address": "123 Sample Street",
            "NearbyTransportation": "Metro Station 200m",
            "BusinessHours": "09:00 - 21:00",
            "Contact": "000-000-0000",
            "Website": "https://example.com",
            "Amenities": ["WiFi", "Parking"],
            "TVAppearance": "None",
            "Description": f"This is a simulated business description for {keyword}.",
        }