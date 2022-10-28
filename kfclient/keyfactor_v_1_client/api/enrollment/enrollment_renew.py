from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_enrollment_renewal_request import ModelsEnrollmentRenewalRequest
from ...models.models_enrollment_renewal_response import ModelsEnrollmentRenewalResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ModelsEnrollmentRenewalRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Enrollment/Renew".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ModelsEnrollmentRenewalResponse]:
    if response.status_code == 200:
        response_200 = ModelsEnrollmentRenewalResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsEnrollmentRenewalResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ModelsEnrollmentRenewalRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsEnrollmentRenewalResponse]:
    """Performs a renewal based upon the passed in request

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsEnrollmentRenewalRequest):  Example: {'CertificateId': 0, 'Thumbprint':
            '<hex thumbprint>', 'CertificateAuthority': '<host>\\<logical>', 'Template': '<template
            name>', 'Timestamp': datetime.datetime(2022, 9, 22, 14, 9, 16, 734610,
            tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))}.

    Returns:
        Response[ModelsEnrollmentRenewalResponse]
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
    json_body: ModelsEnrollmentRenewalRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsEnrollmentRenewalResponse]:
    """Performs a renewal based upon the passed in request

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsEnrollmentRenewalRequest):  Example: {'CertificateId': 0, 'Thumbprint':
            '<hex thumbprint>', 'CertificateAuthority': '<host>\\<logical>', 'Template': '<template
            name>', 'Timestamp': datetime.datetime(2022, 9, 22, 14, 9, 16, 734610,
            tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))}.

    Returns:
        Response[ModelsEnrollmentRenewalResponse]
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
    json_body: ModelsEnrollmentRenewalRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsEnrollmentRenewalResponse]:
    """Performs a renewal based upon the passed in request

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsEnrollmentRenewalRequest):  Example: {'CertificateId': 0, 'Thumbprint':
            '<hex thumbprint>', 'CertificateAuthority': '<host>\\<logical>', 'Template': '<template
            name>', 'Timestamp': datetime.datetime(2022, 9, 22, 14, 9, 16, 734610,
            tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))}.

    Returns:
        Response[ModelsEnrollmentRenewalResponse]
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
    json_body: ModelsEnrollmentRenewalRequest,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsEnrollmentRenewalResponse]:
    """Performs a renewal based upon the passed in request

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsEnrollmentRenewalRequest):  Example: {'CertificateId': 0, 'Thumbprint':
            '<hex thumbprint>', 'CertificateAuthority': '<host>\\<logical>', 'Template': '<template
            name>', 'Timestamp': datetime.datetime(2022, 9, 22, 14, 9, 16, 734610,
            tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))}.

    Returns:
        Response[ModelsEnrollmentRenewalResponse]
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