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

from ..models.keyfactor_api_models_enrollment_management_store_request_properties import (
    KeyfactorApiModelsEnrollmentManagementStoreRequestProperties,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsEnrollmentManagementStoreRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsEnrollmentManagementStoreRequest:
    """
    Attributes:
        store_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        alias (Union[Unset, str]):
        overwrite (Union[Unset, bool]):
        properties (Union[Unset, KeyfactorApiModelsEnrollmentManagementStoreRequestProperties]):
    """

    store_id: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    overwrite: Union[Unset, bool] = UNSET
    properties: Union[Unset, KeyfactorApiModelsEnrollmentManagementStoreRequestProperties] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        store_id = self.store_id
        alias = self.alias
        overwrite = self.overwrite
        properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_id is not UNSET:
            field_dict["StoreId"] = store_id
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if overwrite is not UNSET:
            field_dict["Overwrite"] = overwrite
        if properties is not UNSET:
            field_dict["Properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        store_id = d.pop("StoreId", UNSET)

        alias = d.pop("Alias", UNSET)

        overwrite = d.pop("Overwrite", UNSET)

        _properties = d.pop("Properties", UNSET)
        properties: Union[Unset, KeyfactorApiModelsEnrollmentManagementStoreRequestProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = KeyfactorApiModelsEnrollmentManagementStoreRequestProperties.from_dict(_properties)

        keyfactor_api_models_enrollment_management_store_request = cls(
            store_id=store_id,
            alias=alias,
            overwrite=overwrite,
            properties=properties,
        )

        keyfactor_api_models_enrollment_management_store_request.additional_properties = d
        return keyfactor_api_models_enrollment_management_store_request

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
