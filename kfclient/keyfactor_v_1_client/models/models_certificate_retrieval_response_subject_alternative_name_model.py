from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_certificate_retrieval_response_subject_alternative_name_model_type import (
    ModelsCertificateRetrievalResponseSubjectAlternativeNameModelType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateRetrievalResponseSubjectAlternativeNameModel")


@attr.s(auto_attribs=True)
class ModelsCertificateRetrievalResponseSubjectAlternativeNameModel:
    """
    Attributes:
        id (Union[Unset, int]):
        value (Union[Unset, str]):
        type (Union[Unset, ModelsCertificateRetrievalResponseSubjectAlternativeNameModelType]):
        value_hash (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    type: Union[Unset, ModelsCertificateRetrievalResponseSubjectAlternativeNameModelType] = UNSET
    value_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        value_hash = self.value_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if value is not UNSET:
            field_dict["Value"] = value
        if type is not UNSET:
            field_dict["Type"] = type
        if value_hash is not UNSET:
            field_dict["ValueHash"] = value_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        value = d.pop("Value", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ModelsCertificateRetrievalResponseSubjectAlternativeNameModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ModelsCertificateRetrievalResponseSubjectAlternativeNameModelType(_type)

        value_hash = d.pop("ValueHash", UNSET)

        models_certificate_retrieval_response_subject_alternative_name_model = cls(
            id=id,
            value=value,
            type=type,
            value_hash=value_hash,
        )

        models_certificate_retrieval_response_subject_alternative_name_model.additional_properties = d
        return models_certificate_retrieval_response_subject_alternative_name_model

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
