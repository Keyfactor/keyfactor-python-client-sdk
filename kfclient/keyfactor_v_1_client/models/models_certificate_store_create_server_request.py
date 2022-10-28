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

from ..models.models_keyfactor_api_secret import ModelsKeyfactorAPISecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStoreCreateServerRequest")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreCreateServerRequest:
    """
    Attributes:
        username (ModelsKeyfactorAPISecret):
        password (ModelsKeyfactorAPISecret):
        use_ssl (bool):
        server_type (int):
        name (str):
        container (Union[Unset, int]):
    """

    username: ModelsKeyfactorAPISecret
    password: ModelsKeyfactorAPISecret
    use_ssl: bool
    server_type: int
    name: str
    container: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username.to_dict()

        password = self.password.to_dict()

        use_ssl = self.use_ssl
        server_type = self.server_type
        name = self.name
        container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Username": username,
                "Password": password,
                "UseSSL": use_ssl,
                "ServerType": server_type,
                "Name": name,
            }
        )
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = ModelsKeyfactorAPISecret.from_dict(d.pop("Username"))

        password = ModelsKeyfactorAPISecret.from_dict(d.pop("Password"))

        use_ssl = d.pop("UseSSL")

        server_type = d.pop("ServerType")

        name = d.pop("Name")

        container = d.pop("Container", UNSET)

        models_certificate_store_create_server_request = cls(
            username=username,
            password=password,
            use_ssl=use_ssl,
            server_type=server_type,
            name=name,
            container=container,
        )

        models_certificate_store_create_server_request.additional_properties = d
        return models_certificate_store_create_server_request

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
