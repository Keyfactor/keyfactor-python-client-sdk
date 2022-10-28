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
from ...models.models_revocation_revocation_response import ModelsRevocationRevocationResponse
from ...models.models_revoke_all_certificates_request import ModelsRevokeAllCertificatesRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ModelsRevokeAllCertificatesRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Certificates/RevokeAll".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["collectionId"] = collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelsRevocationRevocationResponse]:
    if response.status_code == 200:
        response_200 = ModelsRevocationRevocationResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsRevocationRevocationResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ModelsRevokeAllCertificatesRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsRevocationRevocationResponse]:
    """Revokes the certificates associated with the provided query and Collection Id and associates the
    provided data with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description              |
    |-------------------|--------------------------|
    | -1                | Remove from hold         |
    | 0                 | Unspecified              |
    | 1                 | Key compromised          |
    | 2                 | CA compromised           |
    | 3                 | Affiliation changed      |
    | 4                 | Superceded               |
    | 5                 | Cessation of operation   |
    | 6                 | Certificate hold         |
    | 7                 | Remove from CRL          |
    | 999               | Unknown                  |

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsRevokeAllCertificatesRequest): Information for revoking all certifictes
            in a query

    Returns:
        Response[ModelsRevocationRevocationResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        collection_id=collection_id,
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
    json_body: ModelsRevokeAllCertificatesRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsRevocationRevocationResponse]:
    """Revokes the certificates associated with the provided query and Collection Id and associates the
    provided data with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description              |
    |-------------------|--------------------------|
    | -1                | Remove from hold         |
    | 0                 | Unspecified              |
    | 1                 | Key compromised          |
    | 2                 | CA compromised           |
    | 3                 | Affiliation changed      |
    | 4                 | Superceded               |
    | 5                 | Cessation of operation   |
    | 6                 | Certificate hold         |
    | 7                 | Remove from CRL          |
    | 999               | Unknown                  |

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsRevokeAllCertificatesRequest): Information for revoking all certifictes
            in a query

    Returns:
        Response[ModelsRevocationRevocationResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ModelsRevokeAllCertificatesRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsRevocationRevocationResponse]:
    """Revokes the certificates associated with the provided query and Collection Id and associates the
    provided data with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description              |
    |-------------------|--------------------------|
    | -1                | Remove from hold         |
    | 0                 | Unspecified              |
    | 1                 | Key compromised          |
    | 2                 | CA compromised           |
    | 3                 | Affiliation changed      |
    | 4                 | Superceded               |
    | 5                 | Cessation of operation   |
    | 6                 | Certificate hold         |
    | 7                 | Remove from CRL          |
    | 999               | Unknown                  |

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsRevokeAllCertificatesRequest): Information for revoking all certifictes
            in a query

    Returns:
        Response[ModelsRevocationRevocationResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: ModelsRevokeAllCertificatesRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsRevocationRevocationResponse]:
    """Revokes the certificates associated with the provided query and Collection Id and associates the
    provided data with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description              |
    |-------------------|--------------------------|
    | -1                | Remove from hold         |
    | 0                 | Unspecified              |
    | 1                 | Key compromised          |
    | 2                 | CA compromised           |
    | 3                 | Affiliation changed      |
    | 4                 | Superceded               |
    | 5                 | Cessation of operation   |
    | 6                 | Certificate hold         |
    | 7                 | Remove from CRL          |
    | 999               | Unknown                  |

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsRevokeAllCertificatesRequest): Information for revoking all certifictes
            in a query

    Returns:
        Response[ModelsRevocationRevocationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            collection_id=collection_id,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
