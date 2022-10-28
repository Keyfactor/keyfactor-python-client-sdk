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

T = TypeVar("T", bound="KeyfactorApiModelsEventHandlerEventHandlerParameterResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsEventHandlerEventHandlerParameterResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        key (Union[Unset, str]):
        default_value (Union[Unset, str]):
        parameter_type (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    parameter_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        default_value = self.default_value
        parameter_type = self.parameter_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if key is not UNSET:
            field_dict["Key"] = key
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if parameter_type is not UNSET:
            field_dict["ParameterType"] = parameter_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        key = d.pop("Key", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        parameter_type = d.pop("ParameterType", UNSET)

        keyfactor_api_models_event_handler_event_handler_parameter_response = cls(
            id=id,
            key=key,
            default_value=default_value,
            parameter_type=parameter_type,
        )

        keyfactor_api_models_event_handler_event_handler_parameter_response.additional_properties = d
        return keyfactor_api_models_event_handler_event_handler_parameter_response

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
