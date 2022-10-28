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

from ..models.keyfactor_common_scheduling_models_interval_model import KeyfactorCommonSchedulingModelsIntervalModel
from ..models.keyfactor_common_scheduling_models_monthly_model import KeyfactorCommonSchedulingModelsMonthlyModel
from ..models.keyfactor_common_scheduling_models_time_model import KeyfactorCommonSchedulingModelsTimeModel
from ..models.keyfactor_common_scheduling_models_weekly_model import KeyfactorCommonSchedulingModelsWeeklyModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorCommonSchedulingKeyfactorSchedule")


@attr.s(auto_attribs=True)
class KeyfactorCommonSchedulingKeyfactorSchedule:
    """
    Attributes:
        immediate (Union[Unset, bool]):
        interval (Union[Unset, KeyfactorCommonSchedulingModelsIntervalModel]):
        daily (Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]):
        weekly (Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]):
        monthly (Union[Unset, KeyfactorCommonSchedulingModelsMonthlyModel]):
        exactly_once (Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]):
    """

    immediate: Union[Unset, bool] = UNSET
    interval: Union[Unset, KeyfactorCommonSchedulingModelsIntervalModel] = UNSET
    daily: Union[Unset, KeyfactorCommonSchedulingModelsTimeModel] = UNSET
    weekly: Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel] = UNSET
    monthly: Union[Unset, KeyfactorCommonSchedulingModelsMonthlyModel] = UNSET
    exactly_once: Union[Unset, KeyfactorCommonSchedulingModelsTimeModel] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        immediate = self.immediate
        interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        daily: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daily, Unset):
            daily = self.daily.to_dict()

        weekly: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        exactly_once: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exactly_once, Unset):
            exactly_once = self.exactly_once.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if immediate is not UNSET:
            field_dict["Immediate"] = immediate
        if interval is not UNSET:
            field_dict["Interval"] = interval
        if daily is not UNSET:
            field_dict["Daily"] = daily
        if weekly is not UNSET:
            field_dict["Weekly"] = weekly
        if monthly is not UNSET:
            field_dict["Monthly"] = monthly
        if exactly_once is not UNSET:
            field_dict["ExactlyOnce"] = exactly_once

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        immediate = d.pop("Immediate", UNSET)

        _interval = d.pop("Interval", UNSET)
        interval: Union[Unset, KeyfactorCommonSchedulingModelsIntervalModel]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = KeyfactorCommonSchedulingModelsIntervalModel.from_dict(_interval)

        _daily = d.pop("Daily", UNSET)
        daily: Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = KeyfactorCommonSchedulingModelsTimeModel.from_dict(_daily)

        _weekly = d.pop("Weekly", UNSET)
        weekly: Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = KeyfactorCommonSchedulingModelsWeeklyModel.from_dict(_weekly)

        _monthly = d.pop("Monthly", UNSET)
        monthly: Union[Unset, KeyfactorCommonSchedulingModelsMonthlyModel]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = KeyfactorCommonSchedulingModelsMonthlyModel.from_dict(_monthly)

        _exactly_once = d.pop("ExactlyOnce", UNSET)
        exactly_once: Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]
        if isinstance(_exactly_once, Unset):
            exactly_once = UNSET
        else:
            exactly_once = KeyfactorCommonSchedulingModelsTimeModel.from_dict(_exactly_once)

        keyfactor_common_scheduling_keyfactor_schedule = cls(
            immediate=immediate,
            interval=interval,
            daily=daily,
            weekly=weekly,
            monthly=monthly,
            exactly_once=exactly_once,
        )

        keyfactor_common_scheduling_keyfactor_schedule.additional_properties = d
        return keyfactor_common_scheduling_keyfactor_schedule

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
