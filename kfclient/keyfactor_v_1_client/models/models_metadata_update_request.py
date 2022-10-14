from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_metadata_update_request_metadata import ModelsMetadataUpdateRequestMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsMetadataUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsMetadataUpdateRequest:
    """
    Attributes:
        metadata (ModelsMetadataUpdateRequestMetadata):
        id (Union[Unset, int]):
    """

    metadata: ModelsMetadataUpdateRequestMetadata
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata = self.metadata.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Metadata": metadata,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metadata = ModelsMetadataUpdateRequestMetadata.from_dict(d.pop("Metadata"))

        id = d.pop("Id", UNSET)

        models_metadata_update_request = cls(
            metadata=metadata,
            id=id,
        )

        models_metadata_update_request.additional_properties = d
        return models_metadata_update_request

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
