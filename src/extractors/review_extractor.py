import logging
from datetime import datetime

class ReviewExtractor:
    """Simulates extraction of review data."""

    def extract_reviews(self, keyword: str):
        logging.info(f"Simulating review extraction for keyword: {keyword}")
        return [
            {
                "Name": f"Reviewer for {keyword}",
                "Author": "John Doe",
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "ReviewTitle": "Sample Review",
                "Content": f"This is a simulated review about {keyword}.",
            }
        ]