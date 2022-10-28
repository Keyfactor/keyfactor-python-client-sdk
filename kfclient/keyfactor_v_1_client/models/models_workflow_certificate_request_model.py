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

from ..models.models_workflow_certificate_request_model_metadata import ModelsWorkflowCertificateRequestModelMetadata
from ..models.models_workflow_certificate_request_model_state import ModelsWorkflowCertificateRequestModelState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsWorkflowCertificateRequestModel")


@attr.s(auto_attribs=True)
class ModelsWorkflowCertificateRequestModel:
    """
    Attributes:
        id (Union[Unset, int]):
        ca_request_id (Union[Unset, str]):
        common_name (Union[Unset, str]):
        distinguished_name (Union[Unset, str]):
        submission_date (Union[Unset, datetime.datetime]):
        certificate_authority (Union[Unset, str]):
        template (Union[Unset, str]):
        requester (Union[Unset, str]):
        state (Union[Unset, ModelsWorkflowCertificateRequestModelState]):
        state_string (Union[Unset, str]):
        metadata (Union[Unset, ModelsWorkflowCertificateRequestModelMetadata]):
    """

    id: Union[Unset, int] = UNSET
    ca_request_id: Union[Unset, str] = UNSET
    common_name: Union[Unset, str] = UNSET
    distinguished_name: Union[Unset, str] = UNSET
    submission_date: Union[Unset, datetime.datetime] = UNSET
    certificate_authority: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    requester: Union[Unset, str] = UNSET
    state: Union[Unset, ModelsWorkflowCertificateRequestModelState] = UNSET
    state_string: Union[Unset, str] = UNSET
    metadata: Union[Unset, ModelsWorkflowCertificateRequestModelMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        ca_request_id = self.ca_request_id
        common_name = self.common_name
        distinguished_name = self.distinguished_name
        submission_date: Union[Unset, str] = UNSET
        if not isinstance(self.submission_date, Unset):
            submission_date = self.submission_date.isoformat()[:-6]+'Z'

        certificate_authority = self.certificate_authority
        template = self.template
        requester = self.requester
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_string = self.state_string
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if ca_request_id is not UNSET:
            field_dict["CARequestId"] = ca_request_id
        if common_name is not UNSET:
            field_dict["CommonName"] = common_name
        if distinguished_name is not UNSET:
            field_dict["DistinguishedName"] = distinguished_name
        if submission_date is not UNSET:
            field_dict["SubmissionDate"] = submission_date
        if certificate_authority is not UNSET:
            field_dict["CertificateAuthority"] = certificate_authority
        if template is not UNSET:
            field_dict["Template"] = template
        if requester is not UNSET:
            field_dict["Requester"] = requester
        if state is not UNSET:
            field_dict["State"] = state
        if state_string is not UNSET:
            field_dict["StateString"] = state_string
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        ca_request_id = d.pop("CARequestId", UNSET)

        common_name = d.pop("CommonName", UNSET)

        distinguished_name = d.pop("DistinguishedName", UNSET)

        _submission_date = d.pop("SubmissionDate", UNSET)
        submission_date: Union[Unset, datetime.datetime]
        if isinstance(_submission_date, Unset):
            submission_date = UNSET
        else:
            submission_date = isoparse(_submission_date)

        certificate_authority = d.pop("CertificateAuthority", UNSET)

        template = d.pop("Template", UNSET)

        requester = d.pop("Requester", UNSET)

        _state = d.pop("State", UNSET)
        state: Union[Unset, ModelsWorkflowCertificateRequestModelState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ModelsWorkflowCertificateRequestModelState(_state)

        state_string = d.pop("StateString", UNSET)

        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, ModelsWorkflowCertificateRequestModelMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsWorkflowCertificateRequestModelMetadata.from_dict(_metadata)

        models_workflow_certificate_request_model = cls(
            id=id,
            ca_request_id=ca_request_id,
            common_name=common_name,
            distinguished_name=distinguished_name,
            submission_date=submission_date,
            certificate_authority=certificate_authority,
            template=template,
            requester=requester,
            state=state,
            state_string=state_string,
            metadata=metadata,
        )

        models_workflow_certificate_request_model.additional_properties = d
        return models_workflow_certificate_request_model

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
