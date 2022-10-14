from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsSecurityRolesRoleIdentitiesRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSecurityRolesRoleIdentitiesRequest:
    """
    Attributes:
        ids (Union[Unset, List[int]]):
    """

    ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["Ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(List[int], d.pop("Ids", UNSET))

        keyfactor_api_models_security_roles_role_identities_request = cls(
            ids=ids,
        )

        keyfactor_api_models_security_roles_role_identities_request.additional_properties = d
        return keyfactor_api_models_security_roles_role_identities_request

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
