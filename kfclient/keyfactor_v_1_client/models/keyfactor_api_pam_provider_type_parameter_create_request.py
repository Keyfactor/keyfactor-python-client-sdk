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

from ..models.keyfactor_api_pam_provider_type_parameter_create_request_data_type import (
    KeyfactorApiPAMProviderTypeParameterCreateRequestDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiPAMProviderTypeParameterCreateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiPAMProviderTypeParameterCreateRequest:
    """
    Attributes:
        name (str):
        display_name (Union[Unset, str]):
        data_type (Union[Unset, KeyfactorApiPAMProviderTypeParameterCreateRequestDataType]):
        instance_level (Union[Unset, bool]):
    """

    name: str
    display_name: Union[Unset, str] = UNSET
    data_type: Union[Unset, KeyfactorApiPAMProviderTypeParameterCreateRequestDataType] = UNSET
    instance_level: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        display_name = self.display_name
        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        instance_level = self.instance_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
            }
        )
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
        name = d.pop("Name")

        display_name = d.pop("DisplayName", UNSET)

        _data_type = d.pop("DataType", UNSET)
        data_type: Union[Unset, KeyfactorApiPAMProviderTypeParameterCreateRequestDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = KeyfactorApiPAMProviderTypeParameterCreateRequestDataType(_data_type)

        instance_level = d.pop("InstanceLevel", UNSET)

        keyfactor_api_pam_provider_type_parameter_create_request = cls(
            name=name,
            display_name=display_name,
            data_type=data_type,
            instance_level=instance_level,
        )

        keyfactor_api_pam_provider_type_parameter_create_request.additional_properties = d
        return keyfactor_api_pam_provider_type_parameter_create_request

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
