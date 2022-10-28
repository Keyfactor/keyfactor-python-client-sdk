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

from ..models.keyfactor_api_models_metadata_field_metadata_field_create_request_data_type import (
    KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestDataType,
)
from ..models.keyfactor_api_models_metadata_field_metadata_field_create_request_enrollment import (
    KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestEnrollment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequest:
    """
    Attributes:
        name (str):
        description (str):
        data_type (KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestDataType):
        hint (Union[Unset, str]):
        validation (Union[Unset, str]):
        enrollment (Union[Unset, KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestEnrollment]):
        message (Union[Unset, str]):
        options (Union[Unset, str]):
        default_value (Union[Unset, str]):
        display_order (Union[Unset, int]):
    """

    name: str
    description: str
    data_type: KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestDataType
    hint: Union[Unset, str] = UNSET
    validation: Union[Unset, str] = UNSET
    enrollment: Union[Unset, KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestEnrollment] = UNSET
    message: Union[Unset, str] = UNSET
    options: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        name = d.pop("Name")

        description = d.pop("Description")

        data_type = KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestDataType(d.pop("DataType"))

        hint = d.pop("Hint", UNSET)

        validation = d.pop("Validation", UNSET)

        _enrollment = d.pop("Enrollment", UNSET)
        enrollment: Union[Unset, KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = KeyfactorApiModelsMetadataFieldMetadataFieldCreateRequestEnrollment(_enrollment)

        message = d.pop("Message", UNSET)

        options = d.pop("Options", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        display_order = d.pop("DisplayOrder", UNSET)

        keyfactor_api_models_metadata_field_metadata_field_create_request = cls(
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

        keyfactor_api_models_metadata_field_metadata_field_create_request.additional_properties = d
        return keyfactor_api_models_metadata_field_metadata_field_create_request

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
