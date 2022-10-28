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

from ..models.models_subject_alternative_name import ModelsSubjectAlternativeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSLEndpointHistoryResponseCertificateModel")


@attr.s(auto_attribs=True)
class ModelsSSLEndpointHistoryResponseCertificateModel:
    """
    Attributes:
        id (Union[Unset, int]):
        issued_dn (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        not_before (Union[Unset, datetime.datetime]):
        not_after (Union[Unset, datetime.datetime]):
        signing_algorithm (Union[Unset, str]):
        thumbprint (Union[Unset, str]):
        issuer_dn (Union[Unset, str]):
        issued_cn (Union[Unset, str]):
        subject_alt_name_elements (Union[Unset, List[ModelsSubjectAlternativeName]]):
    """

    id: Union[Unset, int] = UNSET
    issued_dn: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    signing_algorithm: Union[Unset, str] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    issued_cn: Union[Unset, str] = UNSET
    subject_alt_name_elements: Union[Unset, List[ModelsSubjectAlternativeName]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        issued_dn = self.issued_dn
        serial_number = self.serial_number
        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()[:-6]+'Z'

        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()[:-6]+'Z'

        signing_algorithm = self.signing_algorithm
        thumbprint = self.thumbprint
        issuer_dn = self.issuer_dn
        issued_cn = self.issued_cn
        subject_alt_name_elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subject_alt_name_elements, Unset):
            subject_alt_name_elements = []
            for subject_alt_name_elements_item_data in self.subject_alt_name_elements:
                subject_alt_name_elements_item = subject_alt_name_elements_item_data.to_dict()

                subject_alt_name_elements.append(subject_alt_name_elements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if issued_dn is not UNSET:
            field_dict["IssuedDN"] = issued_dn
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if not_before is not UNSET:
            field_dict["NotBefore"] = not_before
        if not_after is not UNSET:
            field_dict["NotAfter"] = not_after
        if signing_algorithm is not UNSET:
            field_dict["SigningAlgorithm"] = signing_algorithm
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if issued_cn is not UNSET:
            field_dict["IssuedCN"] = issued_cn
        if subject_alt_name_elements is not UNSET:
            field_dict["SubjectAltNameElements"] = subject_alt_name_elements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        issued_dn = d.pop("IssuedDN", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        _not_before = d.pop("NotBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _not_after = d.pop("NotAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        signing_algorithm = d.pop("SigningAlgorithm", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        issuer_dn = d.pop("IssuerDN", UNSET)

        issued_cn = d.pop("IssuedCN", UNSET)

        subject_alt_name_elements = []
        _subject_alt_name_elements = d.pop("SubjectAltNameElements", UNSET)
        for subject_alt_name_elements_item_data in _subject_alt_name_elements or []:
            subject_alt_name_elements_item = ModelsSubjectAlternativeName.from_dict(subject_alt_name_elements_item_data)

            subject_alt_name_elements.append(subject_alt_name_elements_item)

        models_ssl_endpoint_history_response_certificate_model = cls(
            id=id,
            issued_dn=issued_dn,
            serial_number=serial_number,
            not_before=not_before,
            not_after=not_after,
            signing_algorithm=signing_algorithm,
            thumbprint=thumbprint,
            issuer_dn=issuer_dn,
            issued_cn=issued_cn,
            subject_alt_name_elements=subject_alt_name_elements,
        )

        models_ssl_endpoint_history_response_certificate_model.additional_properties = d
        return models_ssl_endpoint_history_response_certificate_model

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
