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
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateAuthoritiesCertificateAuthorityAuthCertificate")


@attr.s(auto_attribs=True)
class ModelsCertificateAuthoritiesCertificateAuthorityAuthCertificate:
    """
    Attributes:
        issued_dn (Union[Unset, str]):
        issuer_dn (Union[Unset, str]):
        thumbprint (Union[Unset, str]):
        expiration_date (Union[Unset, datetime.datetime]):
    """

    issued_dn: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issued_dn = self.issued_dn
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issued_dn is not UNSET:
            field_dict["IssuedDN"] = issued_dn
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if expiration_date is not UNSET:
            field_dict["ExpirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issued_dn = d.pop("IssuedDN", UNSET)

        issuer_dn = d.pop("IssuerDN", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        _expiration_date = d.pop("ExpirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        models_certificate_authorities_certificate_authority_auth_certificate = cls(
            issued_dn=issued_dn,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            expiration_date=expiration_date,
        )

        models_certificate_authorities_certificate_authority_auth_certificate.additional_properties = d
        return models_certificate_authorities_certificate_authority_auth_certificate

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
