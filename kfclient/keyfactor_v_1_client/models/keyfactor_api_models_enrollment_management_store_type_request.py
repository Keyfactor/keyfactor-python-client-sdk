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

from ..models.keyfactor_api_models_enrollment_management_store_type_request_properties_item import (
    KeyfactorApiModelsEnrollmentManagementStoreTypeRequestPropertiesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsEnrollmentManagementStoreTypeRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsEnrollmentManagementStoreTypeRequest:
    """
    Attributes:
        store_type_id (Union[Unset, int]):
        alias (Union[Unset, str]):
        overwrite (Union[Unset, bool]):
        properties (Union[Unset, List[KeyfactorApiModelsEnrollmentManagementStoreTypeRequestPropertiesItem]]):
    """

    store_type_id: Union[Unset, int] = UNSET
    alias: Union[Unset, str] = UNSET
    overwrite: Union[Unset, bool] = UNSET
    properties: Union[Unset, List[KeyfactorApiModelsEnrollmentManagementStoreTypeRequestPropertiesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        store_type_id = self.store_type_id
        alias = self.alias
        overwrite = self.overwrite
        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()

                properties.append(properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_type_id is not UNSET:
            field_dict["StoreTypeId"] = store_type_id
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
        store_type_id = d.pop("StoreTypeId", UNSET)

        alias = d.pop("Alias", UNSET)

        overwrite = d.pop("Overwrite", UNSET)

        properties = []
        _properties = d.pop("Properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = KeyfactorApiModelsEnrollmentManagementStoreTypeRequestPropertiesItem.from_dict(
                properties_item_data
            )

            properties.append(properties_item)

        keyfactor_api_models_enrollment_management_store_type_request = cls(
            store_type_id=store_type_id,
            alias=alias,
            overwrite=overwrite,
            properties=properties,
        )

        keyfactor_api_models_enrollment_management_store_type_request.additional_properties = d
        return keyfactor_api_models_enrollment_management_store_type_request

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
