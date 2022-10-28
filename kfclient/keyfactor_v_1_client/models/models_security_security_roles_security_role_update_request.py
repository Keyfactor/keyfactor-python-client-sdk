# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.models_security_identities_security_identity_identifier import (
    ModelsSecurityIdentitiesSecurityIdentityIdentifier,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSecuritySecurityRolesSecurityRoleUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsSecuritySecurityRolesSecurityRoleUpdateRequest:
    """
    Attributes:
        id (int): The Id of the security role to update
        name (str): The name of the security role to update
        description (str): The description to be used on the updated security role
        enabled (Union[Unset, bool]): Whether or not the security role should be enabled
        private (Union[Unset, bool]): Whether or not the security role should be private
        permissions (Union[Unset, List[str]]): The permissions to include in the role. These must be supplied in the
            format "Area:Permission"
        identities (Union[Unset, List[ModelsSecurityIdentitiesSecurityIdentityIdentifier]]): The Keyfactor identities to
            assign to the updated role
    """

    id: int
    name: str
    description: str
    enabled: Union[Unset, bool] = UNSET
    private: Union[Unset, bool] = UNSET
    permissions: Union[Unset, List[str]] = UNSET
    identities: Union[Unset, List[ModelsSecurityIdentitiesSecurityIdentityIdentifier]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        enabled = self.enabled
        private = self.private
        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        identities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identities, Unset):
            identities = []
            for identities_item_data in self.identities:
                identities_item = identities_item_data.to_dict()

                identities.append(identities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Name": name,
                "Description": description,
            }
        )
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if private is not UNSET:
            field_dict["Private"] = private
        if permissions is not UNSET:
            field_dict["Permissions"] = permissions
        if identities is not UNSET:
            field_dict["Identities"] = identities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        name = d.pop("Name")

        description = d.pop("Description")

        enabled = d.pop("Enabled", UNSET)

        private = d.pop("Private", UNSET)

        permissions = cast(List[str], d.pop("Permissions", UNSET))

        identities = []
        _identities = d.pop("Identities", UNSET)
        for identities_item_data in _identities or []:
            identities_item = ModelsSecurityIdentitiesSecurityIdentityIdentifier.from_dict(identities_item_data)

            identities.append(identities_item)

        models_security_security_roles_security_role_update_request = cls(
            id=id,
            name=name,
            description=description,
            enabled=enabled,
            private=private,
            permissions=permissions,
            identities=identities,
        )

        models_security_security_roles_security_role_update_request.additional_properties = d
        return models_security_security_roles_security_role_update_request

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
