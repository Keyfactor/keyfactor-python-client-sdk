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

T = TypeVar("T", bound="ModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel")


@attr.s(auto_attribs=True)
class ModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel:
    """
    Attributes:
        store_path (Union[Unset, str]):
        agent_pool (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        port (Union[Unset, int]):
        network_name (Union[Unset, str]):
    """

    store_path: Union[Unset, str] = UNSET
    agent_pool: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    network_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        store_path = self.store_path
        agent_pool = self.agent_pool
        ip_address = self.ip_address
        port = self.port
        network_name = self.network_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_path is not UNSET:
            field_dict["StorePath"] = store_path
        if agent_pool is not UNSET:
            field_dict["AgentPool"] = agent_pool
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
        store_path = d.pop("StorePath", UNSET)

        agent_pool = d.pop("AgentPool", UNSET)

        ip_address = d.pop("IPAddress", UNSET)

        port = d.pop("Port", UNSET)

        network_name = d.pop("NetworkName", UNSET)

        models_certificate_retrieval_response_certificate_store_location_detail_model = cls(
            store_path=store_path,
            agent_pool=agent_pool,
            ip_address=ip_address,
            port=port,
            network_name=network_name,
        )

        models_certificate_retrieval_response_certificate_store_location_detail_model.additional_properties = d
        return models_certificate_retrieval_response_certificate_store_location_detail_model

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
