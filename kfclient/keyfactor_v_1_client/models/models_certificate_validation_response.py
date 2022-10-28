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

from ..models.models_certificate_validation_response_results import ModelsCertificateValidationResponseResults
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateValidationResponse")


@attr.s(auto_attribs=True)
class ModelsCertificateValidationResponse:
    """
    Attributes:
        valid (Union[Unset, bool]): States whether the certificate is valid or not
        results (Union[Unset, ModelsCertificateValidationResponseResults]): Lists any reasons why the certificate is not
            valid
    """

    valid: Union[Unset, bool] = UNSET
    results: Union[Unset, ModelsCertificateValidationResponseResults] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        valid = self.valid
        results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid is not UNSET:
            field_dict["Valid"] = valid
        if results is not UNSET:
            field_dict["Results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        valid = d.pop("Valid", UNSET)

        _results = d.pop("Results", UNSET)
        results: Union[Unset, ModelsCertificateValidationResponseResults]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = ModelsCertificateValidationResponseResults.from_dict(_results)

        models_certificate_validation_response = cls(
            valid=valid,
            results=results,
        )

        models_certificate_validation_response.additional_properties = d
        return models_certificate_validation_response

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
