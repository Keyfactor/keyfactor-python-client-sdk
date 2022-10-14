from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateRetrievalResponseLocationCountModel")


@attr.s(auto_attribs=True)
class ModelsCertificateRetrievalResponseLocationCountModel:
    """
    Attributes:
        type (Union[Unset, str]):
        count (Union[Unset, int]):
    """

    type: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if count is not UNSET:
            field_dict["Count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type", UNSET)

        count = d.pop("Count", UNSET)

        models_certificate_retrieval_response_location_count_model = cls(
            type=type,
            count=count,
        )

        models_certificate_retrieval_response_location_count_model.additional_properties = d
        return models_certificate_retrieval_response_location_count_model

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
