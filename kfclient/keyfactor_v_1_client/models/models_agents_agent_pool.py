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

from ..models.models_agents_agent_pool_agent import ModelsAgentsAgentPoolAgent
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsAgentsAgentPool")


@attr.s(auto_attribs=True)
class ModelsAgentsAgentPool:
    """Class representing an SSL agent pool

    Attributes:
        name (str): Name of the agent pool
        agent_pool_id (Union[Unset, str]): GUID identifier of the agent pool Example:
            00000000-0000-0000-0000-000000000000.
        discover_agents_count (Union[Unset, int]): Number of agents that can perform discovery jobs
        monitor_agents_count (Union[Unset, int]): Number of agents that can perform monitoring jobs
        agents (Union[Unset, List[ModelsAgentsAgentPoolAgent]]): List of the agents assigned to the pool
    """

    name: str
    agent_pool_id: Union[Unset, str] = UNSET
    discover_agents_count: Union[Unset, int] = UNSET
    monitor_agents_count: Union[Unset, int] = UNSET
    agents: Union[Unset, List[ModelsAgentsAgentPoolAgent]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        agent_pool_id = self.agent_pool_id
        discover_agents_count = self.discover_agents_count
        monitor_agents_count = self.monitor_agents_count
        agents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()

                agents.append(agents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
            }
        )
        if agent_pool_id is not UNSET:
            field_dict["AgentPoolId"] = agent_pool_id
        if discover_agents_count is not UNSET:
            field_dict["DiscoverAgentsCount"] = discover_agents_count
        if monitor_agents_count is not UNSET:
            field_dict["MonitorAgentsCount"] = monitor_agents_count
        if agents is not UNSET:
            field_dict["Agents"] = agents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        agent_pool_id = d.pop("AgentPoolId", UNSET)

        discover_agents_count = d.pop("DiscoverAgentsCount", UNSET)

        monitor_agents_count = d.pop("MonitorAgentsCount", UNSET)

        agents = []
        _agents = d.pop("Agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = ModelsAgentsAgentPoolAgent.from_dict(agents_item_data)

            agents.append(agents_item)

        models_agents_agent_pool = cls(
            name=name,
            agent_pool_id=agent_pool_id,
            discover_agents_count=discover_agents_count,
            monitor_agents_count=monitor_agents_count,
            agents=agents,
        )

        models_agents_agent_pool.additional_properties = d
        return models_agents_agent_pool

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
