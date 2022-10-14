from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsPendingPendingAlertTestAllRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsPendingPendingAlertTestAllRequest:
    """
    Attributes:
        send_alerts (Union[Unset, bool]):
    """

    send_alerts: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        send_alerts = self.send_alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_alerts is not UNSET:
            field_dict["SendAlerts"] = send_alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        send_alerts = d.pop("SendAlerts", UNSET)

        keyfactor_api_models_alerts_pending_pending_alert_test_all_request = cls(
            send_alerts=send_alerts,
        )

        keyfactor_api_models_alerts_pending_pending_alert_test_all_request.additional_properties = d
        return keyfactor_api_models_alerts_pending_pending_alert_test_all_request

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
