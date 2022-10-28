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

T = TypeVar("T", bound="ModelsCertificateRetrievalResponseDetailedKeyUsageModel")


@attr.s(auto_attribs=True)
class ModelsCertificateRetrievalResponseDetailedKeyUsageModel:
    """
    Attributes:
        crl_sign (Union[Unset, bool]):
        data_encipherment (Union[Unset, bool]):
        decipher_only (Union[Unset, bool]):
        digital_signature (Union[Unset, bool]):
        encipher_only (Union[Unset, bool]):
        key_agreement (Union[Unset, bool]):
        key_cert_sign (Union[Unset, bool]):
        key_encipherment (Union[Unset, bool]):
        non_repudiation (Union[Unset, bool]):
        hex_code (Union[Unset, str]):
    """

    crl_sign: Union[Unset, bool] = UNSET
    data_encipherment: Union[Unset, bool] = UNSET
    decipher_only: Union[Unset, bool] = UNSET
    digital_signature: Union[Unset, bool] = UNSET
    encipher_only: Union[Unset, bool] = UNSET
    key_agreement: Union[Unset, bool] = UNSET
    key_cert_sign: Union[Unset, bool] = UNSET
    key_encipherment: Union[Unset, bool] = UNSET
    non_repudiation: Union[Unset, bool] = UNSET
    hex_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        crl_sign = self.crl_sign
        data_encipherment = self.data_encipherment
        decipher_only = self.decipher_only
        digital_signature = self.digital_signature
        encipher_only = self.encipher_only
        key_agreement = self.key_agreement
        key_cert_sign = self.key_cert_sign
        key_encipherment = self.key_encipherment
        non_repudiation = self.non_repudiation
        hex_code = self.hex_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crl_sign is not UNSET:
            field_dict["CrlSign"] = crl_sign
        if data_encipherment is not UNSET:
            field_dict["DataEncipherment"] = data_encipherment
        if decipher_only is not UNSET:
            field_dict["DecipherOnly"] = decipher_only
        if digital_signature is not UNSET:
            field_dict["DigitalSignature"] = digital_signature
        if encipher_only is not UNSET:
            field_dict["EncipherOnly"] = encipher_only
        if key_agreement is not UNSET:
            field_dict["KeyAgreement"] = key_agreement
        if key_cert_sign is not UNSET:
            field_dict["KeyCertSign"] = key_cert_sign
        if key_encipherment is not UNSET:
            field_dict["KeyEncipherment"] = key_encipherment
        if non_repudiation is not UNSET:
            field_dict["NonRepudiation"] = non_repudiation
        if hex_code is not UNSET:
            field_dict["HexCode"] = hex_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        crl_sign = d.pop("CrlSign", UNSET)

        data_encipherment = d.pop("DataEncipherment", UNSET)

        decipher_only = d.pop("DecipherOnly", UNSET)

        digital_signature = d.pop("DigitalSignature", UNSET)

        encipher_only = d.pop("EncipherOnly", UNSET)

        key_agreement = d.pop("KeyAgreement", UNSET)

        key_cert_sign = d.pop("KeyCertSign", UNSET)

        key_encipherment = d.pop("KeyEncipherment", UNSET)

        non_repudiation = d.pop("NonRepudiation", UNSET)

        hex_code = d.pop("HexCode", UNSET)

        models_certificate_retrieval_response_detailed_key_usage_model = cls(
            crl_sign=crl_sign,
            data_encipherment=data_encipherment,
            decipher_only=decipher_only,
            digital_signature=digital_signature,
            encipher_only=encipher_only,
            key_agreement=key_agreement,
            key_cert_sign=key_cert_sign,
            key_encipherment=key_encipherment,
            non_repudiation=non_repudiation,
            hex_code=hex_code,
        )

        models_certificate_retrieval_response_detailed_key_usage_model.additional_properties = d
        return models_certificate_retrieval_response_detailed_key_usage_model

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
