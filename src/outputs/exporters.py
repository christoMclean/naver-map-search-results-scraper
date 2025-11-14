import json
import logging
from pathlib import Path

class JSONExporter:
    """Exports scraped results into a JSON file."""

    def export(self, data, file_path: Path):
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logging.info(f"JSON exported to {file_path}")
        except Exception as e:
            logging.error(f"Failed to export JSON: {e}")