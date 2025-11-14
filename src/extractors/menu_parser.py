import logging

class MenuParser:
    """Simulates extraction of menu items."""

    def parse_menu(self, keyword: str):
        logging.info(f"Simulating menu extraction for keyword: {keyword}")
        return [
            {
                "name": f"Sample Dish ({keyword})",
                "price": "10000",
                "images": ["https://example.com/sample.jpg"],
            }
        ]