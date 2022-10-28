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

from ..models.models_enrollment_csr_enrollment_response_metadata import ModelsEnrollmentCSREnrollmentResponseMetadata
from ..models.models_pkcs_10_certificate_response import ModelsPkcs10CertificateResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsEnrollmentCSREnrollmentResponse")


@attr.s(auto_attribs=True)
class ModelsEnrollmentCSREnrollmentResponse:
    """
    Attributes:
        certificate_information (Union[Unset, ModelsPkcs10CertificateResponse]):
        metadata (Union[Unset, ModelsEnrollmentCSREnrollmentResponseMetadata]):
    """

    certificate_information: Union[Unset, ModelsPkcs10CertificateResponse] = UNSET
    metadata: Union[Unset, ModelsEnrollmentCSREnrollmentResponseMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificate_information, Unset):
            certificate_information = self.certificate_information.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_information is not UNSET:
            field_dict["CertificateInformation"] = certificate_information
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _certificate_information = d.pop("CertificateInformation", UNSET)
        certificate_information: Union[Unset, ModelsPkcs10CertificateResponse]
        if isinstance(_certificate_information, Unset):
            certificate_information = UNSET
        else:
            certificate_information = ModelsPkcs10CertificateResponse.from_dict(_certificate_information)

        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, ModelsEnrollmentCSREnrollmentResponseMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsEnrollmentCSREnrollmentResponseMetadata.from_dict(_metadata)

        models_enrollment_csr_enrollment_response = cls(
            certificate_information=certificate_information,
            metadata=metadata,
        )

        models_enrollment_csr_enrollment_response.additional_properties = d
        return models_enrollment_csr_enrollment_response

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
