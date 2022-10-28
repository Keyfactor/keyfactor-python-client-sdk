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

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionCreateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionCreateRequest:
    """
    Example:
        {'DisplayName': '<Workflow name>', 'Description': '<Workflow description>', 'Key': '<Numeric Template Id>',
            'WorkflowType': '<Type of workflow>'}

    Attributes:
        display_name (Union[Unset, str]): Display name of the Definition
        description (Union[Unset, str]): Description of the Definition
        key (Union[Unset, str]): Key to be used to look up definition when starting a new workflow.
            For enrollment workflowTypes, this should be a template
        workflow_type (Union[Unset, str]): The Type of Workflow
    """

    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    workflow_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        description = self.description
        key = self.key
        workflow_type = self.workflow_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if description is not UNSET:
            field_dict["Description"] = description
        if key is not UNSET:
            field_dict["Key"] = key
        if workflow_type is not UNSET:
            field_dict["WorkflowType"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("DisplayName", UNSET)

        description = d.pop("Description", UNSET)

        key = d.pop("Key", UNSET)

        workflow_type = d.pop("WorkflowType", UNSET)

        keyfactor_api_models_workflows_definition_create_request = cls(
            display_name=display_name,
            description=description,
            key=key,
            workflow_type=workflow_type,
        )

        keyfactor_api_models_workflows_definition_create_request.additional_properties = d
        return keyfactor_api_models_workflows_definition_create_request

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
