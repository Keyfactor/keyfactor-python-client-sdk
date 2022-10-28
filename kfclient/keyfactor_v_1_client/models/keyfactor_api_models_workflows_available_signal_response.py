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

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsAvailableSignalResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsAvailableSignalResponse:
    """
    Attributes:
        signal_name (Union[Unset, str]): The name of the signal.
        step_signal_id (Union[Unset, str]): The signal Id. Example: 00000000-0000-0000-0000-000000000000.
        signal_received (Union[Unset, bool]): Whether or not the signal has been received.
    """

    signal_name: Union[Unset, str] = UNSET
    step_signal_id: Union[Unset, str] = UNSET
    signal_received: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signal_name = self.signal_name
        step_signal_id = self.step_signal_id
        signal_received = self.signal_received

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal_name is not UNSET:
            field_dict["SignalName"] = signal_name
        if step_signal_id is not UNSET:
            field_dict["StepSignalId"] = step_signal_id
        if signal_received is not UNSET:
            field_dict["SignalReceived"] = signal_received

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        signal_name = d.pop("SignalName", UNSET)

        step_signal_id = d.pop("StepSignalId", UNSET)

        signal_received = d.pop("SignalReceived", UNSET)

        keyfactor_api_models_workflows_available_signal_response = cls(
            signal_name=signal_name,
            step_signal_id=step_signal_id,
            signal_received=signal_received,
        )

        keyfactor_api_models_workflows_available_signal_response.additional_properties = d
        return keyfactor_api_models_workflows_available_signal_response

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
