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

T = TypeVar("T", bound="ModelsWorkflowCertificateRequestCertStoreModel")


@attr.s(auto_attribs=True)
class ModelsWorkflowCertificateRequestCertStoreModel:
    """
    Attributes:
        entry_name (Union[Unset, str]):
        client_machine (Union[Unset, str]):
        store_path (Union[Unset, str]):
    """

    entry_name: Union[Unset, str] = UNSET
    client_machine: Union[Unset, str] = UNSET
    store_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_name = self.entry_name
        client_machine = self.client_machine
        store_path = self.store_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_name is not UNSET:
            field_dict["EntryName"] = entry_name
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if store_path is not UNSET:
            field_dict["StorePath"] = store_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry_name = d.pop("EntryName", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        store_path = d.pop("StorePath", UNSET)

        models_workflow_certificate_request_cert_store_model = cls(
            entry_name=entry_name,
            client_machine=client_machine,
            store_path=store_path,
        )

        models_workflow_certificate_request_cert_store_model.additional_properties = d
        return models_workflow_certificate_request_cert_store_model

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
