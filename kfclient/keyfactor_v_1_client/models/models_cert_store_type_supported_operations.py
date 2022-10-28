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

T = TypeVar("T", bound="ModelsCertStoreTypeSupportedOperations")


@attr.s(auto_attribs=True)
class ModelsCertStoreTypeSupportedOperations:
    """
    Attributes:
        add (Union[Unset, bool]):
        create (Union[Unset, bool]):
        discovery (Union[Unset, bool]):
        enrollment (Union[Unset, bool]):
        remove (Union[Unset, bool]):
    """

    add: Union[Unset, bool] = UNSET
    create: Union[Unset, bool] = UNSET
    discovery: Union[Unset, bool] = UNSET
    enrollment: Union[Unset, bool] = UNSET
    remove: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add = self.add
        create = self.create
        discovery = self.discovery
        enrollment = self.enrollment
        remove = self.remove

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add is not UNSET:
            field_dict["Add"] = add
        if create is not UNSET:
            field_dict["Create"] = create
        if discovery is not UNSET:
            field_dict["Discovery"] = discovery
        if enrollment is not UNSET:
            field_dict["Enrollment"] = enrollment
        if remove is not UNSET:
            field_dict["Remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        add = d.pop("Add", UNSET)

        create = d.pop("Create", UNSET)

        discovery = d.pop("Discovery", UNSET)

        enrollment = d.pop("Enrollment", UNSET)

        remove = d.pop("Remove", UNSET)

        models_cert_store_type_supported_operations = cls(
            add=add,
            create=create,
            discovery=discovery,
            enrollment=enrollment,
            remove=remove,
        )

        models_cert_store_type_supported_operations.additional_properties = d
        return models_cert_store_type_supported_operations

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
