from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMonitoringDashboardRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMonitoringDashboardRequest:
    """
    Attributes:
        show (bool):
        warning_hours (Union[Unset, int]):
    """

    show: bool
    warning_hours: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        show = self.show
        warning_hours = self.warning_hours

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Show": show,
            }
        )
        if warning_hours is not UNSET:
            field_dict["WarningHours"] = warning_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        show = d.pop("Show")

        warning_hours = d.pop("WarningHours", UNSET)

        keyfactor_api_models_monitoring_dashboard_request = cls(
            show=show,
            warning_hours=warning_hours,
        )

        keyfactor_api_models_monitoring_dashboard_request.additional_properties = d
        return keyfactor_api_models_monitoring_dashboard_request

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
