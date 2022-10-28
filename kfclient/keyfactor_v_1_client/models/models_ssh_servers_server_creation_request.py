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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHServersServerCreationRequest")


@attr.s(auto_attribs=True)
class ModelsSSHServersServerCreationRequest:
    """
    Attributes:
        agent_id (str):  Example: 00000000-0000-0000-0000-000000000000.
        hostname (str):
        server_group_id (str):  Example: 00000000-0000-0000-0000-000000000000.
        under_management (Union[Unset, bool]):
        port (Union[Unset, int]):
    """

    agent_id: str
    hostname: str
    server_group_id: str
    under_management: Union[Unset, bool] = UNSET
    port: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        hostname = self.hostname
        server_group_id = self.server_group_id
        under_management = self.under_management
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AgentId": agent_id,
                "Hostname": hostname,
                "ServerGroupId": server_group_id,
            }
        )
        if under_management is not UNSET:
            field_dict["UnderManagement"] = under_management
        if port is not UNSET:
            field_dict["Port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_id = d.pop("AgentId")

        hostname = d.pop("Hostname")

        server_group_id = d.pop("ServerGroupId")

        under_management = d.pop("UnderManagement", UNSET)

        port = d.pop("Port", UNSET)

        models_ssh_servers_server_creation_request = cls(
            agent_id=agent_id,
            hostname=hostname,
            server_group_id=server_group_id,
            under_management=under_management,
            port=port,
        )

        models_ssh_servers_server_creation_request.additional_properties = d
        return models_ssh_servers_server_creation_request

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
