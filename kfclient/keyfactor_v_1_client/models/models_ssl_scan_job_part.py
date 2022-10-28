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

from ..models.models_ssl_scan_job_part_definition import ModelsSSLScanJobPartDefinition
from ..models.models_ssl_scan_job_part_status import ModelsSSLScanJobPartStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSLScanJobPart")


@attr.s(auto_attribs=True)
class ModelsSSLScanJobPart:
    """
    Attributes:
        scan_job_part_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        logical_scan_job_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        agent_job_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        estimated_endpoint_count (Union[Unset, int]):
        status (Union[Unset, ModelsSSLScanJobPartStatus]):
        stat_total_endpoint_count (Union[Unset, int]):
        stat_timed_out_connecting_count (Union[Unset, int]):
        stat_connection_refused_count (Union[Unset, int]):
        stat_timed_out_downloading_count (Union[Unset, int]):
        stat_exception_downloading_count (Union[Unset, int]):
        stat_not_ssl_count (Union[Unset, int]):
        stat_bad_ssl_handshake_count (Union[Unset, int]):
        stat_certificate_found_count (Union[Unset, int]):
        stat_no_certificate_count (Union[Unset, int]):
        scan_job_part_definitions (Union[Unset, List[ModelsSSLScanJobPartDefinition]]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
    """

    scan_job_part_id: Union[Unset, str] = UNSET
    logical_scan_job_id: Union[Unset, str] = UNSET
    agent_job_id: Union[Unset, str] = UNSET
    estimated_endpoint_count: Union[Unset, int] = UNSET
    status: Union[Unset, ModelsSSLScanJobPartStatus] = UNSET
    stat_total_endpoint_count: Union[Unset, int] = UNSET
    stat_timed_out_connecting_count: Union[Unset, int] = UNSET
    stat_connection_refused_count: Union[Unset, int] = UNSET
    stat_timed_out_downloading_count: Union[Unset, int] = UNSET
    stat_exception_downloading_count: Union[Unset, int] = UNSET
    stat_not_ssl_count: Union[Unset, int] = UNSET
    stat_bad_ssl_handshake_count: Union[Unset, int] = UNSET
    stat_certificate_found_count: Union[Unset, int] = UNSET
    stat_no_certificate_count: Union[Unset, int] = UNSET
    scan_job_part_definitions: Union[Unset, List[ModelsSSLScanJobPartDefinition]] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan_job_part_id = self.scan_job_part_id
        logical_scan_job_id = self.logical_scan_job_id
        agent_job_id = self.agent_job_id
        estimated_endpoint_count = self.estimated_endpoint_count
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        stat_total_endpoint_count = self.stat_total_endpoint_count
        stat_timed_out_connecting_count = self.stat_timed_out_connecting_count
        stat_connection_refused_count = self.stat_connection_refused_count
        stat_timed_out_downloading_count = self.stat_timed_out_downloading_count
        stat_exception_downloading_count = self.stat_exception_downloading_count
        stat_not_ssl_count = self.stat_not_ssl_count
        stat_bad_ssl_handshake_count = self.stat_bad_ssl_handshake_count
        stat_certificate_found_count = self.stat_certificate_found_count
        stat_no_certificate_count = self.stat_no_certificate_count
        scan_job_part_definitions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scan_job_part_definitions, Unset):
            scan_job_part_definitions = []
            for scan_job_part_definitions_item_data in self.scan_job_part_definitions:
                scan_job_part_definitions_item = scan_job_part_definitions_item_data.to_dict()

                scan_job_part_definitions.append(scan_job_part_definitions_item)

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()[:-6]+'Z'

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_job_part_id is not UNSET:
            field_dict["ScanJobPartId"] = scan_job_part_id
        if logical_scan_job_id is not UNSET:
            field_dict["LogicalScanJobId"] = logical_scan_job_id
        if agent_job_id is not UNSET:
            field_dict["AgentJobId"] = agent_job_id
        if estimated_endpoint_count is not UNSET:
            field_dict["EstimatedEndpointCount"] = estimated_endpoint_count
        if status is not UNSET:
            field_dict["Status"] = status
        if stat_total_endpoint_count is not UNSET:
            field_dict["StatTotalEndpointCount"] = stat_total_endpoint_count
        if stat_timed_out_connecting_count is not UNSET:
            field_dict["StatTimedOutConnectingCount"] = stat_timed_out_connecting_count
        if stat_connection_refused_count is not UNSET:
            field_dict["StatConnectionRefusedCount"] = stat_connection_refused_count
        if stat_timed_out_downloading_count is not UNSET:
            field_dict["StatTimedOutDownloadingCount"] = stat_timed_out_downloading_count
        if stat_exception_downloading_count is not UNSET:
            field_dict["StatExceptionDownloadingCount"] = stat_exception_downloading_count
        if stat_not_ssl_count is not UNSET:
            field_dict["StatNotSslCount"] = stat_not_ssl_count
        if stat_bad_ssl_handshake_count is not UNSET:
            field_dict["StatBadSslHandshakeCount"] = stat_bad_ssl_handshake_count
        if stat_certificate_found_count is not UNSET:
            field_dict["StatCertificateFoundCount"] = stat_certificate_found_count
        if stat_no_certificate_count is not UNSET:
            field_dict["StatNoCertificateCount"] = stat_no_certificate_count
        if scan_job_part_definitions is not UNSET:
            field_dict["ScanJobPartDefinitions"] = scan_job_part_definitions
        if start_time is not UNSET:
            field_dict["StartTime"] = start_time
        if end_time is not UNSET:
            field_dict["EndTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scan_job_part_id = d.pop("ScanJobPartId", UNSET)

        logical_scan_job_id = d.pop("LogicalScanJobId", UNSET)

        agent_job_id = d.pop("AgentJobId", UNSET)

        estimated_endpoint_count = d.pop("EstimatedEndpointCount", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ModelsSSLScanJobPartStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ModelsSSLScanJobPartStatus(_status)

        stat_total_endpoint_count = d.pop("StatTotalEndpointCount", UNSET)

        stat_timed_out_connecting_count = d.pop("StatTimedOutConnectingCount", UNSET)

        stat_connection_refused_count = d.pop("StatConnectionRefusedCount", UNSET)

        stat_timed_out_downloading_count = d.pop("StatTimedOutDownloadingCount", UNSET)

        stat_exception_downloading_count = d.pop("StatExceptionDownloadingCount", UNSET)

        stat_not_ssl_count = d.pop("StatNotSslCount", UNSET)

        stat_bad_ssl_handshake_count = d.pop("StatBadSslHandshakeCount", UNSET)

        stat_certificate_found_count = d.pop("StatCertificateFoundCount", UNSET)

        stat_no_certificate_count = d.pop("StatNoCertificateCount", UNSET)

        scan_job_part_definitions = []
        _scan_job_part_definitions = d.pop("ScanJobPartDefinitions", UNSET)
        for scan_job_part_definitions_item_data in _scan_job_part_definitions or []:
            scan_job_part_definitions_item = ModelsSSLScanJobPartDefinition.from_dict(
                scan_job_part_definitions_item_data
            )

            scan_job_part_definitions.append(scan_job_part_definitions_item)

        _start_time = d.pop("StartTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("EndTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        models_ssl_scan_job_part = cls(
            scan_job_part_id=scan_job_part_id,
            logical_scan_job_id=logical_scan_job_id,
            agent_job_id=agent_job_id,
            estimated_endpoint_count=estimated_endpoint_count,
            status=status,
            stat_total_endpoint_count=stat_total_endpoint_count,
            stat_timed_out_connecting_count=stat_timed_out_connecting_count,
            stat_connection_refused_count=stat_connection_refused_count,
            stat_timed_out_downloading_count=stat_timed_out_downloading_count,
            stat_exception_downloading_count=stat_exception_downloading_count,
            stat_not_ssl_count=stat_not_ssl_count,
            stat_bad_ssl_handshake_count=stat_bad_ssl_handshake_count,
            stat_certificate_found_count=stat_certificate_found_count,
            stat_no_certificate_count=stat_no_certificate_count,
            scan_job_part_definitions=scan_job_part_definitions,
            start_time=start_time,
            end_time=end_time,
        )

        models_ssl_scan_job_part.additional_properties = d
        return models_ssl_scan_job_part

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
