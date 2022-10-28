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

T = TypeVar("T", bound="KeyfactorApiModelsMacEnrollmentMacEnrollmentAPIModel")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMacEnrollmentMacEnrollmentAPIModel:
    """
    Attributes:
        id (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        interval (Union[Unset, int]):
        use_metadata (Union[Unset, bool]):
        metadata_field (Union[Unset, str]):
        metadata_value (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    interval: Union[Unset, int] = UNSET
    use_metadata: Union[Unset, bool] = UNSET
    metadata_field: Union[Unset, str] = UNSET
    metadata_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        enabled = self.enabled
        interval = self.interval
        use_metadata = self.use_metadata
        metadata_field = self.metadata_field
        metadata_value = self.metadata_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if interval is not UNSET:
            field_dict["Interval"] = interval
        if use_metadata is not UNSET:
            field_dict["UseMetadata"] = use_metadata
        if metadata_field is not UNSET:
            field_dict["MetadataField"] = metadata_field
        if metadata_value is not UNSET:
            field_dict["MetadataValue"] = metadata_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        enabled = d.pop("Enabled", UNSET)

        interval = d.pop("Interval", UNSET)

        use_metadata = d.pop("UseMetadata", UNSET)

        metadata_field = d.pop("MetadataField", UNSET)

        metadata_value = d.pop("MetadataValue", UNSET)

        keyfactor_api_models_mac_enrollment_mac_enrollment_api_model = cls(
            id=id,
            enabled=enabled,
            interval=interval,
            use_metadata=use_metadata,
            metadata_field=metadata_field,
            metadata_value=metadata_value,
        )

        keyfactor_api_models_mac_enrollment_mac_enrollment_api_model.additional_properties = d
        return keyfactor_api_models_mac_enrollment_mac_enrollment_api_model

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
