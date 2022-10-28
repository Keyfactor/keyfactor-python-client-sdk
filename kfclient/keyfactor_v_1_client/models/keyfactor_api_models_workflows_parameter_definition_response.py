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

from ..models.keyfactor_api_models_workflows_parameter_definition_response_control_type import (
    KeyfactorApiModelsWorkflowsParameterDefinitionResponseControlType,
)
from ..models.keyfactor_api_models_workflows_parameter_definition_response_depends_on import (
    KeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn,
)
from ..models.keyfactor_api_models_workflows_parameter_definition_response_parameter_type import (
    KeyfactorApiModelsWorkflowsParameterDefinitionResponseParameterType,
)
from ..models.keyfactor_api_models_workflows_parameter_definition_response_potential_values import (
    KeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsParameterDefinitionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsParameterDefinitionResponse:
    """
    Attributes:
        display_name (Union[Unset, str]):
        parameter_type (Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseParameterType]):
        required (Union[Unset, bool]):
        default_value (Union[Unset, str]):
        control_type (Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseControlType]):
        potential_values (Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues]):
        support_token_replacement (Union[Unset, bool]):
        depends_on (Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn]):
    """

    display_name: Union[Unset, str] = UNSET
    parameter_type: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseParameterType] = UNSET
    required: Union[Unset, bool] = UNSET
    default_value: Union[Unset, str] = UNSET
    control_type: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseControlType] = UNSET
    potential_values: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues] = UNSET
    support_token_replacement: Union[Unset, bool] = UNSET
    depends_on: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        parameter_type: Union[Unset, int] = UNSET
        if not isinstance(self.parameter_type, Unset):
            parameter_type = self.parameter_type.value

        required = self.required
        default_value = self.default_value
        control_type: Union[Unset, int] = UNSET
        if not isinstance(self.control_type, Unset):
            control_type = self.control_type.value

        potential_values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.potential_values, Unset):
            potential_values = self.potential_values.to_dict()

        support_token_replacement = self.support_token_replacement
        depends_on: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.depends_on, Unset):
            depends_on = self.depends_on.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if parameter_type is not UNSET:
            field_dict["ParameterType"] = parameter_type
        if required is not UNSET:
            field_dict["Required"] = required
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if control_type is not UNSET:
            field_dict["ControlType"] = control_type
        if potential_values is not UNSET:
            field_dict["PotentialValues"] = potential_values
        if support_token_replacement is not UNSET:
            field_dict["SupportTokenReplacement"] = support_token_replacement
        if depends_on is not UNSET:
            field_dict["DependsOn"] = depends_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("DisplayName", UNSET)

        _parameter_type = d.pop("ParameterType", UNSET)
        parameter_type: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseParameterType]
        if isinstance(_parameter_type, Unset):
            parameter_type = UNSET
        else:
            parameter_type = KeyfactorApiModelsWorkflowsParameterDefinitionResponseParameterType(_parameter_type)

        required = d.pop("Required", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        _control_type = d.pop("ControlType", UNSET)
        control_type: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseControlType]
        if isinstance(_control_type, Unset):
            control_type = UNSET
        else:
            control_type = KeyfactorApiModelsWorkflowsParameterDefinitionResponseControlType(_control_type)

        _potential_values = d.pop("PotentialValues", UNSET)
        potential_values: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues]
        if isinstance(_potential_values, Unset):
            potential_values = UNSET
        else:
            potential_values = KeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues.from_dict(
                _potential_values
            )

        support_token_replacement = d.pop("SupportTokenReplacement", UNSET)

        _depends_on = d.pop("DependsOn", UNSET)
        depends_on: Union[Unset, KeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn]
        if isinstance(_depends_on, Unset):
            depends_on = UNSET
        else:
            depends_on = KeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn.from_dict(_depends_on)

        keyfactor_api_models_workflows_parameter_definition_response = cls(
            display_name=display_name,
            parameter_type=parameter_type,
            required=required,
            default_value=default_value,
            control_type=control_type,
            potential_values=potential_values,
            support_token_replacement=support_token_replacement,
            depends_on=depends_on,
        )

        keyfactor_api_models_workflows_parameter_definition_response.additional_properties = d
        return keyfactor_api_models_workflows_parameter_definition_response

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
