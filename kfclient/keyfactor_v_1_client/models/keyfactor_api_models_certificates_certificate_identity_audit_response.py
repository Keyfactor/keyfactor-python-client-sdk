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

from ..models.keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission import (
    KeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificatesCertificateIdentityAuditResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificatesCertificateIdentityAuditResponse:
    """Represents an account with a list of permission granted to it on a given certificate by either a role or collection

    Attributes:
        id (Union[Unset, int]): Id of the account represented by the audit response
        account_name (Union[Unset, str]): Name of the account represented by the audit response
        identity_type (Union[Unset, str]): The type of account represented by the audit response (User or Group)
        sid (Union[Unset, str]): The SID of the account represented by the audit reponse
        permissions (Union[Unset,
            List[KeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission]]): Permissions granted
            to the account represented by the audit reponse on the specified certifcate
    """

    id: Union[Unset, int] = UNSET
    account_name: Union[Unset, str] = UNSET
    identity_type: Union[Unset, str] = UNSET
    sid: Union[Unset, str] = UNSET
    permissions: Union[
        Unset, List[KeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission]
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_name = self.account_name
        identity_type = self.identity_type
        sid = self.sid
        permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()

                permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if account_name is not UNSET:
            field_dict["AccountName"] = account_name
        if identity_type is not UNSET:
            field_dict["IdentityType"] = identity_type
        if sid is not UNSET:
            field_dict["SID"] = sid
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        account_name = d.pop("AccountName", UNSET)

        identity_type = d.pop("IdentityType", UNSET)

        sid = d.pop("SID", UNSET)

        permissions = []
        _permissions = d.pop("Permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = (
                KeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission.from_dict(
                    permissions_item_data
                )
            )

            permissions.append(permissions_item)

        keyfactor_api_models_certificates_certificate_identity_audit_response = cls(
            id=id,
            account_name=account_name,
            identity_type=identity_type,
            sid=sid,
            permissions=permissions,
        )

        keyfactor_api_models_certificates_certificate_identity_audit_response.additional_properties = d
        return keyfactor_api_models_certificates_certificate_identity_audit_response

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
