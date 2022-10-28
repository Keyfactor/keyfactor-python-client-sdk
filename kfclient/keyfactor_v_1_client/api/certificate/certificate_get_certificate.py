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
from ...models.models_certificate_retrieval_response import ModelsCertificateRetrievalResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Certificates/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["includeLocations"] = include_locations

    params["includeMetadata"] = include_metadata

    params["collectionId"] = collection_id

    params["verbose"] = verbose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelsCertificateRetrievalResponse]:
    if response.status_code == 200:
        response_200 = ModelsCertificateRetrievalResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsCertificateRetrievalResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsCertificateRetrievalResponse]:
    """Returns a single certificate that matches the id

    Args:
        id (int):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        collection_id (Union[Unset, None, int]):
        verbose (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsCertificateRetrievalResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        include_locations=include_locations,
        include_metadata=include_metadata,
        collection_id=collection_id,
        verbose=verbose,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: Client,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsCertificateRetrievalResponse]:
    """Returns a single certificate that matches the id

    Args:
        id (int):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        collection_id (Union[Unset, None, int]):
        verbose (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsCertificateRetrievalResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        include_locations=include_locations,
        include_metadata=include_metadata,
        collection_id=collection_id,
        verbose=verbose,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsCertificateRetrievalResponse]:
    """Returns a single certificate that matches the id

    Args:
        id (int):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        collection_id (Union[Unset, None, int]):
        verbose (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsCertificateRetrievalResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        include_locations=include_locations,
        include_metadata=include_metadata,
        collection_id=collection_id,
        verbose=verbose,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsCertificateRetrievalResponse]:
    """Returns a single certificate that matches the id

    Args:
        id (int):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        collection_id (Union[Unset, None, int]):
        verbose (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsCertificateRetrievalResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_locations=include_locations,
            include_metadata=include_metadata,
            collection_id=collection_id,
            verbose=verbose,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
