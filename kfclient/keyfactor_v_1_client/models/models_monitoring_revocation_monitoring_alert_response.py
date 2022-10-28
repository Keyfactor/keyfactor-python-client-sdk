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

T = TypeVar("T", bound="ModelsMonitoringRevocationMonitoringAlertResponse")


@attr.s(auto_attribs=True)
class ModelsMonitoringRevocationMonitoringAlertResponse:
    """
    Attributes:
        subject (Union[Unset, str]):
        message (Union[Unset, str]):
        recipients (Union[Unset, List[str]]):
    """

    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    recipients: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        message = self.message
        recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if message is not UNSET:
            field_dict["Message"] = message
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("Subject", UNSET)

        message = d.pop("Message", UNSET)

        recipients = cast(List[str], d.pop("Recipients", UNSET))

        models_monitoring_revocation_monitoring_alert_response = cls(
            subject=subject,
            message=message,
            recipients=recipients,
        )

        models_monitoring_revocation_monitoring_alert_response.additional_properties = d
        return models_monitoring_revocation_monitoring_alert_response

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
