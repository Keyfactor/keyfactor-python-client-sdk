# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.models_revocation_suspended_revocation_response import ModelsRevocationSuspendedRevocationResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsRevocationRevocationResponse")


@attr.s(auto_attribs=True)
class ModelsRevocationRevocationResponse:
    """
    Attributes:
        revoked_ids (Union[Unset, List[int]]):
        suspended_certs (Union[Unset, List[ModelsRevocationSuspendedRevocationResponse]]):
    """

    revoked_ids: Union[Unset, List[int]] = UNSET
    suspended_certs: Union[Unset, List[ModelsRevocationSuspendedRevocationResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        revoked_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.revoked_ids, Unset):
            revoked_ids = self.revoked_ids

        suspended_certs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suspended_certs, Unset):
            suspended_certs = []
            for suspended_certs_item_data in self.suspended_certs:
                suspended_certs_item = suspended_certs_item_data.to_dict()

                suspended_certs.append(suspended_certs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revoked_ids is not UNSET:
            field_dict["RevokedIds"] = revoked_ids
        if suspended_certs is not UNSET:
            field_dict["SuspendedCerts"] = suspended_certs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        revoked_ids = cast(List[int], d.pop("RevokedIds", UNSET))

        suspended_certs = []
        _suspended_certs = d.pop("SuspendedCerts", UNSET)
        for suspended_certs_item_data in _suspended_certs or []:
            suspended_certs_item = ModelsRevocationSuspendedRevocationResponse.from_dict(suspended_certs_item_data)

            suspended_certs.append(suspended_certs_item)

        models_revocation_revocation_response = cls(
            revoked_ids=revoked_ids,
            suspended_certs=suspended_certs,
        )

        models_revocation_revocation_response.additional_properties = d
        return models_revocation_revocation_response

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
