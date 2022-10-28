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

from ..models.keyfactor_api_models_workflows_signal_definition_response_input_parameters import (
    KeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsSignalDefinitionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsSignalDefinitionResponse:
    """
    Attributes:
        input_parameters (Union[Unset, KeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters]):
    """

    input_parameters: Union[Unset, KeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.input_parameters, Unset):
            input_parameters = self.input_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_parameters is not UNSET:
            field_dict["InputParameters"] = input_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _input_parameters = d.pop("InputParameters", UNSET)
        input_parameters: Union[Unset, KeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters]
        if isinstance(_input_parameters, Unset):
            input_parameters = UNSET
        else:
            input_parameters = KeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters.from_dict(
                _input_parameters
            )

        keyfactor_api_models_workflows_signal_definition_response = cls(
            input_parameters=input_parameters,
        )

        keyfactor_api_models_workflows_signal_definition_response.additional_properties = d
        return keyfactor_api_models_workflows_signal_definition_response

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
