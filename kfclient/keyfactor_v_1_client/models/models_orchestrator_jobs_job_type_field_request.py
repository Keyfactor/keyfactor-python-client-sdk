from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_orchestrator_jobs_job_type_field_request_type import ModelsOrchestratorJobsJobTypeFieldRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOrchestratorJobsJobTypeFieldRequest")


@attr.s(auto_attribs=True)
class ModelsOrchestratorJobsJobTypeFieldRequest:
    """
    Attributes:
        name (str):
        type (ModelsOrchestratorJobsJobTypeFieldRequestType):
        default_value (Union[Unset, str]):
        required (Union[Unset, bool]):
    """

    name: str
    type: ModelsOrchestratorJobsJobTypeFieldRequestType
    default_value: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
                "Type": type,
            }
        )
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if required is not UNSET:
            field_dict["Required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        type = ModelsOrchestratorJobsJobTypeFieldRequestType(d.pop("Type"))

        default_value = d.pop("DefaultValue", UNSET)

        required = d.pop("Required", UNSET)

        models_orchestrator_jobs_job_type_field_request = cls(
            name=name,
            type=type,
            default_value=default_value,
            required=required,
        )

        models_orchestrator_jobs_job_type_field_request.additional_properties = d
        return models_orchestrator_jobs_job_type_field_request

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