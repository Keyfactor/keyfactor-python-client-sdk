from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyfactor_api_models_metadata_field_metadata_field_update_request_data_type import (
    KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestDataType,
)
from ..models.keyfactor_api_models_metadata_field_metadata_field_update_request_enrollment import (
    KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestEnrollment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequest:
    """
    Attributes:
        id (int):
        name (str):
        description (str):
        data_type (KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestDataType):
        hint (Union[Unset, str]):
        validation (Union[Unset, str]):
        enrollment (Union[Unset, KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestEnrollment]):
        message (Union[Unset, str]):
        options (Union[Unset, str]):
        default_value (Union[Unset, str]):
        display_order (Union[Unset, int]):
    """

    id: int
    name: str
    description: str
    data_type: KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestDataType
    hint: Union[Unset, str] = UNSET
    validation: Union[Unset, str] = UNSET
    enrollment: Union[Unset, KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestEnrollment] = UNSET
    message: Union[Unset, str] = UNSET
    options: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        data_type = self.data_type.value

        hint = self.hint
        validation = self.validation
        enrollment: Union[Unset, int] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.value

        message = self.message
        options = self.options
        default_value = self.default_value
        display_order = self.display_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Name": name,
                "Description": description,
                "DataType": data_type,
            }
        )
        if hint is not UNSET:
            field_dict["Hint"] = hint
        if validation is not UNSET:
            field_dict["Validation"] = validation
        if enrollment is not UNSET:
            field_dict["Enrollment"] = enrollment
        if message is not UNSET:
            field_dict["Message"] = message
        if options is not UNSET:
            field_dict["Options"] = options
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if display_order is not UNSET:
            field_dict["DisplayOrder"] = display_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        name = d.pop("Name")

        description = d.pop("Description")

        data_type = KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestDataType(d.pop("DataType"))

        hint = d.pop("Hint", UNSET)

        validation = d.pop("Validation", UNSET)

        _enrollment = d.pop("Enrollment", UNSET)
        enrollment: Union[Unset, KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = KeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequestEnrollment(_enrollment)

        message = d.pop("Message", UNSET)

        options = d.pop("Options", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        display_order = d.pop("DisplayOrder", UNSET)

        keyfactor_api_models_metadata_field_metadata_field_update_request = cls(
            id=id,
            name=name,
            description=description,
            data_type=data_type,
            hint=hint,
            validation=validation,
            enrollment=enrollment,
            message=message,
            options=options,
            default_value=default_value,
            display_order=display_order,
        )

        keyfactor_api_models_metadata_field_metadata_field_update_request.additional_properties = d
        return keyfactor_api_models_metadata_field_metadata_field_update_request

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
