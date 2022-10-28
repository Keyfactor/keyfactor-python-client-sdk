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

from ..models.keyfactor_api_models_event_handler_event_handler_parameter_response import (
    KeyfactorApiModelsEventHandlerEventHandlerParameterResponse,
)
from ..models.keyfactor_api_models_event_handler_registered_event_handler_response import (
    KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertDefinitionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, str]):
        subject (Union[Unset, str]):
        message (Union[Unset, str]):
        recipient (Union[Unset, str]):
        rotation_warning_days (Union[Unset, int]):
        registered_event_handler (Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse]):
        event_handler_parameters (Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterResponse]]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    recipient: Union[Unset, str] = UNSET
    rotation_warning_days: Union[Unset, int] = UNSET
    registered_event_handler: Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse] = UNSET
    event_handler_parameters: Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        subject = self.subject
        message = self.message
        recipient = self.recipient
        rotation_warning_days = self.rotation_warning_days
        registered_event_handler: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.registered_event_handler, Unset):
            registered_event_handler = self.registered_event_handler.to_dict()

        event_handler_parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.event_handler_parameters, Unset):
            event_handler_parameters = []
            for event_handler_parameters_item_data in self.event_handler_parameters:
                event_handler_parameters_item = event_handler_parameters_item_data.to_dict()

                event_handler_parameters.append(event_handler_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if message is not UNSET:
            field_dict["Message"] = message
        if recipient is not UNSET:
            field_dict["Recipient"] = recipient
        if rotation_warning_days is not UNSET:
            field_dict["RotationWarningDays"] = rotation_warning_days
        if registered_event_handler is not UNSET:
            field_dict["RegisteredEventHandler"] = registered_event_handler
        if event_handler_parameters is not UNSET:
            field_dict["EventHandlerParameters"] = event_handler_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        subject = d.pop("Subject", UNSET)

        message = d.pop("Message", UNSET)

        recipient = d.pop("Recipient", UNSET)

        rotation_warning_days = d.pop("RotationWarningDays", UNSET)

        _registered_event_handler = d.pop("RegisteredEventHandler", UNSET)
        registered_event_handler: Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse]
        if isinstance(_registered_event_handler, Unset):
            registered_event_handler = UNSET
        else:
            registered_event_handler = KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse.from_dict(
                _registered_event_handler
            )

        event_handler_parameters = []
        _event_handler_parameters = d.pop("EventHandlerParameters", UNSET)
        for event_handler_parameters_item_data in _event_handler_parameters or []:
            event_handler_parameters_item = KeyfactorApiModelsEventHandlerEventHandlerParameterResponse.from_dict(
                event_handler_parameters_item_data
            )

            event_handler_parameters.append(event_handler_parameters_item)

        keyfactor_api_models_alerts_key_rotation_key_rotation_alert_definition_response = cls(
            id=id,
            display_name=display_name,
            subject=subject,
            message=message,
            recipient=recipient,
            rotation_warning_days=rotation_warning_days,
            registered_event_handler=registered_event_handler,
            event_handler_parameters=event_handler_parameters,
        )

        keyfactor_api_models_alerts_key_rotation_key_rotation_alert_definition_response.additional_properties = d
        return keyfactor_api_models_alerts_key_rotation_key_rotation_alert_definition_response

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
