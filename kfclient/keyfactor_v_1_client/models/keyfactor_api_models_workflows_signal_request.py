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

from ..models.keyfactor_api_models_workflows_signal_request_data import KeyfactorApiModelsWorkflowsSignalRequestData
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsSignalRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsSignalRequest:
    """
    Example:
        {'SignalKey': '<STEP_NAME.SIGNAL_NAME>', 'Data': {'Signal': 'Data'}}

    Attributes:
        signal_key (Union[Unset, str]): The signal key. This is expected to be in a format like "STEP_NAME.SIGNAL_NAME"
        data (Union[Unset, KeyfactorApiModelsWorkflowsSignalRequestData]): Arbitrary data to associate with the signal.
    """

    signal_key: Union[Unset, str] = UNSET
    data: Union[Unset, KeyfactorApiModelsWorkflowsSignalRequestData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signal_key = self.signal_key
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal_key is not UNSET:
            field_dict["SignalKey"] = signal_key
        if data is not UNSET:
            field_dict["Data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        signal_key = d.pop("SignalKey", UNSET)

        _data = d.pop("Data", UNSET)
        data: Union[Unset, KeyfactorApiModelsWorkflowsSignalRequestData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = KeyfactorApiModelsWorkflowsSignalRequestData.from_dict(_data)

        keyfactor_api_models_workflows_signal_request = cls(
            signal_key=signal_key,
            data=data,
        )

        keyfactor_api_models_workflows_signal_request.additional_properties = d
        return keyfactor_api_models_workflows_signal_request

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
