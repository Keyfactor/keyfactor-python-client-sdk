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

T = TypeVar("T", bound="ModelsCertStoreLocationsCertificateStoreLocationsDetail")


@attr.s(auto_attribs=True)
class ModelsCertStoreLocationsCertificateStoreLocationsDetail:
    """
    Attributes:
        store_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        store_type_id (Union[Unset, int]):
        client_machine (Union[Unset, str]):
        store_path (Union[Unset, str]):
        agent_pool (Union[Unset, str]):
        alias (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        port (Union[Unset, int]):
        network_name (Union[Unset, str]):
    """

    store_id: Union[Unset, str] = UNSET
    store_type_id: Union[Unset, int] = UNSET
    client_machine: Union[Unset, str] = UNSET
    store_path: Union[Unset, str] = UNSET
    agent_pool: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    network_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        store_id = self.store_id
        store_type_id = self.store_type_id
        client_machine = self.client_machine
        store_path = self.store_path
        agent_pool = self.agent_pool
        alias = self.alias
        ip_address = self.ip_address
        port = self.port
        network_name = self.network_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_id is not UNSET:
            field_dict["StoreId"] = store_id
        if store_type_id is not UNSET:
            field_dict["StoreTypeId"] = store_type_id
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if store_path is not UNSET:
            field_dict["StorePath"] = store_path
        if agent_pool is not UNSET:
            field_dict["AgentPool"] = agent_pool
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if ip_address is not UNSET:
            field_dict["IPAddress"] = ip_address
        if port is not UNSET:
            field_dict["Port"] = port
        if network_name is not UNSET:
            field_dict["NetworkName"] = network_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        store_id = d.pop("StoreId", UNSET)

        store_type_id = d.pop("StoreTypeId", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        store_path = d.pop("StorePath", UNSET)

        agent_pool = d.pop("AgentPool", UNSET)

        alias = d.pop("Alias", UNSET)

        ip_address = d.pop("IPAddress", UNSET)

        port = d.pop("Port", UNSET)

        network_name = d.pop("NetworkName", UNSET)

        models_cert_store_locations_certificate_store_locations_detail = cls(
            store_id=store_id,
            store_type_id=store_type_id,
            client_machine=client_machine,
            store_path=store_path,
            agent_pool=agent_pool,
            alias=alias,
            ip_address=ip_address,
            port=port,
            network_name=network_name,
        )

        models_cert_store_locations_certificate_store_locations_detail.additional_properties = d
        return models_cert_store_locations_certificate_store_locations_detail

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
