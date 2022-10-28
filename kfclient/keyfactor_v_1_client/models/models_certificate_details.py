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

from ..models.models_certificate_details_metadata import ModelsCertificateDetailsMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateDetails")


@attr.s(auto_attribs=True)
class ModelsCertificateDetails:
    """
    Attributes:
        issued_dn (Union[Unset, str]):
        issuer_dn (Union[Unset, str]):
        thumbprint (Union[Unset, str]):
        not_after (Union[Unset, datetime.datetime]):
        not_before (Union[Unset, datetime.datetime]):
        metadata (Union[Unset, ModelsCertificateDetailsMetadata]):
        is_end_entity (Union[Unset, bool]):
    """

    issued_dn: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, ModelsCertificateDetailsMetadata] = UNSET
    is_end_entity: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issued_dn = self.issued_dn
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()[:-6]+'Z'

        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()[:-6]+'Z'

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        is_end_entity = self.is_end_entity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issued_dn is not UNSET:
            field_dict["IssuedDN"] = issued_dn
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if not_after is not UNSET:
            field_dict["NotAfter"] = not_after
        if not_before is not UNSET:
            field_dict["NotBefore"] = not_before
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if is_end_entity is not UNSET:
            field_dict["IsEndEntity"] = is_end_entity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issued_dn = d.pop("IssuedDN", UNSET)

        issuer_dn = d.pop("IssuerDN", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        _not_after = d.pop("NotAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        _not_before = d.pop("NotBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, ModelsCertificateDetailsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsCertificateDetailsMetadata.from_dict(_metadata)

        is_end_entity = d.pop("IsEndEntity", UNSET)

        models_certificate_details = cls(
            issued_dn=issued_dn,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            not_after=not_after,
            not_before=not_before,
            metadata=metadata,
            is_end_entity=is_end_entity,
        )

        models_certificate_details.additional_properties = d
        return models_certificate_details

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
