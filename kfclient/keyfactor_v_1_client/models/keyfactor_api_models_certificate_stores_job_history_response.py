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

from ..models.keyfactor_api_models_certificate_stores_job_history_response_result import (
    KeyfactorApiModelsCertificateStoresJobHistoryResponseResult,
)
from ..models.keyfactor_api_models_certificate_stores_job_history_response_status import (
    KeyfactorApiModelsCertificateStoresJobHistoryResponseStatus,
)
from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificateStoresJobHistoryResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificateStoresJobHistoryResponse:
    """
    Attributes:
        job_history_id (Union[Unset, int]):
        agent_machine (Union[Unset, str]):
        job_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_type (Union[Unset, str]):
        operation_start (Union[Unset, datetime.datetime]):
        operation_end (Union[Unset, datetime.datetime]):
        message (Union[Unset, str]):
        result (Union[Unset, KeyfactorApiModelsCertificateStoresJobHistoryResponseResult]):
        status (Union[Unset, KeyfactorApiModelsCertificateStoresJobHistoryResponseStatus]):
        store_path (Union[Unset, str]):
        client_machine (Union[Unset, str]):
    """

    job_history_id: Union[Unset, int] = UNSET
    agent_machine: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    job_type: Union[Unset, str] = UNSET
    operation_start: Union[Unset, datetime.datetime] = UNSET
    operation_end: Union[Unset, datetime.datetime] = UNSET
    message: Union[Unset, str] = UNSET
    result: Union[Unset, KeyfactorApiModelsCertificateStoresJobHistoryResponseResult] = UNSET
    status: Union[Unset, KeyfactorApiModelsCertificateStoresJobHistoryResponseStatus] = UNSET
    store_path: Union[Unset, str] = UNSET
    client_machine: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_history_id = self.job_history_id
        agent_machine = self.agent_machine
        job_id = self.job_id
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        job_type = self.job_type
        operation_start: Union[Unset, str] = UNSET
        if not isinstance(self.operation_start, Unset):
            operation_start = self.operation_start.isoformat()[:-6]+'Z'

        operation_end: Union[Unset, str] = UNSET
        if not isinstance(self.operation_end, Unset):
            operation_end = self.operation_end.isoformat()[:-6]+'Z'

        message = self.message
        result: Union[Unset, int] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        store_path = self.store_path
        client_machine = self.client_machine

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_history_id is not UNSET:
            field_dict["JobHistoryId"] = job_history_id
        if agent_machine is not UNSET:
            field_dict["AgentMachine"] = agent_machine
        if job_id is not UNSET:
            field_dict["JobId"] = job_id
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule
        if job_type is not UNSET:
            field_dict["JobType"] = job_type
        if operation_start is not UNSET:
            field_dict["OperationStart"] = operation_start
        if operation_end is not UNSET:
            field_dict["OperationEnd"] = operation_end
        if message is not UNSET:
            field_dict["Message"] = message
        if result is not UNSET:
            field_dict["Result"] = result
        if status is not UNSET:
            field_dict["Status"] = status
        if store_path is not UNSET:
            field_dict["StorePath"] = store_path
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_history_id = d.pop("JobHistoryId", UNSET)

        agent_machine = d.pop("AgentMachine", UNSET)

        job_id = d.pop("JobId", UNSET)

        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        job_type = d.pop("JobType", UNSET)

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

        message = d.pop("Message", UNSET)

        _result = d.pop("Result", UNSET)
        result: Union[Unset, KeyfactorApiModelsCertificateStoresJobHistoryResponseResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = KeyfactorApiModelsCertificateStoresJobHistoryResponseResult(_result)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, KeyfactorApiModelsCertificateStoresJobHistoryResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorApiModelsCertificateStoresJobHistoryResponseStatus(_status)

        store_path = d.pop("StorePath", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        keyfactor_api_models_certificate_stores_job_history_response = cls(
            job_history_id=job_history_id,
            agent_machine=agent_machine,
            job_id=job_id,
            schedule=schedule,
            job_type=job_type,
            operation_start=operation_start,
            operation_end=operation_end,
            message=message,
            result=result,
            status=status,
            store_path=store_path,
            client_machine=client_machine,
        )

        keyfactor_api_models_certificate_stores_job_history_response.additional_properties = d
        return keyfactor_api_models_certificate_stores_job_history_response

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
