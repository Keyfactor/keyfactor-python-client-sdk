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

T = TypeVar("T", bound="ModelsSSHKeysKeyGenerationRequest")


@attr.s(auto_attribs=True)
class ModelsSSHKeysKeyGenerationRequest:
    """
    Attributes:
        key_type (str):
        private_key_format (str):
        key_length (int):
        email (str):
        password (str):
        comment (Union[Unset, str]):
    """

    key_type: str
    private_key_format: str
    key_length: int
    email: str
    password: str
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_type = self.key_type
        private_key_format = self.private_key_format
        key_length = self.key_length
        email = self.email
        password = self.password
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "KeyType": key_type,
                "PrivateKeyFormat": private_key_format,
                "KeyLength": key_length,
                "Email": email,
                "Password": password,
            }
        )
        if comment is not UNSET:
            field_dict["Comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_type = d.pop("KeyType")

        private_key_format = d.pop("PrivateKeyFormat")

        key_length = d.pop("KeyLength")

        email = d.pop("Email")

        password = d.pop("Password")

        comment = d.pop("Comment", UNSET)

        models_ssh_keys_key_generation_request = cls(
            key_type=key_type,
            private_key_format=private_key_format,
            key_length=key_length,
            email=email,
            password=password,
            comment=comment,
        )

        models_ssh_keys_key_generation_request.additional_properties = d
        return models_ssh_keys_key_generation_request

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
