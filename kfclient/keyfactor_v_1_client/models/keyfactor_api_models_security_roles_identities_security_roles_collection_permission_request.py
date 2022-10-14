from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest:
    """
    Example:
        {'CollectionId': 1, 'Permission': 'Recover'}

    Attributes:
        collection_id (Union[Unset, int]):
        permission (Union[Unset, str]):
    """

    collection_id: Union[Unset, int] = UNSET
    permission: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection_id = self.collection_id
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_id is not UNSET:
            field_dict["CollectionId"] = collection_id
        if permission is not UNSET:
            field_dict["Permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collection_id = d.pop("CollectionId", UNSET)

        permission = d.pop("Permission", UNSET)

        keyfactor_api_models_security_roles_identities_security_roles_collection_permission_request = cls(
            collection_id=collection_id,
            permission=permission,
        )

        keyfactor_api_models_security_roles_identities_security_roles_collection_permission_request.additional_properties = (
            d
        )
        return keyfactor_api_models_security_roles_identities_security_roles_collection_permission_request

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
