from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsTemplatesGlobalTemplateDefaultRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsTemplatesGlobalTemplateDefaultRequest:
    """
    Attributes:
        subject_part (str): The subject part to apply the default to.
        value (Union[Unset, str]): The value to apply by default.
    """

    subject_part: str
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_part = self.subject_part
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SubjectPart": subject_part,
            }
        )
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_part = d.pop("SubjectPart")

        value = d.pop("Value", UNSET)

        keyfactor_api_models_templates_global_template_default_request = cls(
            subject_part=subject_part,
            value=value,
        )

        keyfactor_api_models_templates_global_template_default_request.additional_properties = d
        return keyfactor_api_models_templates_global_template_default_request

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
