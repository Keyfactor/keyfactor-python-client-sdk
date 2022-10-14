from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorCommonSchedulingModelsIntervalModel")


@attr.s(auto_attribs=True)
class KeyfactorCommonSchedulingModelsIntervalModel:
    """
    Attributes:
        minutes (Union[Unset, int]):
    """

    minutes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        minutes = self.minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minutes is not UNSET:
            field_dict["Minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        minutes = d.pop("Minutes", UNSET)

        keyfactor_common_scheduling_models_interval_model = cls(
            minutes=minutes,
        )

        keyfactor_common_scheduling_models_interval_model.additional_properties = d
        return keyfactor_common_scheduling_models_interval_model

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
