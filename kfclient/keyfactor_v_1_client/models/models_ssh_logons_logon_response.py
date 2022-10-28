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

from ..models.models_ssh_servers_server_response import ModelsSSHServersServerResponse
from ..models.models_ssh_users_ssh_user_response import ModelsSSHUsersSshUserResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHLogonsLogonResponse")


@attr.s(auto_attribs=True)
class ModelsSSHLogonsLogonResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        username (Union[Unset, str]):
        last_logon (Union[Unset, datetime.datetime]):
        server (Union[Unset, ModelsSSHServersServerResponse]):
        key_count (Union[Unset, int]):
        access (Union[Unset, List[ModelsSSHUsersSshUserResponse]]):
    """

    id: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    last_logon: Union[Unset, datetime.datetime] = UNSET
    server: Union[Unset, ModelsSSHServersServerResponse] = UNSET
    key_count: Union[Unset, int] = UNSET
    access: Union[Unset, List[ModelsSSHUsersSshUserResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        last_logon: Union[Unset, str] = UNSET
        if not isinstance(self.last_logon, Unset):
            last_logon = self.last_logon.isoformat()[:-6]+'Z'

        server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        key_count = self.key_count
        access: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access, Unset):
            access = []
            for access_item_data in self.access:
                access_item = access_item_data.to_dict()

                access.append(access_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if username is not UNSET:
            field_dict["Username"] = username
        if last_logon is not UNSET:
            field_dict["LastLogon"] = last_logon
        if server is not UNSET:
            field_dict["Server"] = server
        if key_count is not UNSET:
            field_dict["KeyCount"] = key_count
        if access is not UNSET:
            field_dict["Access"] = access

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

        _server = d.pop("Server", UNSET)
        server: Union[Unset, ModelsSSHServersServerResponse]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = ModelsSSHServersServerResponse.from_dict(_server)

        key_count = d.pop("KeyCount", UNSET)

        access = []
        _access = d.pop("Access", UNSET)
        for access_item_data in _access or []:
            access_item = ModelsSSHUsersSshUserResponse.from_dict(access_item_data)

            access.append(access_item)

        models_ssh_logons_logon_response = cls(
            id=id,
            username=username,
            last_logon=last_logon,
            server=server,
            key_count=key_count,
            access=access,
        )

        models_ssh_logons_logon_response.additional_properties = d
        return models_ssh_logons_logon_response

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
