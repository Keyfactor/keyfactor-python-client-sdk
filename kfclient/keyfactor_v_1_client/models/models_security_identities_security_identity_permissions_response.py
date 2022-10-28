# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_security_identities_permission_roles_pair_response import (
    ModelsSecurityIdentitiesPermissionRolesPairResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSecurityIdentitiesSecurityIdentityPermissionsResponse")


@attr.s(auto_attribs=True)
class ModelsSecurityIdentitiesSecurityIdentityPermissionsResponse:
    """
    Attributes:
        identity (Union[Unset, str]):
        secured_area_permissions (Union[Unset, List[ModelsSecurityIdentitiesPermissionRolesPairResponse]]):
        collection_permissions (Union[Unset, List[ModelsSecurityIdentitiesPermissionRolesPairResponse]]):
        container_permissions (Union[Unset, List[ModelsSecurityIdentitiesPermissionRolesPairResponse]]):
    """

    identity: Union[Unset, str] = UNSET
    secured_area_permissions: Union[Unset, List[ModelsSecurityIdentitiesPermissionRolesPairResponse]] = UNSET
    collection_permissions: Union[Unset, List[ModelsSecurityIdentitiesPermissionRolesPairResponse]] = UNSET
    container_permissions: Union[Unset, List[ModelsSecurityIdentitiesPermissionRolesPairResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identity = self.identity
        secured_area_permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.secured_area_permissions, Unset):
            secured_area_permissions = []
            for secured_area_permissions_item_data in self.secured_area_permissions:
                secured_area_permissions_item = secured_area_permissions_item_data.to_dict()

                secured_area_permissions.append(secured_area_permissions_item)

        collection_permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.collection_permissions, Unset):
            collection_permissions = []
            for collection_permissions_item_data in self.collection_permissions:
                collection_permissions_item = collection_permissions_item_data.to_dict()

                collection_permissions.append(collection_permissions_item)

        container_permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.container_permissions, Unset):
            container_permissions = []
            for container_permissions_item_data in self.container_permissions:
                container_permissions_item = container_permissions_item_data.to_dict()

                container_permissions.append(container_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity is not UNSET:
            field_dict["Identity"] = identity
        if secured_area_permissions is not UNSET:
            field_dict["SecuredAreaPermissions"] = secured_area_permissions
        if collection_permissions is not UNSET:
            field_dict["CollectionPermissions"] = collection_permissions
        if container_permissions is not UNSET:
            field_dict["ContainerPermissions"] = container_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identity = d.pop("Identity", UNSET)

        secured_area_permissions = []
        _secured_area_permissions = d.pop("SecuredAreaPermissions", UNSET)
        for secured_area_permissions_item_data in _secured_area_permissions or []:
            secured_area_permissions_item = ModelsSecurityIdentitiesPermissionRolesPairResponse.from_dict(
                secured_area_permissions_item_data
            )

            secured_area_permissions.append(secured_area_permissions_item)

        collection_permissions = []
        _collection_permissions = d.pop("CollectionPermissions", UNSET)
        for collection_permissions_item_data in _collection_permissions or []:
            collection_permissions_item = ModelsSecurityIdentitiesPermissionRolesPairResponse.from_dict(
                collection_permissions_item_data
            )

            collection_permissions.append(collection_permissions_item)

        container_permissions = []
        _container_permissions = d.pop("ContainerPermissions", UNSET)
        for container_permissions_item_data in _container_permissions or []:
            container_permissions_item = ModelsSecurityIdentitiesPermissionRolesPairResponse.from_dict(
                container_permissions_item_data
            )

            container_permissions.append(container_permissions_item)

        models_security_identities_security_identity_permissions_response = cls(
            identity=identity,
            secured_area_permissions=secured_area_permissions,
            collection_permissions=collection_permissions,
            container_permissions=container_permissions,
        )

        models_security_identities_security_identity_permissions_response.additional_properties = d
        return models_security_identities_security_identity_permissions_response

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
