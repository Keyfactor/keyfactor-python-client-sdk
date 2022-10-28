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

from ..models.models_report_parameters_parameter_type import ModelsReportParametersParameterType
from ..models.models_report_parameters_parameter_visibility import ModelsReportParametersParameterVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsReportParameters")


@attr.s(auto_attribs=True)
class ModelsReportParameters:
    """
    Attributes:
        id (Union[Unset, int]):
        parameter_name (Union[Unset, str]):
        parameter_type (Union[Unset, ModelsReportParametersParameterType]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        default_value (Union[Unset, str]):
        display_order (Union[Unset, int]):
        parameter_visibility (Union[Unset, ModelsReportParametersParameterVisibility]):
    """

    id: Union[Unset, int] = UNSET
    parameter_name: Union[Unset, str] = UNSET
    parameter_type: Union[Unset, ModelsReportParametersParameterType] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    parameter_visibility: Union[Unset, ModelsReportParametersParameterVisibility] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parameter_name = self.parameter_name
        parameter_type: Union[Unset, int] = UNSET
        if not isinstance(self.parameter_type, Unset):
            parameter_type = self.parameter_type.value

        display_name = self.display_name
        description = self.description
        default_value = self.default_value
        display_order = self.display_order
        parameter_visibility: Union[Unset, int] = UNSET
        if not isinstance(self.parameter_visibility, Unset):
            parameter_visibility = self.parameter_visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if parameter_name is not UNSET:
            field_dict["ParameterName"] = parameter_name
        if parameter_type is not UNSET:
            field_dict["ParameterType"] = parameter_type
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if description is not UNSET:
            field_dict["Description"] = description
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if display_order is not UNSET:
            field_dict["DisplayOrder"] = display_order
        if parameter_visibility is not UNSET:
            field_dict["ParameterVisibility"] = parameter_visibility

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        parameter_name = d.pop("ParameterName", UNSET)

        _parameter_type = d.pop("ParameterType", UNSET)
        parameter_type: Union[Unset, ModelsReportParametersParameterType]
        if isinstance(_parameter_type, Unset):
            parameter_type = UNSET
        else:
            parameter_type = ModelsReportParametersParameterType(_parameter_type)

        display_name = d.pop("DisplayName", UNSET)

        description = d.pop("Description", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        display_order = d.pop("DisplayOrder", UNSET)

        _parameter_visibility = d.pop("ParameterVisibility", UNSET)
        parameter_visibility: Union[Unset, ModelsReportParametersParameterVisibility]
        if isinstance(_parameter_visibility, Unset):
            parameter_visibility = UNSET
        else:
            parameter_visibility = ModelsReportParametersParameterVisibility(_parameter_visibility)

        models_report_parameters = cls(
            id=id,
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            display_name=display_name,
            description=description,
            default_value=default_value,
            display_order=display_order,
            parameter_visibility=parameter_visibility,
        )

        models_report_parameters.additional_properties = d
        return models_report_parameters

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
