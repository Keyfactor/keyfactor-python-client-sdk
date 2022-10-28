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

T = TypeVar("T", bound="ModelsTemplateCollectionRetrievalResponseTemplateRegexModel")


@attr.s(auto_attribs=True)
class ModelsTemplateCollectionRetrievalResponseTemplateRegexModel:
    """
    Attributes:
        template_id (Union[Unset, int]):
        subject_part (Union[Unset, str]):
        regex (Union[Unset, str]):
        error (Union[Unset, str]):
    """

    template_id: Union[Unset, int] = UNSET
    subject_part: Union[Unset, str] = UNSET
    regex: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_id = self.template_id
        subject_part = self.subject_part
        regex = self.regex
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["TemplateId"] = template_id
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
        template_id = d.pop("TemplateId", UNSET)

        subject_part = d.pop("SubjectPart", UNSET)

        regex = d.pop("Regex", UNSET)

        error = d.pop("Error", UNSET)

        models_template_collection_retrieval_response_template_regex_model = cls(
            template_id=template_id,
            subject_part=subject_part,
            regex=regex,
            error=error,
        )

        models_template_collection_retrieval_response_template_regex_model.additional_properties = d
        return models_template_collection_retrieval_response_template_regex_model

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
