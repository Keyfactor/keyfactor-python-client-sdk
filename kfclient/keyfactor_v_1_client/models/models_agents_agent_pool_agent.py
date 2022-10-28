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

T = TypeVar("T", bound="ModelsAgentsAgentPoolAgent")


@attr.s(auto_attribs=True)
class ModelsAgentsAgentPoolAgent:
    """
    Attributes:
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        enable_discover (Union[Unset, bool]):
        enable_monitor (Union[Unset, bool]):
        version (Union[Unset, str]):
        allows_discover (Union[Unset, bool]):
        allows_monitor (Union[Unset, bool]):
        client_machine (Union[Unset, str]):
    """

    agent_id: Union[Unset, str] = UNSET
    enable_discover: Union[Unset, bool] = UNSET
    enable_monitor: Union[Unset, bool] = UNSET
    version: Union[Unset, str] = UNSET
    allows_discover: Union[Unset, bool] = UNSET
    allows_monitor: Union[Unset, bool] = UNSET
    client_machine: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        enable_discover = self.enable_discover
        enable_monitor = self.enable_monitor
        version = self.version
        allows_discover = self.allows_discover
        allows_monitor = self.allows_monitor
        client_machine = self.client_machine

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if enable_discover is not UNSET:
            field_dict["EnableDiscover"] = enable_discover
        if enable_monitor is not UNSET:
            field_dict["EnableMonitor"] = enable_monitor
        if version is not UNSET:
            field_dict["Version"] = version
        if allows_discover is not UNSET:
            field_dict["AllowsDiscover"] = allows_discover
        if allows_monitor is not UNSET:
            field_dict["AllowsMonitor"] = allows_monitor
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_id = d.pop("AgentId", UNSET)

        enable_discover = d.pop("EnableDiscover", UNSET)

        enable_monitor = d.pop("EnableMonitor", UNSET)

        version = d.pop("Version", UNSET)

        allows_discover = d.pop("AllowsDiscover", UNSET)

        allows_monitor = d.pop("AllowsMonitor", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        models_agents_agent_pool_agent = cls(
            agent_id=agent_id,
            enable_discover=enable_discover,
            enable_monitor=enable_monitor,
            version=version,
            allows_discover=allows_discover,
            allows_monitor=allows_monitor,
            client_machine=client_machine,
        )

        models_agents_agent_pool_agent.additional_properties = d
        return models_agents_agent_pool_agent

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
