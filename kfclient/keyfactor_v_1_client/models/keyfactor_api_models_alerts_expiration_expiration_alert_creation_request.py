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

from ..models.keyfactor_api_models_event_handler_event_handler_parameter_request import (
    KeyfactorApiModelsEventHandlerEventHandlerParameterRequest,
)
from ..models.keyfactor_api_models_event_handler_registered_event_handler_request import (
    KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsExpirationExpirationAlertCreationRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsExpirationExpirationAlertCreationRequest:
    """
    Attributes:
        display_name (str):
        subject (str):
        message (str):
        expiration_warning_days (int):
        certificate_query_id (Union[Unset, int]):
        registered_event_handler (Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest]):
        recipients (Union[Unset, List[str]]):
        event_handler_parameters (Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterRequest]]):
    """

    display_name: str
    subject: str
    message: str
    expiration_warning_days: int
    certificate_query_id: Union[Unset, int] = UNSET
    registered_event_handler: Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest] = UNSET
    recipients: Union[Unset, List[str]] = UNSET
    event_handler_parameters: Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        subject = self.subject
        message = self.message
        expiration_warning_days = self.expiration_warning_days
        certificate_query_id = self.certificate_query_id
        registered_event_handler: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.registered_event_handler, Unset):
            registered_event_handler = self.registered_event_handler.to_dict()

        recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        event_handler_parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.event_handler_parameters, Unset):
            event_handler_parameters = []
            for event_handler_parameters_item_data in self.event_handler_parameters:
                event_handler_parameters_item = event_handler_parameters_item_data.to_dict()

                event_handler_parameters.append(event_handler_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DisplayName": display_name,
                "Subject": subject,
                "Message": message,
                "ExpirationWarningDays": expiration_warning_days,
            }
        )
        if certificate_query_id is not UNSET:
            field_dict["CertificateQueryId"] = certificate_query_id
        if registered_event_handler is not UNSET:
            field_dict["RegisteredEventHandler"] = registered_event_handler
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients
        if event_handler_parameters is not UNSET:
            field_dict["EventHandlerParameters"] = event_handler_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("DisplayName")

        subject = d.pop("Subject")

        message = d.pop("Message")

        expiration_warning_days = d.pop("ExpirationWarningDays")

        certificate_query_id = d.pop("CertificateQueryId", UNSET)

        _registered_event_handler = d.pop("RegisteredEventHandler", UNSET)
        registered_event_handler: Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest]
        if isinstance(_registered_event_handler, Unset):
            registered_event_handler = UNSET
        else:
            registered_event_handler = KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest.from_dict(
                _registered_event_handler
            )

        recipients = cast(List[str], d.pop("Recipients", UNSET))

        event_handler_parameters = []
        _event_handler_parameters = d.pop("EventHandlerParameters", UNSET)
        for event_handler_parameters_item_data in _event_handler_parameters or []:
            event_handler_parameters_item = KeyfactorApiModelsEventHandlerEventHandlerParameterRequest.from_dict(
                event_handler_parameters_item_data
            )

            event_handler_parameters.append(event_handler_parameters_item)

        keyfactor_api_models_alerts_expiration_expiration_alert_creation_request = cls(
            display_name=display_name,
            subject=subject,
            message=message,
            expiration_warning_days=expiration_warning_days,
            certificate_query_id=certificate_query_id,
            registered_event_handler=registered_event_handler,
            recipients=recipients,
            event_handler_parameters=event_handler_parameters,
        )

        keyfactor_api_models_alerts_expiration_expiration_alert_creation_request.additional_properties = d
        return keyfactor_api_models_alerts_expiration_expiration_alert_creation_request

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
