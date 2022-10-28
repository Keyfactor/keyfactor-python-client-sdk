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

from ..models.keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_response_status import (
    KeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponse:
    """
    Attributes:
        failed_orchestrator_ids (Union[Unset, List[str]]):
        status (Union[Unset,
            KeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponseStatus]):
    """

    failed_orchestrator_ids: Union[Unset, List[str]] = UNSET
    status: Union[
        Unset, KeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponseStatus
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        failed_orchestrator_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.failed_orchestrator_ids, Unset):
            failed_orchestrator_ids = self.failed_orchestrator_ids

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failed_orchestrator_ids is not UNSET:
            field_dict["FailedOrchestratorIds"] = failed_orchestrator_ids
        if status is not UNSET:
            field_dict["Status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        failed_orchestrator_ids = cast(List[str], d.pop("FailedOrchestratorIds", UNSET))

        _status = d.pop("Status", UNSET)
        status: Union[Unset, KeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponseStatus(_status)

        keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_response = cls(
            failed_orchestrator_ids=failed_orchestrator_ids,
            status=status,
        )

        keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_response.additional_properties = (
            d
        )
        return keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_response

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
