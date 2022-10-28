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

T = TypeVar("T", bound="ModelsOrchestratorJobsBulkOrchestratorJobPair")


@attr.s(auto_attribs=True)
class ModelsOrchestratorJobsBulkOrchestratorJobPair:
    """
    Attributes:
        job_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        orchestrator_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
    """

    job_id: Union[Unset, str] = UNSET
    orchestrator_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        orchestrator_id = self.orchestrator_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["JobId"] = job_id
        if orchestrator_id is not UNSET:
            field_dict["OrchestratorId"] = orchestrator_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("JobId", UNSET)

        orchestrator_id = d.pop("OrchestratorId", UNSET)

        models_orchestrator_jobs_bulk_orchestrator_job_pair = cls(
            job_id=job_id,
            orchestrator_id=orchestrator_id,
        )

        models_orchestrator_jobs_bulk_orchestrator_job_pair.additional_properties = d
        return models_orchestrator_jobs_bulk_orchestrator_job_pair

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
