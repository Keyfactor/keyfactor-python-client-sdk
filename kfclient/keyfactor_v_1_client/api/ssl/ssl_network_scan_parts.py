# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.models_ssl_display_scan_job_part import ModelsSSLDisplayScanJobPart
from ...models.ssl_network_scan_parts_paged_query_job_type import SslNetworkScanPartsPagedQueryJobType
from ...models.ssl_network_scan_parts_paged_query_sort_ascending import SslNetworkScanPartsPagedQuerySortAscending
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    paged_query_job_type: Union[Unset, None, SslNetworkScanPartsPagedQueryJobType] = UNSET,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, SslNetworkScanPartsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/SSL/Networks/{id}/Parts".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    json_paged_query_job_type: Union[Unset, None, int] = UNSET
    if not isinstance(paged_query_job_type, Unset):
        json_paged_query_job_type = paged_query_job_type.value if paged_query_job_type else None

    params["pagedQuery.jobType"] = json_paged_query_job_type

    params["pagedQuery.queryString"] = paged_query_query_string

    params["pagedQuery.pageReturned"] = paged_query_page_returned

    params["pagedQuery.returnLimit"] = paged_query_return_limit

    params["pagedQuery.sortField"] = paged_query_sort_field

    json_paged_query_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(paged_query_sort_ascending, Unset):
        json_paged_query_sort_ascending = paged_query_sort_ascending.value if paged_query_sort_ascending else None

    params["pagedQuery.sortAscending"] = json_paged_query_sort_ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ModelsSSLDisplayScanJobPart]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsSSLDisplayScanJobPart.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ModelsSSLDisplayScanJobPart]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    paged_query_job_type: Union[Unset, None, SslNetworkScanPartsPagedQueryJobType] = UNSET,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, SslNetworkScanPartsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsSSLDisplayScanJobPart]]:
    """Returns the scan job components comprising the entire scan job to be executed

    Args:
        id (str):
        paged_query_job_type (Union[Unset, None, SslNetworkScanPartsPagedQueryJobType]):
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            SslNetworkScanPartsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsSSLDisplayScanJobPart]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        paged_query_job_type=paged_query_job_type,
        paged_query_query_string=paged_query_query_string,
        paged_query_page_returned=paged_query_page_returned,
        paged_query_return_limit=paged_query_return_limit,
        paged_query_sort_field=paged_query_sort_field,
        paged_query_sort_ascending=paged_query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    paged_query_job_type: Union[Unset, None, SslNetworkScanPartsPagedQueryJobType] = UNSET,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, SslNetworkScanPartsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsSSLDisplayScanJobPart]]:
    """Returns the scan job components comprising the entire scan job to be executed

    Args:
        id (str):
        paged_query_job_type (Union[Unset, None, SslNetworkScanPartsPagedQueryJobType]):
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            SslNetworkScanPartsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsSSLDisplayScanJobPart]]
    """

    return sync_detailed(
        id=id,
        client=client,
        paged_query_job_type=paged_query_job_type,
        paged_query_query_string=paged_query_query_string,
        paged_query_page_returned=paged_query_page_returned,
        paged_query_return_limit=paged_query_return_limit,
        paged_query_sort_field=paged_query_sort_field,
        paged_query_sort_ascending=paged_query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    paged_query_job_type: Union[Unset, None, SslNetworkScanPartsPagedQueryJobType] = UNSET,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, SslNetworkScanPartsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsSSLDisplayScanJobPart]]:
    """Returns the scan job components comprising the entire scan job to be executed

    Args:
        id (str):
        paged_query_job_type (Union[Unset, None, SslNetworkScanPartsPagedQueryJobType]):
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            SslNetworkScanPartsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsSSLDisplayScanJobPart]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        paged_query_job_type=paged_query_job_type,
        paged_query_query_string=paged_query_query_string,
        paged_query_page_returned=paged_query_page_returned,
        paged_query_return_limit=paged_query_return_limit,
        paged_query_sort_field=paged_query_sort_field,
        paged_query_sort_ascending=paged_query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    paged_query_job_type: Union[Unset, None, SslNetworkScanPartsPagedQueryJobType] = UNSET,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, SslNetworkScanPartsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsSSLDisplayScanJobPart]]:
    """Returns the scan job components comprising the entire scan job to be executed

    Args:
        id (str):
        paged_query_job_type (Union[Unset, None, SslNetworkScanPartsPagedQueryJobType]):
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            SslNetworkScanPartsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsSSLDisplayScanJobPart]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            paged_query_job_type=paged_query_job_type,
            paged_query_query_string=paged_query_query_string,
            paged_query_page_returned=paged_query_page_returned,
            paged_query_return_limit=paged_query_return_limit,
            paged_query_sort_field=paged_query_sort_field,
            paged_query_sort_ascending=paged_query_sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
