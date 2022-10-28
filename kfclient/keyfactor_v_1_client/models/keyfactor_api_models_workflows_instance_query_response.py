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

from ..models.keyfactor_api_models_workflows_instance_definition_response import (
    KeyfactorApiModelsWorkflowsInstanceDefinitionResponse,
)
from ..models.keyfactor_api_models_workflows_instance_query_response_status import (
    KeyfactorApiModelsWorkflowsInstanceQueryResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsInstanceQueryResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsInstanceQueryResponse:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        status (Union[Unset, KeyfactorApiModelsWorkflowsInstanceQueryResponseStatus]):
        current_step_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        status_message (Union[Unset, str]):
        definition (Union[Unset, KeyfactorApiModelsWorkflowsInstanceDefinitionResponse]):
        current_step_display_name (Union[Unset, str]):
        current_step_unique_name (Union[Unset, str]):
        title (Union[Unset, str]):
        last_modified (Union[Unset, datetime.datetime]):
        start_date (Union[Unset, datetime.datetime]):
        reference_id (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, KeyfactorApiModelsWorkflowsInstanceQueryResponseStatus] = UNSET
    current_step_id: Union[Unset, str] = UNSET
    status_message: Union[Unset, str] = UNSET
    definition: Union[Unset, KeyfactorApiModelsWorkflowsInstanceDefinitionResponse] = UNSET
    current_step_display_name: Union[Unset, str] = UNSET
    current_step_unique_name: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    reference_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        current_step_id = self.current_step_id
        status_message = self.status_message
        definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        current_step_display_name = self.current_step_display_name
        current_step_unique_name = self.current_step_unique_name
        title = self.title
        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()[:-6]+'Z'

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()[:-6]+'Z'

        reference_id = self.reference_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if status is not UNSET:
            field_dict["Status"] = status
        if current_step_id is not UNSET:
            field_dict["CurrentStepId"] = current_step_id
        if status_message is not UNSET:
            field_dict["StatusMessage"] = status_message
        if definition is not UNSET:
            field_dict["Definition"] = definition
        if current_step_display_name is not UNSET:
            field_dict["CurrentStepDisplayName"] = current_step_display_name
        if current_step_unique_name is not UNSET:
            field_dict["CurrentStepUniqueName"] = current_step_unique_name
        if title is not UNSET:
            field_dict["Title"] = title
        if last_modified is not UNSET:
            field_dict["LastModified"] = last_modified
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if reference_id is not UNSET:
            field_dict["ReferenceId"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, KeyfactorApiModelsWorkflowsInstanceQueryResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorApiModelsWorkflowsInstanceQueryResponseStatus(_status)

        current_step_id = d.pop("CurrentStepId", UNSET)

        status_message = d.pop("StatusMessage", UNSET)

        _definition = d.pop("Definition", UNSET)
        definition: Union[Unset, KeyfactorApiModelsWorkflowsInstanceDefinitionResponse]
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = KeyfactorApiModelsWorkflowsInstanceDefinitionResponse.from_dict(_definition)

        current_step_display_name = d.pop("CurrentStepDisplayName", UNSET)

        current_step_unique_name = d.pop("CurrentStepUniqueName", UNSET)

        title = d.pop("Title", UNSET)

        _last_modified = d.pop("LastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        _start_date = d.pop("StartDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        reference_id = d.pop("ReferenceId", UNSET)

        keyfactor_api_models_workflows_instance_query_response = cls(
            id=id,
            status=status,
            current_step_id=current_step_id,
            status_message=status_message,
            definition=definition,
            current_step_display_name=current_step_display_name,
            current_step_unique_name=current_step_unique_name,
            title=title,
            last_modified=last_modified,
            start_date=start_date,
            reference_id=reference_id,
        )

        keyfactor_api_models_workflows_instance_query_response.additional_properties = d
        return keyfactor_api_models_workflows_instance_query_response

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
