import argparse
import logging
from pathlib import Path
from typing import Dict, List

from bs4 import BeautifulSoup


def parse_pocket_export(file_path: Path) -> List[Dict[str, str]]:
    """
    Parse the Pocket export HTML file and extract links with time_added.

    Args:
        file_path (Path): Path to the Pocket export HTML file.

    Returns:
        List[Dict[str, str]]: List of dictionaries containing link information.
    """
    try:
        with file_path.open("r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
    except IOError as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return []

    links = soup.find_all("a")
    return [
        {
            "title": link.text.strip(),
            "url": link.get("href", ""),
            "time_added": link.get("time_added", ""),
        }
        for link in links
    ]


def write_to_bookmark_file(
    pocket_links: List[Dict[str, str]], output_file_path: Path
) -> None:
    """
    Write pocket links to a bookmark file using a template.

    Args:
        pocket_links (List[Dict[str, str]]): List of dictionaries containing
                                             link information.
        output_file_path (Path): Path to the output bookmark file.
    """
    bookmark_template = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
{bookmark_entries}
</DL><p>
"""

    bookmark_entry_template = (
        '<DT><A HREF="{url}" ADD_DATE="{time_added}" '
        'LAST_VISIT="" LAST_MODIFIED="">{title}</A>\n'
    )

    try:
        bookmark_entries = "".join(
            bookmark_entry_template.format(
                url=link["url"], time_added=link["time_added"], title=link["title"]
            )
            for link in pocket_links
        )

        formatted_bookmarks = bookmark_template.format(
            bookmark_entries=bookmark_entries
        )

        with output_file_path.open("w", encoding="utf-8") as file:
            file.write(formatted_bookmarks)
    except IOError as e:
        logging.error(f"Error writing to file {output_file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Pocket export to bookmarks file"
    )
    parser.add_argument(
        "input_file", type=Path, help="Path to the Pocket export HTML file"
    )
    parser.add_argument(
        "output_file", type=Path, help="Path to the output bookmark file"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    pocket_links = parse_pocket_export(args.input_file)
    if pocket_links:
        write_to_bookmark_file(pocket_links, args.output_file)
        logging.info(
            f"Successfully converted {len(pocket_links)} links "
            f"to {args.output_file}"
        )
    else:
        logging.warning("No links were found or processed")


if __name__ == "__main__":
    main()
