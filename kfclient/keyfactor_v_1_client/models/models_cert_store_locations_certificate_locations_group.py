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

from ..models.models_cert_store_locations_certificate_store_locations_detail import (
    ModelsCertStoreLocationsCertificateStoreLocationsDetail,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertStoreLocationsCertificateLocationsGroup")


@attr.s(auto_attribs=True)
class ModelsCertStoreLocationsCertificateLocationsGroup:
    """
    Attributes:
        store_type (Union[Unset, str]):
        store_type_id (Union[Unset, int]):
        store_count (Union[Unset, int]):
        locations (Union[Unset, List[ModelsCertStoreLocationsCertificateStoreLocationsDetail]]):
    """

    store_type: Union[Unset, str] = UNSET
    store_type_id: Union[Unset, int] = UNSET
    store_count: Union[Unset, int] = UNSET
    locations: Union[Unset, List[ModelsCertStoreLocationsCertificateStoreLocationsDetail]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        store_type = self.store_type
        store_type_id = self.store_type_id
        store_count = self.store_count
        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()

                locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_type is not UNSET:
            field_dict["StoreType"] = store_type
        if store_type_id is not UNSET:
            field_dict["StoreTypeId"] = store_type_id
        if store_count is not UNSET:
            field_dict["StoreCount"] = store_count
        if locations is not UNSET:
            field_dict["Locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        store_type = d.pop("StoreType", UNSET)

        store_type_id = d.pop("StoreTypeId", UNSET)

        store_count = d.pop("StoreCount", UNSET)

        locations = []
        _locations = d.pop("Locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = ModelsCertStoreLocationsCertificateStoreLocationsDetail.from_dict(locations_item_data)

            locations.append(locations_item)

        models_cert_store_locations_certificate_locations_group = cls(
            store_type=store_type,
            store_type_id=store_type_id,
            store_count=store_count,
            locations=locations,
        )

        models_cert_store_locations_certificate_locations_group.additional_properties = d
        return models_cert_store_locations_certificate_locations_group

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
