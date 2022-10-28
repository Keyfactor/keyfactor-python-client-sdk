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

T = TypeVar("T", bound="ModelsCustomReport")


@attr.s(auto_attribs=True)
class ModelsCustomReport:
    """The CustomReport can be used to create and update a custom report.

    Attributes:
        custom_url (Union[Unset, str]):
        id (Union[Unset, int]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        in_navigator (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    custom_url: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    in_navigator: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_url = self.custom_url
        id = self.id
        display_name = self.display_name
        description = self.description
        in_navigator = self.in_navigator
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_url is not UNSET:
            field_dict["CustomURL"] = custom_url
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if description is not UNSET:
            field_dict["Description"] = description
        if in_navigator is not UNSET:
            field_dict["InNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["Favorite"] = favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_url = d.pop("CustomURL", UNSET)

        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        description = d.pop("Description", UNSET)

        in_navigator = d.pop("InNavigator", UNSET)

        favorite = d.pop("Favorite", UNSET)

        models_custom_report = cls(
            custom_url=custom_url,
            id=id,
            display_name=display_name,
            description=description,
            in_navigator=in_navigator,
            favorite=favorite,
        )

        models_custom_report.additional_properties = d
        return models_custom_report

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
