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
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.models_revoke_certificate_request_reason import ModelsRevokeCertificateRequestReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsRevokeCertificateRequest")


@attr.s(auto_attribs=True)
class ModelsRevokeCertificateRequest:
    """
    Attributes:
        certificate_ids (Union[Unset, List[int]]):
        reason (Union[Unset, ModelsRevokeCertificateRequestReason]):
        comment (Union[Unset, str]):
        effective_date (Union[Unset, datetime.datetime]):
        collection_id (Union[Unset, int]):
    """

    certificate_ids: Union[Unset, List[int]] = UNSET
    reason: Union[Unset, ModelsRevokeCertificateRequestReason] = UNSET
    comment: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.datetime] = UNSET
    collection_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.certificate_ids, Unset):
            certificate_ids = self.certificate_ids

        reason: Union[Unset, int] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        comment = self.comment
        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()[:-6]+'Z'

        collection_id = self.collection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_ids is not UNSET:
            field_dict["CertificateIds"] = certificate_ids
        if reason is not UNSET:
            field_dict["Reason"] = reason
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if effective_date is not UNSET:
            field_dict["EffectiveDate"] = effective_date
        if collection_id is not UNSET:
            field_dict["CollectionId"] = collection_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_ids = cast(List[int], d.pop("CertificateIds", UNSET))

        _reason = d.pop("Reason", UNSET)
        reason: Union[Unset, ModelsRevokeCertificateRequestReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ModelsRevokeCertificateRequestReason(_reason)

        comment = d.pop("Comment", UNSET)

        _effective_date = d.pop("EffectiveDate", UNSET)
        effective_date: Union[Unset, datetime.datetime]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date)

        collection_id = d.pop("CollectionId", UNSET)

        models_revoke_certificate_request = cls(
            certificate_ids=certificate_ids,
            reason=reason,
            comment=comment,
            effective_date=effective_date,
            collection_id=collection_id,
        )

        models_revoke_certificate_request.additional_properties = d
        return models_revoke_certificate_request

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
