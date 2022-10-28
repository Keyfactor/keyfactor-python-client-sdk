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

T = TypeVar("T", bound="KeyfactorApiModelsMonitoringOCSPParametersResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMonitoringOCSPParametersResponse:
    """
    Attributes:
        certificate_authority_id (Union[Unset, int]):
        authority_name (Union[Unset, str]):
        authority_name_id (Union[Unset, str]):
        authority_key_id (Union[Unset, str]):
        sample_serial_number (Union[Unset, str]):
    """

    certificate_authority_id: Union[Unset, int] = UNSET
    authority_name: Union[Unset, str] = UNSET
    authority_name_id: Union[Unset, str] = UNSET
    authority_key_id: Union[Unset, str] = UNSET
    sample_serial_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_authority_id = self.certificate_authority_id
        authority_name = self.authority_name
        authority_name_id = self.authority_name_id
        authority_key_id = self.authority_key_id
        sample_serial_number = self.sample_serial_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_authority_id is not UNSET:
            field_dict["CertificateAuthorityId"] = certificate_authority_id
        if authority_name is not UNSET:
            field_dict["AuthorityName"] = authority_name
        if authority_name_id is not UNSET:
            field_dict["AuthorityNameId"] = authority_name_id
        if authority_key_id is not UNSET:
            field_dict["AuthorityKeyId"] = authority_key_id
        if sample_serial_number is not UNSET:
            field_dict["SampleSerialNumber"] = sample_serial_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_authority_id = d.pop("CertificateAuthorityId", UNSET)

        authority_name = d.pop("AuthorityName", UNSET)

        authority_name_id = d.pop("AuthorityNameId", UNSET)

        authority_key_id = d.pop("AuthorityKeyId", UNSET)

        sample_serial_number = d.pop("SampleSerialNumber", UNSET)

        keyfactor_api_models_monitoring_ocsp_parameters_response = cls(
            certificate_authority_id=certificate_authority_id,
            authority_name=authority_name,
            authority_name_id=authority_name_id,
            authority_key_id=authority_key_id,
            sample_serial_number=sample_serial_number,
        )

        keyfactor_api_models_monitoring_ocsp_parameters_response.additional_properties = d
        return keyfactor_api_models_monitoring_ocsp_parameters_response

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
