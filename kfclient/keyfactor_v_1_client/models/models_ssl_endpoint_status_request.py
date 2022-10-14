from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelsSSLEndpointStatusRequest")


@attr.s(auto_attribs=True)
class ModelsSSLEndpointStatusRequest:
    """
    Attributes:
        id (str):  Example: 00000000-0000-0000-0000-000000000000.
        status (bool):
    """

    id: str
    status: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        status = d.pop("Status")

        models_ssl_endpoint_status_request = cls(
            id=id,
            status=status,
        )

        models_ssl_endpoint_status_request.additional_properties = d
        return models_ssl_endpoint_status_request

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
