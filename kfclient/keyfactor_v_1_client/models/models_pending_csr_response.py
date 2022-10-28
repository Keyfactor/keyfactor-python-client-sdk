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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsPendingCSRResponse")


@attr.s(auto_attribs=True)
class ModelsPendingCSRResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        csr (Union[Unset, str]):
        request_time (Union[Unset, datetime.datetime]):
        subject (Union[Unset, List[str]]):
    """

    id: Union[Unset, int] = UNSET
    csr: Union[Unset, str] = UNSET
    request_time: Union[Unset, datetime.datetime] = UNSET
    subject: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        csr = self.csr
        request_time: Union[Unset, str] = UNSET
        if not isinstance(self.request_time, Unset):
            request_time = self.request_time.isoformat()[:-6]+'Z'

        subject: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if csr is not UNSET:
            field_dict["CSR"] = csr
        if request_time is not UNSET:
            field_dict["RequestTime"] = request_time
        if subject is not UNSET:
            field_dict["Subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        csr = d.pop("CSR", UNSET)

        _request_time = d.pop("RequestTime", UNSET)
        request_time: Union[Unset, datetime.datetime]
        if isinstance(_request_time, Unset):
            request_time = UNSET
        else:
            request_time = isoparse(_request_time)

        subject = cast(List[str], d.pop("Subject", UNSET))

        models_pending_csr_response = cls(
            id=id,
            csr=csr,
            request_time=request_time,
            subject=subject,
        )

        models_pending_csr_response.additional_properties = d
        return models_pending_csr_response

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
