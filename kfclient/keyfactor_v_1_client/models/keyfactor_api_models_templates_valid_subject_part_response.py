from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsTemplatesValidSubjectPartResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsTemplatesValidSubjectPartResponse:
    """
    Attributes:
        subject_part (Union[Unset, str]):
        subject_part_name (Union[Unset, str]):
    """

    subject_part: Union[Unset, str] = UNSET
    subject_part_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_part = self.subject_part
        subject_part_name = self.subject_part_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject_part is not UNSET:
            field_dict["SubjectPart"] = subject_part
        if subject_part_name is not UNSET:
            field_dict["SubjectPartName"] = subject_part_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_part = d.pop("SubjectPart", UNSET)

        subject_part_name = d.pop("SubjectPartName", UNSET)

        keyfactor_api_models_templates_valid_subject_part_response = cls(
            subject_part=subject_part,
            subject_part_name=subject_part_name,
        )

        keyfactor_api_models_templates_valid_subject_part_response.additional_properties = d
        return keyfactor_api_models_templates_valid_subject_part_response

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
