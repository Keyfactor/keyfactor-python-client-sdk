# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHLogonsLogonQueryResponse")


@attr.s(auto_attribs=True)
class ModelsSSHLogonsLogonQueryResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        username (Union[Unset, str]):
        last_logon (Union[Unset, datetime.datetime]):
        server_id (Union[Unset, int]):
        server_name (Union[Unset, str]):
        group_name (Union[Unset, str]):
        key_count (Union[Unset, int]):
        server_under_management (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    last_logon: Union[Unset, datetime.datetime] = UNSET
    server_id: Union[Unset, int] = UNSET
    server_name: Union[Unset, str] = UNSET
    group_name: Union[Unset, str] = UNSET
    key_count: Union[Unset, int] = UNSET
    server_under_management: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        last_logon: Union[Unset, str] = UNSET
        if not isinstance(self.last_logon, Unset):
            last_logon = self.last_logon.isoformat()[:-6]+'Z'

        server_id = self.server_id
        server_name = self.server_name
        group_name = self.group_name
        key_count = self.key_count
        server_under_management = self.server_under_management

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if username is not UNSET:
            field_dict["Username"] = username
        if last_logon is not UNSET:
            field_dict["LastLogon"] = last_logon
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if group_name is not UNSET:
            field_dict["GroupName"] = group_name
        if key_count is not UNSET:
            field_dict["KeyCount"] = key_count
        if server_under_management is not UNSET:
            field_dict["ServerUnderManagement"] = server_under_management

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        username = d.pop("Username", UNSET)

        _last_logon = d.pop("LastLogon", UNSET)
        last_logon: Union[Unset, datetime.datetime]
        if isinstance(_last_logon, Unset):
            last_logon = UNSET
        else:
            last_logon = isoparse(_last_logon)

        server_id = d.pop("ServerId", UNSET)

        server_name = d.pop("ServerName", UNSET)

        group_name = d.pop("GroupName", UNSET)

        key_count = d.pop("KeyCount", UNSET)

        server_under_management = d.pop("ServerUnderManagement", UNSET)

        models_ssh_logons_logon_query_response = cls(
            id=id,
            username=username,
            last_logon=last_logon,
            server_id=server_id,
            server_name=server_name,
            group_name=group_name,
            key_count=key_count,
            server_under_management=server_under_management,
        )

        models_ssh_logons_logon_query_response.additional_properties = d
        return models_ssh_logons_logon_query_response

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
