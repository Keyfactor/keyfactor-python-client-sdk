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

T = TypeVar("T", bound="KeyfactorApiModelsAlertsPendingPendingAlertResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsPendingPendingAlertResponse:
    """
    Attributes:
        subject (Union[Unset, str]):
        message (Union[Unset, str]):
        recipients (Union[Unset, List[str]]):
        ca_request_id (Union[Unset, int]):
        common_name (Union[Unset, str]):
        logical_name (Union[Unset, str]):
    """

    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    recipients: Union[Unset, List[str]] = UNSET
    ca_request_id: Union[Unset, int] = UNSET
    common_name: Union[Unset, str] = UNSET
    logical_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        message = self.message
        recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        ca_request_id = self.ca_request_id
        common_name = self.common_name
        logical_name = self.logical_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if message is not UNSET:
            field_dict["Message"] = message
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients
        if ca_request_id is not UNSET:
            field_dict["CARequestId"] = ca_request_id
        if common_name is not UNSET:
            field_dict["CommonName"] = common_name
        if logical_name is not UNSET:
            field_dict["LogicalName"] = logical_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("Subject", UNSET)

        message = d.pop("Message", UNSET)

        recipients = cast(List[str], d.pop("Recipients", UNSET))

        ca_request_id = d.pop("CARequestId", UNSET)

        common_name = d.pop("CommonName", UNSET)

        logical_name = d.pop("LogicalName", UNSET)

        keyfactor_api_models_alerts_pending_pending_alert_response = cls(
            subject=subject,
            message=message,
            recipients=recipients,
            ca_request_id=ca_request_id,
            common_name=common_name,
            logical_name=logical_name,
        )

        keyfactor_api_models_alerts_pending_pending_alert_response.additional_properties = d
        return keyfactor_api_models_alerts_pending_pending_alert_response

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
