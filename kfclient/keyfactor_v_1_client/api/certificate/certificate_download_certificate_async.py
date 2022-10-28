from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_certificate_download_request import ModelsCertificateDownloadRequest
from ...models.models_certificate_download_response import ModelsCertificateDownloadResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ModelsCertificateDownloadRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Certificates/Download".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ModelsCertificateDownloadResponse]:
    if response.status_code == 200:
        response_200 = ModelsCertificateDownloadResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsCertificateDownloadResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ModelsCertificateDownloadRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsCertificateDownloadResponse]:
    """Downloads the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsCertificateDownloadRequest):

    Returns:
        Response[ModelsCertificateDownloadResponse]
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
    json_body: ModelsCertificateDownloadRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsCertificateDownloadResponse]:
    """Downloads the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsCertificateDownloadRequest):

    Returns:
        Response[ModelsCertificateDownloadResponse]
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
    json_body: ModelsCertificateDownloadRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsCertificateDownloadResponse]:
    """Downloads the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsCertificateDownloadRequest):

    Returns:
        Response[ModelsCertificateDownloadResponse]
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
    json_body: ModelsCertificateDownloadRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsCertificateDownloadResponse]:
    """Downloads the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsCertificateDownloadRequest):

    Returns:
        Response[ModelsCertificateDownloadResponse]
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