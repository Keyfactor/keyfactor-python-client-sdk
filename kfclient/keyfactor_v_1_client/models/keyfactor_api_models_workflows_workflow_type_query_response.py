# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.keyfactor_api_models_workflows_available_step_response import (
    KeyfactorApiModelsWorkflowsAvailableStepResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsWorkflowTypeQueryResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsWorkflowTypeQueryResponse:
    """
    Attributes:
        workflow_type (Union[Unset, str]):
        key_type (Union[Unset, str]):
        context_parameters (Union[Unset, List[str]]):
        built_in_steps (Union[Unset, List[KeyfactorApiModelsWorkflowsAvailableStepResponse]]):
    """

    workflow_type: Union[Unset, str] = UNSET
    key_type: Union[Unset, str] = UNSET
    context_parameters: Union[Unset, List[str]] = UNSET
    built_in_steps: Union[Unset, List[KeyfactorApiModelsWorkflowsAvailableStepResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow_type = self.workflow_type
        key_type = self.key_type
        context_parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.context_parameters, Unset):
            context_parameters = self.context_parameters

        built_in_steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.built_in_steps, Unset):
            built_in_steps = []
            for built_in_steps_item_data in self.built_in_steps:
                built_in_steps_item = built_in_steps_item_data.to_dict()

                built_in_steps.append(built_in_steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_type is not UNSET:
            field_dict["WorkflowType"] = workflow_type
        if key_type is not UNSET:
            field_dict["KeyType"] = key_type
        if context_parameters is not UNSET:
            field_dict["ContextParameters"] = context_parameters
        if built_in_steps is not UNSET:
            field_dict["BuiltInSteps"] = built_in_steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workflow_type = d.pop("WorkflowType", UNSET)

        key_type = d.pop("KeyType", UNSET)

        context_parameters = cast(List[str], d.pop("ContextParameters", UNSET))

        built_in_steps = []
        _built_in_steps = d.pop("BuiltInSteps", UNSET)
        for built_in_steps_item_data in _built_in_steps or []:
            built_in_steps_item = KeyfactorApiModelsWorkflowsAvailableStepResponse.from_dict(built_in_steps_item_data)

            built_in_steps.append(built_in_steps_item)

        keyfactor_api_models_workflows_workflow_type_query_response = cls(
            workflow_type=workflow_type,
            key_type=key_type,
            context_parameters=context_parameters,
            built_in_steps=built_in_steps,
        )

        keyfactor_api_models_workflows_workflow_type_query_response.additional_properties = d
        return keyfactor_api_models_workflows_workflow_type_query_response

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
