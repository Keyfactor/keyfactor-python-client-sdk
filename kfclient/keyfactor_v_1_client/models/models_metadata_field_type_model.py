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

from ..models.models_metadata_field_type_model_data_type import ModelsMetadataFieldTypeModelDataType
from ..models.models_metadata_field_type_model_enrollment import ModelsMetadataFieldTypeModelEnrollment
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsMetadataFieldTypeModel")


@attr.s(auto_attribs=True)
class ModelsMetadataFieldTypeModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        data_type (Union[Unset, ModelsMetadataFieldTypeModelDataType]):
        hint (Union[Unset, str]):
        validation (Union[Unset, str]):
        enrollment (Union[Unset, ModelsMetadataFieldTypeModelEnrollment]):
        message (Union[Unset, str]):
        options (Union[Unset, str]):
        default_value (Union[Unset, str]):
        display_order (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    data_type: Union[Unset, ModelsMetadataFieldTypeModelDataType] = UNSET
    hint: Union[Unset, str] = UNSET
    validation: Union[Unset, str] = UNSET
    enrollment: Union[Unset, ModelsMetadataFieldTypeModelEnrollment] = UNSET
    message: Union[Unset, str] = UNSET
    options: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
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
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if data_type is not UNSET:
            field_dict["DataType"] = data_type
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
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        _data_type = d.pop("DataType", UNSET)
        data_type: Union[Unset, ModelsMetadataFieldTypeModelDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = ModelsMetadataFieldTypeModelDataType(_data_type)

        hint = d.pop("Hint", UNSET)

        validation = d.pop("Validation", UNSET)

        _enrollment = d.pop("Enrollment", UNSET)
        enrollment: Union[Unset, ModelsMetadataFieldTypeModelEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = ModelsMetadataFieldTypeModelEnrollment(_enrollment)

        message = d.pop("Message", UNSET)

        options = d.pop("Options", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        display_order = d.pop("DisplayOrder", UNSET)

        models_metadata_field_type_model = cls(
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

        models_metadata_field_type_model.additional_properties = d
        return models_metadata_field_type_model

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
