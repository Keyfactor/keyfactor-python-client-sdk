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

from ..models.models_ssl_endpoint_history_response_certificate_model import (
    ModelsSSLEndpointHistoryResponseCertificateModel,
)
from ..models.models_ssl_endpoint_history_response_job_type import ModelsSSLEndpointHistoryResponseJobType
from ..models.models_ssl_endpoint_history_response_probe_type import ModelsSSLEndpointHistoryResponseProbeType
from ..models.models_ssl_endpoint_history_response_status import ModelsSSLEndpointHistoryResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSLEndpointHistoryResponse")


@attr.s(auto_attribs=True)
class ModelsSSLEndpointHistoryResponse:
    """
    Attributes:
        history_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        endpoint_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        audit_id (Union[Unset, int]):
        timestamp (Union[Unset, datetime.datetime]):
        status (Union[Unset, ModelsSSLEndpointHistoryResponseStatus]):
        job_type (Union[Unset, ModelsSSLEndpointHistoryResponseJobType]):
        probe_type (Union[Unset, ModelsSSLEndpointHistoryResponseProbeType]):
        reverse_dns (Union[Unset, str]):
        history_certificates (Union[Unset, List[ModelsSSLEndpointHistoryResponseCertificateModel]]):
    """

    history_id: Union[Unset, str] = UNSET
    endpoint_id: Union[Unset, str] = UNSET
    audit_id: Union[Unset, int] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ModelsSSLEndpointHistoryResponseStatus] = UNSET
    job_type: Union[Unset, ModelsSSLEndpointHistoryResponseJobType] = UNSET
    probe_type: Union[Unset, ModelsSSLEndpointHistoryResponseProbeType] = UNSET
    reverse_dns: Union[Unset, str] = UNSET
    history_certificates: Union[Unset, List[ModelsSSLEndpointHistoryResponseCertificateModel]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        history_id = self.history_id
        endpoint_id = self.endpoint_id
        audit_id = self.audit_id
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        job_type: Union[Unset, int] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        probe_type: Union[Unset, int] = UNSET
        if not isinstance(self.probe_type, Unset):
            probe_type = self.probe_type.value

        reverse_dns = self.reverse_dns
        history_certificates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history_certificates, Unset):
            history_certificates = []
            for history_certificates_item_data in self.history_certificates:
                history_certificates_item = history_certificates_item_data.to_dict()

                history_certificates.append(history_certificates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if history_id is not UNSET:
            field_dict["HistoryId"] = history_id
        if endpoint_id is not UNSET:
            field_dict["EndpointId"] = endpoint_id
        if audit_id is not UNSET:
            field_dict["AuditId"] = audit_id
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp
        if status is not UNSET:
            field_dict["Status"] = status
        if job_type is not UNSET:
            field_dict["JobType"] = job_type
        if probe_type is not UNSET:
            field_dict["ProbeType"] = probe_type
        if reverse_dns is not UNSET:
            field_dict["ReverseDNS"] = reverse_dns
        if history_certificates is not UNSET:
            field_dict["HistoryCertificates"] = history_certificates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        history_id = d.pop("HistoryId", UNSET)

        endpoint_id = d.pop("EndpointId", UNSET)

        audit_id = d.pop("AuditId", UNSET)

        _timestamp = d.pop("Timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ModelsSSLEndpointHistoryResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ModelsSSLEndpointHistoryResponseStatus(_status)

        _job_type = d.pop("JobType", UNSET)
        job_type: Union[Unset, ModelsSSLEndpointHistoryResponseJobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = ModelsSSLEndpointHistoryResponseJobType(_job_type)

        _probe_type = d.pop("ProbeType", UNSET)
        probe_type: Union[Unset, ModelsSSLEndpointHistoryResponseProbeType]
        if isinstance(_probe_type, Unset):
            probe_type = UNSET
        else:
            probe_type = ModelsSSLEndpointHistoryResponseProbeType(_probe_type)

        reverse_dns = d.pop("ReverseDNS", UNSET)

        history_certificates = []
        _history_certificates = d.pop("HistoryCertificates", UNSET)
        for history_certificates_item_data in _history_certificates or []:
            history_certificates_item = ModelsSSLEndpointHistoryResponseCertificateModel.from_dict(
                history_certificates_item_data
            )

            history_certificates.append(history_certificates_item)

        models_ssl_endpoint_history_response = cls(
            history_id=history_id,
            endpoint_id=endpoint_id,
            audit_id=audit_id,
            timestamp=timestamp,
            status=status,
            job_type=job_type,
            probe_type=probe_type,
            reverse_dns=reverse_dns,
            history_certificates=history_certificates,
        )

        models_ssl_endpoint_history_response.additional_properties = d
        return models_ssl_endpoint_history_response

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
