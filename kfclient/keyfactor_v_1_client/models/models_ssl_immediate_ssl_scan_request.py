# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelsSSLImmediateSslScanRequest")


@attr.s(auto_attribs=True)
class ModelsSSLImmediateSslScanRequest:
    """
    Attributes:
        discovery (bool):
        monitoring (bool):
    """

    discovery: bool
    monitoring: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        discovery = self.discovery
        monitoring = self.monitoring

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Discovery": discovery,
                "Monitoring": monitoring,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        discovery = d.pop("Discovery")

        monitoring = d.pop("Monitoring")

        models_ssl_immediate_ssl_scan_request = cls(
            discovery=discovery,
            monitoring=monitoring,
        )

        models_ssl_immediate_ssl_scan_request.additional_properties = d
        return models_ssl_immediate_ssl_scan_request

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
