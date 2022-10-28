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

from ..models.models_keyfactor_api_secret import ModelsKeyfactorAPISecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        container_id (Union[Unset, int]):
        cert_store_type (Union[Unset, int]):
        properties (Union[Unset, str]):
        password (Union[Unset, ModelsKeyfactorAPISecret]):
    """

    id: Union[Unset, str] = UNSET
    container_id: Union[Unset, int] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    properties: Union[Unset, str] = UNSET
    password: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        container_id = self.container_id
        cert_store_type = self.cert_store_type
        properties = self.properties
        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if container_id is not UNSET:
            field_dict["ContainerId"] = container_id
        if cert_store_type is not UNSET:
            field_dict["CertStoreType"] = cert_store_type
        if properties is not UNSET:
            field_dict["Properties"] = properties
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        container_id = d.pop("ContainerId", UNSET)

        cert_store_type = d.pop("CertStoreType", UNSET)

        properties = d.pop("Properties", UNSET)

        _password = d.pop("Password", UNSET)
        password: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = ModelsKeyfactorAPISecret.from_dict(_password)

        keyfactor_api_models_certificate_stores_certificate_store_approve_request = cls(
            id=id,
            container_id=container_id,
            cert_store_type=cert_store_type,
            properties=properties,
            password=password,
        )

        keyfactor_api_models_certificate_stores_certificate_store_approve_request.additional_properties = d
        return keyfactor_api_models_certificate_stores_certificate_store_approve_request

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
