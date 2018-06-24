# Pastebin Scraper

Simple library to interact with the Pastebin's scraping API.

## Installation

To install this library just run the follwoing command:

```python
pip install git+ssh://git@github.com/0bscurec0de/pastebin_scraper.git
```
## Example usage

```python
from pastebin_scraper import pastebin_scrapper

# Get last pastes
pastebin_scrapper.get_pastes_list()
pastebin_scrapper.get_pastes_list(limit=50)
pastebin_scrapper.get_pastes_list(language='python')
pastebin_scrapper.get_pastes_list(limit=50, language='python')

# Get paste's content in memory
pastebin_scrapper.get_paste_raw(paste_key='paste_key')

# Get paste's metadata
pastebin_scrapper.get_paste_metadata(paste_key='paste_key')

# Download paste
pastebin_scrapper.download_paste(paste_key='paste_key', file_path='/path/to/save/')

# Get supported languages
pastebin_scrapper.get_supported_languages()
```

## Version  history

* 0.1.0:
    * First release
    * Get list of last pastes
    * Get pastes' metadata and content
    * Download pastes to disk
