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

T = TypeVar("T", bound="ModelsCustomReportCreationRequest")


@attr.s(auto_attribs=True)
class ModelsCustomReportCreationRequest:
    """The CustomReport can be used to create and update a custom report.

    Attributes:
        custom_url (str):
        display_name (str):
        description (str):
        in_navigator (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    custom_url: str
    display_name: str
    description: str
    in_navigator: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_url = self.custom_url
        display_name = self.display_name
        description = self.description
        in_navigator = self.in_navigator
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CustomURL": custom_url,
                "DisplayName": display_name,
                "Description": description,
            }
        )
        if in_navigator is not UNSET:
            field_dict["InNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["Favorite"] = favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_url = d.pop("CustomURL")

        display_name = d.pop("DisplayName")

        description = d.pop("Description")

        in_navigator = d.pop("InNavigator", UNSET)

        favorite = d.pop("Favorite", UNSET)

        models_custom_report_creation_request = cls(
            custom_url=custom_url,
            display_name=display_name,
            description=description,
            in_navigator=in_navigator,
            favorite=favorite,
        )

        models_custom_report_creation_request.additional_properties = d
        return models_custom_report_creation_request

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
