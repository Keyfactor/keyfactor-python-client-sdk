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

from ..models.models_enrollment_available_renewal_available_renewal_type import (
    ModelsEnrollmentAvailableRenewalAvailableRenewalType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsEnrollmentAvailableRenewal")


@attr.s(auto_attribs=True)
class ModelsEnrollmentAvailableRenewal:
    """
    Attributes:
        available_renewal_type (Union[Unset, ModelsEnrollmentAvailableRenewalAvailableRenewalType]):
        message (Union[Unset, str]):
    """

    available_renewal_type: Union[Unset, ModelsEnrollmentAvailableRenewalAvailableRenewalType] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_renewal_type: Union[Unset, int] = UNSET
        if not isinstance(self.available_renewal_type, Unset):
            available_renewal_type = self.available_renewal_type.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_renewal_type is not UNSET:
            field_dict["AvailableRenewalType"] = available_renewal_type
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _available_renewal_type = d.pop("AvailableRenewalType", UNSET)
        available_renewal_type: Union[Unset, ModelsEnrollmentAvailableRenewalAvailableRenewalType]
        if isinstance(_available_renewal_type, Unset):
            available_renewal_type = UNSET
        else:
            available_renewal_type = ModelsEnrollmentAvailableRenewalAvailableRenewalType(_available_renewal_type)

        message = d.pop("Message", UNSET)

        models_enrollment_available_renewal = cls(
            available_renewal_type=available_renewal_type,
            message=message,
        )

        models_enrollment_available_renewal.additional_properties = d
        return models_enrollment_available_renewal

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
