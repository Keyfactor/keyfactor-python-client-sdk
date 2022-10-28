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

T = TypeVar("T", bound="ModelsSecurityIdentitiesSecurityIdentityIdentifier")


@attr.s(auto_attribs=True)
class ModelsSecurityIdentitiesSecurityIdentityIdentifier:
    """Model for looking up a security identity

    Attributes:
        account_name (Union[Unset, str]): The username of the security identity.
        sid (Union[Unset, str]): The SID of the security identity.
    """

    account_name: Union[Unset, str] = UNSET
    sid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_name = self.account_name
        sid = self.sid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_name is not UNSET:
            field_dict["AccountName"] = account_name
        if sid is not UNSET:
            field_dict["SID"] = sid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_name = d.pop("AccountName", UNSET)

        sid = d.pop("SID", UNSET)

        models_security_identities_security_identity_identifier = cls(
            account_name=account_name,
            sid=sid,
        )

        models_security_identities_security_identity_identifier.additional_properties = d
        return models_security_identities_security_identity_identifier

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
