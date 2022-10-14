from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..models.models_orchestrator_jobs_schedule_bulk_job_request_job_fields import (
    ModelsOrchestratorJobsScheduleBulkJobRequestJobFields,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOrchestratorJobsScheduleBulkJobRequest")


@attr.s(auto_attribs=True)
class ModelsOrchestratorJobsScheduleBulkJobRequest:
    """
    Attributes:
        orchestrator_ids (List[str]):
        job_type_name (str):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_fields (Union[Unset, ModelsOrchestratorJobsScheduleBulkJobRequestJobFields]):
    """

    orchestrator_ids: List[str]
    job_type_name: str
    schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    job_fields: Union[Unset, ModelsOrchestratorJobsScheduleBulkJobRequestJobFields] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orchestrator_ids = self.orchestrator_ids

        job_type_name = self.job_type_name
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        job_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = self.job_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OrchestratorIds": orchestrator_ids,
                "JobTypeName": job_type_name,
            }
        )
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule
        if job_fields is not UNSET:
            field_dict["JobFields"] = job_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        orchestrator_ids = cast(List[str], d.pop("OrchestratorIds"))

        job_type_name = d.pop("JobTypeName")

        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        _job_fields = d.pop("JobFields", UNSET)
        job_fields: Union[Unset, ModelsOrchestratorJobsScheduleBulkJobRequestJobFields]
        if isinstance(_job_fields, Unset):
            job_fields = UNSET
        else:
            job_fields = ModelsOrchestratorJobsScheduleBulkJobRequestJobFields.from_dict(_job_fields)

        models_orchestrator_jobs_schedule_bulk_job_request = cls(
            orchestrator_ids=orchestrator_ids,
            job_type_name=job_type_name,
            schedule=schedule,
            job_fields=job_fields,
        )

        models_orchestrator_jobs_schedule_bulk_job_request.additional_properties = d
        return models_orchestrator_jobs_schedule_bulk_job_request

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
