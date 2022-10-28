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

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..models.models_ssh_users_ssh_user_response import ModelsSSHUsersSshUserResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHServersServerResponse")


@attr.s(auto_attribs=True)
class ModelsSSHServersServerResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        hostname (Union[Unset, str]):
        server_group_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        sync_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        under_management (Union[Unset, bool]):
        owner (Union[Unset, ModelsSSHUsersSshUserResponse]):
        group_name (Union[Unset, str]):
        orchestrator (Union[Unset, str]):
        port (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    agent_id: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    server_group_id: Union[Unset, str] = UNSET
    sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    under_management: Union[Unset, bool] = UNSET
    owner: Union[Unset, ModelsSSHUsersSshUserResponse] = UNSET
    group_name: Union[Unset, str] = UNSET
    orchestrator: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        agent_id = self.agent_id
        hostname = self.hostname
        server_group_id = self.server_group_id
        sync_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_schedule, Unset):
            sync_schedule = self.sync_schedule.to_dict()

        under_management = self.under_management
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        group_name = self.group_name
        orchestrator = self.orchestrator
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if hostname is not UNSET:
            field_dict["Hostname"] = hostname
        if server_group_id is not UNSET:
            field_dict["ServerGroupId"] = server_group_id
        if sync_schedule is not UNSET:
            field_dict["SyncSchedule"] = sync_schedule
        if under_management is not UNSET:
            field_dict["UnderManagement"] = under_management
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if group_name is not UNSET:
            field_dict["GroupName"] = group_name
        if orchestrator is not UNSET:
            field_dict["Orchestrator"] = orchestrator
        if port is not UNSET:
            field_dict["Port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        agent_id = d.pop("AgentId", UNSET)

        hostname = d.pop("Hostname", UNSET)

        server_group_id = d.pop("ServerGroupId", UNSET)

        _sync_schedule = d.pop("SyncSchedule", UNSET)
        sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_sync_schedule, Unset):
            sync_schedule = UNSET
        else:
            sync_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_sync_schedule)

        under_management = d.pop("UnderManagement", UNSET)

        _owner = d.pop("Owner", UNSET)
        owner: Union[Unset, ModelsSSHUsersSshUserResponse]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ModelsSSHUsersSshUserResponse.from_dict(_owner)

        group_name = d.pop("GroupName", UNSET)

        orchestrator = d.pop("Orchestrator", UNSET)

        port = d.pop("Port", UNSET)

        models_ssh_servers_server_response = cls(
            id=id,
            agent_id=agent_id,
            hostname=hostname,
            server_group_id=server_group_id,
            sync_schedule=sync_schedule,
            under_management=under_management,
            owner=owner,
            group_name=group_name,
            orchestrator=orchestrator,
            port=port,
        )

        models_ssh_servers_server_response.additional_properties = d
        return models_ssh_servers_server_response

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
