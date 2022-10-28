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

from ..models.keyfactor_api_models_workflows_available_step_response_configuration_parameters_definition import (
    KeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition,
)
from ..models.keyfactor_api_models_workflows_available_step_response_signals_definition import (
    KeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsAvailableStepResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsAvailableStepResponse:
    """
    Attributes:
        display_name (Union[Unset, str]): The display name of the step.
        extension_name (Union[Unset, str]): The name of the extension.
        outputs (Union[Unset, List[str]]): The possible outputs of the step.
        configuration_parameters_definition (Union[Unset,
            KeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition]):
        signals_definition (Union[Unset, KeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition]):
    """

    display_name: Union[Unset, str] = UNSET
    extension_name: Union[Unset, str] = UNSET
    outputs: Union[Unset, List[str]] = UNSET
    configuration_parameters_definition: Union[
        Unset, KeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition
    ] = UNSET
    signals_definition: Union[Unset, KeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        extension_name = self.extension_name
        outputs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs

        configuration_parameters_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration_parameters_definition, Unset):
            configuration_parameters_definition = self.configuration_parameters_definition.to_dict()

        signals_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signals_definition, Unset):
            signals_definition = self.signals_definition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if extension_name is not UNSET:
            field_dict["ExtensionName"] = extension_name
        if outputs is not UNSET:
            field_dict["Outputs"] = outputs
        if configuration_parameters_definition is not UNSET:
            field_dict["ConfigurationParametersDefinition"] = configuration_parameters_definition
        if signals_definition is not UNSET:
            field_dict["SignalsDefinition"] = signals_definition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("DisplayName", UNSET)

        extension_name = d.pop("ExtensionName", UNSET)

        outputs = cast(List[str], d.pop("Outputs", UNSET))

        _configuration_parameters_definition = d.pop("ConfigurationParametersDefinition", UNSET)
        configuration_parameters_definition: Union[
            Unset, KeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition
        ]
        if isinstance(_configuration_parameters_definition, Unset):
            configuration_parameters_definition = UNSET
        else:
            configuration_parameters_definition = (
                KeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition.from_dict(
                    _configuration_parameters_definition
                )
            )

        _signals_definition = d.pop("SignalsDefinition", UNSET)
        signals_definition: Union[Unset, KeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition]
        if isinstance(_signals_definition, Unset):
            signals_definition = UNSET
        else:
            signals_definition = KeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition.from_dict(
                _signals_definition
            )

        keyfactor_api_models_workflows_available_step_response = cls(
            display_name=display_name,
            extension_name=extension_name,
            outputs=outputs,
            configuration_parameters_definition=configuration_parameters_definition,
            signals_definition=signals_definition,
        )

        keyfactor_api_models_workflows_available_step_response.additional_properties = d
        return keyfactor_api_models_workflows_available_step_response

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
