# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="KeyfactorApiModelsTemplatesGlobalTemplatePolicyRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsTemplatesGlobalTemplatePolicyRequest:
    """
    Attributes:
        rsa_valid_key_sizes (List[int]): The allowed RSA key sizes.
        ecc_valid_curves (List[str]): The allowed ECC curves.
        allow_key_reuse (bool): Whether or not keys can be reused.
        allow_wildcards (bool): Whether or not wildcards can be used.
        rfc_enforcement (bool): Whether or not RFC 2818 compliance should be enforced.
    """

    rsa_valid_key_sizes: List[int]
    ecc_valid_curves: List[str]
    allow_key_reuse: bool
    allow_wildcards: bool
    rfc_enforcement: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rsa_valid_key_sizes = self.rsa_valid_key_sizes

        ecc_valid_curves = self.ecc_valid_curves

        allow_key_reuse = self.allow_key_reuse
        allow_wildcards = self.allow_wildcards
        rfc_enforcement = self.rfc_enforcement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "RSAValidKeySizes": rsa_valid_key_sizes,
                "ECCValidCurves": ecc_valid_curves,
                "AllowKeyReuse": allow_key_reuse,
                "AllowWildcards": allow_wildcards,
                "RFCEnforcement": rfc_enforcement,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rsa_valid_key_sizes = cast(List[int], d.pop("RSAValidKeySizes"))

        ecc_valid_curves = cast(List[str], d.pop("ECCValidCurves"))

        allow_key_reuse = d.pop("AllowKeyReuse")

        allow_wildcards = d.pop("AllowWildcards")

        rfc_enforcement = d.pop("RFCEnforcement")

        keyfactor_api_models_templates_global_template_policy_request = cls(
            rsa_valid_key_sizes=rsa_valid_key_sizes,
            ecc_valid_curves=ecc_valid_curves,
            allow_key_reuse=allow_key_reuse,
            allow_wildcards=allow_wildcards,
            rfc_enforcement=rfc_enforcement,
        )

        keyfactor_api_models_templates_global_template_policy_request.additional_properties = d
        return keyfactor_api_models_templates_global_template_policy_request

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
