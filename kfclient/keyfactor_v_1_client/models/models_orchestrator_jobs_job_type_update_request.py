from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_orchestrator_jobs_job_type_field_request import ModelsOrchestratorJobsJobTypeFieldRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOrchestratorJobsJobTypeUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsOrchestratorJobsJobTypeUpdateRequest:
    """
    Attributes:
        id (str):  Example: 00000000-0000-0000-0000-000000000000.
        job_type_name (str):
        description (Union[Unset, str]):
        job_type_fields (Union[Unset, List[ModelsOrchestratorJobsJobTypeFieldRequest]]):
    """

    id: str
    job_type_name: str
    description: Union[Unset, str] = UNSET
    job_type_fields: Union[Unset, List[ModelsOrchestratorJobsJobTypeFieldRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        job_type_name = self.job_type_name
        description = self.description
        job_type_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_type_fields, Unset):
            job_type_fields = []
            for job_type_fields_item_data in self.job_type_fields:
                job_type_fields_item = job_type_fields_item_data.to_dict()

                job_type_fields.append(job_type_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "JobTypeName": job_type_name,
            }
        )
        if description is not UNSET:
            field_dict["Description"] = description
        if job_type_fields is not UNSET:
            field_dict["JobTypeFields"] = job_type_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        job_type_name = d.pop("JobTypeName")

        description = d.pop("Description", UNSET)

        job_type_fields = []
        _job_type_fields = d.pop("JobTypeFields", UNSET)
        for job_type_fields_item_data in _job_type_fields or []:
            job_type_fields_item = ModelsOrchestratorJobsJobTypeFieldRequest.from_dict(job_type_fields_item_data)

            job_type_fields.append(job_type_fields_item)

        models_orchestrator_jobs_job_type_update_request = cls(
            id=id,
            job_type_name=job_type_name,
            description=description,
            job_type_fields=job_type_fields,
        )

        models_orchestrator_jobs_job_type_update_request.additional_properties = d
        return models_orchestrator_jobs_job_type_update_request

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
