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
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.keyfactor_api_models_ssl_network_query_response_discover_status import (
    KeyfactorApiModelsSslNetworkQueryResponseDiscoverStatus,
)
from ..models.keyfactor_api_models_ssl_network_query_response_monitor_status import (
    KeyfactorApiModelsSslNetworkQueryResponseMonitorStatus,
)
from ..models.keyfactor_api_models_ssl_quiet_hour_response import KeyfactorApiModelsSslQuietHourResponse
from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsSslNetworkQueryResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSslNetworkQueryResponse:
    """
    Attributes:
        network_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        name (Union[Unset, str]):
        agent_pool_name (Union[Unset, str]):
        agent_pool_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        discover_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        monitor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        discover_percent_complete (Union[Unset, float]):
        monitor_percent_complete (Union[Unset, float]):
        discover_status (Union[Unset, KeyfactorApiModelsSslNetworkQueryResponseDiscoverStatus]):
        monitor_status (Union[Unset, KeyfactorApiModelsSslNetworkQueryResponseMonitorStatus]):
        discover_last_scanned (Union[Unset, datetime.datetime]):
        monitor_last_scanned (Union[Unset, datetime.datetime]):
        ssl_alert_recipients (Union[Unset, List[str]]):
        auto_monitor (Union[Unset, bool]):
        get_robots (Union[Unset, bool]):
        discover_timeout_ms (Union[Unset, float]):
        monitor_timeout_ms (Union[Unset, float]):
        expiration_alert_days (Union[Unset, float]):
        discover_job_parts (Union[Unset, int]):
        monitor_job_parts (Union[Unset, int]):
        quiet_hours (Union[Unset, List[KeyfactorApiModelsSslQuietHourResponse]]):
    """

    network_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    agent_pool_name: Union[Unset, str] = UNSET
    agent_pool_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    discover_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    monitor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    discover_percent_complete: Union[Unset, float] = UNSET
    monitor_percent_complete: Union[Unset, float] = UNSET
    discover_status: Union[Unset, KeyfactorApiModelsSslNetworkQueryResponseDiscoverStatus] = UNSET
    monitor_status: Union[Unset, KeyfactorApiModelsSslNetworkQueryResponseMonitorStatus] = UNSET
    discover_last_scanned: Union[Unset, datetime.datetime] = UNSET
    monitor_last_scanned: Union[Unset, datetime.datetime] = UNSET
    ssl_alert_recipients: Union[Unset, List[str]] = UNSET
    auto_monitor: Union[Unset, bool] = UNSET
    get_robots: Union[Unset, bool] = UNSET
    discover_timeout_ms: Union[Unset, float] = UNSET
    monitor_timeout_ms: Union[Unset, float] = UNSET
    expiration_alert_days: Union[Unset, float] = UNSET
    discover_job_parts: Union[Unset, int] = UNSET
    monitor_job_parts: Union[Unset, int] = UNSET
    quiet_hours: Union[Unset, List[KeyfactorApiModelsSslQuietHourResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network_id = self.network_id
        name = self.name
        agent_pool_name = self.agent_pool_name
        agent_pool_id = self.agent_pool_id
        description = self.description
        enabled = self.enabled
        discover_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discover_schedule, Unset):
            discover_schedule = self.discover_schedule.to_dict()

        monitor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monitor_schedule, Unset):
            monitor_schedule = self.monitor_schedule.to_dict()

        discover_percent_complete = self.discover_percent_complete
        monitor_percent_complete = self.monitor_percent_complete
        discover_status: Union[Unset, int] = UNSET
        if not isinstance(self.discover_status, Unset):
            discover_status = self.discover_status.value

        monitor_status: Union[Unset, int] = UNSET
        if not isinstance(self.monitor_status, Unset):
            monitor_status = self.monitor_status.value

        discover_last_scanned: Union[Unset, str] = UNSET
        if not isinstance(self.discover_last_scanned, Unset):
            discover_last_scanned = self.discover_last_scanned.isoformat()[:-6]+'Z'

        monitor_last_scanned: Union[Unset, str] = UNSET
        if not isinstance(self.monitor_last_scanned, Unset):
            monitor_last_scanned = self.monitor_last_scanned.isoformat()[:-6]+'Z'

        ssl_alert_recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssl_alert_recipients, Unset):
            ssl_alert_recipients = self.ssl_alert_recipients

        auto_monitor = self.auto_monitor
        get_robots = self.get_robots
        discover_timeout_ms = self.discover_timeout_ms
        monitor_timeout_ms = self.monitor_timeout_ms
        expiration_alert_days = self.expiration_alert_days
        discover_job_parts = self.discover_job_parts
        monitor_job_parts = self.monitor_job_parts
        quiet_hours: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quiet_hours, Unset):
            quiet_hours = []
            for quiet_hours_item_data in self.quiet_hours:
                quiet_hours_item = quiet_hours_item_data.to_dict()

                quiet_hours.append(quiet_hours_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["NetworkId"] = network_id
        if name is not UNSET:
            field_dict["Name"] = name
        if agent_pool_name is not UNSET:
            field_dict["AgentPoolName"] = agent_pool_name
        if agent_pool_id is not UNSET:
            field_dict["AgentPoolId"] = agent_pool_id
        if description is not UNSET:
            field_dict["Description"] = description
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if discover_schedule is not UNSET:
            field_dict["DiscoverSchedule"] = discover_schedule
        if monitor_schedule is not UNSET:
            field_dict["MonitorSchedule"] = monitor_schedule
        if discover_percent_complete is not UNSET:
            field_dict["DiscoverPercentComplete"] = discover_percent_complete
        if monitor_percent_complete is not UNSET:
            field_dict["MonitorPercentComplete"] = monitor_percent_complete
        if discover_status is not UNSET:
            field_dict["DiscoverStatus"] = discover_status
        if monitor_status is not UNSET:
            field_dict["MonitorStatus"] = monitor_status
        if discover_last_scanned is not UNSET:
            field_dict["DiscoverLastScanned"] = discover_last_scanned
        if monitor_last_scanned is not UNSET:
            field_dict["MonitorLastScanned"] = monitor_last_scanned
        if ssl_alert_recipients is not UNSET:
            field_dict["SslAlertRecipients"] = ssl_alert_recipients
        if auto_monitor is not UNSET:
            field_dict["AutoMonitor"] = auto_monitor
        if get_robots is not UNSET:
            field_dict["GetRobots"] = get_robots
        if discover_timeout_ms is not UNSET:
            field_dict["DiscoverTimeoutMs"] = discover_timeout_ms
        if monitor_timeout_ms is not UNSET:
            field_dict["MonitorTimeoutMs"] = monitor_timeout_ms
        if expiration_alert_days is not UNSET:
            field_dict["ExpirationAlertDays"] = expiration_alert_days
        if discover_job_parts is not UNSET:
            field_dict["DiscoverJobParts"] = discover_job_parts
        if monitor_job_parts is not UNSET:
            field_dict["MonitorJobParts"] = monitor_job_parts
        if quiet_hours is not UNSET:
            field_dict["QuietHours"] = quiet_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network_id = d.pop("NetworkId", UNSET)

        name = d.pop("Name", UNSET)

        agent_pool_name = d.pop("AgentPoolName", UNSET)

        agent_pool_id = d.pop("AgentPoolId", UNSET)

        description = d.pop("Description", UNSET)

        enabled = d.pop("Enabled", UNSET)

        _discover_schedule = d.pop("DiscoverSchedule", UNSET)
        discover_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_discover_schedule, Unset):
            discover_schedule = UNSET
        else:
            discover_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_discover_schedule)

        _monitor_schedule = d.pop("MonitorSchedule", UNSET)
        monitor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_monitor_schedule, Unset):
            monitor_schedule = UNSET
        else:
            monitor_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_monitor_schedule)

        discover_percent_complete = d.pop("DiscoverPercentComplete", UNSET)

        monitor_percent_complete = d.pop("MonitorPercentComplete", UNSET)

        _discover_status = d.pop("DiscoverStatus", UNSET)
        discover_status: Union[Unset, KeyfactorApiModelsSslNetworkQueryResponseDiscoverStatus]
        if isinstance(_discover_status, Unset):
            discover_status = UNSET
        else:
            discover_status = KeyfactorApiModelsSslNetworkQueryResponseDiscoverStatus(_discover_status)

        _monitor_status = d.pop("MonitorStatus", UNSET)
        monitor_status: Union[Unset, KeyfactorApiModelsSslNetworkQueryResponseMonitorStatus]
        if isinstance(_monitor_status, Unset):
            monitor_status = UNSET
        else:
            monitor_status = KeyfactorApiModelsSslNetworkQueryResponseMonitorStatus(_monitor_status)

        _discover_last_scanned = d.pop("DiscoverLastScanned", UNSET)
        discover_last_scanned: Union[Unset, datetime.datetime]
        if isinstance(_discover_last_scanned, Unset):
            discover_last_scanned = UNSET
        else:
            discover_last_scanned = isoparse(_discover_last_scanned)

        _monitor_last_scanned = d.pop("MonitorLastScanned", UNSET)
        monitor_last_scanned: Union[Unset, datetime.datetime]
        if isinstance(_monitor_last_scanned, Unset):
            monitor_last_scanned = UNSET
        else:
            monitor_last_scanned = isoparse(_monitor_last_scanned)

        ssl_alert_recipients = cast(List[str], d.pop("SslAlertRecipients", UNSET))

        auto_monitor = d.pop("AutoMonitor", UNSET)

        get_robots = d.pop("GetRobots", UNSET)

        discover_timeout_ms = d.pop("DiscoverTimeoutMs", UNSET)

        monitor_timeout_ms = d.pop("MonitorTimeoutMs", UNSET)

        expiration_alert_days = d.pop("ExpirationAlertDays", UNSET)

        discover_job_parts = d.pop("DiscoverJobParts", UNSET)

        monitor_job_parts = d.pop("MonitorJobParts", UNSET)

        quiet_hours = []
        _quiet_hours = d.pop("QuietHours", UNSET)
        for quiet_hours_item_data in _quiet_hours or []:
            quiet_hours_item = KeyfactorApiModelsSslQuietHourResponse.from_dict(quiet_hours_item_data)

            quiet_hours.append(quiet_hours_item)

        keyfactor_api_models_ssl_network_query_response = cls(
            network_id=network_id,
            name=name,
            agent_pool_name=agent_pool_name,
            agent_pool_id=agent_pool_id,
            description=description,
            enabled=enabled,
            discover_schedule=discover_schedule,
            monitor_schedule=monitor_schedule,
            discover_percent_complete=discover_percent_complete,
            monitor_percent_complete=monitor_percent_complete,
            discover_status=discover_status,
            monitor_status=monitor_status,
            discover_last_scanned=discover_last_scanned,
            monitor_last_scanned=monitor_last_scanned,
            ssl_alert_recipients=ssl_alert_recipients,
            auto_monitor=auto_monitor,
            get_robots=get_robots,
            discover_timeout_ms=discover_timeout_ms,
            monitor_timeout_ms=monitor_timeout_ms,
            expiration_alert_days=expiration_alert_days,
            discover_job_parts=discover_job_parts,
            monitor_job_parts=monitor_job_parts,
            quiet_hours=quiet_hours,
        )

        keyfactor_api_models_ssl_network_query_response.additional_properties = d
        return keyfactor_api_models_ssl_network_query_response

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
