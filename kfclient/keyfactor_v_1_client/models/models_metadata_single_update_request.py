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

T = TypeVar("T", bound="ModelsMetadataSingleUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsMetadataSingleUpdateRequest:
    """
    Attributes:
        metadata_name (Union[Unset, str]):
        value (Union[Unset, str]):
        overwrite_existing (Union[Unset, bool]):
    """

    metadata_name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    overwrite_existing: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata_name = self.metadata_name
        value = self.value
        overwrite_existing = self.overwrite_existing

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata_name is not UNSET:
            field_dict["MetadataName"] = metadata_name
        if value is not UNSET:
            field_dict["Value"] = value
        if overwrite_existing is not UNSET:
            field_dict["OverwriteExisting"] = overwrite_existing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metadata_name = d.pop("MetadataName", UNSET)

        value = d.pop("Value", UNSET)

        overwrite_existing = d.pop("OverwriteExisting", UNSET)

        models_metadata_single_update_request = cls(
            metadata_name=metadata_name,
            value=value,
            overwrite_existing=overwrite_existing,
        )

        models_metadata_single_update_request.additional_properties = d
        return models_metadata_single_update_request

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
