from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.keyfactor_api_models_alerts_alert_certificate_query_alert_certificate_query_response import (
    KeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse,
)
from ..models.keyfactor_api_models_event_handler_event_handler_parameter_response import (
    KeyfactorApiModelsEventHandlerEventHandlerParameterResponse,
)
from ..models.keyfactor_api_models_event_handler_registered_event_handler_response import (
    KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsExpirationExpirationAlertDefinitionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsExpirationExpirationAlertDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, str]):
        subject (Union[Unset, str]):
        message (Union[Unset, str]):
        expiration_warning_days (Union[Unset, int]):
        recipients (Union[Unset, List[str]]):
        certificate_query (Union[Unset, KeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse]):
        registered_event_handler (Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse]):
        event_handler_parameters (Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterResponse]]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    expiration_warning_days: Union[Unset, int] = UNSET
    recipients: Union[Unset, List[str]] = UNSET
    certificate_query: Union[Unset, KeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse] = UNSET
    registered_event_handler: Union[Unset, KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse] = UNSET
    event_handler_parameters: Union[Unset, List[KeyfactorApiModelsEventHandlerEventHandlerParameterResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        subject = self.subject
        message = self.message
        expiration_warning_days = self.expiration_warning_days
        recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        certificate_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificate_query, Unset):
            certificate_query = self.certificate_query.to_dict()

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
        if expiration_warning_days is not UNSET:
            field_dict["ExpirationWarningDays"] = expiration_warning_days
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients
        if certificate_query is not UNSET:
            field_dict["CertificateQuery"] = certificate_query
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

        expiration_warning_days = d.pop("ExpirationWarningDays", UNSET)

        recipients = cast(List[str], d.pop("Recipients", UNSET))

        _certificate_query = d.pop("CertificateQuery", UNSET)
        certificate_query: Union[Unset, KeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse]
        if isinstance(_certificate_query, Unset):
            certificate_query = UNSET
        else:
            certificate_query = KeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse.from_dict(
                _certificate_query
            )

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

        keyfactor_api_models_alerts_expiration_expiration_alert_definition_response = cls(
            id=id,
            display_name=display_name,
            subject=subject,
            message=message,
            expiration_warning_days=expiration_warning_days,
            recipients=recipients,
            certificate_query=certificate_query,
            registered_event_handler=registered_event_handler,
            event_handler_parameters=event_handler_parameters,
        )

        keyfactor_api_models_alerts_expiration_expiration_alert_definition_response.additional_properties = d
        return keyfactor_api_models_alerts_expiration_expiration_alert_definition_response

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
