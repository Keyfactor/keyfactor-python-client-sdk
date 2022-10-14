import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorCommonSchedulingModelsMonthlyModel")


@attr.s(auto_attribs=True)
class KeyfactorCommonSchedulingModelsMonthlyModel:
    """
    Attributes:
        day (Union[Unset, int]):
        time (Union[Unset, datetime.datetime]):
    """

    day: Union[Unset, int] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day = self.day
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["Day"] = day
        if time is not UNSET:
            field_dict["Time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        day = d.pop("Day", UNSET)

        _time = d.pop("Time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        keyfactor_common_scheduling_models_monthly_model = cls(
            day=day,
            time=time,
        )

        keyfactor_common_scheduling_models_monthly_model.additional_properties = d
        return keyfactor_common_scheduling_models_monthly_model

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
