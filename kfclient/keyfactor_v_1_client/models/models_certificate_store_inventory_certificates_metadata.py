# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.models_certificate_store_inventory_certificates_metadata_additional_property import (
    ModelsCertificateStoreInventoryCertificatesMetadataAdditionalProperty,
)

T = TypeVar("T", bound="ModelsCertificateStoreInventoryCertificatesMetadata")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreInventoryCertificatesMetadata:
    """ """

    additional_properties: Dict[str, ModelsCertificateStoreInventoryCertificatesMetadataAdditionalProperty] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        models_certificate_store_inventory_certificates_metadata = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ModelsCertificateStoreInventoryCertificatesMetadataAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        models_certificate_store_inventory_certificates_metadata.additional_properties = additional_properties
        return models_certificate_store_inventory_certificates_metadata

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ModelsCertificateStoreInventoryCertificatesMetadataAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: ModelsCertificateStoreInventoryCertificatesMetadataAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
