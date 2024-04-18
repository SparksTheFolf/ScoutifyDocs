Generate API Keys for a Given Username
======================================

This route generates API keys for a given username and team number.

HTTP Method: ``GET``
Path: ``/:teamNum/:username``

Request Parameters
------------------

- ``teamNum``: The team number.
- ``username``: The username for which API keys are generated.

Response
--------

The response contains a JSON object with the following fields:

- ``comment``: A comment stating that the generated API key is in DEV mode and not valid for production use.
- ``key``:
    - ``username``: The username.
    - ``UUID``: A unique identifier.
    - ``teamNum``: The team number in the format "frc" + team number.
    - ``apiKey``: The generated API key.
    - ``timestamp``: The timestamp of the key generation.

Example Request
---------------

```http
GET /1234/johndoe
