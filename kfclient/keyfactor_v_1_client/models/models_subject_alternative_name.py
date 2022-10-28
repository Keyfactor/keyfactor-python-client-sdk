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

from ..models.models_subject_alternative_name_type import ModelsSubjectAlternativeNameType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSubjectAlternativeName")


@attr.s(auto_attribs=True)
class ModelsSubjectAlternativeName:
    """
    Attributes:
        id (Union[Unset, int]):
        value (Union[Unset, str]):
        type (Union[Unset, ModelsSubjectAlternativeNameType]):
        value_hash (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    type: Union[Unset, ModelsSubjectAlternativeNameType] = UNSET
    value_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        value_hash = self.value_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if value is not UNSET:
            field_dict["Value"] = value
        if type is not UNSET:
            field_dict["Type"] = type
        if value_hash is not UNSET:
            field_dict["ValueHash"] = value_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        value = d.pop("Value", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ModelsSubjectAlternativeNameType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ModelsSubjectAlternativeNameType(_type)

        value_hash = d.pop("ValueHash", UNSET)

        models_subject_alternative_name = cls(
            id=id,
            value=value,
            type=type,
            value_hash=value_hash,
        )

        models_subject_alternative_name.additional_properties = d
        return models_subject_alternative_name

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
