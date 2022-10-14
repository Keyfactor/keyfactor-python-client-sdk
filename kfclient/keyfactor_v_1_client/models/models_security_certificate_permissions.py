from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_security_security_roles_security_role_response_base import (
    ModelsSecuritySecurityRolesSecurityRoleResponseBase,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSecurityCertificatePermissions")


@attr.s(auto_attribs=True)
class ModelsSecurityCertificatePermissions:
    """A list of permissions for a given certificate and which security role(s) granted them.

    Attributes:
        roles (Union[Unset, List[ModelsSecuritySecurityRolesSecurityRoleResponseBase]]):
    """

    roles: Union[Unset, List[ModelsSecuritySecurityRolesSecurityRoleResponseBase]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()

                roles.append(roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roles is not UNSET:
            field_dict["Roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        roles = []
        _roles = d.pop("Roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = ModelsSecuritySecurityRolesSecurityRoleResponseBase.from_dict(roles_item_data)

            roles.append(roles_item)

        models_security_certificate_permissions = cls(
            roles=roles,
        )

        models_security_certificate_permissions.additional_properties = d
        return models_security_certificate_permissions

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
