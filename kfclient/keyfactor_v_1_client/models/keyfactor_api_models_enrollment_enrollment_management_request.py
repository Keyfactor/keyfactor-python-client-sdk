# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.keyfactor_api_models_enrollment_management_store_request import (
    KeyfactorApiModelsEnrollmentManagementStoreRequest,
)
from ..models.keyfactor_api_models_enrollment_management_store_type_request import (
    KeyfactorApiModelsEnrollmentManagementStoreTypeRequest,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsEnrollmentEnrollmentManagementRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsEnrollmentEnrollmentManagementRequest:
    """
    Example:
        {'Stores': [{'StoreId': '00000000-0000-0000-0000-000000000000', 'Alias': '<store alias>', 'Overwrite': True,
            'Properties': {'Netscalervserver': 'thevalue'}}], 'CertificateId': 0, 'RequestId': 0, 'Password': '<pfx
            password>', 'JobTime': datetime.datetime(2022, 9, 23, 18, 9, 16, 719678, tzinfo=datetime.timezone.utc)}

    Attributes:
        password (str):
        stores (Union[Unset, List[KeyfactorApiModelsEnrollmentManagementStoreRequest]]): The stores to add the
            certificate to. Values in this collection will take precedence over values in
            {Models.Enrollment.SpecificEnrollmentManagementRequest.StoreTypes}.
        store_ids (Union[Unset, List[str]]):
        store_types (Union[Unset, List[KeyfactorApiModelsEnrollmentManagementStoreTypeRequest]]):
        certificate_id (Union[Unset, int]):
        request_id (Union[Unset, int]):
        job_time (Union[Unset, datetime.datetime]):
    """

    password: str
    stores: Union[Unset, List[KeyfactorApiModelsEnrollmentManagementStoreRequest]] = UNSET
    store_ids: Union[Unset, List[str]] = UNSET
    store_types: Union[Unset, List[KeyfactorApiModelsEnrollmentManagementStoreTypeRequest]] = UNSET
    certificate_id: Union[Unset, int] = UNSET
    request_id: Union[Unset, int] = UNSET
    job_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        stores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stores, Unset):
            stores = []
            for stores_item_data in self.stores:
                stores_item = stores_item_data.to_dict()

                stores.append(stores_item)

        store_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.store_ids, Unset):
            store_ids = self.store_ids

        store_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.store_types, Unset):
            store_types = []
            for store_types_item_data in self.store_types:
                store_types_item = store_types_item_data.to_dict()

                store_types.append(store_types_item)

        certificate_id = self.certificate_id
        request_id = self.request_id
        job_time: Union[Unset, str] = UNSET
        if not isinstance(self.job_time, Unset):
            job_time = self.job_time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Password": password,
            }
        )
        if stores is not UNSET:
            field_dict["Stores"] = stores
        if store_ids is not UNSET:
            field_dict["StoreIds"] = store_ids
        if store_types is not UNSET:
            field_dict["StoreTypes"] = store_types
        if certificate_id is not UNSET:
            field_dict["CertificateId"] = certificate_id
        if request_id is not UNSET:
            field_dict["RequestId"] = request_id
        if job_time is not UNSET:
            field_dict["JobTime"] = job_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("Password")

        stores = []
        _stores = d.pop("Stores", UNSET)
        for stores_item_data in _stores or []:
            stores_item = KeyfactorApiModelsEnrollmentManagementStoreRequest.from_dict(stores_item_data)

            stores.append(stores_item)

        store_ids = cast(List[str], d.pop("StoreIds", UNSET))

        store_types = []
        _store_types = d.pop("StoreTypes", UNSET)
        for store_types_item_data in _store_types or []:
            store_types_item = KeyfactorApiModelsEnrollmentManagementStoreTypeRequest.from_dict(store_types_item_data)

            store_types.append(store_types_item)

        certificate_id = d.pop("CertificateId", UNSET)

        request_id = d.pop("RequestId", UNSET)

        _job_time = d.pop("JobTime", UNSET)
        job_time: Union[Unset, datetime.datetime]
        if isinstance(_job_time, Unset):
            job_time = UNSET
        else:
            job_time = isoparse(_job_time)

        keyfactor_api_models_enrollment_enrollment_management_request = cls(
            password=password,
            stores=stores,
            store_ids=store_ids,
            store_types=store_types,
            certificate_id=certificate_id,
            request_id=request_id,
            job_time=job_time,
        )

        keyfactor_api_models_enrollment_enrollment_management_request.additional_properties = d
        return keyfactor_api_models_enrollment_enrollment_management_request

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
