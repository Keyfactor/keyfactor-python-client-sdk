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

T = TypeVar("T", bound="KeyfactorApiModelsSecurityRolesAreaPermissionResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsSecurityRolesAreaPermissionResponse:
    """
    Attributes:
        type (Union[Unset, str]):
        area (Union[Unset, str]):
        permission (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    area: Union[Unset, str] = UNSET
    permission: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        area = self.area
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if area is not UNSET:
            field_dict["Area"] = area
        if permission is not UNSET:
            field_dict["Permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type", UNSET)

        area = d.pop("Area", UNSET)

        permission = d.pop("Permission", UNSET)

        keyfactor_api_models_security_roles_area_permission_response = cls(
            type=type,
            area=area,
            permission=permission,
        )

        keyfactor_api_models_security_roles_area_permission_response.additional_properties = d
        return keyfactor_api_models_security_roles_area_permission_response

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
