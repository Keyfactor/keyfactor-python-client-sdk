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

from ..models.models_keyfactor_api_secret_parameters import ModelsKeyfactorAPISecretParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsKeyfactorAPISecret")


@attr.s(auto_attribs=True)
class ModelsKeyfactorAPISecret:
    """
    Attributes:
        secret_value (Union[Unset, str]):
        parameters (Union[Unset, ModelsKeyfactorAPISecretParameters]):
        provider (Union[Unset, int]):
    """

    secret_value: Union[Unset, str] = UNSET
    parameters: Union[Unset, ModelsKeyfactorAPISecretParameters] = UNSET
    provider: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secret_value = self.secret_value
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        provider = self.provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret_value is not UNSET:
            field_dict["SecretValue"] = secret_value
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters
        if provider is not UNSET:
            field_dict["Provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        secret_value = d.pop("SecretValue", UNSET)

        _parameters = d.pop("Parameters", UNSET)
        parameters: Union[Unset, ModelsKeyfactorAPISecretParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ModelsKeyfactorAPISecretParameters.from_dict(_parameters)

        provider = d.pop("Provider", UNSET)

        models_keyfactor_api_secret = cls(
            secret_value=secret_value,
            parameters=parameters,
            provider=provider,
        )

        models_keyfactor_api_secret.additional_properties = d
        return models_keyfactor_api_secret

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
