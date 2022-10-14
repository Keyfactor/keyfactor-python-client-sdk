from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.models_report import ModelsReport
from ...models.reports_query_reports_query_sort_ascending import ReportsQueryReportsQuerySortAscending
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    query_query_string: Union[Unset, None, str] = UNSET,
    query_page_returned: Union[Unset, None, int] = UNSET,
    query_return_limit: Union[Unset, None, int] = UNSET,
    query_sort_field: Union[Unset, None, str] = UNSET,
    query_sort_ascending: Union[Unset, None, ReportsQueryReportsQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Reports".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["query.queryString"] = query_query_string

    params["query.pageReturned"] = query_page_returned

    params["query.returnLimit"] = query_return_limit

    params["query.sortField"] = query_sort_field

    json_query_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(query_sort_ascending, Unset):
        json_query_sort_ascending = query_sort_ascending.value if query_sort_ascending else None

    params["query.sortAscending"] = json_query_sort_ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ModelsReport]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsReport.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ModelsReport]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    query_query_string: Union[Unset, None, str] = UNSET,
    query_page_returned: Union[Unset, None, int] = UNSET,
    query_return_limit: Union[Unset, None, int] = UNSET,
    query_sort_field: Union[Unset, None, str] = UNSET,
    query_sort_ascending: Union[Unset, None, ReportsQueryReportsQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsReport]]:
    """Returns all built-in reports according to the provided filter and output parameters

    Args:
        query_query_string (Union[Unset, None, str]):
        query_page_returned (Union[Unset, None, int]):
        query_return_limit (Union[Unset, None, int]):
        query_sort_field (Union[Unset, None, str]):
        query_sort_ascending (Union[Unset, None, ReportsQueryReportsQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsReport]]
    """

    kwargs = _get_kwargs(
        client=client,
        query_query_string=query_query_string,
        query_page_returned=query_page_returned,
        query_return_limit=query_return_limit,
        query_sort_field=query_sort_field,
        query_sort_ascending=query_sort_ascending,
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
    query_query_string: Union[Unset, None, str] = UNSET,
    query_page_returned: Union[Unset, None, int] = UNSET,
    query_return_limit: Union[Unset, None, int] = UNSET,
    query_sort_field: Union[Unset, None, str] = UNSET,
    query_sort_ascending: Union[Unset, None, ReportsQueryReportsQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsReport]]:
    """Returns all built-in reports according to the provided filter and output parameters

    Args:
        query_query_string (Union[Unset, None, str]):
        query_page_returned (Union[Unset, None, int]):
        query_return_limit (Union[Unset, None, int]):
        query_sort_field (Union[Unset, None, str]):
        query_sort_ascending (Union[Unset, None, ReportsQueryReportsQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsReport]]
    """

    return sync_detailed(
        client=client,
        query_query_string=query_query_string,
        query_page_returned=query_page_returned,
        query_return_limit=query_return_limit,
        query_sort_field=query_sort_field,
        query_sort_ascending=query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    query_query_string: Union[Unset, None, str] = UNSET,
    query_page_returned: Union[Unset, None, int] = UNSET,
    query_return_limit: Union[Unset, None, int] = UNSET,
    query_sort_field: Union[Unset, None, str] = UNSET,
    query_sort_ascending: Union[Unset, None, ReportsQueryReportsQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsReport]]:
    """Returns all built-in reports according to the provided filter and output parameters

    Args:
        query_query_string (Union[Unset, None, str]):
        query_page_returned (Union[Unset, None, int]):
        query_return_limit (Union[Unset, None, int]):
        query_sort_field (Union[Unset, None, str]):
        query_sort_ascending (Union[Unset, None, ReportsQueryReportsQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsReport]]
    """

    kwargs = _get_kwargs(
        client=client,
        query_query_string=query_query_string,
        query_page_returned=query_page_returned,
        query_return_limit=query_return_limit,
        query_sort_field=query_sort_field,
        query_sort_ascending=query_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    query_query_string: Union[Unset, None, str] = UNSET,
    query_page_returned: Union[Unset, None, int] = UNSET,
    query_return_limit: Union[Unset, None, int] = UNSET,
    query_sort_field: Union[Unset, None, str] = UNSET,
    query_sort_ascending: Union[Unset, None, ReportsQueryReportsQuerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsReport]]:
    """Returns all built-in reports according to the provided filter and output parameters

    Args:
        query_query_string (Union[Unset, None, str]):
        query_page_returned (Union[Unset, None, int]):
        query_return_limit (Union[Unset, None, int]):
        query_sort_field (Union[Unset, None, str]):
        query_sort_ascending (Union[Unset, None, ReportsQueryReportsQuerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsReport]]
    """

    return (
        await asyncio_detailed(
            client=client,
            query_query_string=query_query_string,
            query_page_returned=query_page_returned,
            query_return_limit=query_return_limit,
            query_sort_field=query_sort_field,
            query_sort_ascending=query_sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
