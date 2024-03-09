# Zotero - Overleaf integration


## Introduction
This repository contains a Python script that allows you to retrieve collections from your Zotero library, with the ability to retrieve their sub-collections. The script will then combine all the references into a single BibTeX and return it as a plain text. This can be useful for importing your Zotero library reference collections with their sub-collections into Overleaf, as Overleaf does not have the ability to retrieve specific collections, nor does Zotero have the ability to export a collection with its sub-collections from its API (as far as I know).

## Requirements
- Python 3.11 or later
- Flask (for serving the web application)
- Docker (optional, for containerized deployment)
- A Zotero API Key ([Obtain here](https://www.zotero.org/settings/keys))
- Your Zotero User ID ([Find here](https://www.zotero.org/settings/keys))
- The Zotero Collection ID ([Find here](https://www.zotero.org/bishowb/library))

## Usage
1. Clone the repository (`git clone`)
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Run the script
```bash
python main.py
```

4. Open your browser and go to the given URL (e.g. `http://127.0.0.1:5000/` for testing purposes) for the web server

### Endpoints
- `/` - The main page
  
- `/fetch_bibtex` - The fetch page returns the BibTeX for the given collection. The following parameters are required:
    - `api_key` - Your Zotero API Key
    - `collection_key` - The collection ID you want to fetch
    - `user_id` - Your Zotero User ID
    - `include_subcollections` - `True` or `False` to include subcollections in the BibTeX or not



## Docker
You can also run the web server in a Docker container. To do so, run the docker compose file:
```bash
docker-compose up
```
This will build the image and run the container.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

