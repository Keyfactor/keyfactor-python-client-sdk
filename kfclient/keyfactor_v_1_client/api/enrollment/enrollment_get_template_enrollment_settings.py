# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_templates_template_enrollment_settings_response import (
    KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse,
)
from ...types import Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Enrollment/Settings/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]:
    if response.status_code == 200:
        response_200 = KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsTemplatesTemplateEnrollmentSettingsResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
