from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsConditionConfigurationResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsConditionConfigurationResponse:
    """Information about the configuration of a workflow condition.

    Attributes:
        id (Union[Unset, str]): The Id of the condition. Example: 00000000-0000-0000-0000-000000000000.
        value (Union[Unset, str]): The value to compare to. This value will be compared to a true value.
    """

    id: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        value = d.pop("Value", UNSET)

        keyfactor_api_models_workflows_condition_configuration_response = cls(
            id=id,
            value=value,
        )

        keyfactor_api_models_workflows_condition_configuration_response.additional_properties = d
        return keyfactor_api_models_workflows_condition_configuration_response

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
