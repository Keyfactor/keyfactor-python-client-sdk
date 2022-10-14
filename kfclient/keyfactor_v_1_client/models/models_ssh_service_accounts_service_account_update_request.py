from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.models_ssh_keys_key_update_request import ModelsSSHKeysKeyUpdateRequest

T = TypeVar("T", bound="ModelsSSHServiceAccountsServiceAccountUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsSSHServiceAccountsServiceAccountUpdateRequest:
    """
    Attributes:
        key_update_request (ModelsSSHKeysKeyUpdateRequest):
        id (int):
    """

    key_update_request: ModelsSSHKeysKeyUpdateRequest
    id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_update_request = self.key_update_request.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "KeyUpdateRequest": key_update_request,
                "Id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_update_request = ModelsSSHKeysKeyUpdateRequest.from_dict(d.pop("KeyUpdateRequest"))

        id = d.pop("Id")

        models_ssh_service_accounts_service_account_update_request = cls(
            key_update_request=key_update_request,
            id=id,
        )

        models_ssh_service_accounts_service_account_update_request.additional_properties = d
        return models_ssh_service_accounts_service_account_update_request

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
