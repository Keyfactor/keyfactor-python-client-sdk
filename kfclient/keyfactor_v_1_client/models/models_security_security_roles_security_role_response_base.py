from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSecuritySecurityRolesSecurityRoleResponseBase")


@attr.s(auto_attribs=True)
class ModelsSecuritySecurityRolesSecurityRoleResponseBase:
    """
    Attributes:
        name (Union[Unset, str]): The name of the created role
        permissions (Union[Unset, List[str]]): The permissions included in the created security role
    """

    name: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        permissions = cast(List[str], d.pop("Permissions", UNSET))

        models_security_security_roles_security_role_response_base = cls(
            name=name,
            permissions=permissions,
        )

        models_security_security_roles_security_role_response_base.additional_properties = d
        return models_security_security_roles_security_role_response_base

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
