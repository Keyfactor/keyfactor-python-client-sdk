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

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsSignalConfigurationRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsSignalConfigurationRequest:
    """
    Attributes:
        signal_name (Union[Unset, str]): The name of the signal.
        role_ids (Union[Unset, List[int]]): The roles that are allowed to send the signal.
    """

    signal_name: Union[Unset, str] = UNSET
    role_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signal_name = self.signal_name
        role_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal_name is not UNSET:
            field_dict["SignalName"] = signal_name
        if role_ids is not UNSET:
            field_dict["RoleIds"] = role_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        signal_name = d.pop("SignalName", UNSET)

        role_ids = cast(List[int], d.pop("RoleIds", UNSET))

        keyfactor_api_models_workflows_signal_configuration_request = cls(
            signal_name=signal_name,
            role_ids=role_ids,
        )

        keyfactor_api_models_workflows_signal_configuration_request.additional_properties = d
        return keyfactor_api_models_workflows_signal_configuration_request

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
