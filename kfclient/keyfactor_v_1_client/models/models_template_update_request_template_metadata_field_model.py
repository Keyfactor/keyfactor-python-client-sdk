from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_template_update_request_template_metadata_field_model_enrollment import (
    ModelsTemplateUpdateRequestTemplateMetadataFieldModelEnrollment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTemplateUpdateRequestTemplateMetadataFieldModel")


@attr.s(auto_attribs=True)
class ModelsTemplateUpdateRequestTemplateMetadataFieldModel:
    """
    Attributes:
        id (Union[Unset, int]):
        default_value (Union[Unset, str]):
        metadata_id (Union[Unset, int]):
        validation (Union[Unset, str]):
        enrollment (Union[Unset, ModelsTemplateUpdateRequestTemplateMetadataFieldModelEnrollment]):
        message (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    default_value: Union[Unset, str] = UNSET
    metadata_id: Union[Unset, int] = UNSET
    validation: Union[Unset, str] = UNSET
    enrollment: Union[Unset, ModelsTemplateUpdateRequestTemplateMetadataFieldModelEnrollment] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        default_value = self.default_value
        metadata_id = self.metadata_id
        validation = self.validation
        enrollment: Union[Unset, int] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if metadata_id is not UNSET:
            field_dict["MetadataId"] = metadata_id
        if validation is not UNSET:
            field_dict["Validation"] = validation
        if enrollment is not UNSET:
            field_dict["Enrollment"] = enrollment
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        metadata_id = d.pop("MetadataId", UNSET)

        validation = d.pop("Validation", UNSET)

        _enrollment = d.pop("Enrollment", UNSET)
        enrollment: Union[Unset, ModelsTemplateUpdateRequestTemplateMetadataFieldModelEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = ModelsTemplateUpdateRequestTemplateMetadataFieldModelEnrollment(_enrollment)

        message = d.pop("Message", UNSET)

        models_template_update_request_template_metadata_field_model = cls(
            id=id,
            default_value=default_value,
            metadata_id=metadata_id,
            validation=validation,
            enrollment=enrollment,
            message=message,
        )

        models_template_update_request_template_metadata_field_model.additional_properties = d
        return models_template_update_request_template_metadata_field_model

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
