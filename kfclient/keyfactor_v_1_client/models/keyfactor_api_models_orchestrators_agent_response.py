# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.keyfactor_api_models_orchestrators_agent_response_agent_platform import (
    KeyfactorApiModelsOrchestratorsAgentResponseAgentPlatform,
)
from ..models.keyfactor_api_models_orchestrators_agent_response_status import (
    KeyfactorApiModelsOrchestratorsAgentResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorsAgentResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorsAgentResponse:
    """
    Attributes:
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        client_machine (Union[Unset, str]):
        username (Union[Unset, str]):
        agent_platform (Union[Unset, KeyfactorApiModelsOrchestratorsAgentResponseAgentPlatform]):
        version (Union[Unset, str]):
        status (Union[Unset, KeyfactorApiModelsOrchestratorsAgentResponseStatus]):
        last_seen (Union[Unset, datetime.datetime]):
        capabilities (Union[Unset, List[str]]):
        blueprint (Union[Unset, str]):
        thumbprint (Union[Unset, str]):
        legacy_thumbprint (Union[Unset, str]):
        auth_certificate_reenrollment (Union[Unset, str]):
        last_thumbprint_used (Union[Unset, str]):
        last_error_code (Union[Unset, int]):
        last_error_message (Union[Unset, str]):
    """

    agent_id: Union[Unset, str] = UNSET
    client_machine: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    agent_platform: Union[Unset, KeyfactorApiModelsOrchestratorsAgentResponseAgentPlatform] = UNSET
    version: Union[Unset, str] = UNSET
    status: Union[Unset, KeyfactorApiModelsOrchestratorsAgentResponseStatus] = UNSET
    last_seen: Union[Unset, datetime.datetime] = UNSET
    capabilities: Union[Unset, List[str]] = UNSET
    blueprint: Union[Unset, str] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    legacy_thumbprint: Union[Unset, str] = UNSET
    auth_certificate_reenrollment: Union[Unset, str] = UNSET
    last_thumbprint_used: Union[Unset, str] = UNSET
    last_error_code: Union[Unset, int] = UNSET
    last_error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        client_machine = self.client_machine
        username = self.username
        agent_platform: Union[Unset, int] = UNSET
        if not isinstance(self.agent_platform, Unset):
            agent_platform = self.agent_platform.value

        version = self.version
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_seen: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()[:-6]+'Z'

        capabilities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        blueprint = self.blueprint
        thumbprint = self.thumbprint
        legacy_thumbprint = self.legacy_thumbprint
        auth_certificate_reenrollment = self.auth_certificate_reenrollment
        last_thumbprint_used = self.last_thumbprint_used
        last_error_code = self.last_error_code
        last_error_message = self.last_error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if username is not UNSET:
            field_dict["Username"] = username
        if agent_platform is not UNSET:
            field_dict["AgentPlatform"] = agent_platform
        if version is not UNSET:
            field_dict["Version"] = version
        if status is not UNSET:
            field_dict["Status"] = status
        if last_seen is not UNSET:
            field_dict["LastSeen"] = last_seen
        if capabilities is not UNSET:
            field_dict["Capabilities"] = capabilities
        if blueprint is not UNSET:
            field_dict["Blueprint"] = blueprint
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if legacy_thumbprint is not UNSET:
            field_dict["LegacyThumbprint"] = legacy_thumbprint
        if auth_certificate_reenrollment is not UNSET:
            field_dict["AuthCertificateReenrollment"] = auth_certificate_reenrollment
        if last_thumbprint_used is not UNSET:
            field_dict["LastThumbprintUsed"] = last_thumbprint_used
        if last_error_code is not UNSET:
            field_dict["LastErrorCode"] = last_error_code
        if last_error_message is not UNSET:
            field_dict["LastErrorMessage"] = last_error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_id = d.pop("AgentId", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        username = d.pop("Username", UNSET)

        _agent_platform = d.pop("AgentPlatform", UNSET)
        agent_platform: Union[Unset, KeyfactorApiModelsOrchestratorsAgentResponseAgentPlatform]
        if isinstance(_agent_platform, Unset):
            agent_platform = UNSET
        else:
            agent_platform = KeyfactorApiModelsOrchestratorsAgentResponseAgentPlatform(_agent_platform)

        version = d.pop("Version", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, KeyfactorApiModelsOrchestratorsAgentResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorApiModelsOrchestratorsAgentResponseStatus(_status)

        _last_seen = d.pop("LastSeen", UNSET)
        last_seen: Union[Unset, datetime.datetime]
        if isinstance(_last_seen, Unset):
            last_seen = UNSET
        else:
            last_seen = isoparse(_last_seen)

        capabilities = cast(List[str], d.pop("Capabilities", UNSET))

        blueprint = d.pop("Blueprint", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        legacy_thumbprint = d.pop("LegacyThumbprint", UNSET)

        auth_certificate_reenrollment = d.pop("AuthCertificateReenrollment", UNSET)

        last_thumbprint_used = d.pop("LastThumbprintUsed", UNSET)

        last_error_code = d.pop("LastErrorCode", UNSET)

        last_error_message = d.pop("LastErrorMessage", UNSET)

        keyfactor_api_models_orchestrators_agent_response = cls(
            agent_id=agent_id,
            client_machine=client_machine,
            username=username,
            agent_platform=agent_platform,
            version=version,
            status=status,
            last_seen=last_seen,
            capabilities=capabilities,
            blueprint=blueprint,
            thumbprint=thumbprint,
            legacy_thumbprint=legacy_thumbprint,
            auth_certificate_reenrollment=auth_certificate_reenrollment,
            last_thumbprint_used=last_thumbprint_used,
            last_error_code=last_error_code,
            last_error_message=last_error_message,
        )

        keyfactor_api_models_orchestrators_agent_response.additional_properties = d
        return keyfactor_api_models_orchestrators_agent_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
