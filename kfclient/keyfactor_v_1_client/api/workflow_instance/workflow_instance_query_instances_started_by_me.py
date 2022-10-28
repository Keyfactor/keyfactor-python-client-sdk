from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_workflows_instance_query_response import (
    KeyfactorApiModelsWorkflowsInstanceQueryResponse,
)
from ...models.workflow_instance_query_instances_started_by_me_instance_query_sort_ascending import (
    WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    instance_query_query_string: Union[Unset, None, str] = UNSET,
    instance_query_page_returned: Union[Unset, None, int] = UNSET,
    instance_query_return_limit: Union[Unset, None, int] = UNSET,
    instance_query_sort_field: Union[Unset, None, str] = UNSET,
    instance_query_sort_ascending: Union[
        Unset, None, WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending
    ] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Workflow/Instances/My".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["instanceQuery.queryString"] = instance_query_query_string

    params["instanceQuery.pageReturned"] = instance_query_page_returned

    params["instanceQuery.returnLimit"] = instance_query_return_limit

    params["instanceQuery.sortField"] = instance_query_sort_field

    json_instance_query_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(instance_query_sort_ascending, Unset):
        json_instance_query_sort_ascending = (
            instance_query_sort_ascending.value if instance_query_sort_ascending else None
        )

    params["instanceQuery.sortAscending"] = json_instance_query_sort_ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KeyfactorApiModelsWorkflowsInstanceQueryResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    instance_query_query_string: Union[Unset, None, str] = UNSET,
    instance_query_page_returned: Union[Unset, None, int] = UNSET,
    instance_query_return_limit: Union[Unset, None, int] = UNSET,
    instance_query_sort_field: Union[Unset, None, str] = UNSET,
    instance_query_sort_ascending: Union[
        Unset, None, WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending
    ] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]:
    """Gets the workflow instances started by the user.

    Args:
        instance_query_query_string (Union[Unset, None, str]):
        instance_query_page_returned (Union[Unset, None, int]):
        instance_query_return_limit (Union[Unset, None, int]):
        instance_query_sort_field (Union[Unset, None, str]):
        instance_query_sort_ascending (Union[Unset, None,
            WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        instance_query_query_string=instance_query_query_string,
        instance_query_page_returned=instance_query_page_returned,
        instance_query_return_limit=instance_query_return_limit,
        instance_query_sort_field=instance_query_sort_field,
        instance_query_sort_ascending=instance_query_sort_ascending,
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
    instance_query_query_string: Union[Unset, None, str] = UNSET,
    instance_query_page_returned: Union[Unset, None, int] = UNSET,
    instance_query_return_limit: Union[Unset, None, int] = UNSET,
    instance_query_sort_field: Union[Unset, None, str] = UNSET,
    instance_query_sort_ascending: Union[
        Unset, None, WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending
    ] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]:
    """Gets the workflow instances started by the user.

    Args:
        instance_query_query_string (Union[Unset, None, str]):
        instance_query_page_returned (Union[Unset, None, int]):
        instance_query_return_limit (Union[Unset, None, int]):
        instance_query_sort_field (Union[Unset, None, str]):
        instance_query_sort_ascending (Union[Unset, None,
            WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]
    """

    return sync_detailed(
        client=client,
        instance_query_query_string=instance_query_query_string,
        instance_query_page_returned=instance_query_page_returned,
        instance_query_return_limit=instance_query_return_limit,
        instance_query_sort_field=instance_query_sort_field,
        instance_query_sort_ascending=instance_query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    instance_query_query_string: Union[Unset, None, str] = UNSET,
    instance_query_page_returned: Union[Unset, None, int] = UNSET,
    instance_query_return_limit: Union[Unset, None, int] = UNSET,
    instance_query_sort_field: Union[Unset, None, str] = UNSET,
    instance_query_sort_ascending: Union[
        Unset, None, WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending
    ] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]:
    """Gets the workflow instances started by the user.

    Args:
        instance_query_query_string (Union[Unset, None, str]):
        instance_query_page_returned (Union[Unset, None, int]):
        instance_query_return_limit (Union[Unset, None, int]):
        instance_query_sort_field (Union[Unset, None, str]):
        instance_query_sort_ascending (Union[Unset, None,
            WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        instance_query_query_string=instance_query_query_string,
        instance_query_page_returned=instance_query_page_returned,
        instance_query_return_limit=instance_query_return_limit,
        instance_query_sort_field=instance_query_sort_field,
        instance_query_sort_ascending=instance_query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    instance_query_query_string: Union[Unset, None, str] = UNSET,
    instance_query_page_returned: Union[Unset, None, int] = UNSET,
    instance_query_return_limit: Union[Unset, None, int] = UNSET,
    instance_query_sort_field: Union[Unset, None, str] = UNSET,
    instance_query_sort_ascending: Union[
        Unset, None, WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending
    ] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]:
    """Gets the workflow instances started by the user.

    Args:
        instance_query_query_string (Union[Unset, None, str]):
        instance_query_page_returned (Union[Unset, None, int]):
        instance_query_return_limit (Union[Unset, None, int]):
        instance_query_sort_field (Union[Unset, None, str]):
        instance_query_sort_ascending (Union[Unset, None,
            WorkflowInstanceQueryInstancesStartedByMeInstanceQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsWorkflowsInstanceQueryResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            instance_query_query_string=instance_query_query_string,
            instance_query_page_returned=instance_query_page_returned,
            instance_query_return_limit=instance_query_return_limit,
            instance_query_sort_field=instance_query_sort_field,
            instance_query_sort_ascending=instance_query_sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed