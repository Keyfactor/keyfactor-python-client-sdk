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

from ..models.keyfactor_api_models_ssl_quiet_hour_response_end_day import KeyfactorApiModelsSslQuietHourResponseEndDay
from ..models.keyfactor_api_models_ssl_quiet_hour_response_start_day import (
    KeyfactorApiModelsSslQuietHourResponseStartDay,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsSslQuietHourResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSslQuietHourResponse:
    """
    Attributes:
        start_day (Union[Unset, KeyfactorApiModelsSslQuietHourResponseStartDay]):
        start_time (Union[Unset, datetime.datetime]):
        end_day (Union[Unset, KeyfactorApiModelsSslQuietHourResponseEndDay]):
        end_time (Union[Unset, datetime.datetime]):
    """

    start_day: Union[Unset, KeyfactorApiModelsSslQuietHourResponseStartDay] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_day: Union[Unset, KeyfactorApiModelsSslQuietHourResponseEndDay] = UNSET
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
        start_day: Union[Unset, KeyfactorApiModelsSslQuietHourResponseStartDay]
        if isinstance(_start_day, Unset):
            start_day = UNSET
        else:
            start_day = KeyfactorApiModelsSslQuietHourResponseStartDay(_start_day)

        _start_time = d.pop("StartTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_day = d.pop("EndDay", UNSET)
        end_day: Union[Unset, KeyfactorApiModelsSslQuietHourResponseEndDay]
        if isinstance(_end_day, Unset):
            end_day = UNSET
        else:
            end_day = KeyfactorApiModelsSslQuietHourResponseEndDay(_end_day)

        _end_time = d.pop("EndTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        keyfactor_api_models_ssl_quiet_hour_response = cls(
            start_day=start_day,
            start_time=start_time,
            end_day=end_day,
            end_time=end_time,
        )

        keyfactor_api_models_ssl_quiet_hour_response.additional_properties = d
        return keyfactor_api_models_ssl_quiet_hour_response

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
