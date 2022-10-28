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
from ..models.models_orchestrator_jobs_schedule_job_request_job_fields import (
    ModelsOrchestratorJobsScheduleJobRequestJobFields,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOrchestratorJobsScheduleJobRequest")


@attr.s(auto_attribs=True)
class ModelsOrchestratorJobsScheduleJobRequest:
    """
    Attributes:
        agent_id (str):  Example: 00000000-0000-0000-0000-000000000000.
        job_type_name (str):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_fields (Union[Unset, ModelsOrchestratorJobsScheduleJobRequestJobFields]):
    """

    agent_id: str
    job_type_name: str
    schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    job_fields: Union[Unset, ModelsOrchestratorJobsScheduleJobRequestJobFields] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        job_type_name = self.job_type_name
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        job_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = self.job_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AgentId": agent_id,
                "JobTypeName": job_type_name,
            }
        )
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule
        if job_fields is not UNSET:
            field_dict["JobFields"] = job_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_id = d.pop("AgentId")

        job_type_name = d.pop("JobTypeName")

        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        _job_fields = d.pop("JobFields", UNSET)
        job_fields: Union[Unset, ModelsOrchestratorJobsScheduleJobRequestJobFields]
        if isinstance(_job_fields, Unset):
            job_fields = UNSET
        else:
            job_fields = ModelsOrchestratorJobsScheduleJobRequestJobFields.from_dict(_job_fields)

        models_orchestrator_jobs_schedule_job_request = cls(
            agent_id=agent_id,
            job_type_name=job_type_name,
            schedule=schedule,
            job_fields=job_fields,
        )

        models_orchestrator_jobs_schedule_job_request.additional_properties = d
        return models_orchestrator_jobs_schedule_job_request

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
