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

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..models.models_certificate_store_entry import ModelsCertificateStoreEntry
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificateStoresAddCertificateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificateStoresAddCertificateRequest:
    """
    Attributes:
        certificate_id (int):
        certificate_stores (List[ModelsCertificateStoreEntry]):
        schedule (KeyfactorCommonSchedulingKeyfactorSchedule):
        collection_id (Union[Unset, int]):
    """

    certificate_id: int
    certificate_stores: List[ModelsCertificateStoreEntry]
    schedule: KeyfactorCommonSchedulingKeyfactorSchedule
    collection_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_id = self.certificate_id
        certificate_stores = []
        for certificate_stores_item_data in self.certificate_stores:
            certificate_stores_item = certificate_stores_item_data.to_dict()

            certificate_stores.append(certificate_stores_item)

        schedule = self.schedule.to_dict()

        collection_id = self.collection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CertificateId": certificate_id,
                "CertificateStores": certificate_stores,
                "Schedule": schedule,
            }
        )
        if collection_id is not UNSET:
            field_dict["CollectionId"] = collection_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_id = d.pop("CertificateId")

        certificate_stores = []
        _certificate_stores = d.pop("CertificateStores")
        for certificate_stores_item_data in _certificate_stores:
            certificate_stores_item = ModelsCertificateStoreEntry.from_dict(certificate_stores_item_data)

            certificate_stores.append(certificate_stores_item)

        schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(d.pop("Schedule"))

        collection_id = d.pop("CollectionId", UNSET)

        keyfactor_api_models_certificate_stores_add_certificate_request = cls(
            certificate_id=certificate_id,
            certificate_stores=certificate_stores,
            schedule=schedule,
            collection_id=collection_id,
        )

        keyfactor_api_models_certificate_stores_add_certificate_request.additional_properties = d
        return keyfactor_api_models_certificate_stores_add_certificate_request

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
