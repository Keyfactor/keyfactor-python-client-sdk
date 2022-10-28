# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorJobsRescheduleJobRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorJobsRescheduleJobRequest:
    """Class representing orchestrator jobs to be rescheduled

    Attributes:
        job_audit_ids (Union[Unset, List[int]]): List of orchestrator job audit ids to be rescheduled
        query (Union[Unset, str]): Query identifying orchestrator jobs to be rescheduled
    """

    job_audit_ids: Union[Unset, List[int]] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_audit_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.job_audit_ids, Unset):
            job_audit_ids = self.job_audit_ids

        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_audit_ids is not UNSET:
            field_dict["JobAuditIds"] = job_audit_ids
        if query is not UNSET:
            field_dict["Query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_audit_ids = cast(List[int], d.pop("JobAuditIds", UNSET))

        query = d.pop("Query", UNSET)

        keyfactor_api_models_orchestrator_jobs_reschedule_job_request = cls(
            job_audit_ids=job_audit_ids,
            query=query,
        )

        keyfactor_api_models_orchestrator_jobs_reschedule_job_request.additional_properties = d
        return keyfactor_api_models_orchestrator_jobs_reschedule_job_request

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
