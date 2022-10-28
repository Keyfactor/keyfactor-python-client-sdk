from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsSecurityRolesContainerPermissionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSecurityRolesContainerPermissionResponse:
    """
    Attributes:
        container_id (Union[Unset, int]):
        name (Union[Unset, str]):
        permission (Union[Unset, str]):
    """

    container_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    permission: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_id = self.container_id
        name = self.name
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_id is not UNSET:
            field_dict["ContainerId"] = container_id
        if name is not UNSET:
            field_dict["Name"] = name
        if permission is not UNSET:
            field_dict["Permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        container_id = d.pop("ContainerId", UNSET)

        name = d.pop("Name", UNSET)

        permission = d.pop("Permission", UNSET)

        keyfactor_api_models_security_roles_container_permission_response = cls(
            container_id=container_id,
            name=name,
            permission=permission,
        )

        keyfactor_api_models_security_roles_container_permission_response.additional_properties = d
        return keyfactor_api_models_security_roles_container_permission_response

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