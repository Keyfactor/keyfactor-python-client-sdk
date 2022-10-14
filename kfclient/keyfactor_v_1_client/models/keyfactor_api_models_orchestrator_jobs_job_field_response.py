from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorJobsJobFieldResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorJobsJobFieldResponse:
    """
    Attributes:
        job_type_field (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    job_type_field: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_type_field = self.job_type_field
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_type_field is not UNSET:
            field_dict["JobTypeField"] = job_type_field
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_type_field = d.pop("JobTypeField", UNSET)

        value = d.pop("Value", UNSET)

        keyfactor_api_models_orchestrator_jobs_job_field_response = cls(
            job_type_field=job_type_field,
            value=value,
        )

        keyfactor_api_models_orchestrator_jobs_job_field_response.additional_properties = d
        return keyfactor_api_models_orchestrator_jobs_job_field_response

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
