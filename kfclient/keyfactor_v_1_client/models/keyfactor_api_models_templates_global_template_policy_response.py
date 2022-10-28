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

T = TypeVar("T", bound="KeyfactorApiModelsTemplatesGlobalTemplatePolicyResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsTemplatesGlobalTemplatePolicyResponse:
    """
    Attributes:
        rsa_valid_key_sizes (Union[Unset, List[int]]): The allowed RSA key sizes.
        ecc_valid_curves (Union[Unset, List[str]]): The allowed ECC curves.
        allow_key_reuse (Union[Unset, bool]): Whether or not keys can be reused.
        allow_wildcards (Union[Unset, bool]): Whether or not wildcards can be used.
        rfc_enforcement (Union[Unset, bool]): Whether or not RFC 2818 compliance should be enforced.
    """

    rsa_valid_key_sizes: Union[Unset, List[int]] = UNSET
    ecc_valid_curves: Union[Unset, List[str]] = UNSET
    allow_key_reuse: Union[Unset, bool] = UNSET
    allow_wildcards: Union[Unset, bool] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        rsa_valid_key_sizes = cast(List[int], d.pop("RSAValidKeySizes", UNSET))

        ecc_valid_curves = cast(List[str], d.pop("ECCValidCurves", UNSET))

        allow_key_reuse = d.pop("AllowKeyReuse", UNSET)

        allow_wildcards = d.pop("AllowWildcards", UNSET)

        rfc_enforcement = d.pop("RFCEnforcement", UNSET)

        keyfactor_api_models_templates_global_template_policy_response = cls(
            rsa_valid_key_sizes=rsa_valid_key_sizes,
            ecc_valid_curves=ecc_valid_curves,
            allow_key_reuse=allow_key_reuse,
            allow_wildcards=allow_wildcards,
            rfc_enforcement=rfc_enforcement,
        )

        keyfactor_api_models_templates_global_template_policy_response.additional_properties = d
        return keyfactor_api_models_templates_global_template_policy_response

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
