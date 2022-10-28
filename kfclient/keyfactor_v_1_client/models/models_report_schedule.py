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

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..models.models_report_schedule_runtime_parameters import ModelsReportScheduleRuntimeParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsReportSchedule")


@attr.s(auto_attribs=True)
class ModelsReportSchedule:
    """
    Attributes:
        id (Union[Unset, int]):
        send_report (Union[Unset, bool]):
        save_report (Union[Unset, bool]):
        save_report_path (Union[Unset, str]):
        report_format (Union[Unset, str]):
        keyfactor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        certificate_collection_id (Union[Unset, int]):
        email_recipients (Union[Unset, List[str]]):
        runtime_parameters (Union[Unset, ModelsReportScheduleRuntimeParameters]):
    """

    id: Union[Unset, int] = UNSET
    send_report: Union[Unset, bool] = UNSET
    save_report: Union[Unset, bool] = UNSET
    save_report_path: Union[Unset, str] = UNSET
    report_format: Union[Unset, str] = UNSET
    keyfactor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    certificate_collection_id: Union[Unset, int] = UNSET
    email_recipients: Union[Unset, List[str]] = UNSET
    runtime_parameters: Union[Unset, ModelsReportScheduleRuntimeParameters] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        send_report = self.send_report
        save_report = self.save_report
        save_report_path = self.save_report_path
        report_format = self.report_format
        keyfactor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keyfactor_schedule, Unset):
            keyfactor_schedule = self.keyfactor_schedule.to_dict()

        certificate_collection_id = self.certificate_collection_id
        email_recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.email_recipients, Unset):
            email_recipients = self.email_recipients

        runtime_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.runtime_parameters, Unset):
            runtime_parameters = self.runtime_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if send_report is not UNSET:
            field_dict["SendReport"] = send_report
        if save_report is not UNSET:
            field_dict["SaveReport"] = save_report
        if save_report_path is not UNSET:
            field_dict["SaveReportPath"] = save_report_path
        if report_format is not UNSET:
            field_dict["ReportFormat"] = report_format
        if keyfactor_schedule is not UNSET:
            field_dict["KeyfactorSchedule"] = keyfactor_schedule
        if certificate_collection_id is not UNSET:
            field_dict["CertificateCollectionId"] = certificate_collection_id
        if email_recipients is not UNSET:
            field_dict["EmailRecipients"] = email_recipients
        if runtime_parameters is not UNSET:
            field_dict["RuntimeParameters"] = runtime_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        send_report = d.pop("SendReport", UNSET)

        save_report = d.pop("SaveReport", UNSET)

        save_report_path = d.pop("SaveReportPath", UNSET)

        report_format = d.pop("ReportFormat", UNSET)

        _keyfactor_schedule = d.pop("KeyfactorSchedule", UNSET)
        keyfactor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_keyfactor_schedule, Unset):
            keyfactor_schedule = UNSET
        else:
            keyfactor_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_keyfactor_schedule)

        certificate_collection_id = d.pop("CertificateCollectionId", UNSET)

        email_recipients = cast(List[str], d.pop("EmailRecipients", UNSET))

        _runtime_parameters = d.pop("RuntimeParameters", UNSET)
        runtime_parameters: Union[Unset, ModelsReportScheduleRuntimeParameters]
        if isinstance(_runtime_parameters, Unset):
            runtime_parameters = UNSET
        else:
            runtime_parameters = ModelsReportScheduleRuntimeParameters.from_dict(_runtime_parameters)

        models_report_schedule = cls(
            id=id,
            send_report=send_report,
            save_report=save_report,
            save_report_path=save_report_path,
            report_format=report_format,
            keyfactor_schedule=keyfactor_schedule,
            certificate_collection_id=certificate_collection_id,
            email_recipients=email_recipients,
            runtime_parameters=runtime_parameters,
        )

        models_report_schedule.additional_properties = d
        return models_report_schedule

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
