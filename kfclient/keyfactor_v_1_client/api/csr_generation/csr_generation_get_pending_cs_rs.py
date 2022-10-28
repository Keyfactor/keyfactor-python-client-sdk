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
from ...models.csr_generation_get_pending_cs_rs_sq_sort_ascending import CSRGenerationGetPendingCSRsSqSortAscending
from ...models.models_pending_csr_response import ModelsPendingCSRResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sq_query_string: Union[Unset, None, str] = UNSET,
    sq_page_returned: Union[Unset, None, int] = UNSET,
    sq_return_limit: Union[Unset, None, int] = UNSET,
    sq_sort_field: Union[Unset, None, str] = UNSET,
    sq_sort_ascending: Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/CSRGeneration/Pending".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["sq.queryString"] = sq_query_string

    params["sq.pageReturned"] = sq_page_returned

    params["sq.returnLimit"] = sq_return_limit

    params["sq.sortField"] = sq_sort_field

    json_sq_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(sq_sort_ascending, Unset):
        json_sq_sort_ascending = sq_sort_ascending.value if sq_sort_ascending else None

    params["sq.sortAscending"] = json_sq_sort_ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ModelsPendingCSRResponse]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsPendingCSRResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ModelsPendingCSRResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sq_query_string: Union[Unset, None, str] = UNSET,
    sq_page_returned: Union[Unset, None, int] = UNSET,
    sq_return_limit: Union[Unset, None, int] = UNSET,
    sq_sort_field: Union[Unset, None, str] = UNSET,
    sq_sort_ascending: Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsPendingCSRResponse]]:
    """Returns a list of the currently pending CSRs according to the provided query

    Args:
        sq_query_string (Union[Unset, None, str]):
        sq_page_returned (Union[Unset, None, int]):
        sq_return_limit (Union[Unset, None, int]):
        sq_sort_field (Union[Unset, None, str]):
        sq_sort_ascending (Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsPendingCSRResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        sq_query_string=sq_query_string,
        sq_page_returned=sq_page_returned,
        sq_return_limit=sq_return_limit,
        sq_sort_field=sq_sort_field,
        sq_sort_ascending=sq_sort_ascending,
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
    sq_query_string: Union[Unset, None, str] = UNSET,
    sq_page_returned: Union[Unset, None, int] = UNSET,
    sq_return_limit: Union[Unset, None, int] = UNSET,
    sq_sort_field: Union[Unset, None, str] = UNSET,
    sq_sort_ascending: Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsPendingCSRResponse]]:
    """Returns a list of the currently pending CSRs according to the provided query

    Args:
        sq_query_string (Union[Unset, None, str]):
        sq_page_returned (Union[Unset, None, int]):
        sq_return_limit (Union[Unset, None, int]):
        sq_sort_field (Union[Unset, None, str]):
        sq_sort_ascending (Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsPendingCSRResponse]]
    """

    return sync_detailed(
        client=client,
        sq_query_string=sq_query_string,
        sq_page_returned=sq_page_returned,
        sq_return_limit=sq_return_limit,
        sq_sort_field=sq_sort_field,
        sq_sort_ascending=sq_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sq_query_string: Union[Unset, None, str] = UNSET,
    sq_page_returned: Union[Unset, None, int] = UNSET,
    sq_return_limit: Union[Unset, None, int] = UNSET,
    sq_sort_field: Union[Unset, None, str] = UNSET,
    sq_sort_ascending: Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsPendingCSRResponse]]:
    """Returns a list of the currently pending CSRs according to the provided query

    Args:
        sq_query_string (Union[Unset, None, str]):
        sq_page_returned (Union[Unset, None, int]):
        sq_return_limit (Union[Unset, None, int]):
        sq_sort_field (Union[Unset, None, str]):
        sq_sort_ascending (Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsPendingCSRResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        sq_query_string=sq_query_string,
        sq_page_returned=sq_page_returned,
        sq_return_limit=sq_return_limit,
        sq_sort_field=sq_sort_field,
        sq_sort_ascending=sq_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    sq_query_string: Union[Unset, None, str] = UNSET,
    sq_page_returned: Union[Unset, None, int] = UNSET,
    sq_return_limit: Union[Unset, None, int] = UNSET,
    sq_sort_field: Union[Unset, None, str] = UNSET,
    sq_sort_ascending: Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsPendingCSRResponse]]:
    """Returns a list of the currently pending CSRs according to the provided query

    Args:
        sq_query_string (Union[Unset, None, str]):
        sq_page_returned (Union[Unset, None, int]):
        sq_return_limit (Union[Unset, None, int]):
        sq_sort_field (Union[Unset, None, str]):
        sq_sort_ascending (Union[Unset, None, CSRGenerationGetPendingCSRsSqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsPendingCSRResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            sq_query_string=sq_query_string,
            sq_page_returned=sq_page_returned,
            sq_return_limit=sq_return_limit,
            sq_sort_field=sq_sort_field,
            sq_sort_ascending=sq_sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
