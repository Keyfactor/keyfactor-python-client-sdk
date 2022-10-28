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

from ..models.keyfactor_api_models_license_license_response_licensed_customer import (
    KeyfactorApiModelsLicenseLicenseResponseLicensedCustomer,
)
from ..models.keyfactor_api_models_license_license_response_licensed_product import (
    KeyfactorApiModelsLicenseLicenseResponseLicensedProduct,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsLicenseLicenseResponseLicense")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsLicenseLicenseResponseLicense:
    """
    Attributes:
        license_id (Union[Unset, str]):
        customer (Union[Unset, KeyfactorApiModelsLicenseLicenseResponseLicensedCustomer]):
        issued_date (Union[Unset, datetime.datetime]):
        expiration_date (Union[Unset, datetime.datetime]):
        licensed_products (Union[Unset, List[KeyfactorApiModelsLicenseLicenseResponseLicensedProduct]]):
    """

    license_id: Union[Unset, str] = UNSET
    customer: Union[Unset, KeyfactorApiModelsLicenseLicenseResponseLicensedCustomer] = UNSET
    issued_date: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    licensed_products: Union[Unset, List[KeyfactorApiModelsLicenseLicenseResponseLicensedProduct]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        license_id = self.license_id
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        issued_date: Union[Unset, str] = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.isoformat()[:-6]+'Z'

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()[:-6]+'Z'

        licensed_products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licensed_products, Unset):
            licensed_products = []
            for licensed_products_item_data in self.licensed_products:
                licensed_products_item = licensed_products_item_data.to_dict()

                licensed_products.append(licensed_products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_id is not UNSET:
            field_dict["LicenseId"] = license_id
        if customer is not UNSET:
            field_dict["Customer"] = customer
        if issued_date is not UNSET:
            field_dict["IssuedDate"] = issued_date
        if expiration_date is not UNSET:
            field_dict["ExpirationDate"] = expiration_date
        if licensed_products is not UNSET:
            field_dict["LicensedProducts"] = licensed_products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        license_id = d.pop("LicenseId", UNSET)

        _customer = d.pop("Customer", UNSET)
        customer: Union[Unset, KeyfactorApiModelsLicenseLicenseResponseLicensedCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = KeyfactorApiModelsLicenseLicenseResponseLicensedCustomer.from_dict(_customer)

        _issued_date = d.pop("IssuedDate", UNSET)
        issued_date: Union[Unset, datetime.datetime]
        if isinstance(_issued_date, Unset):
            issued_date = UNSET
        else:
            issued_date = isoparse(_issued_date)

        _expiration_date = d.pop("ExpirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        licensed_products = []
        _licensed_products = d.pop("LicensedProducts", UNSET)
        for licensed_products_item_data in _licensed_products or []:
            licensed_products_item = KeyfactorApiModelsLicenseLicenseResponseLicensedProduct.from_dict(
                licensed_products_item_data
            )

            licensed_products.append(licensed_products_item)

        keyfactor_api_models_license_license_response_license = cls(
            license_id=license_id,
            customer=customer,
            issued_date=issued_date,
            expiration_date=expiration_date,
            licensed_products=licensed_products,
        )

        keyfactor_api_models_license_license_response_license.additional_properties = d
        return keyfactor_api_models_license_license_response_license

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
