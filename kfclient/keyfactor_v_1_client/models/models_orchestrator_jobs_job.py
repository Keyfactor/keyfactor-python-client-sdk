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
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOrchestratorJobsJob")


@attr.s(auto_attribs=True)
class ModelsOrchestratorJobsJob:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        client_machine (Union[Unset, str]):
        target (Union[Unset, str]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        requested (Union[Unset, str]):
        job_type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    client_machine: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    requested: Union[Unset, str] = UNSET
    job_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        client_machine = self.client_machine
        target = self.target
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        requested = self.requested
        job_type = self.job_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if target is not UNSET:
            field_dict["Target"] = target
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule
        if requested is not UNSET:
            field_dict["Requested"] = requested
        if job_type is not UNSET:
            field_dict["JobType"] = job_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        target = d.pop("Target", UNSET)

        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        requested = d.pop("Requested", UNSET)

        job_type = d.pop("JobType", UNSET)

        models_orchestrator_jobs_job = cls(
            id=id,
            client_machine=client_machine,
            target=target,
            schedule=schedule,
            requested=requested,
            job_type=job_type,
        )

        models_orchestrator_jobs_job.additional_properties = d
        return models_orchestrator_jobs_job

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
