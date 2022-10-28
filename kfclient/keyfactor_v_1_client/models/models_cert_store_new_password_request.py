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

from ..models.models_cert_store_new_password_request_new_password import ModelsCertStoreNewPasswordRequestNewPassword

T = TypeVar("T", bound="ModelsCertStoreNewPasswordRequest")


@attr.s(auto_attribs=True)
class ModelsCertStoreNewPasswordRequest:
    """NewPassword must be provided and be of type string or KeyfactorAPISecret.

    Example:
        {'CertStoreId': '00000000-0000-0000-0000-000000000000', 'NewPassword': {'SecretValue': '<string password>',
            'Parameters': {'<optional PAM parameters key>': '<optional PAM parameters value'}, 'Provider': 0}}

    Attributes:
        cert_store_id (str):  Example: 00000000-0000-0000-0000-000000000000.
        new_password (ModelsCertStoreNewPasswordRequestNewPassword):
    """

    cert_store_id: str
    new_password: ModelsCertStoreNewPasswordRequestNewPassword
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert_store_id = self.cert_store_id
        new_password = self.new_password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CertStoreId": cert_store_id,
                "NewPassword": new_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert_store_id = d.pop("CertStoreId")

        new_password = ModelsCertStoreNewPasswordRequestNewPassword.from_dict(d.pop("NewPassword"))

        models_cert_store_new_password_request = cls(
            cert_store_id=cert_store_id,
            new_password=new_password,
        )

        models_cert_store_new_password_request.additional_properties = d
        return models_cert_store_new_password_request

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
