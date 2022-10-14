from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_alerts_pending_pending_alert_definition_response import (
    KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse,
)
from ...models.pending_alert_get_pending_alerts_paged_query_sort_ascending import (
    PendingAlertGetPendingAlertsPagedQuerySortAscending,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, PendingAlertGetPendingAlertsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Alerts/Pending".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, PendingAlertGetPendingAlertsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]:
    """Gets all pending alerts according to the provided filter and output parameters

    Args:
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            PendingAlertGetPendingAlertsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
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
    *,
    client: Client,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, PendingAlertGetPendingAlertsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]:
    """Gets all pending alerts according to the provided filter and output parameters

    Args:
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            PendingAlertGetPendingAlertsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]
    """

    return sync_detailed(
        client=client,
        paged_query_query_string=paged_query_query_string,
        paged_query_page_returned=paged_query_page_returned,
        paged_query_return_limit=paged_query_return_limit,
        paged_query_sort_field=paged_query_sort_field,
        paged_query_sort_ascending=paged_query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, PendingAlertGetPendingAlertsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]:
    """Gets all pending alerts according to the provided filter and output parameters

    Args:
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            PendingAlertGetPendingAlertsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
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
    *,
    client: Client,
    paged_query_query_string: Union[Unset, None, str] = UNSET,
    paged_query_page_returned: Union[Unset, None, int] = UNSET,
    paged_query_return_limit: Union[Unset, None, int] = UNSET,
    paged_query_sort_field: Union[Unset, None, str] = UNSET,
    paged_query_sort_ascending: Union[Unset, None, PendingAlertGetPendingAlertsPagedQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]:
    """Gets all pending alerts according to the provided filter and output parameters

    Args:
        paged_query_query_string (Union[Unset, None, str]):
        paged_query_page_returned (Union[Unset, None, int]):
        paged_query_return_limit (Union[Unset, None, int]):
        paged_query_sort_field (Union[Unset, None, str]):
        paged_query_sort_ascending (Union[Unset, None,
            PendingAlertGetPendingAlertsPagedQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            paged_query_query_string=paged_query_query_string,
            paged_query_page_returned=paged_query_page_returned,
            paged_query_return_limit=paged_query_return_limit,
            paged_query_sort_field=paged_query_sort_field,
            paged_query_sort_ascending=paged_query_sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
