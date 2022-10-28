# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.models_ssh_access_logon_user_access_request import ModelsSSHAccessLogonUserAccessRequest

T = TypeVar("T", bound="ModelsSSHAccessServerAccessRequest")


@attr.s(auto_attribs=True)
class ModelsSSHAccessServerAccessRequest:
    """
    Attributes:
        server_id (int):
        logon_users (List[ModelsSSHAccessLogonUserAccessRequest]):
    """

    server_id: int
    logon_users: List[ModelsSSHAccessLogonUserAccessRequest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_id = self.server_id
        logon_users = []
        for logon_users_item_data in self.logon_users:
            logon_users_item = logon_users_item_data.to_dict()

            logon_users.append(logon_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ServerId": server_id,
                "LogonUsers": logon_users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_id = d.pop("ServerId")

        logon_users = []
        _logon_users = d.pop("LogonUsers")
        for logon_users_item_data in _logon_users:
            logon_users_item = ModelsSSHAccessLogonUserAccessRequest.from_dict(logon_users_item_data)

            logon_users.append(logon_users_item)

        models_ssh_access_server_access_request = cls(
            server_id=server_id,
            logon_users=logon_users,
        )

        models_ssh_access_server_access_request.additional_properties = d
        return models_ssh_access_server_access_request

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
