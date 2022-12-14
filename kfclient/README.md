# keyfactor-v-1-client

A client library for accessing Keyfactor-v1

## Install

### Using pip
```bash
pip install keyfactor-v-1-client
```

### From source
```bash
git clone https://github.com/Keyfactor/keyfactor-python-client-sdk.git
cd keyfactor-python-client-sdk/kfclient
poetry install 
# Alternatively
python -m pip install .
```
## Config

### Using Environment Variables

```bash
export KEYFACTOR_HOSTNAME=<hostname> # e.g. https://keyfactor.example.com
export KEYFACTOR_USERNAME=<username> # e.g. admin
export KEYFACTOR_PASSWORD=<password> # e.g. password
export KEYFACTOR_DOMAIN=<domain>     # e.g. example.com
```

### Using a Config File

```bash
export KEYFACTOR_CONFIG=<path to config file> # e.g. /etc/keyfactor/config.json. Defaults to cwd "environment.json"
```

Sample Config:

```json
{
  "host": "<hostname>",
  "username": "<username>",
  "password": "<password>",
  "domain": "<domain>"
}
```

## Usage

First, create a client:

```python
from keyfactor_v_1_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from keyfactor_v_1_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from keyfactor_v_1_client.models import MyDataModel
from keyfactor_v_1_client.api.my_tag import get_my_data_model
from keyfactor_v_1_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from keyfactor_v_1_client.models import MyDataModel
from keyfactor_v_1_client.api.my_tag import get_my_data_model
from keyfactor_v_1_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate
verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially
an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl=False
)
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request
       was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `keyfactor_v_1_client.api.default`

## Building / publishing this Client

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging. Here are the basics:

1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI,
   just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:

1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
