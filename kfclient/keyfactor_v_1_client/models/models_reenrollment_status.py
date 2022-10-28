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

from ..models.models_certificate_store_types_certificate_store_type_entry_parameter import (
    ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsReenrollmentStatus")


@attr.s(auto_attribs=True)
class ModelsReenrollmentStatus:
    """
    Attributes:
        data (Union[Unset, bool]):
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        message (Union[Unset, str]):
        job_properties (Union[Unset, str]):
        custom_alias_allowed (Union[Unset, int]):
        entry_parameters (Union[Unset, List[ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter]]):
    """

    data: Union[Unset, bool] = UNSET
    agent_id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    job_properties: Union[Unset, str] = UNSET
    custom_alias_allowed: Union[Unset, int] = UNSET
    entry_parameters: Union[Unset, List[ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        agent_id = self.agent_id
        message = self.message
        job_properties = self.job_properties
        custom_alias_allowed = self.custom_alias_allowed
        entry_parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry_parameters, Unset):
            entry_parameters = []
            for entry_parameters_item_data in self.entry_parameters:
                entry_parameters_item = entry_parameters_item_data.to_dict()

                entry_parameters.append(entry_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["Data"] = data
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if message is not UNSET:
            field_dict["Message"] = message
        if job_properties is not UNSET:
            field_dict["JobProperties"] = job_properties
        if custom_alias_allowed is not UNSET:
            field_dict["CustomAliasAllowed"] = custom_alias_allowed
        if entry_parameters is not UNSET:
            field_dict["EntryParameters"] = entry_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("Data", UNSET)

        agent_id = d.pop("AgentId", UNSET)

        message = d.pop("Message", UNSET)

        job_properties = d.pop("JobProperties", UNSET)

        custom_alias_allowed = d.pop("CustomAliasAllowed", UNSET)

        entry_parameters = []
        _entry_parameters = d.pop("EntryParameters", UNSET)
        for entry_parameters_item_data in _entry_parameters or []:
            entry_parameters_item = ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter.from_dict(
                entry_parameters_item_data
            )

            entry_parameters.append(entry_parameters_item)

        models_reenrollment_status = cls(
            data=data,
            agent_id=agent_id,
            message=message,
            job_properties=job_properties,
            custom_alias_allowed=custom_alias_allowed,
            entry_parameters=entry_parameters,
        )

        models_reenrollment_status.additional_properties = d
        return models_reenrollment_status

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
