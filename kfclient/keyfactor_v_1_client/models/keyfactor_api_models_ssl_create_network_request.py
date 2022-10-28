# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.keyfactor_api_models_ssl_quiet_hour_request import KeyfactorApiModelsSslQuietHourRequest
from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsSslCreateNetworkRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSslCreateNetworkRequest:
    """
    Attributes:
        name (str):
        agent_pool_name (str):
        description (str):
        enabled (Union[Unset, bool]):
        discover_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        monitor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        ssl_alert_recipients (Union[Unset, List[str]]):
        auto_monitor (Union[Unset, bool]):
        get_robots (Union[Unset, bool]):
        discover_timeout_ms (Union[Unset, float]):
        monitor_timeout_ms (Union[Unset, float]):
        expiration_alert_days (Union[Unset, float]):
        quiet_hours (Union[Unset, List[KeyfactorApiModelsSslQuietHourRequest]]):
    """

    name: str
    agent_pool_name: str
    description: str
    enabled: Union[Unset, bool] = UNSET
    discover_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    monitor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    ssl_alert_recipients: Union[Unset, List[str]] = UNSET
    auto_monitor: Union[Unset, bool] = UNSET
    get_robots: Union[Unset, bool] = UNSET
    discover_timeout_ms: Union[Unset, float] = UNSET
    monitor_timeout_ms: Union[Unset, float] = UNSET
    expiration_alert_days: Union[Unset, float] = UNSET
    quiet_hours: Union[Unset, List[KeyfactorApiModelsSslQuietHourRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        agent_pool_name = self.agent_pool_name
        description = self.description
        enabled = self.enabled
        discover_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discover_schedule, Unset):
            discover_schedule = self.discover_schedule.to_dict()

        monitor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monitor_schedule, Unset):
            monitor_schedule = self.monitor_schedule.to_dict()

        ssl_alert_recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssl_alert_recipients, Unset):
            ssl_alert_recipients = self.ssl_alert_recipients

        auto_monitor = self.auto_monitor
        get_robots = self.get_robots
        discover_timeout_ms = self.discover_timeout_ms
        monitor_timeout_ms = self.monitor_timeout_ms
        expiration_alert_days = self.expiration_alert_days
        quiet_hours: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quiet_hours, Unset):
            quiet_hours = []
            for quiet_hours_item_data in self.quiet_hours:
                quiet_hours_item = quiet_hours_item_data.to_dict()

                quiet_hours.append(quiet_hours_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
                "AgentPoolName": agent_pool_name,
                "Description": description,
            }
        )
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if discover_schedule is not UNSET:
            field_dict["DiscoverSchedule"] = discover_schedule
        if monitor_schedule is not UNSET:
            field_dict["MonitorSchedule"] = monitor_schedule
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
        if quiet_hours is not UNSET:
            field_dict["QuietHours"] = quiet_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        agent_pool_name = d.pop("AgentPoolName")

        description = d.pop("Description")

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

        ssl_alert_recipients = cast(List[str], d.pop("SslAlertRecipients", UNSET))

        auto_monitor = d.pop("AutoMonitor", UNSET)

        get_robots = d.pop("GetRobots", UNSET)

        discover_timeout_ms = d.pop("DiscoverTimeoutMs", UNSET)

        monitor_timeout_ms = d.pop("MonitorTimeoutMs", UNSET)

        expiration_alert_days = d.pop("ExpirationAlertDays", UNSET)

        quiet_hours = []
        _quiet_hours = d.pop("QuietHours", UNSET)
        for quiet_hours_item_data in _quiet_hours or []:
            quiet_hours_item = KeyfactorApiModelsSslQuietHourRequest.from_dict(quiet_hours_item_data)

            quiet_hours.append(quiet_hours_item)

        keyfactor_api_models_ssl_create_network_request = cls(
            name=name,
            agent_pool_name=agent_pool_name,
            description=description,
            enabled=enabled,
            discover_schedule=discover_schedule,
            monitor_schedule=monitor_schedule,
            ssl_alert_recipients=ssl_alert_recipients,
            auto_monitor=auto_monitor,
            get_robots=get_robots,
            discover_timeout_ms=discover_timeout_ms,
            monitor_timeout_ms=monitor_timeout_ms,
            expiration_alert_days=expiration_alert_days,
            quiet_hours=quiet_hours,
        )

        keyfactor_api_models_ssl_create_network_request.additional_properties = d
        return keyfactor_api_models_ssl_create_network_request

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
