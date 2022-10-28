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

from ..models.models_invalid_keystore_reason import ModelsInvalidKeystoreReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsInvalidKeystore")


@attr.s(auto_attribs=True)
class ModelsInvalidKeystore:
    """
    Attributes:
        keystore_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        client_machine (Union[Unset, str]):
        store_path (Union[Unset, str]):
        alias (Union[Unset, str]):
        reason (Union[Unset, ModelsInvalidKeystoreReason]):
        explanation (Union[Unset, str]):
    """

    keystore_id: Union[Unset, str] = UNSET
    client_machine: Union[Unset, str] = UNSET
    store_path: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    reason: Union[Unset, ModelsInvalidKeystoreReason] = UNSET
    explanation: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keystore_id = self.keystore_id
        client_machine = self.client_machine
        store_path = self.store_path
        alias = self.alias
        reason: Union[Unset, int] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        explanation = self.explanation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keystore_id is not UNSET:
            field_dict["KeystoreId"] = keystore_id
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if store_path is not UNSET:
            field_dict["StorePath"] = store_path
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if reason is not UNSET:
            field_dict["Reason"] = reason
        if explanation is not UNSET:
            field_dict["Explanation"] = explanation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keystore_id = d.pop("KeystoreId", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        store_path = d.pop("StorePath", UNSET)

        alias = d.pop("Alias", UNSET)

        _reason = d.pop("Reason", UNSET)
        reason: Union[Unset, ModelsInvalidKeystoreReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ModelsInvalidKeystoreReason(_reason)

        explanation = d.pop("Explanation", UNSET)

        models_invalid_keystore = cls(
            keystore_id=keystore_id,
            client_machine=client_machine,
            store_path=store_path,
            alias=alias,
            reason=reason,
            explanation=explanation,
        )

        models_invalid_keystore.additional_properties = d
        return models_invalid_keystore

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
