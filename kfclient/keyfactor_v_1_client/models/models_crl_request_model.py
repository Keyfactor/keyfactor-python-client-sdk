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

T = TypeVar("T", bound="ModelsCRLRequestModel")


@attr.s(auto_attribs=True)
class ModelsCRLRequestModel:
    """
    Attributes:
        certificate_authority_logical_name (str):
        certificate_authority_host_name (Union[Unset, str]):
    """

    certificate_authority_logical_name: str
    certificate_authority_host_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_authority_logical_name = self.certificate_authority_logical_name
        certificate_authority_host_name = self.certificate_authority_host_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CertificateAuthorityLogicalName": certificate_authority_logical_name,
            }
        )
        if certificate_authority_host_name is not UNSET:
            field_dict["CertificateAuthorityHostName"] = certificate_authority_host_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_authority_logical_name = d.pop("CertificateAuthorityLogicalName")

        certificate_authority_host_name = d.pop("CertificateAuthorityHostName", UNSET)

        models_crl_request_model = cls(
            certificate_authority_logical_name=certificate_authority_logical_name,
            certificate_authority_host_name=certificate_authority_host_name,
        )

        models_crl_request_model.additional_properties = d
        return models_crl_request_model

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
