# Wikipedia-API

API was developed in Flask with the aim of performing searches on Wikipedia and returning this content in JSON

## Routers

API Routes:

| URL | Methods | Description |
| -------- | ------------- | --------- |
| `/api/v1/search=&lang=` | GET | Searches for questions on Wikipedia and returns JSON |

Parameters:

| Parameters | Value type | Default | Mandatory | Description |
| -------- | ------------- | ---------- | --------- | --------- |
| search | str | null | Yes | Question |
| lang | str | null | Yes | Search Language |

Example:

`api-wikipedia.herokuapp.com/api/v1/search=Google&lang=pt`
