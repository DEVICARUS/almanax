<h1 align="center">Welcome to almanax 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> Scrapes the official Krosmoz [Almanax](http://www.krosmoz.com/en/almanax) (Dofus and Wakfu portal) and serves the data as REST API.

**Currently supports only todays Dofus 2 offering.**

## Requirements
- Python 3

## Usage

1. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

2. Run
   ```sh
   gunicorn main:app
   ```

## API

Endpoint: `/api`

Response:
```json
{
   "meridian": "<Name of the meridian>",
   "offering": {
      "name": "<Name of the required item>",
      "quantity": "<Required quantity>",
      "image": "<Image of the item>", 
      "link": "<Link on game wiki>"
}
```