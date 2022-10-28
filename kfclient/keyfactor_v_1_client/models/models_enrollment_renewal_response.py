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

T = TypeVar("T", bound="ModelsEnrollmentRenewalResponse")


@attr.s(auto_attribs=True)
class ModelsEnrollmentRenewalResponse:
    """
    Attributes:
        keyfactor_id (Union[Unset, int]):
        keyfactor_request_id (Union[Unset, int]):
        thumbprint (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        issuer_dn (Union[Unset, str]):
        request_disposition (Union[Unset, str]):
        disposition_message (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    keyfactor_id: Union[Unset, int] = UNSET
    keyfactor_request_id: Union[Unset, int] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    request_disposition: Union[Unset, str] = UNSET
    disposition_message: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keyfactor_id = self.keyfactor_id
        keyfactor_request_id = self.keyfactor_request_id
        thumbprint = self.thumbprint
        serial_number = self.serial_number
        issuer_dn = self.issuer_dn
        request_disposition = self.request_disposition
        disposition_message = self.disposition_message
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyfactor_id is not UNSET:
            field_dict["KeyfactorId"] = keyfactor_id
        if keyfactor_request_id is not UNSET:
            field_dict["KeyfactorRequestId"] = keyfactor_request_id
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if request_disposition is not UNSET:
            field_dict["RequestDisposition"] = request_disposition
        if disposition_message is not UNSET:
            field_dict["DispositionMessage"] = disposition_message
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyfactor_id = d.pop("KeyfactorId", UNSET)

        keyfactor_request_id = d.pop("KeyfactorRequestId", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        issuer_dn = d.pop("IssuerDN", UNSET)

        request_disposition = d.pop("RequestDisposition", UNSET)

        disposition_message = d.pop("DispositionMessage", UNSET)

        password = d.pop("Password", UNSET)

        models_enrollment_renewal_response = cls(
            keyfactor_id=keyfactor_id,
            keyfactor_request_id=keyfactor_request_id,
            thumbprint=thumbprint,
            serial_number=serial_number,
            issuer_dn=issuer_dn,
            request_disposition=request_disposition,
            disposition_message=disposition_message,
            password=password,
        )

        models_enrollment_renewal_response.additional_properties = d
        return models_enrollment_renewal_response

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
