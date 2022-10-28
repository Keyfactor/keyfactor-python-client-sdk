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

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorJobsUnscheduleJobRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorJobsUnscheduleJobRequest:
    """Class representing orchestrator jobs to be unscheduled

    Attributes:
        job_ids (Union[Unset, List[str]]): List of orchestrator job ids to be unscheduled
        query (Union[Unset, str]): Query identifying orchestrator jobs to be unscheduled
    """

    job_ids: Union[Unset, List[str]] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.job_ids, Unset):
            job_ids = self.job_ids

        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_ids is not UNSET:
            field_dict["JobIds"] = job_ids
        if query is not UNSET:
            field_dict["Query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_ids = cast(List[str], d.pop("JobIds", UNSET))

        query = d.pop("Query", UNSET)

        keyfactor_api_models_orchestrator_jobs_unschedule_job_request = cls(
            job_ids=job_ids,
            query=query,
        )

        keyfactor_api_models_orchestrator_jobs_unschedule_job_request.additional_properties = d
        return keyfactor_api_models_orchestrator_jobs_unschedule_job_request

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
