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

from ..models.models_certificate_store_type_property_type import ModelsCertificateStoreTypePropertyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStoreTypeProperty")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreTypeProperty:
    """
    Attributes:
        store_type_id (Union[Unset, int]):
        name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        type (Union[Unset, ModelsCertificateStoreTypePropertyType]):
        depends_on (Union[Unset, str]):
        default_value (Union[Unset, str]):
        required (Union[Unset, bool]):
    """

    store_type_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    type: Union[Unset, ModelsCertificateStoreTypePropertyType] = UNSET
    depends_on: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        store_type_id = self.store_type_id
        name = self.name
        display_name = self.display_name
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        depends_on = self.depends_on
        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_type_id is not UNSET:
            field_dict["StoreTypeId"] = store_type_id
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if type is not UNSET:
            field_dict["Type"] = type
        if depends_on is not UNSET:
            field_dict["DependsOn"] = depends_on
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if required is not UNSET:
            field_dict["Required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        store_type_id = d.pop("StoreTypeId", UNSET)

        name = d.pop("Name", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ModelsCertificateStoreTypePropertyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ModelsCertificateStoreTypePropertyType(_type)

        depends_on = d.pop("DependsOn", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        required = d.pop("Required", UNSET)

        models_certificate_store_type_property = cls(
            store_type_id=store_type_id,
            name=name,
            display_name=display_name,
            type=type,
            depends_on=depends_on,
            default_value=default_value,
            required=required,
        )

        models_certificate_store_type_property.additional_properties = d
        return models_certificate_store_type_property

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
