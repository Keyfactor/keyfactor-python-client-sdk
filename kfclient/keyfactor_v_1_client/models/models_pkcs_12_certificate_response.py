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

from ..models.models_pkcs_12_certificate_response_enrollment_context import (
    ModelsPkcs12CertificateResponseEnrollmentContext,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsPkcs12CertificateResponse")


@attr.s(auto_attribs=True)
class ModelsPkcs12CertificateResponse:
    """
    Attributes:
        serial_number (Union[Unset, str]):
        issuer_dn (Union[Unset, str]):
        thumbprint (Union[Unset, str]):
        keyfactor_id (Union[Unset, int]):
        pkcs_12_blob (Union[Unset, str]):
        password (Union[Unset, str]):
        keyfactor_request_id (Union[Unset, int]): The integer id of the certificate request in the Keyfactor database,
            if one exists.
        request_disposition (Union[Unset, str]):
        disposition_message (Union[Unset, str]):
        enrollment_context (Union[Unset, None, ModelsPkcs12CertificateResponseEnrollmentContext]):
    """

    serial_number: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    keyfactor_id: Union[Unset, int] = UNSET
    pkcs_12_blob: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    keyfactor_request_id: Union[Unset, int] = UNSET
    request_disposition: Union[Unset, str] = UNSET
    disposition_message: Union[Unset, str] = UNSET
    enrollment_context: Union[Unset, None, ModelsPkcs12CertificateResponseEnrollmentContext] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        serial_number = self.serial_number
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        keyfactor_id = self.keyfactor_id
        pkcs_12_blob = self.pkcs_12_blob
        password = self.password
        keyfactor_request_id = self.keyfactor_request_id
        request_disposition = self.request_disposition
        disposition_message = self.disposition_message
        enrollment_context: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_context, Unset):
            enrollment_context = self.enrollment_context.to_dict() if self.enrollment_context else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if keyfactor_id is not UNSET:
            field_dict["KeyfactorId"] = keyfactor_id
        if pkcs_12_blob is not UNSET:
            field_dict["Pkcs12Blob"] = pkcs_12_blob
        if password is not UNSET:
            field_dict["Password"] = password
        if keyfactor_request_id is not UNSET:
            field_dict["KeyfactorRequestId"] = keyfactor_request_id
        if request_disposition is not UNSET:
            field_dict["RequestDisposition"] = request_disposition
        if disposition_message is not UNSET:
            field_dict["DispositionMessage"] = disposition_message
        if enrollment_context is not UNSET:
            field_dict["EnrollmentContext"] = enrollment_context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        serial_number = d.pop("SerialNumber", UNSET)

        issuer_dn = d.pop("IssuerDN", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        keyfactor_id = d.pop("KeyfactorId", UNSET)

        pkcs_12_blob = d.pop("Pkcs12Blob", UNSET)

        password = d.pop("Password", UNSET)

        keyfactor_request_id = d.pop("KeyfactorRequestId", UNSET)

        request_disposition = d.pop("RequestDisposition", UNSET)

        disposition_message = d.pop("DispositionMessage", UNSET)

        _enrollment_context = d.pop("EnrollmentContext", UNSET)
        enrollment_context: Union[Unset, None, ModelsPkcs12CertificateResponseEnrollmentContext]
        if _enrollment_context is None:
            enrollment_context = None
        elif isinstance(_enrollment_context, Unset):
            enrollment_context = UNSET
        else:
            enrollment_context = ModelsPkcs12CertificateResponseEnrollmentContext.from_dict(_enrollment_context)

        models_pkcs_12_certificate_response = cls(
            serial_number=serial_number,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            keyfactor_id=keyfactor_id,
            pkcs_12_blob=pkcs_12_blob,
            password=password,
            keyfactor_request_id=keyfactor_request_id,
            request_disposition=request_disposition,
            disposition_message=disposition_message,
            enrollment_context=enrollment_context,
        )

        models_pkcs_12_certificate_response.additional_properties = d
        return models_pkcs_12_certificate_response

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
