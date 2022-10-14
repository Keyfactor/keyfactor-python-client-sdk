import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMonitoringRevocationMonitoringAlertTestAllRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMonitoringRevocationMonitoringAlertTestAllRequest:
    """
    Attributes:
        evaluation_date (Union[Unset, datetime.datetime]):
        send_alerts (Union[Unset, bool]):
    """

    evaluation_date: Union[Unset, datetime.datetime] = UNSET
    send_alerts: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        evaluation_date: Union[Unset, str] = UNSET
        if not isinstance(self.evaluation_date, Unset):
            evaluation_date = self.evaluation_date.isoformat()[:-6]+'Z'

        send_alerts = self.send_alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evaluation_date is not UNSET:
            field_dict["EvaluationDate"] = evaluation_date
        if send_alerts is not UNSET:
            field_dict["SendAlerts"] = send_alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _evaluation_date = d.pop("EvaluationDate", UNSET)
        evaluation_date: Union[Unset, datetime.datetime]
        if isinstance(_evaluation_date, Unset):
            evaluation_date = UNSET
        else:
            evaluation_date = isoparse(_evaluation_date)

        send_alerts = d.pop("SendAlerts", UNSET)

        keyfactor_api_models_monitoring_revocation_monitoring_alert_test_all_request = cls(
            evaluation_date=evaluation_date,
            send_alerts=send_alerts,
        )

        keyfactor_api_models_monitoring_revocation_monitoring_alert_test_all_request.additional_properties = d
        return keyfactor_api_models_monitoring_revocation_monitoring_alert_test_all_request

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
