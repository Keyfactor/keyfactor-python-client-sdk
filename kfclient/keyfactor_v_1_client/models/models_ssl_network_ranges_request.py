from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ModelsSSLNetworkRangesRequest")


@attr.s(auto_attribs=True)
class ModelsSSLNetworkRangesRequest:
    """
    Attributes:
        network_id (str):  Example: 00000000-0000-0000-0000-000000000000.
        ranges (List[str]):
    """

    network_id: str
    ranges: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network_id = self.network_id
        ranges = self.ranges

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "NetworkId": network_id,
                "Ranges": ranges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network_id = d.pop("NetworkId")

        ranges = cast(List[str], d.pop("Ranges"))

        models_ssl_network_ranges_request = cls(
            network_id=network_id,
            ranges=ranges,
        )

        models_ssl_network_ranges_request.additional_properties = d
        return models_ssl_network_ranges_request

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
