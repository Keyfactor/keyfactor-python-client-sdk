# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.models_keyfactor_api_secret import ModelsKeyfactorAPISecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsDiscoveryJobRequest")


@attr.s(auto_attribs=True)
class ModelsDiscoveryJobRequest:
    """
    Attributes:
        type (int):
        client_machine (Union[Unset, str]):
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        job_execution_timestamp (Union[Unset, datetime.datetime]):
        dirs (Union[Unset, str]):
        ignored_dirs (Union[Unset, str]):
        extensions (Union[Unset, str]):
        name_patterns (Union[Unset, str]):
        sym_links (Union[Unset, bool]):
        compatibility (Union[Unset, bool]):
        server_username (Union[Unset, ModelsKeyfactorAPISecret]):
        server_password (Union[Unset, ModelsKeyfactorAPISecret]):
        server_use_ssl (Union[Unset, bool]):
    """

    type: int
    client_machine: Union[Unset, str] = UNSET
    agent_id: Union[Unset, str] = UNSET
    job_execution_timestamp: Union[Unset, datetime.datetime] = UNSET
    dirs: Union[Unset, str] = UNSET
    ignored_dirs: Union[Unset, str] = UNSET
    extensions: Union[Unset, str] = UNSET
    name_patterns: Union[Unset, str] = UNSET
    sym_links: Union[Unset, bool] = UNSET
    compatibility: Union[Unset, bool] = UNSET
    server_username: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    server_password: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    server_use_ssl: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        client_machine = self.client_machine
        agent_id = self.agent_id
        job_execution_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.job_execution_timestamp, Unset):
            job_execution_timestamp = self.job_execution_timestamp.isoformat()[:-6]+'Z'

        dirs = self.dirs
        ignored_dirs = self.ignored_dirs
        extensions = self.extensions
        name_patterns = self.name_patterns
        sym_links = self.sym_links
        compatibility = self.compatibility
        server_username: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_username, Unset):
            server_username = self.server_username.to_dict()

        server_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_password, Unset):
            server_password = self.server_password.to_dict()

        server_use_ssl = self.server_use_ssl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Type": type,
            }
        )
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if job_execution_timestamp is not UNSET:
            field_dict["JobExecutionTimestamp"] = job_execution_timestamp
        if dirs is not UNSET:
            field_dict["Dirs"] = dirs
        if ignored_dirs is not UNSET:
            field_dict["IgnoredDirs"] = ignored_dirs
        if extensions is not UNSET:
            field_dict["Extensions"] = extensions
        if name_patterns is not UNSET:
            field_dict["NamePatterns"] = name_patterns
        if sym_links is not UNSET:
            field_dict["SymLinks"] = sym_links
        if compatibility is not UNSET:
            field_dict["Compatibility"] = compatibility
        if server_username is not UNSET:
            field_dict["ServerUsername"] = server_username
        if server_password is not UNSET:
            field_dict["ServerPassword"] = server_password
        if server_use_ssl is not UNSET:
            field_dict["ServerUseSsl"] = server_use_ssl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type")

        client_machine = d.pop("ClientMachine", UNSET)

        agent_id = d.pop("AgentId", UNSET)

        _job_execution_timestamp = d.pop("JobExecutionTimestamp", UNSET)
        job_execution_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_job_execution_timestamp, Unset):
            job_execution_timestamp = UNSET
        else:
            job_execution_timestamp = isoparse(_job_execution_timestamp)

        dirs = d.pop("Dirs", UNSET)

        ignored_dirs = d.pop("IgnoredDirs", UNSET)

        extensions = d.pop("Extensions", UNSET)

        name_patterns = d.pop("NamePatterns", UNSET)

        sym_links = d.pop("SymLinks", UNSET)

        compatibility = d.pop("Compatibility", UNSET)

        _server_username = d.pop("ServerUsername", UNSET)
        server_username: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_server_username, Unset):
            server_username = UNSET
        else:
            server_username = ModelsKeyfactorAPISecret.from_dict(_server_username)

        _server_password = d.pop("ServerPassword", UNSET)
        server_password: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_server_password, Unset):
            server_password = UNSET
        else:
            server_password = ModelsKeyfactorAPISecret.from_dict(_server_password)

        server_use_ssl = d.pop("ServerUseSsl", UNSET)

        models_discovery_job_request = cls(
            type=type,
            client_machine=client_machine,
            agent_id=agent_id,
            job_execution_timestamp=job_execution_timestamp,
            dirs=dirs,
            ignored_dirs=ignored_dirs,
            extensions=extensions,
            name_patterns=name_patterns,
            sym_links=sym_links,
            compatibility=compatibility,
            server_username=server_username,
            server_password=server_password,
            server_use_ssl=server_use_ssl,
        )

        models_discovery_job_request.additional_properties = d
        return models_discovery_job_request

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
