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

T = TypeVar("T", bound="ModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel")


@attr.s(auto_attribs=True)
class ModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel:
    """
    Attributes:
        store_machine (Union[Unset, str]):
        store_path (Union[Unset, str]):
        store_type (Union[Unset, int]):
        alias (Union[Unset, str]):
        chain_level (Union[Unset, int]):
        cert_store_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
    """

    store_machine: Union[Unset, str] = UNSET
    store_path: Union[Unset, str] = UNSET
    store_type: Union[Unset, int] = UNSET
    alias: Union[Unset, str] = UNSET
    chain_level: Union[Unset, int] = UNSET
    cert_store_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        store_machine = self.store_machine
        store_path = self.store_path
        store_type = self.store_type
        alias = self.alias
        chain_level = self.chain_level
        cert_store_id = self.cert_store_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_machine is not UNSET:
            field_dict["StoreMachine"] = store_machine
        if store_path is not UNSET:
            field_dict["StorePath"] = store_path
        if store_type is not UNSET:
            field_dict["StoreType"] = store_type
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if chain_level is not UNSET:
            field_dict["ChainLevel"] = chain_level
        if cert_store_id is not UNSET:
            field_dict["CertStoreId"] = cert_store_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        store_machine = d.pop("StoreMachine", UNSET)

        store_path = d.pop("StorePath", UNSET)

        store_type = d.pop("StoreType", UNSET)

        alias = d.pop("Alias", UNSET)

        chain_level = d.pop("ChainLevel", UNSET)

        cert_store_id = d.pop("CertStoreId", UNSET)

        models_certificate_retrieval_response_certificate_store_inventory_item_model = cls(
            store_machine=store_machine,
            store_path=store_path,
            store_type=store_type,
            alias=alias,
            chain_level=chain_level,
            cert_store_id=cert_store_id,
        )

        models_certificate_retrieval_response_certificate_store_inventory_item_model.additional_properties = d
        return models_certificate_retrieval_response_certificate_store_inventory_item_model

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
