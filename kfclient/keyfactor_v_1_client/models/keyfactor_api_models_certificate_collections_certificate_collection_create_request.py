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

from ..models.keyfactor_api_models_certificate_collections_certificate_collection_create_request_duplication_field import (
    KeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequestDuplicationField,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequest:
    """
    Attributes:
        name (str):
        copy_from_id (Union[Unset, int]):
        id (Union[Unset, int]):
        description (Union[Unset, str]):
        query (Union[Unset, str]):
        duplication_field (Union[Unset,
            KeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequestDuplicationField]):
        show_on_dashboard (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    name: str
    copy_from_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    duplication_field: Union[
        Unset, KeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequestDuplicationField
    ] = UNSET
    show_on_dashboard: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        copy_from_id = self.copy_from_id
        id = self.id
        description = self.description
        query = self.query
        duplication_field: Union[Unset, int] = UNSET
        if not isinstance(self.duplication_field, Unset):
            duplication_field = self.duplication_field.value

        show_on_dashboard = self.show_on_dashboard
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
            }
        )
        if copy_from_id is not UNSET:
            field_dict["CopyFromId"] = copy_from_id
        if id is not UNSET:
            field_dict["Id"] = id
        if description is not UNSET:
            field_dict["Description"] = description
        if query is not UNSET:
            field_dict["Query"] = query
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
        name = d.pop("Name")

        copy_from_id = d.pop("CopyFromId", UNSET)

        id = d.pop("Id", UNSET)

        description = d.pop("Description", UNSET)

        query = d.pop("Query", UNSET)

        _duplication_field = d.pop("DuplicationField", UNSET)
        duplication_field: Union[
            Unset, KeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequestDuplicationField
        ]
        if isinstance(_duplication_field, Unset):
            duplication_field = UNSET
        else:
            duplication_field = (
                KeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequestDuplicationField(
                    _duplication_field
                )
            )

        show_on_dashboard = d.pop("ShowOnDashboard", UNSET)

        favorite = d.pop("Favorite", UNSET)

        keyfactor_api_models_certificate_collections_certificate_collection_create_request = cls(
            name=name,
            copy_from_id=copy_from_id,
            id=id,
            description=description,
            query=query,
            duplication_field=duplication_field,
            show_on_dashboard=show_on_dashboard,
            favorite=favorite,
        )

        keyfactor_api_models_certificate_collections_certificate_collection_create_request.additional_properties = d
        return keyfactor_api_models_certificate_collections_certificate_collection_create_request

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
