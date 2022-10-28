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

from ..models.models_ssh_server_groups_server_group_response import ModelsSSHServerGroupsServerGroupResponse
from ..models.models_ssh_users_ssh_user_response import ModelsSSHUsersSshUserResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHServiceAccountsServiceAccountResponse")


@attr.s(auto_attribs=True)
class ModelsSSHServiceAccountsServiceAccountResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        client_hostname (Union[Unset, str]):
        server_group (Union[Unset, ModelsSSHServerGroupsServerGroupResponse]):
        user (Union[Unset, ModelsSSHUsersSshUserResponse]):
    """

    id: Union[Unset, int] = UNSET
    client_hostname: Union[Unset, str] = UNSET
    server_group: Union[Unset, ModelsSSHServerGroupsServerGroupResponse] = UNSET
    user: Union[Unset, ModelsSSHUsersSshUserResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        client_hostname = self.client_hostname
        server_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_group, Unset):
            server_group = self.server_group.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if client_hostname is not UNSET:
            field_dict["ClientHostname"] = client_hostname
        if server_group is not UNSET:
            field_dict["ServerGroup"] = server_group
        if user is not UNSET:
            field_dict["User"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        client_hostname = d.pop("ClientHostname", UNSET)

        _server_group = d.pop("ServerGroup", UNSET)
        server_group: Union[Unset, ModelsSSHServerGroupsServerGroupResponse]
        if isinstance(_server_group, Unset):
            server_group = UNSET
        else:
            server_group = ModelsSSHServerGroupsServerGroupResponse.from_dict(_server_group)

        _user = d.pop("User", UNSET)
        user: Union[Unset, ModelsSSHUsersSshUserResponse]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ModelsSSHUsersSshUserResponse.from_dict(_user)

        models_ssh_service_accounts_service_account_response = cls(
            id=id,
            client_hostname=client_hostname,
            server_group=server_group,
            user=user,
        )

        models_ssh_service_accounts_service_account_response.additional_properties = d
        return models_ssh_service_accounts_service_account_response

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
