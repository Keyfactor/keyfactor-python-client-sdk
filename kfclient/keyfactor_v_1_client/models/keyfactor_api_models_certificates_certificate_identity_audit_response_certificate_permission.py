# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission:
    """Represents a permission granted to an account for a certificate

    Attributes:
        name (Union[Unset, str]): The name of the permission
        granted_by (Union[Unset, List[str]]): A list of roles or collections that grant the given permission
    """

    name: Union[Unset, str] = UNSET
    granted_by: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        granted_by: Union[Unset, List[str]] = UNSET
        if not isinstance(self.granted_by, Unset):
            granted_by = self.granted_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if granted_by is not UNSET:
            field_dict["GrantedBy"] = granted_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        granted_by = cast(List[str], d.pop("GrantedBy", UNSET))

        keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission = cls(
            name=name,
            granted_by=granted_by,
        )

        keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission.additional_properties = (
            d
        )
        return keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission

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
