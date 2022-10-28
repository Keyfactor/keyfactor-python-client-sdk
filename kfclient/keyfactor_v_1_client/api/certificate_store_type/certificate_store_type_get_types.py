from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.certificate_store_type_get_types_cstquery_sort_ascending import (
    CertificateStoreTypeGetTypesCstquerySortAscending,
)
from ...models.keyfactor_api_models_certificate_stores_types_certificate_store_type_response import (
    KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    cstquery_query_string: Union[Unset, None, str] = UNSET,
    cstquery_page_returned: Union[Unset, None, int] = UNSET,
    cstquery_return_limit: Union[Unset, None, int] = UNSET,
    cstquery_sort_field: Union[Unset, None, str] = UNSET,
    cstquery_sort_ascending: Union[Unset, None, CertificateStoreTypeGetTypesCstquerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/CertificateStoreTypes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["cstquery.queryString"] = cstquery_query_string

    params["cstquery.pageReturned"] = cstquery_page_returned

    params["cstquery.returnLimit"] = cstquery_return_limit

    params["cstquery.sortField"] = cstquery_sort_field

    json_cstquery_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(cstquery_sort_ascending, Unset):
        json_cstquery_sort_ascending = cstquery_sort_ascending.value if cstquery_sort_ascending else None

    params["cstquery.sortAscending"] = json_cstquery_sort_ascending

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
) -> Optional[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    cstquery_query_string: Union[Unset, None, str] = UNSET,
    cstquery_page_returned: Union[Unset, None, int] = UNSET,
    cstquery_return_limit: Union[Unset, None, int] = UNSET,
    cstquery_sort_field: Union[Unset, None, str] = UNSET,
    cstquery_sort_ascending: Union[Unset, None, CertificateStoreTypeGetTypesCstquerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]:
    """Returns all certificate store types according to the provided filter and output parameters

    Args:
        cstquery_query_string (Union[Unset, None, str]):
        cstquery_page_returned (Union[Unset, None, int]):
        cstquery_return_limit (Union[Unset, None, int]):
        cstquery_sort_field (Union[Unset, None, str]):
        cstquery_sort_ascending (Union[Unset, None,
            CertificateStoreTypeGetTypesCstquerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        cstquery_query_string=cstquery_query_string,
        cstquery_page_returned=cstquery_page_returned,
        cstquery_return_limit=cstquery_return_limit,
        cstquery_sort_field=cstquery_sort_field,
        cstquery_sort_ascending=cstquery_sort_ascending,
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
    cstquery_query_string: Union[Unset, None, str] = UNSET,
    cstquery_page_returned: Union[Unset, None, int] = UNSET,
    cstquery_return_limit: Union[Unset, None, int] = UNSET,
    cstquery_sort_field: Union[Unset, None, str] = UNSET,
    cstquery_sort_ascending: Union[Unset, None, CertificateStoreTypeGetTypesCstquerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]:
    """Returns all certificate store types according to the provided filter and output parameters

    Args:
        cstquery_query_string (Union[Unset, None, str]):
        cstquery_page_returned (Union[Unset, None, int]):
        cstquery_return_limit (Union[Unset, None, int]):
        cstquery_sort_field (Union[Unset, None, str]):
        cstquery_sort_ascending (Union[Unset, None,
            CertificateStoreTypeGetTypesCstquerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]
    """

    return sync_detailed(
        client=client,
        cstquery_query_string=cstquery_query_string,
        cstquery_page_returned=cstquery_page_returned,
        cstquery_return_limit=cstquery_return_limit,
        cstquery_sort_field=cstquery_sort_field,
        cstquery_sort_ascending=cstquery_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    cstquery_query_string: Union[Unset, None, str] = UNSET,
    cstquery_page_returned: Union[Unset, None, int] = UNSET,
    cstquery_return_limit: Union[Unset, None, int] = UNSET,
    cstquery_sort_field: Union[Unset, None, str] = UNSET,
    cstquery_sort_ascending: Union[Unset, None, CertificateStoreTypeGetTypesCstquerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]:
    """Returns all certificate store types according to the provided filter and output parameters

    Args:
        cstquery_query_string (Union[Unset, None, str]):
        cstquery_page_returned (Union[Unset, None, int]):
        cstquery_return_limit (Union[Unset, None, int]):
        cstquery_sort_field (Union[Unset, None, str]):
        cstquery_sort_ascending (Union[Unset, None,
            CertificateStoreTypeGetTypesCstquerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        cstquery_query_string=cstquery_query_string,
        cstquery_page_returned=cstquery_page_returned,
        cstquery_return_limit=cstquery_return_limit,
        cstquery_sort_field=cstquery_sort_field,
        cstquery_sort_ascending=cstquery_sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    cstquery_query_string: Union[Unset, None, str] = UNSET,
    cstquery_page_returned: Union[Unset, None, int] = UNSET,
    cstquery_return_limit: Union[Unset, None, int] = UNSET,
    cstquery_sort_field: Union[Unset, None, str] = UNSET,
    cstquery_sort_ascending: Union[Unset, None, CertificateStoreTypeGetTypesCstquerySortAscending] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]:
    """Returns all certificate store types according to the provided filter and output parameters

    Args:
        cstquery_query_string (Union[Unset, None, str]):
        cstquery_page_returned (Union[Unset, None, int]):
        cstquery_return_limit (Union[Unset, None, int]):
        cstquery_sort_field (Union[Unset, None, str]):
        cstquery_sort_ascending (Union[Unset, None,
            CertificateStoreTypeGetTypesCstquerySortAscending]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cstquery_query_string=cstquery_query_string,
            cstquery_page_returned=cstquery_page_returned,
            cstquery_return_limit=cstquery_return_limit,
            cstquery_sort_field=cstquery_sort_field,
            cstquery_sort_ascending=cstquery_sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed