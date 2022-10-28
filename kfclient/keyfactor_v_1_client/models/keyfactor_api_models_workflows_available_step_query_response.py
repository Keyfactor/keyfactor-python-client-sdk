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

from ..models.keyfactor_api_models_workflows_available_step_query_response_configuration_parameters_definition import (
    KeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition,
)
from ..models.keyfactor_api_models_workflows_available_step_query_response_signals_definition import (
    KeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsAvailableStepQueryResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsAvailableStepQueryResponse:
    """
    Attributes:
        display_name (Union[Unset, str]): The display name of the step.
        extension_name (Union[Unset, str]): The extension name of the step.
        supported_workflow_types (Union[Unset, List[str]]): The workflow types which this step can be a part of.
        configuration_parameters_definition (Union[Unset,
            KeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition]):
        signals_definition (Union[Unset, KeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition]):
    """

    display_name: Union[Unset, str] = UNSET
    extension_name: Union[Unset, str] = UNSET
    supported_workflow_types: Union[Unset, List[str]] = UNSET
    configuration_parameters_definition: Union[
        Unset, KeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition
    ] = UNSET
    signals_definition: Union[Unset, KeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        extension_name = self.extension_name
        supported_workflow_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.supported_workflow_types, Unset):
            supported_workflow_types = self.supported_workflow_types

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
        if supported_workflow_types is not UNSET:
            field_dict["SupportedWorkflowTypes"] = supported_workflow_types
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

        supported_workflow_types = cast(List[str], d.pop("SupportedWorkflowTypes", UNSET))

        _configuration_parameters_definition = d.pop("ConfigurationParametersDefinition", UNSET)
        configuration_parameters_definition: Union[
            Unset, KeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition
        ]
        if isinstance(_configuration_parameters_definition, Unset):
            configuration_parameters_definition = UNSET
        else:
            configuration_parameters_definition = (
                KeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition.from_dict(
                    _configuration_parameters_definition
                )
            )

        _signals_definition = d.pop("SignalsDefinition", UNSET)
        signals_definition: Union[Unset, KeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition]
        if isinstance(_signals_definition, Unset):
            signals_definition = UNSET
        else:
            signals_definition = KeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition.from_dict(
                _signals_definition
            )

        keyfactor_api_models_workflows_available_step_query_response = cls(
            display_name=display_name,
            extension_name=extension_name,
            supported_workflow_types=supported_workflow_types,
            configuration_parameters_definition=configuration_parameters_definition,
            signals_definition=signals_definition,
        )

        keyfactor_api_models_workflows_available_step_query_response.additional_properties = d
        return keyfactor_api_models_workflows_available_step_query_response

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
