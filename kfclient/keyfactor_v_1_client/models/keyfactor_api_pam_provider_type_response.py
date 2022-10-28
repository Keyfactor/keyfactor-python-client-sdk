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

from ..models.keyfactor_api_pam_provider_type_parameter_response import KeyfactorApiPAMProviderTypeParameterResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiPAMProviderTypeResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiPAMProviderTypeResponse:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        name (Union[Unset, str]):
        parameters (Union[Unset, List[KeyfactorApiPAMProviderTypeParameterResponse]]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[KeyfactorApiPAMProviderTypeParameterResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()

                parameters.append(parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        parameters = []
        _parameters = d.pop("Parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = KeyfactorApiPAMProviderTypeParameterResponse.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        keyfactor_api_pam_provider_type_response = cls(
            id=id,
            name=name,
            parameters=parameters,
        )

        keyfactor_api_pam_provider_type_response.additional_properties = d
        return keyfactor_api_pam_provider_type_response

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
