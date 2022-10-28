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

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorsAgentBlueprintResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorsAgentBlueprintResponse:
    """
    Attributes:
        agent_blueprint_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        name (Union[Unset, str]):
        required_capabilities (Union[Unset, List[str]]):
        last_modified (Union[Unset, datetime.datetime]):
    """

    agent_blueprint_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    required_capabilities: Union[Unset, List[str]] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_blueprint_id = self.agent_blueprint_id
        name = self.name
        required_capabilities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_capabilities, Unset):
            required_capabilities = self.required_capabilities

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_blueprint_id is not UNSET:
            field_dict["AgentBlueprintId"] = agent_blueprint_id
        if name is not UNSET:
            field_dict["Name"] = name
        if required_capabilities is not UNSET:
            field_dict["RequiredCapabilities"] = required_capabilities
        if last_modified is not UNSET:
            field_dict["LastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_blueprint_id = d.pop("AgentBlueprintId", UNSET)

        name = d.pop("Name", UNSET)

        required_capabilities = cast(List[str], d.pop("RequiredCapabilities", UNSET))

        _last_modified = d.pop("LastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        keyfactor_api_models_orchestrators_agent_blueprint_response = cls(
            agent_blueprint_id=agent_blueprint_id,
            name=name,
            required_capabilities=required_capabilities,
            last_modified=last_modified,
        )

        keyfactor_api_models_orchestrators_agent_blueprint_response.additional_properties = d
        return keyfactor_api_models_orchestrators_agent_blueprint_response

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
