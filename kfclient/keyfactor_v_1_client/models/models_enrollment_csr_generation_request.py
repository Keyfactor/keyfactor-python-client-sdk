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

from ..models.models_enrollment_csr_generation_request_sa_ns import ModelsEnrollmentCSRGenerationRequestSANs
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsEnrollmentCSRGenerationRequest")


@attr.s(auto_attribs=True)
class ModelsEnrollmentCSRGenerationRequest:
    """
    Attributes:
        subject (str): Subject for the requested certificate
        key_type (str): Certificate key type [RSA, ECC]
        key_length (int): Size of the certificate key (ex: RSA 1024, 2048, 4096/ECC 256, 384, 521)
        template (Union[Unset, str]):
        sa_ns (Union[Unset, ModelsEnrollmentCSRGenerationRequestSANs]):
    """

    subject: str
    key_type: str
    key_length: int
    template: Union[Unset, str] = UNSET
    sa_ns: Union[Unset, ModelsEnrollmentCSRGenerationRequestSANs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        key_type = self.key_type
        key_length = self.key_length
        template = self.template
        sa_ns: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sa_ns, Unset):
            sa_ns = self.sa_ns.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Subject": subject,
                "KeyType": key_type,
                "KeyLength": key_length,
            }
        )
        if template is not UNSET:
            field_dict["Template"] = template
        if sa_ns is not UNSET:
            field_dict["SANs"] = sa_ns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("Subject")

        key_type = d.pop("KeyType")

        key_length = d.pop("KeyLength")

        template = d.pop("Template", UNSET)

        _sa_ns = d.pop("SANs", UNSET)
        sa_ns: Union[Unset, ModelsEnrollmentCSRGenerationRequestSANs]
        if isinstance(_sa_ns, Unset):
            sa_ns = UNSET
        else:
            sa_ns = ModelsEnrollmentCSRGenerationRequestSANs.from_dict(_sa_ns)

        models_enrollment_csr_generation_request = cls(
            subject=subject,
            key_type=key_type,
            key_length=key_length,
            template=template,
            sa_ns=sa_ns,
        )

        models_enrollment_csr_generation_request.additional_properties = d
        return models_enrollment_csr_generation_request

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
