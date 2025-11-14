import json
import logging
from pathlib import Path
from extractors.naver_map_parser import NaverMapParser
from extractors.review_extractor import ReviewExtractor
from extractors.menu_parser import MenuParser
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def load_input_keywords(file_path: Path):
    if not file_path.exists():
        logging.error(f"Input file not found: {file_path}")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def main():
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "data" / "inputs.sample.txt"
    output_file = base_dir / "data" / "sample.json"

    keywords = load_input_keywords(input_file)
    if not keywords:
        logging.warning("No keywords provided. Exiting.")
        return

    parser = NaverMapParser()
    review_extractor = ReviewExtractor()
    menu_parser = MenuParser()
    exporter = JSONExporter()

    results = []

    for kw in keywords:
        logging.info(f"Processing keyword: {kw}")
        listing = parser.parse_listing(kw)

        listing["Reviews"] = review_extractor.extract_reviews(kw)
        listing["MenuItems"] = menu_parser.parse_menu(kw)
        listing["SearchKeyword"] = kw

        results.append(listing)

    exporter.export(results, output_file)
    logging.info(f"Export complete: {output_file}")

if __name__ == "__main__":
    main()