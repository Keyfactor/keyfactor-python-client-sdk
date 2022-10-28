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

from ..models.models_workflow_processed_certificate_request import ModelsWorkflowProcessedCertificateRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsWorkflowApproveDenyResult")


@attr.s(auto_attribs=True)
class ModelsWorkflowApproveDenyResult:
    """
    Attributes:
        failures (Union[Unset, List[ModelsWorkflowProcessedCertificateRequest]]):
        denials (Union[Unset, List[ModelsWorkflowProcessedCertificateRequest]]):
        successes (Union[Unset, List[ModelsWorkflowProcessedCertificateRequest]]):
    """

    failures: Union[Unset, List[ModelsWorkflowProcessedCertificateRequest]] = UNSET
    denials: Union[Unset, List[ModelsWorkflowProcessedCertificateRequest]] = UNSET
    successes: Union[Unset, List[ModelsWorkflowProcessedCertificateRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        failures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.failures, Unset):
            failures = []
            for failures_item_data in self.failures:
                failures_item = failures_item_data.to_dict()

                failures.append(failures_item)

        denials: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.denials, Unset):
            denials = []
            for denials_item_data in self.denials:
                denials_item = denials_item_data.to_dict()

                denials.append(denials_item)

        successes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.successes, Unset):
            successes = []
            for successes_item_data in self.successes:
                successes_item = successes_item_data.to_dict()

                successes.append(successes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failures is not UNSET:
            field_dict["Failures"] = failures
        if denials is not UNSET:
            field_dict["Denials"] = denials
        if successes is not UNSET:
            field_dict["Successes"] = successes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        failures = []
        _failures = d.pop("Failures", UNSET)
        for failures_item_data in _failures or []:
            failures_item = ModelsWorkflowProcessedCertificateRequest.from_dict(failures_item_data)

            failures.append(failures_item)

        denials = []
        _denials = d.pop("Denials", UNSET)
        for denials_item_data in _denials or []:
            denials_item = ModelsWorkflowProcessedCertificateRequest.from_dict(denials_item_data)

            denials.append(denials_item)

        successes = []
        _successes = d.pop("Successes", UNSET)
        for successes_item_data in _successes or []:
            successes_item = ModelsWorkflowProcessedCertificateRequest.from_dict(successes_item_data)

            successes.append(successes_item)

        models_workflow_approve_deny_result = cls(
            failures=failures,
            denials=denials,
            successes=successes,
        )

        models_workflow_approve_deny_result.additional_properties = d
        return models_workflow_approve_deny_result

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
