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
from ...models.models_orchestrator_jobs_job import ModelsOrchestratorJobsJob
from ...models.orchestrator_job_get_scheduled_jobs_pq_sort_ascending import (
    OrchestratorJobGetScheduledJobsPqSortAscending,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/OrchestratorJobs/ScheduledJobs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["pq.queryString"] = pq_query_string

    params["pq.pageReturned"] = pq_page_returned

    params["pq.returnLimit"] = pq_return_limit

    params["pq.sortField"] = pq_sort_field

    json_pq_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(pq_sort_ascending, Unset):
        json_pq_sort_ascending = pq_sort_ascending.value if pq_sort_ascending else None

    params["pq.sortAscending"] = json_pq_sort_ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ModelsOrchestratorJobsJob]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsOrchestratorJobsJob.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ModelsOrchestratorJobsJob]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsOrchestratorJobsJob]]:
    """Returns all scheduled orchestrator jobs according to the provided filter and output parameters

    Args:
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsOrchestratorJobsJob]]
    """

    kwargs = _get_kwargs(
        client=client,
        pq_query_string=pq_query_string,
        pq_page_returned=pq_page_returned,
        pq_return_limit=pq_return_limit,
        pq_sort_field=pq_sort_field,
        pq_sort_ascending=pq_sort_ascending,
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
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsOrchestratorJobsJob]]:
    """Returns all scheduled orchestrator jobs according to the provided filter and output parameters

    Args:
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsOrchestratorJobsJob]]
    """

    return sync_detailed(
        client=client,
        pq_query_string=pq_query_string,
        pq_page_returned=pq_page_returned,
        pq_return_limit=pq_return_limit,
        pq_sort_field=pq_sort_field,
        pq_sort_ascending=pq_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsOrchestratorJobsJob]]:
    """Returns all scheduled orchestrator jobs according to the provided filter and output parameters

    Args:
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsOrchestratorJobsJob]]
    """

    kwargs = _get_kwargs(
        client=client,
        pq_query_string=pq_query_string,
        pq_page_returned=pq_page_returned,
        pq_return_limit=pq_return_limit,
        pq_sort_field=pq_sort_field,
        pq_sort_ascending=pq_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsOrchestratorJobsJob]]:
    """Returns all scheduled orchestrator jobs according to the provided filter and output parameters

    Args:
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, OrchestratorJobGetScheduledJobsPqSortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsOrchestratorJobsJob]]
    """

    return (
        await asyncio_detailed(
            client=client,
            pq_query_string=pq_query_string,
            pq_page_returned=pq_page_returned,
            pq_return_limit=pq_return_limit,
            pq_sort_field=pq_sort_field,
            pq_sort_ascending=pq_sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
