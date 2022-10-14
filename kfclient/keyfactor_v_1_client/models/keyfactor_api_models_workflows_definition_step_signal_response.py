from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionStepSignalResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionStepSignalResponse:
    """
    Attributes:
        role_ids (Union[Unset, List[int]]): The roles that are allowed to send this signal.
        signal_name (Union[Unset, str]):
    """

    role_ids: Union[Unset, List[int]] = UNSET
    signal_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

        signal_name = self.signal_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_ids is not UNSET:
            field_dict["RoleIds"] = role_ids
        if signal_name is not UNSET:
            field_dict["SignalName"] = signal_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_ids = cast(List[int], d.pop("RoleIds", UNSET))

        signal_name = d.pop("SignalName", UNSET)

        keyfactor_api_models_workflows_definition_step_signal_response = cls(
            role_ids=role_ids,
            signal_name=signal_name,
        )

        keyfactor_api_models_workflows_definition_step_signal_response.additional_properties = d
        return keyfactor_api_models_workflows_definition_step_signal_response

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
