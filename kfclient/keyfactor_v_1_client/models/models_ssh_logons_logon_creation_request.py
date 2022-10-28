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

T = TypeVar("T", bound="ModelsSSHLogonsLogonCreationRequest")


@attr.s(auto_attribs=True)
class ModelsSSHLogonsLogonCreationRequest:
    """
    Attributes:
        username (str):
        server_id (int):
        user_ids (Union[Unset, List[int]]):
    """

    username: str
    server_id: int
    user_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        server_id = self.server_id
        user_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Username": username,
                "ServerId": server_id,
            }
        )
        if user_ids is not UNSET:
            field_dict["UserIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("Username")

        server_id = d.pop("ServerId")

        user_ids = cast(List[int], d.pop("UserIds", UNSET))

        models_ssh_logons_logon_creation_request = cls(
            username=username,
            server_id=server_id,
            user_ids=user_ids,
        )

        models_ssh_logons_logon_creation_request.additional_properties = d
        return models_ssh_logons_logon_creation_request

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
