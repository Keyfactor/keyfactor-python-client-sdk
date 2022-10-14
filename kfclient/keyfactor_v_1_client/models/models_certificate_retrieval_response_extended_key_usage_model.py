from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateRetrievalResponseExtendedKeyUsageModel")


@attr.s(auto_attribs=True)
class ModelsCertificateRetrievalResponseExtendedKeyUsageModel:
    """
    Attributes:
        id (Union[Unset, int]):
        oid (Union[Unset, str]):
        display_name (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    oid: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        oid = self.oid
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if oid is not UNSET:
            field_dict["Oid"] = oid
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        oid = d.pop("Oid", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        models_certificate_retrieval_response_extended_key_usage_model = cls(
            id=id,
            oid=oid,
            display_name=display_name,
        )

        models_certificate_retrieval_response_extended_key_usage_model.additional_properties = d
        return models_certificate_retrieval_response_extended_key_usage_model

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
