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

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMonitoringDashboardResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMonitoringDashboardResponse:
    """
    Attributes:
        show (Union[Unset, bool]):
        warning_hours (Union[Unset, int]):
    """

    show: Union[Unset, bool] = UNSET
    warning_hours: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        show = self.show
        warning_hours = self.warning_hours

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if show is not UNSET:
            field_dict["Show"] = show
        if warning_hours is not UNSET:
            field_dict["WarningHours"] = warning_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        show = d.pop("Show", UNSET)

        warning_hours = d.pop("WarningHours", UNSET)

        keyfactor_api_models_monitoring_dashboard_response = cls(
            show=show,
            warning_hours=warning_hours,
        )

        keyfactor_api_models_monitoring_dashboard_response.additional_properties = d
        return keyfactor_api_models_monitoring_dashboard_response

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
