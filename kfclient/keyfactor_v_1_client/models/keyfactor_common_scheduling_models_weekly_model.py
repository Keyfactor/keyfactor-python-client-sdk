import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.keyfactor_common_scheduling_models_weekly_model_days_item import (
    KeyfactorCommonSchedulingModelsWeeklyModelDaysItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorCommonSchedulingModelsWeeklyModel")


@attr.s(auto_attribs=True)
class KeyfactorCommonSchedulingModelsWeeklyModel:
    """
    Attributes:
        days (Union[Unset, List[KeyfactorCommonSchedulingModelsWeeklyModelDaysItem]]):
        time (Union[Unset, datetime.datetime]):
    """

    days: Union[Unset, List[KeyfactorCommonSchedulingModelsWeeklyModelDaysItem]] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days: Union[Unset, List[int]] = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.value

                days.append(days_item)

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["Days"] = days
        if time is not UNSET:
            field_dict["Time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days = []
        _days = d.pop("Days", UNSET)
        for days_item_data in _days or []:
            days_item = KeyfactorCommonSchedulingModelsWeeklyModelDaysItem(days_item_data)

            days.append(days_item)

        _time = d.pop("Time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        keyfactor_common_scheduling_models_weekly_model = cls(
            days=days,
            time=time,
        )

        keyfactor_common_scheduling_models_weekly_model.additional_properties = d
        return keyfactor_common_scheduling_models_weekly_model

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
