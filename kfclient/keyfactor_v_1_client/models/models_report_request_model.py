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

T = TypeVar("T", bound="ModelsReportRequestModel")


@attr.s(auto_attribs=True)
class ModelsReportRequestModel:
    """The ReportRequestModel can be used to update a report.

    Attributes:
        id (Union[Unset, int]):
        in_navigator (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
        remove_duplicates (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    in_navigator: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    remove_duplicates: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        in_navigator = self.in_navigator
        favorite = self.favorite
        remove_duplicates = self.remove_duplicates

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if in_navigator is not UNSET:
            field_dict["InNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["Favorite"] = favorite
        if remove_duplicates is not UNSET:
            field_dict["RemoveDuplicates"] = remove_duplicates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        in_navigator = d.pop("InNavigator", UNSET)

        favorite = d.pop("Favorite", UNSET)

        remove_duplicates = d.pop("RemoveDuplicates", UNSET)

        models_report_request_model = cls(
            id=id,
            in_navigator=in_navigator,
            favorite=favorite,
            remove_duplicates=remove_duplicates,
        )

        models_report_request_model.additional_properties = d
        return models_report_request_model

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
