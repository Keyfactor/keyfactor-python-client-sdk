from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsAlertScheduleAlertScheduleResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsAlertScheduleAlertScheduleResponse:
    """
    Attributes:
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
    """

    schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        keyfactor_api_models_alerts_alert_schedule_alert_schedule_response = cls(
            schedule=schedule,
        )

        keyfactor_api_models_alerts_alert_schedule_alert_schedule_response.additional_properties = d
        return keyfactor_api_models_alerts_alert_schedule_alert_schedule_response

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
