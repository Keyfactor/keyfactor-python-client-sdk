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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTemplateUpdateRequestTemplatePolicyModel")


@attr.s(auto_attribs=True)
class ModelsTemplateUpdateRequestTemplatePolicyModel:
    """
    Attributes:
        template_id (Union[Unset, int]):
        rsa_valid_key_sizes (Union[Unset, List[int]]):
        ecc_valid_curves (Union[Unset, List[str]]):
        allow_key_reuse (Union[Unset, bool]):
        allow_wildcards (Union[Unset, bool]):
        rfc_enforcement (Union[Unset, bool]):
    """

    template_id: Union[Unset, int] = UNSET
    rsa_valid_key_sizes: Union[Unset, List[int]] = UNSET
    ecc_valid_curves: Union[Unset, List[str]] = UNSET
    allow_key_reuse: Union[Unset, bool] = UNSET
    allow_wildcards: Union[Unset, bool] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_id = self.template_id
        rsa_valid_key_sizes: Union[Unset, List[int]] = UNSET
        if not isinstance(self.rsa_valid_key_sizes, Unset):
            rsa_valid_key_sizes = self.rsa_valid_key_sizes

        ecc_valid_curves: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ecc_valid_curves, Unset):
            ecc_valid_curves = self.ecc_valid_curves

        allow_key_reuse = self.allow_key_reuse
        allow_wildcards = self.allow_wildcards
        rfc_enforcement = self.rfc_enforcement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["TemplateId"] = template_id
        if rsa_valid_key_sizes is not UNSET:
            field_dict["RSAValidKeySizes"] = rsa_valid_key_sizes
        if ecc_valid_curves is not UNSET:
            field_dict["ECCValidCurves"] = ecc_valid_curves
        if allow_key_reuse is not UNSET:
            field_dict["AllowKeyReuse"] = allow_key_reuse
        if allow_wildcards is not UNSET:
            field_dict["AllowWildcards"] = allow_wildcards
        if rfc_enforcement is not UNSET:
            field_dict["RFCEnforcement"] = rfc_enforcement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template_id = d.pop("TemplateId", UNSET)

        rsa_valid_key_sizes = cast(List[int], d.pop("RSAValidKeySizes", UNSET))

        ecc_valid_curves = cast(List[str], d.pop("ECCValidCurves", UNSET))

        allow_key_reuse = d.pop("AllowKeyReuse", UNSET)

        allow_wildcards = d.pop("AllowWildcards", UNSET)

        rfc_enforcement = d.pop("RFCEnforcement", UNSET)

        models_template_update_request_template_policy_model = cls(
            template_id=template_id,
            rsa_valid_key_sizes=rsa_valid_key_sizes,
            ecc_valid_curves=ecc_valid_curves,
            allow_key_reuse=allow_key_reuse,
            allow_wildcards=allow_wildcards,
            rfc_enforcement=rfc_enforcement,
        )

        models_template_update_request_template_policy_model.additional_properties = d
        return models_template_update_request_template_policy_model

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
