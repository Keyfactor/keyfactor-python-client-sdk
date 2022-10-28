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

from ..models.keyfactor_api_models_workflows_definition_step_response import (
    KeyfactorApiModelsWorkflowsDefinitionStepResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        key (Union[Unset, str]):
        key_display_name (Union[Unset, str]):
        is_published (Union[Unset, bool]):
        workflow_type (Union[Unset, str]):
        steps (Union[Unset, List[KeyfactorApiModelsWorkflowsDefinitionStepResponse]]):
        draft_version (Union[Unset, int]):
        published_version (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    key_display_name: Union[Unset, str] = UNSET
    is_published: Union[Unset, bool] = UNSET
    workflow_type: Union[Unset, str] = UNSET
    steps: Union[Unset, List[KeyfactorApiModelsWorkflowsDefinitionStepResponse]] = UNSET
    draft_version: Union[Unset, int] = UNSET
    published_version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        description = self.description
        key = self.key
        key_display_name = self.key_display_name
        is_published = self.is_published
        workflow_type = self.workflow_type
        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()

                steps.append(steps_item)

        draft_version = self.draft_version
        published_version = self.published_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if description is not UNSET:
            field_dict["Description"] = description
        if key is not UNSET:
            field_dict["Key"] = key
        if key_display_name is not UNSET:
            field_dict["KeyDisplayName"] = key_display_name
        if is_published is not UNSET:
            field_dict["IsPublished"] = is_published
        if workflow_type is not UNSET:
            field_dict["WorkflowType"] = workflow_type
        if steps is not UNSET:
            field_dict["Steps"] = steps
        if draft_version is not UNSET:
            field_dict["DraftVersion"] = draft_version
        if published_version is not UNSET:
            field_dict["PublishedVersion"] = published_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        description = d.pop("Description", UNSET)

        key = d.pop("Key", UNSET)

        key_display_name = d.pop("KeyDisplayName", UNSET)

        is_published = d.pop("IsPublished", UNSET)

        workflow_type = d.pop("WorkflowType", UNSET)

        steps = []
        _steps = d.pop("Steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = KeyfactorApiModelsWorkflowsDefinitionStepResponse.from_dict(steps_item_data)

            steps.append(steps_item)

        draft_version = d.pop("DraftVersion", UNSET)

        published_version = d.pop("PublishedVersion", UNSET)

        keyfactor_api_models_workflows_definition_response = cls(
            id=id,
            display_name=display_name,
            description=description,
            key=key,
            key_display_name=key_display_name,
            is_published=is_published,
            workflow_type=workflow_type,
            steps=steps,
            draft_version=draft_version,
            published_version=published_version,
        )

        keyfactor_api_models_workflows_definition_response.additional_properties = d
        return keyfactor_api_models_workflows_definition_response

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
