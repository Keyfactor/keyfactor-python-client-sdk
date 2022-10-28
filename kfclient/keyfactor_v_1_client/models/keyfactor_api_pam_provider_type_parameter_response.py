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

from ..models.keyfactor_api_pam_provider_type_parameter_response_data_type import (
    KeyfactorApiPAMProviderTypeParameterResponseDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiPAMProviderTypeParameterResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiPAMProviderTypeParameterResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        data_type (Union[Unset, KeyfactorApiPAMProviderTypeParameterResponseDataType]):
        instance_level (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    data_type: Union[Unset, KeyfactorApiPAMProviderTypeParameterResponseDataType] = UNSET
    instance_level: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        instance_level = self.instance_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if data_type is not UNSET:
            field_dict["DataType"] = data_type
        if instance_level is not UNSET:
            field_dict["InstanceLevel"] = instance_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        _data_type = d.pop("DataType", UNSET)
        data_type: Union[Unset, KeyfactorApiPAMProviderTypeParameterResponseDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = KeyfactorApiPAMProviderTypeParameterResponseDataType(_data_type)

        instance_level = d.pop("InstanceLevel", UNSET)

        keyfactor_api_pam_provider_type_parameter_response = cls(
            id=id,
            name=name,
            display_name=display_name,
            data_type=data_type,
            instance_level=instance_level,
        )

        keyfactor_api_pam_provider_type_parameter_response.additional_properties = d
        return keyfactor_api_pam_provider_type_parameter_response

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
