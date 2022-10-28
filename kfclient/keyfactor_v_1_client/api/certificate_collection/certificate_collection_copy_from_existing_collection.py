# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_certificate_collections_certificate_collection_copy_request import (
    KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest,
)
from ...models.keyfactor_api_models_certificate_collections_certificate_collection_response import (
    KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse,
)
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/CertificateCollections/Copy".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]:
    if response.status_code == 200:
        response_200 = KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]:
    """Creates a new certificate collection from an existing collection. The permissions, query and
    description of the
    existing collection are copied when creating the new record, with the option to overwrite the query
    or description.

     ### Duplication Field Values ###
    The field used to determine if a certificate is a duplicate of another.
    | Value              | Description               |
    |--------------------|---------------------------|
    | 1                  | Common name               |
    | 2                  | Distinguished name        |
    | 3                  | Principal name            |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest):

    Returns:
        Response[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]:
    """Creates a new certificate collection from an existing collection. The permissions, query and
    description of the
    existing collection are copied when creating the new record, with the option to overwrite the query
    or description.

     ### Duplication Field Values ###
    The field used to determine if a certificate is a duplicate of another.
    | Value              | Description               |
    |--------------------|---------------------------|
    | 1                  | Common name               |
    | 2                  | Distinguished name        |
    | 3                  | Principal name            |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest):

    Returns:
        Response[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]:
    """Creates a new certificate collection from an existing collection. The permissions, query and
    description of the
    existing collection are copied when creating the new record, with the option to overwrite the query
    or description.

     ### Duplication Field Values ###
    The field used to determine if a certificate is a duplicate of another.
    | Value              | Description               |
    |--------------------|---------------------------|
    | 1                  | Common name               |
    | 2                  | Distinguished name        |
    | 3                  | Principal name            |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest):

    Returns:
        Response[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]:
    """Creates a new certificate collection from an existing collection. The permissions, query and
    description of the
    existing collection are copied when creating the new record, with the option to overwrite the query
    or description.

     ### Duplication Field Values ###
    The field used to determine if a certificate is a duplicate of another.
    | Value              | Description               |
    |--------------------|---------------------------|
    | 1                  | Common name               |
    | 2                  | Distinguished name        |
    | 3                  | Principal name            |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest):

    Returns:
        Response[KeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
