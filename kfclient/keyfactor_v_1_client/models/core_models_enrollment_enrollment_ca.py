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

T = TypeVar("T", bound="CoreModelsEnrollmentEnrollmentCA")


@attr.s(auto_attribs=True)
class CoreModelsEnrollmentEnrollmentCA:
    """
    Attributes:
        name (Union[Unset, str]):
        rfc_enforcement (Union[Unset, bool]):
        subscriber_terms (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    subscriber_terms: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        rfc_enforcement = self.rfc_enforcement
        subscriber_terms = self.subscriber_terms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if rfc_enforcement is not UNSET:
            field_dict["RFCEnforcement"] = rfc_enforcement
        if subscriber_terms is not UNSET:
            field_dict["SubscriberTerms"] = subscriber_terms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        rfc_enforcement = d.pop("RFCEnforcement", UNSET)

        subscriber_terms = d.pop("SubscriberTerms", UNSET)

        core_models_enrollment_enrollment_ca = cls(
            name=name,
            rfc_enforcement=rfc_enforcement,
            subscriber_terms=subscriber_terms,
        )

        core_models_enrollment_enrollment_ca.additional_properties = d
        return core_models_enrollment_enrollment_ca

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
