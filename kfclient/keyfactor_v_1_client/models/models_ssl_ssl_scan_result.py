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

T = TypeVar("T", bound="ModelsSSLSslScanResult")


@attr.s(auto_attribs=True)
class ModelsSSLSslScanResult:
    """
    Attributes:
        endpoint_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        reverse_dns (Union[Unset, str]):
        sni_name (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        port (Union[Unset, int]):
        certificate_found (Union[Unset, bool]):
        agent_pool_name (Union[Unset, str]):
        network_name (Union[Unset, str]):
        monitor_status (Union[Unset, bool]):
        certificate_cn (Union[Unset, str]):
        reviewed (Union[Unset, bool]):
    """

    endpoint_id: Union[Unset, str] = UNSET
    reverse_dns: Union[Unset, str] = UNSET
    sni_name: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    certificate_found: Union[Unset, bool] = UNSET
    agent_pool_name: Union[Unset, str] = UNSET
    network_name: Union[Unset, str] = UNSET
    monitor_status: Union[Unset, bool] = UNSET
    certificate_cn: Union[Unset, str] = UNSET
    reviewed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint_id = self.endpoint_id
        reverse_dns = self.reverse_dns
        sni_name = self.sni_name
        ip_address = self.ip_address
        port = self.port
        certificate_found = self.certificate_found
        agent_pool_name = self.agent_pool_name
        network_name = self.network_name
        monitor_status = self.monitor_status
        certificate_cn = self.certificate_cn
        reviewed = self.reviewed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint_id is not UNSET:
            field_dict["EndpointId"] = endpoint_id
        if reverse_dns is not UNSET:
            field_dict["ReverseDNS"] = reverse_dns
        if sni_name is not UNSET:
            field_dict["SNIName"] = sni_name
        if ip_address is not UNSET:
            field_dict["IpAddress"] = ip_address
        if port is not UNSET:
            field_dict["Port"] = port
        if certificate_found is not UNSET:
            field_dict["CertificateFound"] = certificate_found
        if agent_pool_name is not UNSET:
            field_dict["AgentPoolName"] = agent_pool_name
        if network_name is not UNSET:
            field_dict["NetworkName"] = network_name
        if monitor_status is not UNSET:
            field_dict["MonitorStatus"] = monitor_status
        if certificate_cn is not UNSET:
            field_dict["CertificateCN"] = certificate_cn
        if reviewed is not UNSET:
            field_dict["Reviewed"] = reviewed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endpoint_id = d.pop("EndpointId", UNSET)

        reverse_dns = d.pop("ReverseDNS", UNSET)

        sni_name = d.pop("SNIName", UNSET)

        ip_address = d.pop("IpAddress", UNSET)

        port = d.pop("Port", UNSET)

        certificate_found = d.pop("CertificateFound", UNSET)

        agent_pool_name = d.pop("AgentPoolName", UNSET)

        network_name = d.pop("NetworkName", UNSET)

        monitor_status = d.pop("MonitorStatus", UNSET)

        certificate_cn = d.pop("CertificateCN", UNSET)

        reviewed = d.pop("Reviewed", UNSET)

        models_ssl_ssl_scan_result = cls(
            endpoint_id=endpoint_id,
            reverse_dns=reverse_dns,
            sni_name=sni_name,
            ip_address=ip_address,
            port=port,
            certificate_found=certificate_found,
            agent_pool_name=agent_pool_name,
            network_name=network_name,
            monitor_status=monitor_status,
            certificate_cn=certificate_cn,
            reviewed=reviewed,
        )

        models_ssl_ssl_scan_result.additional_properties = d
        return models_ssl_ssl_scan_result

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
