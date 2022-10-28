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
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHKeysKeyResponse")


@attr.s(auto_attribs=True)
class ModelsSSHKeysKeyResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        fingerprint (Union[Unset, str]):
        public_key (Union[Unset, str]):
        private_key (Union[Unset, str]):
        key_type (Union[Unset, str]):
        key_length (Union[Unset, int]):
        creation_date (Union[Unset, datetime.datetime]):
        stale_date (Union[Unset, datetime.datetime]):
        email (Union[Unset, str]):
        comments (Union[Unset, List[str]]):
        logon_count (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    key_type: Union[Unset, str] = UNSET
    key_length: Union[Unset, int] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    stale_date: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    comments: Union[Unset, List[str]] = UNSET
    logon_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        fingerprint = self.fingerprint
        public_key = self.public_key
        private_key = self.private_key
        key_type = self.key_type
        key_length = self.key_length
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()[:-6]+'Z'

        stale_date: Union[Unset, str] = UNSET
        if not isinstance(self.stale_date, Unset):
            stale_date = self.stale_date.isoformat()[:-6]+'Z'

        email = self.email
        comments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments

        logon_count = self.logon_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if fingerprint is not UNSET:
            field_dict["Fingerprint"] = fingerprint
        if public_key is not UNSET:
            field_dict["PublicKey"] = public_key
        if private_key is not UNSET:
            field_dict["PrivateKey"] = private_key
        if key_type is not UNSET:
            field_dict["KeyType"] = key_type
        if key_length is not UNSET:
            field_dict["KeyLength"] = key_length
        if creation_date is not UNSET:
            field_dict["CreationDate"] = creation_date
        if stale_date is not UNSET:
            field_dict["StaleDate"] = stale_date
        if email is not UNSET:
            field_dict["Email"] = email
        if comments is not UNSET:
            field_dict["Comments"] = comments
        if logon_count is not UNSET:
            field_dict["LogonCount"] = logon_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        fingerprint = d.pop("Fingerprint", UNSET)

        public_key = d.pop("PublicKey", UNSET)

        private_key = d.pop("PrivateKey", UNSET)

        key_type = d.pop("KeyType", UNSET)

        key_length = d.pop("KeyLength", UNSET)

        _creation_date = d.pop("CreationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _stale_date = d.pop("StaleDate", UNSET)
        stale_date: Union[Unset, datetime.datetime]
        if isinstance(_stale_date, Unset):
            stale_date = UNSET
        else:
            stale_date = isoparse(_stale_date)

        email = d.pop("Email", UNSET)

        comments = cast(List[str], d.pop("Comments", UNSET))

        logon_count = d.pop("LogonCount", UNSET)

        models_ssh_keys_key_response = cls(
            id=id,
            fingerprint=fingerprint,
            public_key=public_key,
            private_key=private_key,
            key_type=key_type,
            key_length=key_length,
            creation_date=creation_date,
            stale_date=stale_date,
            email=email,
            comments=comments,
            logon_count=logon_count,
        )

        models_ssh_keys_key_response.additional_properties = d
        return models_ssh_keys_key_response

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
