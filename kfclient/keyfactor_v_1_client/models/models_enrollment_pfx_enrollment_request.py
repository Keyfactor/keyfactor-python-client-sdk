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

from ..models.models_enrollment_pfx_enrollment_request_additional_enrollment_fields import (
    ModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields,
)
from ..models.models_enrollment_pfx_enrollment_request_metadata import ModelsEnrollmentPFXEnrollmentRequestMetadata
from ..models.models_enrollment_pfx_enrollment_request_sa_ns import ModelsEnrollmentPFXEnrollmentRequestSANs
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsEnrollmentPFXEnrollmentRequest")


@attr.s(auto_attribs=True)
class ModelsEnrollmentPFXEnrollmentRequest:
    """
    Example:
        {'CustomFriendlyName': '<custom name>', 'Password': '<pfx password>', 'PopulateMissingValuesFromAD': False,
            'Subject': '<certificate subject>', 'IncludeChain': True, 'RenewalCertificateId': 0, 'CertificateAuthority':
            '<host>\\<logical>', 'Timestamp': datetime.datetime(2022, 9, 22, 18, 9, 16, 719678,
            tzinfo=datetime.timezone.utc), 'Template': '<template short name>', 'SANs': {'ip4': ['192.168.2.2']}}

    Attributes:
        custom_friendly_name (Union[Unset, str]):
        password (Union[Unset, str]):
        populate_missing_values_from_ad (Union[Unset, bool]):
        subject (Union[Unset, str]):
        include_chain (Union[Unset, bool]):
        renewal_certificate_id (Union[Unset, int]):
        certificate_authority (Union[Unset, str]):
        metadata (Union[Unset, ModelsEnrollmentPFXEnrollmentRequestMetadata]):
        additional_enrollment_fields (Union[Unset, ModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields]):
        timestamp (Union[Unset, datetime.datetime]):
        template (Union[Unset, str]):
        sa_ns (Union[Unset, ModelsEnrollmentPFXEnrollmentRequestSANs]):
    """

    custom_friendly_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    populate_missing_values_from_ad: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    include_chain: Union[Unset, bool] = UNSET
    renewal_certificate_id: Union[Unset, int] = UNSET
    certificate_authority: Union[Unset, str] = UNSET
    metadata: Union[Unset, ModelsEnrollmentPFXEnrollmentRequestMetadata] = UNSET
    additional_enrollment_fields: Union[Unset, ModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    template: Union[Unset, str] = UNSET
    sa_ns: Union[Unset, ModelsEnrollmentPFXEnrollmentRequestSANs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_friendly_name = self.custom_friendly_name
        password = self.password
        populate_missing_values_from_ad = self.populate_missing_values_from_ad
        subject = self.subject
        include_chain = self.include_chain
        renewal_certificate_id = self.renewal_certificate_id
        certificate_authority = self.certificate_authority
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        additional_enrollment_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_enrollment_fields, Unset):
            additional_enrollment_fields = self.additional_enrollment_fields.to_dict()

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        template = self.template
        sa_ns: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sa_ns, Unset):
            sa_ns = self.sa_ns.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_friendly_name is not UNSET:
            field_dict["CustomFriendlyName"] = custom_friendly_name
        if password is not UNSET:
            field_dict["Password"] = password
        if populate_missing_values_from_ad is not UNSET:
            field_dict["PopulateMissingValuesFromAD"] = populate_missing_values_from_ad
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if include_chain is not UNSET:
            field_dict["IncludeChain"] = include_chain
        if renewal_certificate_id is not UNSET:
            field_dict["RenewalCertificateId"] = renewal_certificate_id
        if certificate_authority is not UNSET:
            field_dict["CertificateAuthority"] = certificate_authority
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if additional_enrollment_fields is not UNSET:
            field_dict["AdditionalEnrollmentFields"] = additional_enrollment_fields
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp
        if template is not UNSET:
            field_dict["Template"] = template
        if sa_ns is not UNSET:
            field_dict["SANs"] = sa_ns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_friendly_name = d.pop("CustomFriendlyName", UNSET)

        password = d.pop("Password", UNSET)

        populate_missing_values_from_ad = d.pop("PopulateMissingValuesFromAD", UNSET)

        subject = d.pop("Subject", UNSET)

        include_chain = d.pop("IncludeChain", UNSET)

        renewal_certificate_id = d.pop("RenewalCertificateId", UNSET)

        certificate_authority = d.pop("CertificateAuthority", UNSET)

        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, ModelsEnrollmentPFXEnrollmentRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsEnrollmentPFXEnrollmentRequestMetadata.from_dict(_metadata)

        _additional_enrollment_fields = d.pop("AdditionalEnrollmentFields", UNSET)
        additional_enrollment_fields: Union[Unset, ModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields]
        if isinstance(_additional_enrollment_fields, Unset):
            additional_enrollment_fields = UNSET
        else:
            additional_enrollment_fields = ModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields.from_dict(
                _additional_enrollment_fields
            )

        _timestamp = d.pop("Timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        template = d.pop("Template", UNSET)

        _sa_ns = d.pop("SANs", UNSET)
        sa_ns: Union[Unset, ModelsEnrollmentPFXEnrollmentRequestSANs]
        if isinstance(_sa_ns, Unset):
            sa_ns = UNSET
        else:
            sa_ns = ModelsEnrollmentPFXEnrollmentRequestSANs.from_dict(_sa_ns)

        models_enrollment_pfx_enrollment_request = cls(
            custom_friendly_name=custom_friendly_name,
            password=password,
            populate_missing_values_from_ad=populate_missing_values_from_ad,
            subject=subject,
            include_chain=include_chain,
            renewal_certificate_id=renewal_certificate_id,
            certificate_authority=certificate_authority,
            metadata=metadata,
            additional_enrollment_fields=additional_enrollment_fields,
            timestamp=timestamp,
            template=template,
            sa_ns=sa_ns,
        )

        models_enrollment_pfx_enrollment_request.additional_properties = d
        return models_enrollment_pfx_enrollment_request

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
