# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.models_template_update_request_template_enrollment_field_model_data_type import (
    ModelsTemplateUpdateRequestTemplateEnrollmentFieldModelDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTemplateUpdateRequestTemplateEnrollmentFieldModel")


@attr.s(auto_attribs=True)
class ModelsTemplateUpdateRequestTemplateEnrollmentFieldModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        options (Union[Unset, List[str]]):
        data_type (Union[Unset, ModelsTemplateUpdateRequestTemplateEnrollmentFieldModelDataType]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    options: Union[Unset, List[str]] = UNSET
    data_type: Union[Unset, ModelsTemplateUpdateRequestTemplateEnrollmentFieldModelDataType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        options: Union[Unset, List[str]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if options is not UNSET:
            field_dict["Options"] = options
        if data_type is not UNSET:
            field_dict["DataType"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        options = cast(List[str], d.pop("Options", UNSET))

        _data_type = d.pop("DataType", UNSET)
        data_type: Union[Unset, ModelsTemplateUpdateRequestTemplateEnrollmentFieldModelDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = ModelsTemplateUpdateRequestTemplateEnrollmentFieldModelDataType(_data_type)

        models_template_update_request_template_enrollment_field_model = cls(
            id=id,
            name=name,
            options=options,
            data_type=data_type,
        )

        models_template_update_request_template_enrollment_field_model.additional_properties = d
        return models_template_update_request_template_enrollment_field_model

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
