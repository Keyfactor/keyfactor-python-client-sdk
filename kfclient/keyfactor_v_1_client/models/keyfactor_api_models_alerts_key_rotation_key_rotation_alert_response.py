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

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse:
    """
    Attributes:
        subject (Union[Unset, str]):
        message (Union[Unset, str]):
        recipient (Union[Unset, str]):
    """

    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    recipient: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        message = self.message
        recipient = self.recipient

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if message is not UNSET:
            field_dict["Message"] = message
        if recipient is not UNSET:
            field_dict["Recipient"] = recipient

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("Subject", UNSET)

        message = d.pop("Message", UNSET)

        recipient = d.pop("Recipient", UNSET)

        keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response = cls(
            subject=subject,
            message=message,
            recipient=recipient,
        )

        keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response.additional_properties = d
        return keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response

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
