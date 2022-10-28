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

from ..models.keyfactor_api_models_certificate_stores_reenrollment_request_job_properties import (
    KeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificateStoresReenrollmentRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificateStoresReenrollmentRequest:
    """
    Attributes:
        keystore_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        subject_name (Union[Unset, str]):
        agent_guid (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        alias (Union[Unset, str]):
        job_properties (Union[Unset, KeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties]):
        certificate_authority (Union[Unset, str]):
        certificate_template (Union[Unset, str]):
    """

    keystore_id: Union[Unset, str] = UNSET
    subject_name: Union[Unset, str] = UNSET
    agent_guid: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    job_properties: Union[Unset, KeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties] = UNSET
    certificate_authority: Union[Unset, str] = UNSET
    certificate_template: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keystore_id = self.keystore_id
        subject_name = self.subject_name
        agent_guid = self.agent_guid
        alias = self.alias
        job_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_properties, Unset):
            job_properties = self.job_properties.to_dict()

        certificate_authority = self.certificate_authority
        certificate_template = self.certificate_template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keystore_id is not UNSET:
            field_dict["KeystoreId"] = keystore_id
        if subject_name is not UNSET:
            field_dict["SubjectName"] = subject_name
        if agent_guid is not UNSET:
            field_dict["AgentGuid"] = agent_guid
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if job_properties is not UNSET:
            field_dict["JobProperties"] = job_properties
        if certificate_authority is not UNSET:
            field_dict["CertificateAuthority"] = certificate_authority
        if certificate_template is not UNSET:
            field_dict["CertificateTemplate"] = certificate_template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keystore_id = d.pop("KeystoreId", UNSET)

        subject_name = d.pop("SubjectName", UNSET)

        agent_guid = d.pop("AgentGuid", UNSET)

        alias = d.pop("Alias", UNSET)

        _job_properties = d.pop("JobProperties", UNSET)
        job_properties: Union[Unset, KeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties]
        if isinstance(_job_properties, Unset):
            job_properties = UNSET
        else:
            job_properties = KeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties.from_dict(
                _job_properties
            )

        certificate_authority = d.pop("CertificateAuthority", UNSET)

        certificate_template = d.pop("CertificateTemplate", UNSET)

        keyfactor_api_models_certificate_stores_reenrollment_request = cls(
            keystore_id=keystore_id,
            subject_name=subject_name,
            agent_guid=agent_guid,
            alias=alias,
            job_properties=job_properties,
            certificate_authority=certificate_authority,
            certificate_template=certificate_template,
        )

        keyfactor_api_models_certificate_stores_reenrollment_request.additional_properties = d
        return keyfactor_api_models_certificate_stores_reenrollment_request

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
