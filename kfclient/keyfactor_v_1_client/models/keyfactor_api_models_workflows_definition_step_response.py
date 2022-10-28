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

from ..models.keyfactor_api_models_workflows_condition_configuration_response import (
    KeyfactorApiModelsWorkflowsConditionConfigurationResponse,
)
from ..models.keyfactor_api_models_workflows_definition_step_response_configuration_parameters import (
    KeyfactorApiModelsWorkflowsDefinitionStepResponseConfigurationParameters,
)
from ..models.keyfactor_api_models_workflows_definition_step_response_outputs import (
    KeyfactorApiModelsWorkflowsDefinitionStepResponseOutputs,
)
from ..models.keyfactor_api_models_workflows_definition_step_signal_response import (
    KeyfactorApiModelsWorkflowsDefinitionStepSignalResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionStepResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionStepResponse:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        display_name (Union[Unset, str]):
        unique_name (Union[Unset, str]):
        extension_name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        configuration_parameters (Union[Unset,
            KeyfactorApiModelsWorkflowsDefinitionStepResponseConfigurationParameters]):
        signals (Union[Unset, List[KeyfactorApiModelsWorkflowsDefinitionStepSignalResponse]]):
        conditions (Union[Unset, List[KeyfactorApiModelsWorkflowsConditionConfigurationResponse]]):
        outputs (Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepResponseOutputs]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    unique_name: Union[Unset, str] = UNSET
    extension_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    configuration_parameters: Union[
        Unset, KeyfactorApiModelsWorkflowsDefinitionStepResponseConfigurationParameters
    ] = UNSET
    signals: Union[Unset, List[KeyfactorApiModelsWorkflowsDefinitionStepSignalResponse]] = UNSET
    conditions: Union[Unset, List[KeyfactorApiModelsWorkflowsConditionConfigurationResponse]] = UNSET
    outputs: Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepResponseOutputs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        unique_name = self.unique_name
        extension_name = self.extension_name
        enabled = self.enabled
        configuration_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = self.configuration_parameters.to_dict()

        signals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signals, Unset):
            signals = []
            for signals_item_data in self.signals:
                signals_item = signals_item_data.to_dict()

                signals.append(signals_item)

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()

                conditions.append(conditions_item)

        outputs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if unique_name is not UNSET:
            field_dict["UniqueName"] = unique_name
        if extension_name is not UNSET:
            field_dict["ExtensionName"] = extension_name
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if configuration_parameters is not UNSET:
            field_dict["ConfigurationParameters"] = configuration_parameters
        if signals is not UNSET:
            field_dict["Signals"] = signals
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if outputs is not UNSET:
            field_dict["Outputs"] = outputs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        unique_name = d.pop("UniqueName", UNSET)

        extension_name = d.pop("ExtensionName", UNSET)

        enabled = d.pop("Enabled", UNSET)

        _configuration_parameters = d.pop("ConfigurationParameters", UNSET)
        configuration_parameters: Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepResponseConfigurationParameters]
        if isinstance(_configuration_parameters, Unset):
            configuration_parameters = UNSET
        else:
            configuration_parameters = (
                KeyfactorApiModelsWorkflowsDefinitionStepResponseConfigurationParameters.from_dict(
                    _configuration_parameters
                )
            )

        signals = []
        _signals = d.pop("Signals", UNSET)
        for signals_item_data in _signals or []:
            signals_item = KeyfactorApiModelsWorkflowsDefinitionStepSignalResponse.from_dict(signals_item_data)

            signals.append(signals_item)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = KeyfactorApiModelsWorkflowsConditionConfigurationResponse.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        _outputs = d.pop("Outputs", UNSET)
        outputs: Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepResponseOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = KeyfactorApiModelsWorkflowsDefinitionStepResponseOutputs.from_dict(_outputs)

        keyfactor_api_models_workflows_definition_step_response = cls(
            id=id,
            display_name=display_name,
            unique_name=unique_name,
            extension_name=extension_name,
            enabled=enabled,
            configuration_parameters=configuration_parameters,
            signals=signals,
            conditions=conditions,
            outputs=outputs,
        )

        keyfactor_api_models_workflows_definition_step_response.additional_properties = d
        return keyfactor_api_models_workflows_definition_step_response

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
