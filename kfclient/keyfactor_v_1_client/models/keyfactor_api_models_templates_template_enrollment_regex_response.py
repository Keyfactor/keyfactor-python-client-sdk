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

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsTemplatesTemplateEnrollmentRegexResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsTemplatesTemplateEnrollmentRegexResponse:
    """
    Attributes:
        subject_part (Union[Unset, str]): The subject part to apply the regular expression to.
        regex (Union[Unset, str]): The regular expression to apply to the subject part.
        error (Union[Unset, str]): The error message to show when the regex validation fails.
    """

    subject_part: Union[Unset, str] = UNSET
    regex: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_part = self.subject_part
        regex = self.regex
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject_part is not UNSET:
            field_dict["SubjectPart"] = subject_part
        if regex is not UNSET:
            field_dict["Regex"] = regex
        if error is not UNSET:
            field_dict["Error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_part = d.pop("SubjectPart", UNSET)

        regex = d.pop("Regex", UNSET)

        error = d.pop("Error", UNSET)

        keyfactor_api_models_templates_template_enrollment_regex_response = cls(
            subject_part=subject_part,
            regex=regex,
            error=error,
        )

        keyfactor_api_models_templates_template_enrollment_regex_response.additional_properties = d
        return keyfactor_api_models_templates_template_enrollment_regex_response

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
