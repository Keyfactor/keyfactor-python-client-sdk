from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.keyfactor_api_models_event_handler_event_handler_parameter_request import (
    KeyfactorApiModelsEventHandlerEventHandlerParameterRequest,
)
from ..models.keyfactor_api_models_event_handler_registered_event_handler_request import (
    KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsPendingPendingAlertCreationRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsPendingPendingAlertCreationRequest:
    """
    Attributes:
        display_name (str):
        subject (str):
        message (str):
        template_id (Union[Unset, int]):
        registered_event_handler (Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest]):
        recipients (Union[Unset, List[str]]):
        event_handler_parameters (Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterRequest]]):
    """

    display_name: str
    subject: str
    message: str
    template_id: Union[Unset, int] = UNSET
    registered_event_handler: Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest] = UNSET
    recipients: Union[Unset, List[str]] = UNSET
    event_handler_parameters: Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        subject = self.subject
        message = self.message
        template_id = self.template_id
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
            }
        )
        if template_id is not UNSET:
            field_dict["TemplateId"] = template_id
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

        template_id = d.pop("TemplateId", UNSET)

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

        keyfactor_api_models_alerts_pending_pending_alert_creation_request = cls(
            display_name=display_name,
            subject=subject,
            message=message,
            template_id=template_id,
            registered_event_handler=registered_event_handler,
            recipients=recipients,
            event_handler_parameters=event_handler_parameters,
        )

        keyfactor_api_models_alerts_pending_pending_alert_creation_request.additional_properties = d
        return keyfactor_api_models_alerts_pending_pending_alert_creation_request

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
