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

from ..models.models_certificate_location_specifier_job_fields import ModelsCertificateLocationSpecifierJobFields
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateLocationSpecifier")


@attr.s(auto_attribs=True)
class ModelsCertificateLocationSpecifier:
    """
    Attributes:
        alias (Union[Unset, str]):
        certificate_store_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        job_fields (Union[Unset, ModelsCertificateLocationSpecifierJobFields]):
    """

    alias: Union[Unset, str] = UNSET
    certificate_store_id: Union[Unset, str] = UNSET
    job_fields: Union[Unset, ModelsCertificateLocationSpecifierJobFields] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias = self.alias
        certificate_store_id = self.certificate_store_id
        job_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = self.job_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if certificate_store_id is not UNSET:
            field_dict["CertificateStoreId"] = certificate_store_id
        if job_fields is not UNSET:
            field_dict["JobFields"] = job_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alias = d.pop("Alias", UNSET)

        certificate_store_id = d.pop("CertificateStoreId", UNSET)

        _job_fields = d.pop("JobFields", UNSET)
        job_fields: Union[Unset, ModelsCertificateLocationSpecifierJobFields]
        if isinstance(_job_fields, Unset):
            job_fields = UNSET
        else:
            job_fields = ModelsCertificateLocationSpecifierJobFields.from_dict(_job_fields)

        models_certificate_location_specifier = cls(
            alias=alias,
            certificate_store_id=certificate_store_id,
            job_fields=job_fields,
        )

        models_certificate_location_specifier.additional_properties = d
        return models_certificate_location_specifier

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
