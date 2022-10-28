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

from ..models.models_certificate_store_inventory_certificates import ModelsCertificateStoreInventoryCertificates
from ..models.models_certificate_store_inventory_parameters import ModelsCertificateStoreInventoryParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStoreInventory")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreInventory:
    """
    Attributes:
        name (Union[Unset, str]):
        certificates (Union[Unset, List[ModelsCertificateStoreInventoryCertificates]]):
        parameters (Union[Unset, ModelsCertificateStoreInventoryParameters]):
    """

    name: Union[Unset, str] = UNSET
    certificates: Union[Unset, List[ModelsCertificateStoreInventoryCertificates]] = UNSET
    parameters: Union[Unset, ModelsCertificateStoreInventoryParameters] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        certificates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()

                certificates.append(certificates_item)

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if certificates is not UNSET:
            field_dict["Certificates"] = certificates
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        certificates = []
        _certificates = d.pop("Certificates", UNSET)
        for certificates_item_data in _certificates or []:
            certificates_item = ModelsCertificateStoreInventoryCertificates.from_dict(certificates_item_data)

            certificates.append(certificates_item)

        _parameters = d.pop("Parameters", UNSET)
        parameters: Union[Unset, ModelsCertificateStoreInventoryParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ModelsCertificateStoreInventoryParameters.from_dict(_parameters)

        models_certificate_store_inventory = cls(
            name=name,
            certificates=certificates,
            parameters=parameters,
        )

        models_certificate_store_inventory.additional_properties = d
        return models_certificate_store_inventory

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
