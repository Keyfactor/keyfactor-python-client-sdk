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

from ..models.keyfactor_api_models_monitoring_dashboard_request import KeyfactorApiModelsMonitoringDashboardRequest
from ..models.keyfactor_api_models_monitoring_email_request import KeyfactorApiModelsMonitoringEmailRequest
from ..models.keyfactor_api_models_monitoring_ocsp_parameters_request import (
    KeyfactorApiModelsMonitoringOCSPParametersRequest,
)
from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMonitoringRevocationMonitoringCreationRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMonitoringRevocationMonitoringCreationRequest:
    """
    Attributes:
        name (str):
        endpoint_type (str):
        location (str):
        dashboard (KeyfactorApiModelsMonitoringDashboardRequest):
        email (Union[Unset, KeyfactorApiModelsMonitoringEmailRequest]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        ocsp_parameters (Union[Unset, KeyfactorApiModelsMonitoringOCSPParametersRequest]):  Example:
            {'CertificateContents': '<Certificate Content>', 'CertificateAuthorityId': 1}.
    """

    name: str
    endpoint_type: str
    location: str
    dashboard: KeyfactorApiModelsMonitoringDashboardRequest
    email: Union[Unset, KeyfactorApiModelsMonitoringEmailRequest] = UNSET
    schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    ocsp_parameters: Union[Unset, KeyfactorApiModelsMonitoringOCSPParametersRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        endpoint_type = self.endpoint_type
        location = self.location
        dashboard = self.dashboard.to_dict()

        email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        ocsp_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ocsp_parameters, Unset):
            ocsp_parameters = self.ocsp_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
                "EndpointType": endpoint_type,
                "Location": location,
                "Dashboard": dashboard,
            }
        )
        if email is not UNSET:
            field_dict["Email"] = email
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule
        if ocsp_parameters is not UNSET:
            field_dict["OCSPParameters"] = ocsp_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        endpoint_type = d.pop("EndpointType")

        location = d.pop("Location")

        dashboard = KeyfactorApiModelsMonitoringDashboardRequest.from_dict(d.pop("Dashboard"))

        _email = d.pop("Email", UNSET)
        email: Union[Unset, KeyfactorApiModelsMonitoringEmailRequest]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = KeyfactorApiModelsMonitoringEmailRequest.from_dict(_email)

        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        _ocsp_parameters = d.pop("OCSPParameters", UNSET)
        ocsp_parameters: Union[Unset, KeyfactorApiModelsMonitoringOCSPParametersRequest]
        if isinstance(_ocsp_parameters, Unset):
            ocsp_parameters = UNSET
        else:
            ocsp_parameters = KeyfactorApiModelsMonitoringOCSPParametersRequest.from_dict(_ocsp_parameters)

        keyfactor_api_models_monitoring_revocation_monitoring_creation_request = cls(
            name=name,
            endpoint_type=endpoint_type,
            location=location,
            dashboard=dashboard,
            email=email,
            schedule=schedule,
            ocsp_parameters=ocsp_parameters,
        )

        keyfactor_api_models_monitoring_revocation_monitoring_creation_request.additional_properties = d
        return keyfactor_api_models_monitoring_revocation_monitoring_creation_request

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
