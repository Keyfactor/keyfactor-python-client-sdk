import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.keyfactor_api_models_ssl_quiet_hour_request_end_day import KeyfactorApiModelsSslQuietHourRequestEndDay
from ..models.keyfactor_api_models_ssl_quiet_hour_request_start_day import KeyfactorApiModelsSslQuietHourRequestStartDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsSslQuietHourRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSslQuietHourRequest:
    """
    Attributes:
        start_day (Union[Unset, KeyfactorApiModelsSslQuietHourRequestStartDay]):
        start_time (Union[Unset, datetime.datetime]):
        end_day (Union[Unset, KeyfactorApiModelsSslQuietHourRequestEndDay]):
        end_time (Union[Unset, datetime.datetime]):
    """

    start_day: Union[Unset, KeyfactorApiModelsSslQuietHourRequestStartDay] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_day: Union[Unset, KeyfactorApiModelsSslQuietHourRequestEndDay] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_day: Union[Unset, int] = UNSET
        if not isinstance(self.start_day, Unset):
            start_day = self.start_day.value

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()[:-6]+'Z'

        end_day: Union[Unset, int] = UNSET
        if not isinstance(self.end_day, Unset):
            end_day = self.end_day.value

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_day is not UNSET:
            field_dict["StartDay"] = start_day
        if start_time is not UNSET:
            field_dict["StartTime"] = start_time
        if end_day is not UNSET:
            field_dict["EndDay"] = end_day
        if end_time is not UNSET:
            field_dict["EndTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_day = d.pop("StartDay", UNSET)
        start_day: Union[Unset, KeyfactorApiModelsSslQuietHourRequestStartDay]
        if isinstance(_start_day, Unset):
            start_day = UNSET
        else:
            start_day = KeyfactorApiModelsSslQuietHourRequestStartDay(_start_day)

        _start_time = d.pop("StartTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_day = d.pop("EndDay", UNSET)
        end_day: Union[Unset, KeyfactorApiModelsSslQuietHourRequestEndDay]
        if isinstance(_end_day, Unset):
            end_day = UNSET
        else:
            end_day = KeyfactorApiModelsSslQuietHourRequestEndDay(_end_day)

        _end_time = d.pop("EndTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        keyfactor_api_models_ssl_quiet_hour_request = cls(
            start_day=start_day,
            start_time=start_time,
            end_day=end_day,
            end_time=end_time,
        )

        keyfactor_api_models_ssl_quiet_hour_request.additional_properties = d
        return keyfactor_api_models_ssl_quiet_hour_request

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
