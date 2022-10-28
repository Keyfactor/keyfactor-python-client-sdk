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

from ..models.keyfactor_api_models_orchestrators_agent_blueprint_stores_response import (
    KeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse,
)
from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorsAgentBlueprintJobsResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorsAgentBlueprintJobsResponse:
    """
    Attributes:
        agent_blueprint_job_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        agent_blueprint_store_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        agent_blueprint_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        job_type (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        job_type_name (Union[Unset, str]):
        operation_type (Union[Unset, int]):
        thumbprint (Union[Unset, str]):
        contents (Union[Unset, str]):
        alias (Union[Unset, str]):
        private_key_entry (Union[Unset, bool]):
        overwrite (Union[Unset, bool]):
        has_entry_password (Union[Unset, bool]):
        has_pfx_password (Union[Unset, bool]):
        request_timestamp (Union[Unset, datetime.datetime]):
        keyfactor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        subject (Union[Unset, str]):
        directories (Union[Unset, str]):
        ignored_directories (Union[Unset, str]):
        sym_links (Union[Unset, bool]):
        compatibility (Union[Unset, bool]):
        file_extensions (Union[Unset, str]):
        file_name_patterns (Union[Unset, str]):
        agent_blueprint_stores (Union[Unset, KeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse]):
    """

    agent_blueprint_job_id: Union[Unset, str] = UNSET
    agent_blueprint_store_id: Union[Unset, str] = UNSET
    agent_blueprint_id: Union[Unset, str] = UNSET
    job_type: Union[Unset, str] = UNSET
    job_type_name: Union[Unset, str] = UNSET
    operation_type: Union[Unset, int] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    contents: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    private_key_entry: Union[Unset, bool] = UNSET
    overwrite: Union[Unset, bool] = UNSET
    has_entry_password: Union[Unset, bool] = UNSET
    has_pfx_password: Union[Unset, bool] = UNSET
    request_timestamp: Union[Unset, datetime.datetime] = UNSET
    keyfactor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    subject: Union[Unset, str] = UNSET
    directories: Union[Unset, str] = UNSET
    ignored_directories: Union[Unset, str] = UNSET
    sym_links: Union[Unset, bool] = UNSET
    compatibility: Union[Unset, bool] = UNSET
    file_extensions: Union[Unset, str] = UNSET
    file_name_patterns: Union[Unset, str] = UNSET
    agent_blueprint_stores: Union[Unset, KeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_blueprint_job_id = self.agent_blueprint_job_id
        agent_blueprint_store_id = self.agent_blueprint_store_id
        agent_blueprint_id = self.agent_blueprint_id
        job_type = self.job_type
        job_type_name = self.job_type_name
        operation_type = self.operation_type
        thumbprint = self.thumbprint
        contents = self.contents
        alias = self.alias
        private_key_entry = self.private_key_entry
        overwrite = self.overwrite
        has_entry_password = self.has_entry_password
        has_pfx_password = self.has_pfx_password
        request_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.request_timestamp, Unset):
            request_timestamp = self.request_timestamp.isoformat()[:-6]+'Z'

        keyfactor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keyfactor_schedule, Unset):
            keyfactor_schedule = self.keyfactor_schedule.to_dict()

        subject = self.subject
        directories = self.directories
        ignored_directories = self.ignored_directories
        sym_links = self.sym_links
        compatibility = self.compatibility
        file_extensions = self.file_extensions
        file_name_patterns = self.file_name_patterns
        agent_blueprint_stores: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.agent_blueprint_stores, Unset):
            agent_blueprint_stores = self.agent_blueprint_stores.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_blueprint_job_id is not UNSET:
            field_dict["AgentBlueprintJobId"] = agent_blueprint_job_id
        if agent_blueprint_store_id is not UNSET:
            field_dict["AgentBlueprintStoreId"] = agent_blueprint_store_id
        if agent_blueprint_id is not UNSET:
            field_dict["AgentBlueprintId"] = agent_blueprint_id
        if job_type is not UNSET:
            field_dict["JobType"] = job_type
        if job_type_name is not UNSET:
            field_dict["JobTypeName"] = job_type_name
        if operation_type is not UNSET:
            field_dict["OperationType"] = operation_type
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if contents is not UNSET:
            field_dict["Contents"] = contents
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if private_key_entry is not UNSET:
            field_dict["PrivateKeyEntry"] = private_key_entry
        if overwrite is not UNSET:
            field_dict["Overwrite"] = overwrite
        if has_entry_password is not UNSET:
            field_dict["HasEntryPassword"] = has_entry_password
        if has_pfx_password is not UNSET:
            field_dict["HasPfxPassword"] = has_pfx_password
        if request_timestamp is not UNSET:
            field_dict["RequestTimestamp"] = request_timestamp
        if keyfactor_schedule is not UNSET:
            field_dict["KeyfactorSchedule"] = keyfactor_schedule
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if directories is not UNSET:
            field_dict["Directories"] = directories
        if ignored_directories is not UNSET:
            field_dict["IgnoredDirectories"] = ignored_directories
        if sym_links is not UNSET:
            field_dict["SymLinks"] = sym_links
        if compatibility is not UNSET:
            field_dict["Compatibility"] = compatibility
        if file_extensions is not UNSET:
            field_dict["FileExtensions"] = file_extensions
        if file_name_patterns is not UNSET:
            field_dict["FileNamePatterns"] = file_name_patterns
        if agent_blueprint_stores is not UNSET:
            field_dict["AgentBlueprintStores"] = agent_blueprint_stores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_blueprint_job_id = d.pop("AgentBlueprintJobId", UNSET)

        agent_blueprint_store_id = d.pop("AgentBlueprintStoreId", UNSET)

        agent_blueprint_id = d.pop("AgentBlueprintId", UNSET)

        job_type = d.pop("JobType", UNSET)

        job_type_name = d.pop("JobTypeName", UNSET)

        operation_type = d.pop("OperationType", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        contents = d.pop("Contents", UNSET)

        alias = d.pop("Alias", UNSET)

        private_key_entry = d.pop("PrivateKeyEntry", UNSET)

        overwrite = d.pop("Overwrite", UNSET)

        has_entry_password = d.pop("HasEntryPassword", UNSET)

        has_pfx_password = d.pop("HasPfxPassword", UNSET)

        _request_timestamp = d.pop("RequestTimestamp", UNSET)
        request_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_request_timestamp, Unset):
            request_timestamp = UNSET
        else:
            request_timestamp = isoparse(_request_timestamp)

        _keyfactor_schedule = d.pop("KeyfactorSchedule", UNSET)
        keyfactor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_keyfactor_schedule, Unset):
            keyfactor_schedule = UNSET
        else:
            keyfactor_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_keyfactor_schedule)

        subject = d.pop("Subject", UNSET)

        directories = d.pop("Directories", UNSET)

        ignored_directories = d.pop("IgnoredDirectories", UNSET)

        sym_links = d.pop("SymLinks", UNSET)

        compatibility = d.pop("Compatibility", UNSET)

        file_extensions = d.pop("FileExtensions", UNSET)

        file_name_patterns = d.pop("FileNamePatterns", UNSET)

        _agent_blueprint_stores = d.pop("AgentBlueprintStores", UNSET)
        agent_blueprint_stores: Union[Unset, KeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse]
        if isinstance(_agent_blueprint_stores, Unset):
            agent_blueprint_stores = UNSET
        else:
            agent_blueprint_stores = KeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse.from_dict(
                _agent_blueprint_stores
            )

        keyfactor_api_models_orchestrators_agent_blueprint_jobs_response = cls(
            agent_blueprint_job_id=agent_blueprint_job_id,
            agent_blueprint_store_id=agent_blueprint_store_id,
            agent_blueprint_id=agent_blueprint_id,
            job_type=job_type,
            job_type_name=job_type_name,
            operation_type=operation_type,
            thumbprint=thumbprint,
            contents=contents,
            alias=alias,
            private_key_entry=private_key_entry,
            overwrite=overwrite,
            has_entry_password=has_entry_password,
            has_pfx_password=has_pfx_password,
            request_timestamp=request_timestamp,
            keyfactor_schedule=keyfactor_schedule,
            subject=subject,
            directories=directories,
            ignored_directories=ignored_directories,
            sym_links=sym_links,
            compatibility=compatibility,
            file_extensions=file_extensions,
            file_name_patterns=file_name_patterns,
            agent_blueprint_stores=agent_blueprint_stores,
        )

        keyfactor_api_models_orchestrators_agent_blueprint_jobs_response.additional_properties = d
        return keyfactor_api_models_orchestrators_agent_blueprint_jobs_response

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
