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

T = TypeVar("T", bound="ModelsSSHServersServerUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsSSHServersServerUpdateRequest:
    """
    Attributes:
        id (int):
        under_management (Union[Unset, bool]):
        port (Union[Unset, int]):
    """

    id: int
    under_management: Union[Unset, bool] = UNSET
    port: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        under_management = self.under_management
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
            }
        )
        if under_management is not UNSET:
            field_dict["UnderManagement"] = under_management
        if port is not UNSET:
            field_dict["Port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        under_management = d.pop("UnderManagement", UNSET)

        port = d.pop("Port", UNSET)

        models_ssh_servers_server_update_request = cls(
            id=id,
            under_management=under_management,
            port=port,
        )

        models_ssh_servers_server_update_request.additional_properties = d
        return models_ssh_servers_server_update_request

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
