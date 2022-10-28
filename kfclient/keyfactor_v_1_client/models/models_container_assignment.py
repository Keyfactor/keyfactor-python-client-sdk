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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsContainerAssignment")


@attr.s(auto_attribs=True)
class ModelsContainerAssignment:
    """
    Attributes:
        keystore_ids (List[str]):
        cert_store_container_id (Union[Unset, int]):
        new_container_name (Union[Unset, str]):
        new_container_type (Union[Unset, int]):
    """

    keystore_ids: List[str]
    cert_store_container_id: Union[Unset, int] = UNSET
    new_container_name: Union[Unset, str] = UNSET
    new_container_type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keystore_ids = self.keystore_ids

        cert_store_container_id = self.cert_store_container_id
        new_container_name = self.new_container_name
        new_container_type = self.new_container_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "KeystoreIds": keystore_ids,
            }
        )
        if cert_store_container_id is not UNSET:
            field_dict["CertStoreContainerId"] = cert_store_container_id
        if new_container_name is not UNSET:
            field_dict["NewContainerName"] = new_container_name
        if new_container_type is not UNSET:
            field_dict["NewContainerType"] = new_container_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keystore_ids = cast(List[str], d.pop("KeystoreIds"))

        cert_store_container_id = d.pop("CertStoreContainerId", UNSET)

        new_container_name = d.pop("NewContainerName", UNSET)

        new_container_type = d.pop("NewContainerType", UNSET)

        models_container_assignment = cls(
            keystore_ids=keystore_ids,
            cert_store_container_id=cert_store_container_id,
            new_container_name=new_container_name,
            new_container_type=new_container_type,
        )

        models_container_assignment.additional_properties = d
        return models_container_assignment

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
