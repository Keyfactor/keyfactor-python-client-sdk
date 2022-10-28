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

T = TypeVar("T", bound="KeyfactorApiModelsAlertsExpirationExpirationAlertResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsExpirationExpirationAlertResponse:
    """
    Attributes:
        ca_name (Union[Unset, str]):
        ca_row (Union[Unset, int]):
        issued_cn (Union[Unset, str]):
        expiry (Union[Unset, str]):
        subject (Union[Unset, str]):
        message (Union[Unset, str]):
        recipients (Union[Unset, List[str]]):
        send_date (Union[Unset, str]):
    """

    ca_name: Union[Unset, str] = UNSET
    ca_row: Union[Unset, int] = UNSET
    issued_cn: Union[Unset, str] = UNSET
    expiry: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    recipients: Union[Unset, List[str]] = UNSET
    send_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ca_name = self.ca_name
        ca_row = self.ca_row
        issued_cn = self.issued_cn
        expiry = self.expiry
        subject = self.subject
        message = self.message
        recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        send_date = self.send_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ca_name is not UNSET:
            field_dict["CAName"] = ca_name
        if ca_row is not UNSET:
            field_dict["CARow"] = ca_row
        if issued_cn is not UNSET:
            field_dict["IssuedCN"] = issued_cn
        if expiry is not UNSET:
            field_dict["Expiry"] = expiry
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if message is not UNSET:
            field_dict["Message"] = message
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients
        if send_date is not UNSET:
            field_dict["SendDate"] = send_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ca_name = d.pop("CAName", UNSET)

        ca_row = d.pop("CARow", UNSET)

        issued_cn = d.pop("IssuedCN", UNSET)

        expiry = d.pop("Expiry", UNSET)

        subject = d.pop("Subject", UNSET)

        message = d.pop("Message", UNSET)

        recipients = cast(List[str], d.pop("Recipients", UNSET))

        send_date = d.pop("SendDate", UNSET)

        keyfactor_api_models_alerts_expiration_expiration_alert_response = cls(
            ca_name=ca_name,
            ca_row=ca_row,
            issued_cn=issued_cn,
            expiry=expiry,
            subject=subject,
            message=message,
            recipients=recipients,
            send_date=send_date,
        )

        keyfactor_api_models_alerts_expiration_expiration_alert_response.additional_properties = d
        return keyfactor_api_models_alerts_expiration_expiration_alert_response

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
