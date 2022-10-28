# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsInstanceDefinitionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsInstanceDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        display_name (Union[Unset, str]):
        version (Union[Unset, int]):
        workflow_type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    workflow_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        version = self.version
        workflow_type = self.workflow_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if version is not UNSET:
            field_dict["Version"] = version
        if workflow_type is not UNSET:
            field_dict["WorkflowType"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        version = d.pop("Version", UNSET)

        workflow_type = d.pop("WorkflowType", UNSET)

        keyfactor_api_models_workflows_instance_definition_response = cls(
            id=id,
            display_name=display_name,
            version=version,
            workflow_type=workflow_type,
        )

        keyfactor_api_models_workflows_instance_definition_response.additional_properties = d
        return keyfactor_api_models_workflows_instance_definition_response

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
