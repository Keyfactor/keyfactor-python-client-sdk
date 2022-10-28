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

from ..models.keyfactor_api_models_orchestrator_jobs_job_type_field_response_type import (
    KeyfactorApiModelsOrchestratorJobsJobTypeFieldResponseType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorJobsJobTypeFieldResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorJobsJobTypeFieldResponse:
    """
    Attributes:
        name (Union[Unset, str]):
        type (Union[Unset, KeyfactorApiModelsOrchestratorJobsJobTypeFieldResponseType]):
        default_value (Union[Unset, str]):
        required (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, KeyfactorApiModelsOrchestratorJobsJobTypeFieldResponseType] = UNSET
    default_value: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if type is not UNSET:
            field_dict["Type"] = type
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if required is not UNSET:
            field_dict["Required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, KeyfactorApiModelsOrchestratorJobsJobTypeFieldResponseType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = KeyfactorApiModelsOrchestratorJobsJobTypeFieldResponseType(_type)

        default_value = d.pop("DefaultValue", UNSET)

        required = d.pop("Required", UNSET)

        keyfactor_api_models_orchestrator_jobs_job_type_field_response = cls(
            name=name,
            type=type,
            default_value=default_value,
            required=required,
        )

        keyfactor_api_models_orchestrator_jobs_job_type_field_response.additional_properties = d
        return keyfactor_api_models_orchestrator_jobs_job_type_field_response

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
