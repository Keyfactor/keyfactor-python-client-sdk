from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_ssl_network_definition_item_type import ModelsSSLNetworkDefinitionItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSLNetworkDefinition")


@attr.s(auto_attribs=True)
class ModelsSSLNetworkDefinition:
    """
    Attributes:
        item_type (Union[Unset, ModelsSSLNetworkDefinitionItemType]):
        value (Union[Unset, str]):
    """

    item_type: Union[Unset, ModelsSSLNetworkDefinitionItemType] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, int] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _item_type = d.pop("ItemType", UNSET)
        item_type: Union[Unset, ModelsSSLNetworkDefinitionItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = ModelsSSLNetworkDefinitionItemType(_item_type)

        value = d.pop("Value", UNSET)

        models_ssl_network_definition = cls(
            item_type=item_type,
            value=value,
        )

        models_ssl_network_definition.additional_properties = d
        return models_ssl_network_definition

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
