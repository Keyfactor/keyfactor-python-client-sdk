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

from ..models.keyfactor_api_models_workflows_available_signal_response import (
    KeyfactorApiModelsWorkflowsAvailableSignalResponse,
)
from ..models.keyfactor_api_models_workflows_instance_definition_response import (
    KeyfactorApiModelsWorkflowsInstanceDefinitionResponse,
)
from ..models.keyfactor_api_models_workflows_instance_response_current_state_data import (
    KeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData,
)
from ..models.keyfactor_api_models_workflows_instance_response_initial_data import (
    KeyfactorApiModelsWorkflowsInstanceResponseInitialData,
)
from ..models.keyfactor_api_models_workflows_instance_response_status import (
    KeyfactorApiModelsWorkflowsInstanceResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsInstanceResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsInstanceResponse:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        status (Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseStatus]):
        current_step_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        status_message (Union[Unset, str]):
        signals (Union[Unset, List[KeyfactorApiModelsWorkflowsAvailableSignalResponse]]):
        definition (Union[Unset, KeyfactorApiModelsWorkflowsInstanceDefinitionResponse]):
        current_step_display_name (Union[Unset, str]):
        current_step_unique_name (Union[Unset, str]):
        title (Union[Unset, str]):
        last_modified (Union[Unset, datetime.datetime]):
        start_date (Union[Unset, datetime.datetime]):
        initial_data (Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseInitialData]):
        current_state_data (Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData]):
        reference_id (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseStatus] = UNSET
    current_step_id: Union[Unset, str] = UNSET
    status_message: Union[Unset, str] = UNSET
    signals: Union[Unset, List[KeyfactorApiModelsWorkflowsAvailableSignalResponse]] = UNSET
    definition: Union[Unset, KeyfactorApiModelsWorkflowsInstanceDefinitionResponse] = UNSET
    current_step_display_name: Union[Unset, str] = UNSET
    current_step_unique_name: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    initial_data: Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseInitialData] = UNSET
    current_state_data: Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData] = UNSET
    reference_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        current_step_id = self.current_step_id
        status_message = self.status_message
        signals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signals, Unset):
            signals = []
            for signals_item_data in self.signals:
                signals_item = signals_item_data.to_dict()

                signals.append(signals_item)

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

        initial_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initial_data, Unset):
            initial_data = self.initial_data.to_dict()

        current_state_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_state_data, Unset):
            current_state_data = self.current_state_data.to_dict()

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
        if signals is not UNSET:
            field_dict["Signals"] = signals
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
        if initial_data is not UNSET:
            field_dict["InitialData"] = initial_data
        if current_state_data is not UNSET:
            field_dict["CurrentStateData"] = current_state_data
        if reference_id is not UNSET:
            field_dict["ReferenceId"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorApiModelsWorkflowsInstanceResponseStatus(_status)

        current_step_id = d.pop("CurrentStepId", UNSET)

        status_message = d.pop("StatusMessage", UNSET)

        signals = []
        _signals = d.pop("Signals", UNSET)
        for signals_item_data in _signals or []:
            signals_item = KeyfactorApiModelsWorkflowsAvailableSignalResponse.from_dict(signals_item_data)

            signals.append(signals_item)

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

        _initial_data = d.pop("InitialData", UNSET)
        initial_data: Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseInitialData]
        if isinstance(_initial_data, Unset):
            initial_data = UNSET
        else:
            initial_data = KeyfactorApiModelsWorkflowsInstanceResponseInitialData.from_dict(_initial_data)

        _current_state_data = d.pop("CurrentStateData", UNSET)
        current_state_data: Union[Unset, KeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData]
        if isinstance(_current_state_data, Unset):
            current_state_data = UNSET
        else:
            current_state_data = KeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData.from_dict(
                _current_state_data
            )

        reference_id = d.pop("ReferenceId", UNSET)

        keyfactor_api_models_workflows_instance_response = cls(
            id=id,
            status=status,
            current_step_id=current_step_id,
            status_message=status_message,
            signals=signals,
            definition=definition,
            current_step_display_name=current_step_display_name,
            current_step_unique_name=current_step_unique_name,
            title=title,
            last_modified=last_modified,
            start_date=start_date,
            initial_data=initial_data,
            current_state_data=current_state_data,
            reference_id=reference_id,
        )

        keyfactor_api_models_workflows_instance_response.additional_properties = d
        return keyfactor_api_models_workflows_instance_response

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
