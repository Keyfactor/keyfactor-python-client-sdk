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

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMonitoringEmailResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMonitoringEmailResponse:
    """
    Attributes:
        enable_reminder (Union[Unset, bool]):
        warning_days (Union[Unset, int]):
        recipients (Union[Unset, List[str]]):
    """

    enable_reminder: Union[Unset, bool] = UNSET
    warning_days: Union[Unset, int] = UNSET
    recipients: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable_reminder = self.enable_reminder
        warning_days = self.warning_days
        recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_reminder is not UNSET:
            field_dict["EnableReminder"] = enable_reminder
        if warning_days is not UNSET:
            field_dict["WarningDays"] = warning_days
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_reminder = d.pop("EnableReminder", UNSET)

        warning_days = d.pop("WarningDays", UNSET)

        recipients = cast(List[str], d.pop("Recipients", UNSET))

        keyfactor_api_models_monitoring_email_response = cls(
            enable_reminder=enable_reminder,
            warning_days=warning_days,
            recipients=recipients,
        )

        keyfactor_api_models_monitoring_email_response.additional_properties = d
        return keyfactor_api_models_monitoring_email_response

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
