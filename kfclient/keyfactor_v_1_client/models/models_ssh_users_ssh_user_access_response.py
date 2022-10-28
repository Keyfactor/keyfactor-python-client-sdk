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

from ..models.models_ssh_keys_key_response import ModelsSSHKeysKeyResponse
from ..models.models_ssh_logons_logon_response import ModelsSSHLogonsLogonResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHUsersSshUserAccessResponse")


@attr.s(auto_attribs=True)
class ModelsSSHUsersSshUserAccessResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        key (Union[Unset, ModelsSSHKeysKeyResponse]):
        username (Union[Unset, str]):
        access (Union[Unset, List[ModelsSSHLogonsLogonResponse]]):
        is_group (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    key: Union[Unset, ModelsSSHKeysKeyResponse] = UNSET
    username: Union[Unset, str] = UNSET
    access: Union[Unset, List[ModelsSSHLogonsLogonResponse]] = UNSET
    is_group: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        username = self.username
        access: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access, Unset):
            access = []
            for access_item_data in self.access:
                access_item = access_item_data.to_dict()

                access.append(access_item)

        is_group = self.is_group

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if key is not UNSET:
            field_dict["Key"] = key
        if username is not UNSET:
            field_dict["Username"] = username
        if access is not UNSET:
            field_dict["Access"] = access
        if is_group is not UNSET:
            field_dict["IsGroup"] = is_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _key = d.pop("Key", UNSET)
        key: Union[Unset, ModelsSSHKeysKeyResponse]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = ModelsSSHKeysKeyResponse.from_dict(_key)

        username = d.pop("Username", UNSET)

        access = []
        _access = d.pop("Access", UNSET)
        for access_item_data in _access or []:
            access_item = ModelsSSHLogonsLogonResponse.from_dict(access_item_data)

            access.append(access_item)

        is_group = d.pop("IsGroup", UNSET)

        models_ssh_users_ssh_user_access_response = cls(
            id=id,
            key=key,
            username=username,
            access=access,
            is_group=is_group,
        )

        models_ssh_users_ssh_user_access_response.additional_properties = d
        return models_ssh_users_ssh_user_access_response

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
