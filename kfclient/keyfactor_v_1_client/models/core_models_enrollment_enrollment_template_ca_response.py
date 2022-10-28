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

from ..models.core_models_enrollment_enrollment_ca import CoreModelsEnrollmentEnrollmentCA
from ..models.core_models_enrollment_enrollment_template import CoreModelsEnrollmentEnrollmentTemplate
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoreModelsEnrollmentEnrollmentTemplateCAResponse")


@attr.s(auto_attribs=True)
class CoreModelsEnrollmentEnrollmentTemplateCAResponse:
    """
    Attributes:
        templates (Union[Unset, List[CoreModelsEnrollmentEnrollmentTemplate]]):
        standalone_c_as (Union[Unset, List[CoreModelsEnrollmentEnrollmentCA]]):
    """

    templates: Union[Unset, List[CoreModelsEnrollmentEnrollmentTemplate]] = UNSET
    standalone_c_as: Union[Unset, List[CoreModelsEnrollmentEnrollmentCA]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        templates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()

                templates.append(templates_item)

        standalone_c_as: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.standalone_c_as, Unset):
            standalone_c_as = []
            for standalone_c_as_item_data in self.standalone_c_as:
                standalone_c_as_item = standalone_c_as_item_data.to_dict()

                standalone_c_as.append(standalone_c_as_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if templates is not UNSET:
            field_dict["Templates"] = templates
        if standalone_c_as is not UNSET:
            field_dict["StandaloneCAs"] = standalone_c_as

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        templates = []
        _templates = d.pop("Templates", UNSET)
        for templates_item_data in _templates or []:
            templates_item = CoreModelsEnrollmentEnrollmentTemplate.from_dict(templates_item_data)

            templates.append(templates_item)

        standalone_c_as = []
        _standalone_c_as = d.pop("StandaloneCAs", UNSET)
        for standalone_c_as_item_data in _standalone_c_as or []:
            standalone_c_as_item = CoreModelsEnrollmentEnrollmentCA.from_dict(standalone_c_as_item_data)

            standalone_c_as.append(standalone_c_as_item)

        core_models_enrollment_enrollment_template_ca_response = cls(
            templates=templates,
            standalone_c_as=standalone_c_as,
        )

        core_models_enrollment_enrollment_template_ca_response.additional_properties = d
        return core_models_enrollment_enrollment_template_ca_response

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
