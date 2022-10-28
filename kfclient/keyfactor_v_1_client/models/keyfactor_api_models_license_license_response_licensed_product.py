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

from ..models.keyfactor_api_models_license_license_response_licensed_feature import (
    KeyfactorApiModelsLicenseLicenseResponseLicensedFeature,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsLicenseLicenseResponseLicensedProduct")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsLicenseLicenseResponseLicensedProduct:
    """
    Attributes:
        product_id (Union[Unset, str]):
        display_name (Union[Unset, str]):
        major_rev (Union[Unset, str]):
        minor_rev (Union[Unset, str]):
        licensed_features (Union[Unset, List[KeyfactorApiModelsLicenseLicenseResponseLicensedFeature]]):
    """

    product_id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    major_rev: Union[Unset, str] = UNSET
    minor_rev: Union[Unset, str] = UNSET
    licensed_features: Union[Unset, List[KeyfactorApiModelsLicenseLicenseResponseLicensedFeature]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id
        display_name = self.display_name
        major_rev = self.major_rev
        minor_rev = self.minor_rev
        licensed_features: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licensed_features, Unset):
            licensed_features = []
            for licensed_features_item_data in self.licensed_features:
                licensed_features_item = licensed_features_item_data.to_dict()

                licensed_features.append(licensed_features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["ProductId"] = product_id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if major_rev is not UNSET:
            field_dict["MajorRev"] = major_rev
        if minor_rev is not UNSET:
            field_dict["MinorRev"] = minor_rev
        if licensed_features is not UNSET:
            field_dict["LicensedFeatures"] = licensed_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("ProductId", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        major_rev = d.pop("MajorRev", UNSET)

        minor_rev = d.pop("MinorRev", UNSET)

        licensed_features = []
        _licensed_features = d.pop("LicensedFeatures", UNSET)
        for licensed_features_item_data in _licensed_features or []:
            licensed_features_item = KeyfactorApiModelsLicenseLicenseResponseLicensedFeature.from_dict(
                licensed_features_item_data
            )

            licensed_features.append(licensed_features_item)

        keyfactor_api_models_license_license_response_licensed_product = cls(
            product_id=product_id,
            display_name=display_name,
            major_rev=major_rev,
            minor_rev=minor_rev,
            licensed_features=licensed_features,
        )

        keyfactor_api_models_license_license_response_licensed_product.additional_properties = d
        return keyfactor_api_models_license_license_response_licensed_product

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
