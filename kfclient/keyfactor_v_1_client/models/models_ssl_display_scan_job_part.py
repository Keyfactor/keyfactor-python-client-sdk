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

from ..models.models_ssl_display_scan_job_part_status import ModelsSSLDisplayScanJobPartStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSLDisplayScanJobPart")


@attr.s(auto_attribs=True)
class ModelsSSLDisplayScanJobPart:
    """
    Attributes:
        scan_job_part_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        agent (Union[Unset, str]):
        status (Union[Unset, ModelsSSLDisplayScanJobPartStatus]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        endpoint_count (Union[Unset, int]):
    """

    scan_job_part_id: Union[Unset, str] = UNSET
    agent: Union[Unset, str] = UNSET
    status: Union[Unset, ModelsSSLDisplayScanJobPartStatus] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    endpoint_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan_job_part_id = self.scan_job_part_id
        agent = self.agent
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()[:-6]+'Z'

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()[:-6]+'Z'

        endpoint_count = self.endpoint_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_job_part_id is not UNSET:
            field_dict["ScanJobPartId"] = scan_job_part_id
        if agent is not UNSET:
            field_dict["Agent"] = agent
        if status is not UNSET:
            field_dict["Status"] = status
        if start_time is not UNSET:
            field_dict["StartTime"] = start_time
        if end_time is not UNSET:
            field_dict["EndTime"] = end_time
        if endpoint_count is not UNSET:
            field_dict["EndpointCount"] = endpoint_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scan_job_part_id = d.pop("ScanJobPartId", UNSET)

        agent = d.pop("Agent", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, ModelsSSLDisplayScanJobPartStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ModelsSSLDisplayScanJobPartStatus(_status)

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

        endpoint_count = d.pop("EndpointCount", UNSET)

        models_ssl_display_scan_job_part = cls(
            scan_job_part_id=scan_job_part_id,
            agent=agent,
            status=status,
            start_time=start_time,
            end_time=end_time,
            endpoint_count=endpoint_count,
        )

        models_ssl_display_scan_job_part.additional_properties = d
        return models_ssl_display_scan_job_part

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
