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

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsWorkflowProcessedCertificateRequest")


@attr.s(auto_attribs=True)
class ModelsWorkflowProcessedCertificateRequest:
    """
    Attributes:
        ca_row_id (Union[Unset, int]):
        ca_request_id (Union[Unset, str]):
        ca_host (Union[Unset, str]):
        ca_logical_name (Union[Unset, str]):
        keyfactor_request_id (Union[Unset, int]):
        comment (Union[Unset, str]):
    """

    ca_row_id: Union[Unset, int] = UNSET
    ca_request_id: Union[Unset, str] = UNSET
    ca_host: Union[Unset, str] = UNSET
    ca_logical_name: Union[Unset, str] = UNSET
    keyfactor_request_id: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ca_row_id = self.ca_row_id
        ca_request_id = self.ca_request_id
        ca_host = self.ca_host
        ca_logical_name = self.ca_logical_name
        keyfactor_request_id = self.keyfactor_request_id
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ca_row_id is not UNSET:
            field_dict["CARowId"] = ca_row_id
        if ca_request_id is not UNSET:
            field_dict["CARequestId"] = ca_request_id
        if ca_host is not UNSET:
            field_dict["CAHost"] = ca_host
        if ca_logical_name is not UNSET:
            field_dict["CALogicalName"] = ca_logical_name
        if keyfactor_request_id is not UNSET:
            field_dict["KeyfactorRequestId"] = keyfactor_request_id
        if comment is not UNSET:
            field_dict["Comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ca_row_id = d.pop("CARowId", UNSET)

        ca_request_id = d.pop("CARequestId", UNSET)

        ca_host = d.pop("CAHost", UNSET)

        ca_logical_name = d.pop("CALogicalName", UNSET)

        keyfactor_request_id = d.pop("KeyfactorRequestId", UNSET)

        comment = d.pop("Comment", UNSET)

        models_workflow_processed_certificate_request = cls(
            ca_row_id=ca_row_id,
            ca_request_id=ca_request_id,
            ca_host=ca_host,
            ca_logical_name=ca_logical_name,
            keyfactor_request_id=keyfactor_request_id,
            comment=comment,
        )

        models_workflow_processed_certificate_request.additional_properties = d
        return models_workflow_processed_certificate_request

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
