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

from ..models.models_certificate_query_duplication_field import ModelsCertificateQueryDuplicationField
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateQuery")


@attr.s(auto_attribs=True)
class ModelsCertificateQuery:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        automated (Union[Unset, bool]):
        content (Union[Unset, str]):
        duplication_field (Union[Unset, ModelsCertificateQueryDuplicationField]):
        show_on_dashboard (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    automated: Union[Unset, bool] = UNSET
    content: Union[Unset, str] = UNSET
    duplication_field: Union[Unset, ModelsCertificateQueryDuplicationField] = UNSET
    show_on_dashboard: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        automated = self.automated
        content = self.content
        duplication_field: Union[Unset, int] = UNSET
        if not isinstance(self.duplication_field, Unset):
            duplication_field = self.duplication_field.value

        show_on_dashboard = self.show_on_dashboard
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if automated is not UNSET:
            field_dict["Automated"] = automated
        if content is not UNSET:
            field_dict["Content"] = content
        if duplication_field is not UNSET:
            field_dict["DuplicationField"] = duplication_field
        if show_on_dashboard is not UNSET:
            field_dict["ShowOnDashboard"] = show_on_dashboard
        if favorite is not UNSET:
            field_dict["Favorite"] = favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        automated = d.pop("Automated", UNSET)

        content = d.pop("Content", UNSET)

        _duplication_field = d.pop("DuplicationField", UNSET)
        duplication_field: Union[Unset, ModelsCertificateQueryDuplicationField]
        if isinstance(_duplication_field, Unset):
            duplication_field = UNSET
        else:
            duplication_field = ModelsCertificateQueryDuplicationField(_duplication_field)

        show_on_dashboard = d.pop("ShowOnDashboard", UNSET)

        favorite = d.pop("Favorite", UNSET)

        models_certificate_query = cls(
            id=id,
            name=name,
            description=description,
            automated=automated,
            content=content,
            duplication_field=duplication_field,
            show_on_dashboard=show_on_dashboard,
            favorite=favorite,
        )

        models_certificate_query.additional_properties = d
        return models_certificate_query

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
