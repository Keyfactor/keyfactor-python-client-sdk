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

from ..models.models_cert_store_locations_certificate_locations_group import (
    ModelsCertStoreLocationsCertificateLocationsGroup,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificatesCertificateLocationsResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificatesCertificateLocationsResponse:
    """
    Attributes:
        details (Union[Unset, List[ModelsCertStoreLocationsCertificateLocationsGroup]]):
    """

    details: Union[Unset, List[ModelsCertStoreLocationsCertificateLocationsGroup]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()

                details.append(details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["Details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        details = []
        _details = d.pop("Details", UNSET)
        for details_item_data in _details or []:
            details_item = ModelsCertStoreLocationsCertificateLocationsGroup.from_dict(details_item_data)

            details.append(details_item)

        keyfactor_api_models_certificates_certificate_locations_response = cls(
            details=details,
        )

        keyfactor_api_models_certificates_certificate_locations_response.additional_properties = d
        return keyfactor_api_models_certificates_certificate_locations_response

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
