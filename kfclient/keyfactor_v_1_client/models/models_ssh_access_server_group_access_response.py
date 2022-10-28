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

from ..models.models_ssh_access_logon_user_access_response import ModelsSSHAccessLogonUserAccessResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHAccessServerGroupAccessResponse")


@attr.s(auto_attribs=True)
class ModelsSSHAccessServerGroupAccessResponse:
    """
    Attributes:
        server_group_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        logon_users (Union[Unset, List[ModelsSSHAccessLogonUserAccessResponse]]):
    """

    server_group_id: Union[Unset, str] = UNSET
    logon_users: Union[Unset, List[ModelsSSHAccessLogonUserAccessResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_group_id = self.server_group_id
        logon_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logon_users, Unset):
            logon_users = []
            for logon_users_item_data in self.logon_users:
                logon_users_item = logon_users_item_data.to_dict()

                logon_users.append(logon_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_group_id is not UNSET:
            field_dict["ServerGroupId"] = server_group_id
        if logon_users is not UNSET:
            field_dict["LogonUsers"] = logon_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_group_id = d.pop("ServerGroupId", UNSET)

        logon_users = []
        _logon_users = d.pop("LogonUsers", UNSET)
        for logon_users_item_data in _logon_users or []:
            logon_users_item = ModelsSSHAccessLogonUserAccessResponse.from_dict(logon_users_item_data)

            logon_users.append(logon_users_item)

        models_ssh_access_server_group_access_response = cls(
            server_group_id=server_group_id,
            logon_users=logon_users,
        )

        models_ssh_access_server_group_access_response.additional_properties = d
        return models_ssh_access_server_group_access_response

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
