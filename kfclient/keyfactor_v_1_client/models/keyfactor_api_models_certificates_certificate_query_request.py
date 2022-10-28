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

from ..models.keyfactor_api_models_certificates_certificate_query_request_sort_ascending import (
    KeyfactorApiModelsCertificatesCertificateQueryRequestSortAscending,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificatesCertificateQueryRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificatesCertificateQueryRequest:
    """
    Attributes:
        query_string (Union[Unset, str]): Contents of the query (ex: field1 -eq value1 AND field2 -gt value2)
        page_returned (Union[Unset, int]): The current page within the result set to be returned
        return_limit (Union[Unset, int]): Maximum number of records to be returned in a single call
        sort_field (Union[Unset, str]): Field by which the results should be sorted (view results via Management Portal
            for sortable columns)
        sort_ascending (Union[Unset, KeyfactorApiModelsCertificatesCertificateQueryRequestSortAscending]): Field sort
            direction [0=ascending, 1=descending]
        include_revoked (Union[Unset, bool]): Select 'true' to include revoked certificates in the results
        include_expired (Union[Unset, bool]): Select 'true' to include expired certificates in the results
    """

    query_string: Union[Unset, str] = UNSET
    page_returned: Union[Unset, int] = UNSET
    return_limit: Union[Unset, int] = UNSET
    sort_field: Union[Unset, str] = UNSET
    sort_ascending: Union[Unset, KeyfactorApiModelsCertificatesCertificateQueryRequestSortAscending] = UNSET
    include_revoked: Union[Unset, bool] = UNSET
    include_expired: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_string = self.query_string
        page_returned = self.page_returned
        return_limit = self.return_limit
        sort_field = self.sort_field
        sort_ascending: Union[Unset, int] = UNSET
        if not isinstance(self.sort_ascending, Unset):
            sort_ascending = self.sort_ascending.value

        include_revoked = self.include_revoked
        include_expired = self.include_expired

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_string is not UNSET:
            field_dict["QueryString"] = query_string
        if page_returned is not UNSET:
            field_dict["PageReturned"] = page_returned
        if return_limit is not UNSET:
            field_dict["ReturnLimit"] = return_limit
        if sort_field is not UNSET:
            field_dict["SortField"] = sort_field
        if sort_ascending is not UNSET:
            field_dict["SortAscending"] = sort_ascending
        if include_revoked is not UNSET:
            field_dict["IncludeRevoked"] = include_revoked
        if include_expired is not UNSET:
            field_dict["IncludeExpired"] = include_expired

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query_string = d.pop("QueryString", UNSET)

        page_returned = d.pop("PageReturned", UNSET)

        return_limit = d.pop("ReturnLimit", UNSET)

        sort_field = d.pop("SortField", UNSET)

        _sort_ascending = d.pop("SortAscending", UNSET)
        sort_ascending: Union[Unset, KeyfactorApiModelsCertificatesCertificateQueryRequestSortAscending]
        if isinstance(_sort_ascending, Unset):
            sort_ascending = UNSET
        else:
            sort_ascending = KeyfactorApiModelsCertificatesCertificateQueryRequestSortAscending(_sort_ascending)

        include_revoked = d.pop("IncludeRevoked", UNSET)

        include_expired = d.pop("IncludeExpired", UNSET)

        keyfactor_api_models_certificates_certificate_query_request = cls(
            query_string=query_string,
            page_returned=page_returned,
            return_limit=return_limit,
            sort_field=sort_field,
            sort_ascending=sort_ascending,
            include_revoked=include_revoked,
            include_expired=include_expired,
        )

        keyfactor_api_models_certificates_certificate_query_request.additional_properties = d
        return keyfactor_api_models_certificates_certificate_query_request

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
