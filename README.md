# Pocket-to-Bookmarks Converter

This Python script converts a Pocket export HTML file to a standard bookmarks file format. It extracts links from your Pocket export and creates a new HTML file compatible with most web browsers' bookmark import features.

## Features

- Parses Pocket export HTML files
- Extracts link information including title, URL, and time added
- Generates a new HTML file in standard bookmarks format
- Preserves the original "time added" information for each bookmark
- Provides informative logging throughout the conversion process

## Requirements

- Python 3.6+
- BeautifulSoup4

## Installation

1. Clone this repository or download the `pocket-to-bookmarks-html.py` file.
2. Install the required dependencies:

```
pip install beautifulsoup4
```

## Usage

Run the script from the command line, providing the input Pocket export file and the desired output file name:

```
python pocket-to-bookmarks-html.py input_pocket_export.html output_bookmarks.html
```

Replace `input_pocket_export.html` with the path to your Pocket export file, and `output_bookmarks.html` with your desired output file name.

## How It Works

1. The script parses the Pocket export HTML file using BeautifulSoup.
2. It extracts the title, URL, and time added for each link.
3. The extracted information is then formatted into a standard bookmarks HTML file.
4. The resulting file can be imported into most web browsers as bookmarks.

## Error Handling

- The script includes error handling for file reading and writing operations.
- Informative error messages are logged in case of any issues during the conversion process.

## Logging

The script uses Python's logging module to provide information about the conversion process, including:

- The number of links successfully converted
- Any errors encountered during file operations
- A warning if no links were found or processed

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

David Poblador i Garcia

---

For more information or support, please open an issue in the repository.
