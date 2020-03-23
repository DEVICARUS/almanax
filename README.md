<h1 align="center">Welcome to almanax 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.1.0-blue.svg?cacheSeconds=2592000" />
</p>

> Scrapes the official Krosmoz [Almanax](http://www.krosmoz.com/en/almanax) (Dofus and Wakfu portal) and serves the data as REST API.

**Currently supports only todays Dofus 2 offering and meridian info.**

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

### Dofus 2

Endpoint: `/api/dofus`

Response:
```json
{
   "meridian": "<Name of the meridian>",
   "bonus": {
      "name": "<Name of the bonus>",
      "description": "<Description of the bonus>"
   },
   "offering": {
      "name": "<Name of the required item>",
      "quantity": <Required quantity>,
      "image": "<Image of the item>", 
      "link": "<Link on game wiki>"
}
```

### Meridian

Endpoint: `/api/meridian`

Response:
```json
{
   "name": "<Name of the meridian>",
   "description": "<Description of the meridian>"
}
```