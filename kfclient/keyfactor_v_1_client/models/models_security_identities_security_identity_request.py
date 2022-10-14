from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelsSecurityIdentitiesSecurityIdentityRequest")


@attr.s(auto_attribs=True)
class ModelsSecurityIdentitiesSecurityIdentityRequest:
    """Model for requesting a security identity.

    Attributes:
        account_name (str): The username of the security identity.
    """

    account_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_name = self.account_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AccountName": account_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_name = d.pop("AccountName")

        models_security_identities_security_identity_request = cls(
            account_name=account_name,
        )

        models_security_identities_security_identity_request.additional_properties = d
        return models_security_identities_security_identity_request

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
