from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionUpdateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionUpdateRequest:
    """
    Example:
        {'DisplayName': '<Updated workflow name>', 'Description': '<Updated workflow description>'}

    Attributes:
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if description is not UNSET:
            field_dict["Description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("DisplayName", UNSET)

        description = d.pop("Description", UNSET)

        keyfactor_api_models_workflows_definition_update_request = cls(
            display_name=display_name,
            description=description,
        )

        keyfactor_api_models_workflows_definition_update_request.additional_properties = d
        return keyfactor_api_models_workflows_definition_update_request

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
