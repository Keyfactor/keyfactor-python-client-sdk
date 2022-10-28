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

from ..models.models_report_parameters import ModelsReportParameters
from ..models.models_report_schedule import ModelsReportSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsReport")


@attr.s(auto_attribs=True)
class ModelsReport:
    """
    Attributes:
        id (Union[Unset, int]):
        scheduled (Union[Unset, int]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        report_path (Union[Unset, str]):
        version_number (Union[Unset, str]):
        categories (Union[Unset, str]):
        short_name (Union[Unset, str]):
        in_navigator (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
        remove_duplicates (Union[Unset, bool]):
        uses_collection (Union[Unset, bool]):
        report_parameter (Union[Unset, List[ModelsReportParameters]]):
        schedules (Union[Unset, List[ModelsReportSchedule]]):
        accepted_schedule_formats (Union[Unset, List[str]]):
    """

    id: Union[Unset, int] = UNSET
    scheduled: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    report_path: Union[Unset, str] = UNSET
    version_number: Union[Unset, str] = UNSET
    categories: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    in_navigator: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    remove_duplicates: Union[Unset, bool] = UNSET
    uses_collection: Union[Unset, bool] = UNSET
    report_parameter: Union[Unset, List[ModelsReportParameters]] = UNSET
    schedules: Union[Unset, List[ModelsReportSchedule]] = UNSET
    accepted_schedule_formats: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        scheduled = self.scheduled
        display_name = self.display_name
        description = self.description
        report_path = self.report_path
        version_number = self.version_number
        categories = self.categories
        short_name = self.short_name
        in_navigator = self.in_navigator
        favorite = self.favorite
        remove_duplicates = self.remove_duplicates
        uses_collection = self.uses_collection
        report_parameter: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_parameter, Unset):
            report_parameter = []
            for report_parameter_item_data in self.report_parameter:
                report_parameter_item = report_parameter_item_data.to_dict()

                report_parameter.append(report_parameter_item)

        schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()

                schedules.append(schedules_item)

        accepted_schedule_formats: Union[Unset, List[str]] = UNSET
        if not isinstance(self.accepted_schedule_formats, Unset):
            accepted_schedule_formats = self.accepted_schedule_formats

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if scheduled is not UNSET:
            field_dict["Scheduled"] = scheduled
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if description is not UNSET:
            field_dict["Description"] = description
        if report_path is not UNSET:
            field_dict["ReportPath"] = report_path
        if version_number is not UNSET:
            field_dict["VersionNumber"] = version_number
        if categories is not UNSET:
            field_dict["Categories"] = categories
        if short_name is not UNSET:
            field_dict["ShortName"] = short_name
        if in_navigator is not UNSET:
            field_dict["InNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["Favorite"] = favorite
        if remove_duplicates is not UNSET:
            field_dict["RemoveDuplicates"] = remove_duplicates
        if uses_collection is not UNSET:
            field_dict["UsesCollection"] = uses_collection
        if report_parameter is not UNSET:
            field_dict["ReportParameter"] = report_parameter
        if schedules is not UNSET:
            field_dict["Schedules"] = schedules
        if accepted_schedule_formats is not UNSET:
            field_dict["AcceptedScheduleFormats"] = accepted_schedule_formats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        scheduled = d.pop("Scheduled", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        description = d.pop("Description", UNSET)

        report_path = d.pop("ReportPath", UNSET)

        version_number = d.pop("VersionNumber", UNSET)

        categories = d.pop("Categories", UNSET)

        short_name = d.pop("ShortName", UNSET)

        in_navigator = d.pop("InNavigator", UNSET)

        favorite = d.pop("Favorite", UNSET)

        remove_duplicates = d.pop("RemoveDuplicates", UNSET)

        uses_collection = d.pop("UsesCollection", UNSET)

        report_parameter = []
        _report_parameter = d.pop("ReportParameter", UNSET)
        for report_parameter_item_data in _report_parameter or []:
            report_parameter_item = ModelsReportParameters.from_dict(report_parameter_item_data)

            report_parameter.append(report_parameter_item)

        schedules = []
        _schedules = d.pop("Schedules", UNSET)
        for schedules_item_data in _schedules or []:
            schedules_item = ModelsReportSchedule.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        accepted_schedule_formats = cast(List[str], d.pop("AcceptedScheduleFormats", UNSET))

        models_report = cls(
            id=id,
            scheduled=scheduled,
            display_name=display_name,
            description=description,
            report_path=report_path,
            version_number=version_number,
            categories=categories,
            short_name=short_name,
            in_navigator=in_navigator,
            favorite=favorite,
            remove_duplicates=remove_duplicates,
            uses_collection=uses_collection,
            report_parameter=report_parameter,
            schedules=schedules,
            accepted_schedule_formats=accepted_schedule_formats,
        )

        models_report.additional_properties = d
        return models_report

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
