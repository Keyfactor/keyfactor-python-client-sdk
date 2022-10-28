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

from ..models.models_cert_store_type_password_options_style import ModelsCertStoreTypePasswordOptionsStyle
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertStoreTypePasswordOptions")


@attr.s(auto_attribs=True)
class ModelsCertStoreTypePasswordOptions:
    """
    Attributes:
        entry_supported (Union[Unset, bool]):
        store_required (Union[Unset, bool]):
        style (Union[Unset, ModelsCertStoreTypePasswordOptionsStyle]):
    """

    entry_supported: Union[Unset, bool] = UNSET
    store_required: Union[Unset, bool] = UNSET
    style: Union[Unset, ModelsCertStoreTypePasswordOptionsStyle] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_supported = self.entry_supported
        store_required = self.store_required
        style: Union[Unset, int] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_supported is not UNSET:
            field_dict["EntrySupported"] = entry_supported
        if store_required is not UNSET:
            field_dict["StoreRequired"] = store_required
        if style is not UNSET:
            field_dict["Style"] = style

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry_supported = d.pop("EntrySupported", UNSET)

        store_required = d.pop("StoreRequired", UNSET)

        _style = d.pop("Style", UNSET)
        style: Union[Unset, ModelsCertStoreTypePasswordOptionsStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ModelsCertStoreTypePasswordOptionsStyle(_style)

        models_cert_store_type_password_options = cls(
            entry_supported=entry_supported,
            store_required=store_required,
            style=style,
        )

        models_cert_store_type_password_options.additional_properties = d
        return models_cert_store_type_password_options

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
