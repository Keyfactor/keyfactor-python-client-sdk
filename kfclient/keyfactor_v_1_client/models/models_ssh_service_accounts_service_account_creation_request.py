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

from ..models.models_ssh_keys_key_generation_request import ModelsSSHKeysKeyGenerationRequest
from ..models.models_ssh_service_accounts_service_account_user_creation_request import (
    ModelsSSHServiceAccountsServiceAccountUserCreationRequest,
)

T = TypeVar("T", bound="ModelsSSHServiceAccountsServiceAccountCreationRequest")


@attr.s(auto_attribs=True)
class ModelsSSHServiceAccountsServiceAccountCreationRequest:
    """
    Attributes:
        key_generation_request (ModelsSSHKeysKeyGenerationRequest):
        user (ModelsSSHServiceAccountsServiceAccountUserCreationRequest):
        client_hostname (str):
        server_group_id (str):  Example: 00000000-0000-0000-0000-000000000000.
    """

    key_generation_request: ModelsSSHKeysKeyGenerationRequest
    user: ModelsSSHServiceAccountsServiceAccountUserCreationRequest
    client_hostname: str
    server_group_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_generation_request = self.key_generation_request.to_dict()

        user = self.user.to_dict()

        client_hostname = self.client_hostname
        server_group_id = self.server_group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "KeyGenerationRequest": key_generation_request,
                "User": user,
                "ClientHostname": client_hostname,
                "ServerGroupId": server_group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_generation_request = ModelsSSHKeysKeyGenerationRequest.from_dict(d.pop("KeyGenerationRequest"))

        user = ModelsSSHServiceAccountsServiceAccountUserCreationRequest.from_dict(d.pop("User"))

        client_hostname = d.pop("ClientHostname")

        server_group_id = d.pop("ServerGroupId")

        models_ssh_service_accounts_service_account_creation_request = cls(
            key_generation_request=key_generation_request,
            user=user,
            client_hostname=client_hostname,
            server_group_id=server_group_id,
        )

        models_ssh_service_accounts_service_account_creation_request.additional_properties = d
        return models_ssh_service_accounts_service_account_creation_request

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
