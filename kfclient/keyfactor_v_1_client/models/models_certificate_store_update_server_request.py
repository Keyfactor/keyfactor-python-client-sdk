from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_keyfactor_api_secret import ModelsKeyfactorAPISecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStoreUpdateServerRequest")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreUpdateServerRequest:
    """
    Attributes:
        id (int):
        username (ModelsKeyfactorAPISecret):
        password (ModelsKeyfactorAPISecret):
        use_ssl (bool):
        name (str):
        container (Union[Unset, int]):
    """

    id: int
    username: ModelsKeyfactorAPISecret
    password: ModelsKeyfactorAPISecret
    use_ssl: bool
    name: str
    container: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username.to_dict()

        password = self.password.to_dict()

        use_ssl = self.use_ssl
        name = self.name
        container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Username": username,
                "Password": password,
                "UseSSL": use_ssl,
                "Name": name,
            }
        )
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        username = ModelsKeyfactorAPISecret.from_dict(d.pop("Username"))

        password = ModelsKeyfactorAPISecret.from_dict(d.pop("Password"))

        use_ssl = d.pop("UseSSL")

        name = d.pop("Name")

        container = d.pop("Container", UNSET)

        models_certificate_store_update_server_request = cls(
            id=id,
            username=username,
            password=password,
            use_ssl=use_ssl,
            name=name,
            container=container,
        )

        models_certificate_store_update_server_request.additional_properties = d
        return models_certificate_store_update_server_request

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
