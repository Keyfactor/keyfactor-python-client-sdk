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

from ..models.models_certificate_store_inventory_certificates_metadata import (
    ModelsCertificateStoreInventoryCertificatesMetadata,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStoreInventoryCertificates")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreInventoryCertificates:
    """
    Attributes:
        id (Union[Unset, int]):
        issued_dn (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        not_before (Union[Unset, datetime.datetime]):
        not_after (Union[Unset, datetime.datetime]):
        signing_algorithm (Union[Unset, str]):
        issuer_dn (Union[Unset, str]):
        thumbprint (Union[Unset, str]):
        cert_store_inventory_item_id (Union[Unset, int]):
        metadata (Union[Unset, ModelsCertificateStoreInventoryCertificatesMetadata]):
    """

    id: Union[Unset, int] = UNSET
    issued_dn: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    signing_algorithm: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    cert_store_inventory_item_id: Union[Unset, int] = UNSET
    metadata: Union[Unset, ModelsCertificateStoreInventoryCertificatesMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        issued_dn = self.issued_dn
        serial_number = self.serial_number
        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()[:-6]+'Z'

        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()[:-6]+'Z'

        signing_algorithm = self.signing_algorithm
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        cert_store_inventory_item_id = self.cert_store_inventory_item_id
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if issued_dn is not UNSET:
            field_dict["IssuedDN"] = issued_dn
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if not_before is not UNSET:
            field_dict["NotBefore"] = not_before
        if not_after is not UNSET:
            field_dict["NotAfter"] = not_after
        if signing_algorithm is not UNSET:
            field_dict["SigningAlgorithm"] = signing_algorithm
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if cert_store_inventory_item_id is not UNSET:
            field_dict["CertStoreInventoryItemId"] = cert_store_inventory_item_id
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        issued_dn = d.pop("IssuedDN", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        _not_before = d.pop("NotBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _not_after = d.pop("NotAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        signing_algorithm = d.pop("SigningAlgorithm", UNSET)

        issuer_dn = d.pop("IssuerDN", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        cert_store_inventory_item_id = d.pop("CertStoreInventoryItemId", UNSET)

        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, ModelsCertificateStoreInventoryCertificatesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsCertificateStoreInventoryCertificatesMetadata.from_dict(_metadata)

        models_certificate_store_inventory_certificates = cls(
            id=id,
            issued_dn=issued_dn,
            serial_number=serial_number,
            not_before=not_before,
            not_after=not_after,
            signing_algorithm=signing_algorithm,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            cert_store_inventory_item_id=cert_store_inventory_item_id,
            metadata=metadata,
        )

        models_certificate_store_inventory_certificates.additional_properties = d
        return models_certificate_store_inventory_certificates

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
