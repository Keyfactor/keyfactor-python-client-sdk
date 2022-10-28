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

T = TypeVar("T", bound="ModelsEnrollmentExistingEnrollmentManagementRequest")


@attr.s(auto_attribs=True)
class ModelsEnrollmentExistingEnrollmentManagementRequest:
    """
    Example:
        {'ExistingCertificateId': 0, 'CertificateId': 0, 'RequestId': 0, 'Password': '<pfx password>', 'JobTime':
            datetime.datetime(2022, 9, 23, 18, 9, 16, 719678, tzinfo=datetime.timezone.utc)}

    Attributes:
        existing_certificate_id (Union[Unset, int]):
        certificate_id (Union[Unset, int]):
        request_id (Union[Unset, int]):
        password (Union[Unset, str]):
        job_time (Union[Unset, datetime.datetime]):
    """

    existing_certificate_id: Union[Unset, int] = UNSET
    certificate_id: Union[Unset, int] = UNSET
    request_id: Union[Unset, int] = UNSET
    password: Union[Unset, str] = UNSET
    job_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        existing_certificate_id = self.existing_certificate_id
        certificate_id = self.certificate_id
        request_id = self.request_id
        password = self.password
        job_time: Union[Unset, str] = UNSET
        if not isinstance(self.job_time, Unset):
            job_time = self.job_time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if existing_certificate_id is not UNSET:
            field_dict["ExistingCertificateId"] = existing_certificate_id
        if certificate_id is not UNSET:
            field_dict["CertificateId"] = certificate_id
        if request_id is not UNSET:
            field_dict["RequestId"] = request_id
        if password is not UNSET:
            field_dict["Password"] = password
        if job_time is not UNSET:
            field_dict["JobTime"] = job_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        existing_certificate_id = d.pop("ExistingCertificateId", UNSET)

        certificate_id = d.pop("CertificateId", UNSET)

        request_id = d.pop("RequestId", UNSET)

        password = d.pop("Password", UNSET)

        _job_time = d.pop("JobTime", UNSET)
        job_time: Union[Unset, datetime.datetime]
        if isinstance(_job_time, Unset):
            job_time = UNSET
        else:
            job_time = isoparse(_job_time)

        models_enrollment_existing_enrollment_management_request = cls(
            existing_certificate_id=existing_certificate_id,
            certificate_id=certificate_id,
            request_id=request_id,
            password=password,
            job_time=job_time,
        )

        models_enrollment_existing_enrollment_management_request.additional_properties = d
        return models_enrollment_existing_enrollment_management_request

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
