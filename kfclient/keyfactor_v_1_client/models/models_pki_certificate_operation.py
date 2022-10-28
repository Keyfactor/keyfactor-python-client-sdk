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

T = TypeVar("T", bound="ModelsPKICertificateOperation")


@attr.s(auto_attribs=True)
class ModelsPKICertificateOperation:
    """Details of an operation done on a certificate.

    Attributes:
        id (Union[Unset, int]):
        operation_start (Union[Unset, datetime.datetime]):
        operation_end (Union[Unset, datetime.datetime]):
        username (Union[Unset, str]):
        comment (Union[Unset, str]):
        action (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    operation_start: Union[Unset, datetime.datetime] = UNSET
    operation_end: Union[Unset, datetime.datetime] = UNSET
    username: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        operation_start: Union[Unset, str] = UNSET
        if not isinstance(self.operation_start, Unset):
            operation_start = self.operation_start.isoformat()[:-6]+'Z'

        operation_end: Union[Unset, str] = UNSET
        if not isinstance(self.operation_end, Unset):
            operation_end = self.operation_end.isoformat()[:-6]+'Z'

        username = self.username
        comment = self.comment
        action = self.action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if operation_start is not UNSET:
            field_dict["OperationStart"] = operation_start
        if operation_end is not UNSET:
            field_dict["OperationEnd"] = operation_end
        if username is not UNSET:
            field_dict["Username"] = username
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if action is not UNSET:
            field_dict["Action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _operation_start = d.pop("OperationStart", UNSET)
        operation_start: Union[Unset, datetime.datetime]
        if isinstance(_operation_start, Unset):
            operation_start = UNSET
        else:
            operation_start = isoparse(_operation_start)

        _operation_end = d.pop("OperationEnd", UNSET)
        operation_end: Union[Unset, datetime.datetime]
        if isinstance(_operation_end, Unset):
            operation_end = UNSET
        else:
            operation_end = isoparse(_operation_end)

        username = d.pop("Username", UNSET)

        comment = d.pop("Comment", UNSET)

        action = d.pop("Action", UNSET)

        models_pki_certificate_operation = cls(
            id=id,
            operation_start=operation_start,
            operation_end=operation_end,
            username=username,
            comment=comment,
            action=action,
        )

        models_pki_certificate_operation.additional_properties = d
        return models_pki_certificate_operation

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
