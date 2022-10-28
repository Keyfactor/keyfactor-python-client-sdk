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

T = TypeVar("T", bound="ModelsSSLEndpoint")


@attr.s(auto_attribs=True)
class ModelsSSLEndpoint:
    """
    Attributes:
        endpoint_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        network_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        last_history_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        ip_address_bytes (Union[Unset, str]):
        port (Union[Unset, int]):
        sni_name (Union[Unset, str]):
        enable_monitor (Union[Unset, bool]):
        reviewed (Union[Unset, bool]):
    """

    endpoint_id: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    last_history_id: Union[Unset, str] = UNSET
    ip_address_bytes: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    sni_name: Union[Unset, str] = UNSET
    enable_monitor: Union[Unset, bool] = UNSET
    reviewed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint_id = self.endpoint_id
        network_id = self.network_id
        last_history_id = self.last_history_id
        ip_address_bytes = self.ip_address_bytes
        port = self.port
        sni_name = self.sni_name
        enable_monitor = self.enable_monitor
        reviewed = self.reviewed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint_id is not UNSET:
            field_dict["EndpointId"] = endpoint_id
        if network_id is not UNSET:
            field_dict["NetworkId"] = network_id
        if last_history_id is not UNSET:
            field_dict["LastHistoryId"] = last_history_id
        if ip_address_bytes is not UNSET:
            field_dict["IpAddressBytes"] = ip_address_bytes
        if port is not UNSET:
            field_dict["Port"] = port
        if sni_name is not UNSET:
            field_dict["SNIName"] = sni_name
        if enable_monitor is not UNSET:
            field_dict["EnableMonitor"] = enable_monitor
        if reviewed is not UNSET:
            field_dict["Reviewed"] = reviewed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endpoint_id = d.pop("EndpointId", UNSET)

        network_id = d.pop("NetworkId", UNSET)

        last_history_id = d.pop("LastHistoryId", UNSET)

        ip_address_bytes = d.pop("IpAddressBytes", UNSET)

        port = d.pop("Port", UNSET)

        sni_name = d.pop("SNIName", UNSET)

        enable_monitor = d.pop("EnableMonitor", UNSET)

        reviewed = d.pop("Reviewed", UNSET)

        models_ssl_endpoint = cls(
            endpoint_id=endpoint_id,
            network_id=network_id,
            last_history_id=last_history_id,
            ip_address_bytes=ip_address_bytes,
            port=port,
            sni_name=sni_name,
            enable_monitor=enable_monitor,
            reviewed=reviewed,
        )

        models_ssl_endpoint.additional_properties = d
        return models_ssl_endpoint

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
