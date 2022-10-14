from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSecurityIdentitiesSecurityIdentityLookupResponse")


@attr.s(auto_attribs=True)
class ModelsSecurityIdentitiesSecurityIdentityLookupResponse:
    """A public DTO representing the result of a security identity lookup.

    Attributes:
        valid (Union[Unset, bool]): Whether or not the identity is valid.
    """

    valid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        valid = self.valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid is not UNSET:
            field_dict["Valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        valid = d.pop("Valid", UNSET)

        models_security_identities_security_identity_lookup_response = cls(
            valid=valid,
        )

        models_security_identities_security_identity_lookup_response.additional_properties = d
        return models_security_identities_security_identity_lookup_response

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
