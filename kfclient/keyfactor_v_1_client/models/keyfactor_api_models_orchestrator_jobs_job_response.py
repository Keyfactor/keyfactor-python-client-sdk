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

from ..models.keyfactor_api_models_orchestrator_jobs_job_field_response import (
    KeyfactorApiModelsOrchestratorJobsJobFieldResponse,
)
from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorJobsJobResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorJobsJobResponse:
    """
    Attributes:
        job_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        orchestrator_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        job_type_name (Union[Unset, str]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_fields (Union[Unset, List[KeyfactorApiModelsOrchestratorJobsJobFieldResponse]]):
        request_timestamp (Union[Unset, datetime.datetime]):
    """

    job_id: Union[Unset, str] = UNSET
    orchestrator_id: Union[Unset, str] = UNSET
    job_type_name: Union[Unset, str] = UNSET
    schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    job_fields: Union[Unset, List[KeyfactorApiModelsOrchestratorJobsJobFieldResponse]] = UNSET
    request_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        orchestrator_id = self.orchestrator_id
        job_type_name = self.job_type_name
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        job_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = []
            for job_fields_item_data in self.job_fields:
                job_fields_item = job_fields_item_data.to_dict()

                job_fields.append(job_fields_item)

        request_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.request_timestamp, Unset):
            request_timestamp = self.request_timestamp.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["JobId"] = job_id
        if orchestrator_id is not UNSET:
            field_dict["OrchestratorId"] = orchestrator_id
        if job_type_name is not UNSET:
            field_dict["JobTypeName"] = job_type_name
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule
        if job_fields is not UNSET:
            field_dict["JobFields"] = job_fields
        if request_timestamp is not UNSET:
            field_dict["RequestTimestamp"] = request_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("JobId", UNSET)

        orchestrator_id = d.pop("OrchestratorId", UNSET)

        job_type_name = d.pop("JobTypeName", UNSET)

        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        job_fields = []
        _job_fields = d.pop("JobFields", UNSET)
        for job_fields_item_data in _job_fields or []:
            job_fields_item = KeyfactorApiModelsOrchestratorJobsJobFieldResponse.from_dict(job_fields_item_data)

            job_fields.append(job_fields_item)

        _request_timestamp = d.pop("RequestTimestamp", UNSET)
        request_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_request_timestamp, Unset):
            request_timestamp = UNSET
        else:
            request_timestamp = isoparse(_request_timestamp)

        keyfactor_api_models_orchestrator_jobs_job_response = cls(
            job_id=job_id,
            orchestrator_id=orchestrator_id,
            job_type_name=job_type_name,
            schedule=schedule,
            job_fields=job_fields,
            request_timestamp=request_timestamp,
        )

        keyfactor_api_models_orchestrator_jobs_job_response.additional_properties = d
        return keyfactor_api_models_orchestrator_jobs_job_response

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
