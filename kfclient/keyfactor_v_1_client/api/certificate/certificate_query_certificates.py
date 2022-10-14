from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.certificate_query_certificates_pq_sort_ascending import CertificateQueryCertificatesPqSortAscending
from ...models.models_certificate_retrieval_response import ModelsCertificateRetrievalResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    collection_id: Union[Unset, None, int] = UNSET,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    include_has_private_key: Union[Unset, None, bool] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, CertificateQueryCertificatesPqSortAscending] = UNSET,
    pq_include_revoked: Union[Unset, None, bool] = UNSET,
    pq_include_expired: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Certificates".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["collectionId"] = collection_id

    params["includeLocations"] = include_locations

    params["includeMetadata"] = include_metadata

    params["includeHasPrivateKey"] = include_has_private_key

    params["verbose"] = verbose

    params["pq.queryString"] = pq_query_string

    params["pq.pageReturned"] = pq_page_returned

    params["pq.returnLimit"] = pq_return_limit

    params["pq.sortField"] = pq_sort_field

    json_pq_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(pq_sort_ascending, Unset):
        json_pq_sort_ascending = pq_sort_ascending.value if pq_sort_ascending else None

    params["pq.sortAscending"] = json_pq_sort_ascending

    params["pq.includeRevoked"] = pq_include_revoked

    params["pq.includeExpired"] = pq_include_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ModelsCertificateRetrievalResponse]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelsCertificateRetrievalResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ModelsCertificateRetrievalResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    collection_id: Union[Unset, None, int] = UNSET,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    include_has_private_key: Union[Unset, None, bool] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, CertificateQueryCertificatesPqSortAscending] = UNSET,
    pq_include_revoked: Union[Unset, None, bool] = UNSET,
    pq_include_expired: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsCertificateRetrievalResponse]]:
    """Returns all certificates according to the provided filter and output parameters

    Args:
        collection_id (Union[Unset, None, int]):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        include_has_private_key (Union[Unset, None, bool]):
        verbose (Union[Unset, None, int]):
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, CertificateQueryCertificatesPqSortAscending]):
        pq_include_revoked (Union[Unset, None, bool]):
        pq_include_expired (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsCertificateRetrievalResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        collection_id=collection_id,
        include_locations=include_locations,
        include_metadata=include_metadata,
        include_has_private_key=include_has_private_key,
        verbose=verbose,
        pq_query_string=pq_query_string,
        pq_page_returned=pq_page_returned,
        pq_return_limit=pq_return_limit,
        pq_sort_field=pq_sort_field,
        pq_sort_ascending=pq_sort_ascending,
        pq_include_revoked=pq_include_revoked,
        pq_include_expired=pq_include_expired,
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
    collection_id: Union[Unset, None, int] = UNSET,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    include_has_private_key: Union[Unset, None, bool] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, CertificateQueryCertificatesPqSortAscending] = UNSET,
    pq_include_revoked: Union[Unset, None, bool] = UNSET,
    pq_include_expired: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsCertificateRetrievalResponse]]:
    """Returns all certificates according to the provided filter and output parameters

    Args:
        collection_id (Union[Unset, None, int]):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        include_has_private_key (Union[Unset, None, bool]):
        verbose (Union[Unset, None, int]):
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, CertificateQueryCertificatesPqSortAscending]):
        pq_include_revoked (Union[Unset, None, bool]):
        pq_include_expired (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsCertificateRetrievalResponse]]
    """

    return sync_detailed(
        client=client,
        collection_id=collection_id,
        include_locations=include_locations,
        include_metadata=include_metadata,
        include_has_private_key=include_has_private_key,
        verbose=verbose,
        pq_query_string=pq_query_string,
        pq_page_returned=pq_page_returned,
        pq_return_limit=pq_return_limit,
        pq_sort_field=pq_sort_field,
        pq_sort_ascending=pq_sort_ascending,
        pq_include_revoked=pq_include_revoked,
        pq_include_expired=pq_include_expired,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    collection_id: Union[Unset, None, int] = UNSET,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    include_has_private_key: Union[Unset, None, bool] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, CertificateQueryCertificatesPqSortAscending] = UNSET,
    pq_include_revoked: Union[Unset, None, bool] = UNSET,
    pq_include_expired: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[ModelsCertificateRetrievalResponse]]:
    """Returns all certificates according to the provided filter and output parameters

    Args:
        collection_id (Union[Unset, None, int]):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        include_has_private_key (Union[Unset, None, bool]):
        verbose (Union[Unset, None, int]):
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, CertificateQueryCertificatesPqSortAscending]):
        pq_include_revoked (Union[Unset, None, bool]):
        pq_include_expired (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsCertificateRetrievalResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        collection_id=collection_id,
        include_locations=include_locations,
        include_metadata=include_metadata,
        include_has_private_key=include_has_private_key,
        verbose=verbose,
        pq_query_string=pq_query_string,
        pq_page_returned=pq_page_returned,
        pq_return_limit=pq_return_limit,
        pq_sort_field=pq_sort_field,
        pq_sort_ascending=pq_sort_ascending,
        pq_include_revoked=pq_include_revoked,
        pq_include_expired=pq_include_expired,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    collection_id: Union[Unset, None, int] = UNSET,
    include_locations: Union[Unset, None, bool] = UNSET,
    include_metadata: Union[Unset, None, bool] = UNSET,
    include_has_private_key: Union[Unset, None, bool] = UNSET,
    verbose: Union[Unset, None, int] = UNSET,
    pq_query_string: Union[Unset, None, str] = UNSET,
    pq_page_returned: Union[Unset, None, int] = UNSET,
    pq_return_limit: Union[Unset, None, int] = UNSET,
    pq_sort_field: Union[Unset, None, str] = UNSET,
    pq_sort_ascending: Union[Unset, None, CertificateQueryCertificatesPqSortAscending] = UNSET,
    pq_include_revoked: Union[Unset, None, bool] = UNSET,
    pq_include_expired: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[ModelsCertificateRetrievalResponse]]:
    """Returns all certificates according to the provided filter and output parameters

    Args:
        collection_id (Union[Unset, None, int]):
        include_locations (Union[Unset, None, bool]):
        include_metadata (Union[Unset, None, bool]):
        include_has_private_key (Union[Unset, None, bool]):
        verbose (Union[Unset, None, int]):
        pq_query_string (Union[Unset, None, str]):
        pq_page_returned (Union[Unset, None, int]):
        pq_return_limit (Union[Unset, None, int]):
        pq_sort_field (Union[Unset, None, str]):
        pq_sort_ascending (Union[Unset, None, CertificateQueryCertificatesPqSortAscending]):
        pq_include_revoked (Union[Unset, None, bool]):
        pq_include_expired (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[List[ModelsCertificateRetrievalResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            collection_id=collection_id,
            include_locations=include_locations,
            include_metadata=include_metadata,
            include_has_private_key=include_has_private_key,
            verbose=verbose,
            pq_query_string=pq_query_string,
            pq_page_returned=pq_page_returned,
            pq_return_limit=pq_return_limit,
            pq_sort_field=pq_sort_field,
            pq_sort_ascending=pq_sort_ascending,
            pq_include_revoked=pq_include_revoked,
            pq_include_expired=pq_include_expired,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
