from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSecurityIdentitiesPermissionRolesPairResponse")


@attr.s(auto_attribs=True)
class ModelsSecurityIdentitiesPermissionRolesPairResponse:
    """
    Attributes:
        permission (Union[Unset, str]):
        granted_by_roles (Union[Unset, List[str]]):
    """

    permission: Union[Unset, str] = UNSET
    granted_by_roles: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission
        granted_by_roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.granted_by_roles, Unset):
            granted_by_roles = self.granted_by_roles

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["Permission"] = permission
        if granted_by_roles is not UNSET:
            field_dict["GrantedByRoles"] = granted_by_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permission = d.pop("Permission", UNSET)

        granted_by_roles = cast(List[str], d.pop("GrantedByRoles", UNSET))

        models_security_identities_permission_roles_pair_response = cls(
            permission=permission,
            granted_by_roles=granted_by_roles,
        )

        models_security_identities_permission_roles_pair_response.additional_properties = d
        return models_security_identities_permission_roles_pair_response

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
