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

from ..models.models_revoke_all_certificates_request_reason import ModelsRevokeAllCertificatesRequestReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsRevokeAllCertificatesRequest")


@attr.s(auto_attribs=True)
class ModelsRevokeAllCertificatesRequest:
    """Information for revoking all certifictes in a query

    Attributes:
        reason (ModelsRevokeAllCertificatesRequestReason): The Reason for revocation
        comment (str): A comment for auditing purposes
        query (Union[Unset, str]): The query string of the certificates to revoke
        effective_date (Union[Unset, datetime.datetime]): The date when the certificates are to appear on the revocation
            list
        include_revoked (Union[Unset, bool]): A flag telling the query to include revoked certificates
        include_expired (Union[Unset, bool]): A flag telling the query to include expired certificates
    """

    reason: ModelsRevokeAllCertificatesRequestReason
    comment: str
    query: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.datetime] = UNSET
    include_revoked: Union[Unset, bool] = UNSET
    include_expired: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason = self.reason.value

        comment = self.comment
        query = self.query
        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()[:-6]+'Z'

        include_revoked = self.include_revoked
        include_expired = self.include_expired

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Reason": reason,
                "Comment": comment,
            }
        )
        if query is not UNSET:
            field_dict["Query"] = query
        if effective_date is not UNSET:
            field_dict["EffectiveDate"] = effective_date
        if include_revoked is not UNSET:
            field_dict["IncludeRevoked"] = include_revoked
        if include_expired is not UNSET:
            field_dict["IncludeExpired"] = include_expired

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reason = ModelsRevokeAllCertificatesRequestReason(d.pop("Reason"))

        comment = d.pop("Comment")

        query = d.pop("Query", UNSET)

        _effective_date = d.pop("EffectiveDate", UNSET)
        effective_date: Union[Unset, datetime.datetime]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date)

        include_revoked = d.pop("IncludeRevoked", UNSET)

        include_expired = d.pop("IncludeExpired", UNSET)

        models_revoke_all_certificates_request = cls(
            reason=reason,
            comment=comment,
            query=query,
            effective_date=effective_date,
            include_revoked=include_revoked,
            include_expired=include_expired,
        )

        models_revoke_all_certificates_request.additional_properties = d
        return models_revoke_all_certificates_request

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
