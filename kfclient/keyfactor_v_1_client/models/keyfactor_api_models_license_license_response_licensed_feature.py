# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsLicenseLicenseResponseLicensedFeature")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsLicenseLicenseResponseLicensedFeature:
    """
    Attributes:
        feature_id (Union[Unset, str]):
        display_name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        quantity (Union[Unset, int]):
        expiration_date (Union[Unset, datetime.datetime]):
    """

    feature_id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    quantity: Union[Unset, int] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feature_id = self.feature_id
        display_name = self.display_name
        enabled = self.enabled
        quantity = self.quantity
        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_id is not UNSET:
            field_dict["FeatureID"] = feature_id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if expiration_date is not UNSET:
            field_dict["ExpirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feature_id = d.pop("FeatureID", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        enabled = d.pop("Enabled", UNSET)

        quantity = d.pop("Quantity", UNSET)

        _expiration_date = d.pop("ExpirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        keyfactor_api_models_license_license_response_licensed_feature = cls(
            feature_id=feature_id,
            display_name=display_name,
            enabled=enabled,
            quantity=quantity,
            expiration_date=expiration_date,
        )

        keyfactor_api_models_license_license_response_licensed_feature.additional_properties = d
        return keyfactor_api_models_license_license_response_licensed_feature

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
