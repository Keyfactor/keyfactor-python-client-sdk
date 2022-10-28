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

from ..models.models_metadata_single_update_request import ModelsMetadataSingleUpdateRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsMetadataAllUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsMetadataAllUpdateRequest:
    """
    Attributes:
        metadata (List[ModelsMetadataSingleUpdateRequest]):
        query (Union[Unset, str]):
        certificate_ids (Union[Unset, List[int]]):
    """

    metadata: List[ModelsMetadataSingleUpdateRequest]
    query: Union[Unset, str] = UNSET
    certificate_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata = []
        for metadata_item_data in self.metadata:
            metadata_item = metadata_item_data.to_dict()

            metadata.append(metadata_item)

        query = self.query
        certificate_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.certificate_ids, Unset):
            certificate_ids = self.certificate_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Metadata": metadata,
            }
        )
        if query is not UNSET:
            field_dict["Query"] = query
        if certificate_ids is not UNSET:
            field_dict["CertificateIds"] = certificate_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metadata = []
        _metadata = d.pop("Metadata")
        for metadata_item_data in _metadata:
            metadata_item = ModelsMetadataSingleUpdateRequest.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        query = d.pop("Query", UNSET)

        certificate_ids = cast(List[int], d.pop("CertificateIds", UNSET))

        models_metadata_all_update_request = cls(
            metadata=metadata,
            query=query,
            certificate_ids=certificate_ids,
        )

        models_metadata_all_update_request.additional_properties = d
        return models_metadata_all_update_request

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
