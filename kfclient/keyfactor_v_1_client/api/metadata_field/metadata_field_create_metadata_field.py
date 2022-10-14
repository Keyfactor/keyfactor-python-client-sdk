from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_metadata_field_metadata_field_create_request import (
    KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest,
)
from ...models.keyfactor_api_models_metadata_field_metadata_field_response import (
    KeyfactorApiModelsMetadataFieldMetadataFieldResponse,
)
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/MetadataFields".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]:
    if response.status_code == 200:
        response_200 = KeyfactorApiModelsMetadataFieldMetadataFieldResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]:
    """Creates a new metadata field type with the given metadata field type properties

     *NOTE: Metadata Field in this context refers to MetadataFieldType, as opposed to the value of a
    metadata field associated with a certificate.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest):

    Returns:
        Response[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]:
    """Creates a new metadata field type with the given metadata field type properties

     *NOTE: Metadata Field in this context refers to MetadataFieldType, as opposed to the value of a
    metadata field associated with a certificate.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest):

    Returns:
        Response[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]:
    """Creates a new metadata field type with the given metadata field type properties

     *NOTE: Metadata Field in this context refers to MetadataFieldType, as opposed to the value of a
    metadata field associated with a certificate.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest):

    Returns:
        Response[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]:
    """Creates a new metadata field type with the given metadata field type properties

     *NOTE: Metadata Field in this context refers to MetadataFieldType, as opposed to the value of a
    metadata field associated with a certificate.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest):

    Returns:
        Response[KeyfactorApiModelsMetadataFieldMetadataFieldResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
