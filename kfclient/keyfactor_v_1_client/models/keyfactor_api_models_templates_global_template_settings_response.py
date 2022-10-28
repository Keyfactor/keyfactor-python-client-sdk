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

from ..models.keyfactor_api_models_templates_global_template_default_response import (
    KeyfactorApiModelsTemplatesGlobalTemplateDefaultResponse,
)
from ..models.keyfactor_api_models_templates_global_template_policy_response import (
    KeyfactorApiModelsTemplatesGlobalTemplatePolicyResponse,
)
from ..models.keyfactor_api_models_templates_global_template_regex_response import (
    KeyfactorApiModelsTemplatesGlobalTemplateRegexResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsTemplatesGlobalTemplateSettingsResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsTemplatesGlobalTemplateSettingsResponse:
    """
    Attributes:
        template_regexes (Union[Unset, List[KeyfactorApiModelsTemplatesGlobalTemplateRegexResponse]]): The regular
            expressions to use for validation during enrollment.
        template_defaults (Union[Unset, List[KeyfactorApiModelsTemplatesGlobalTemplateDefaultResponse]]): The default
            values to use during enrollment.
        template_policy (Union[Unset, KeyfactorApiModelsTemplatesGlobalTemplatePolicyResponse]):
    """

    template_regexes: Union[Unset, List[KeyfactorApiModelsTemplatesGlobalTemplateRegexResponse]] = UNSET
    template_defaults: Union[Unset, List[KeyfactorApiModelsTemplatesGlobalTemplateDefaultResponse]] = UNSET
    template_policy: Union[Unset, KeyfactorApiModelsTemplatesGlobalTemplatePolicyResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_regexes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.template_regexes, Unset):
            template_regexes = []
            for template_regexes_item_data in self.template_regexes:
                template_regexes_item = template_regexes_item_data.to_dict()

                template_regexes.append(template_regexes_item)

        template_defaults: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.template_defaults, Unset):
            template_defaults = []
            for template_defaults_item_data in self.template_defaults:
                template_defaults_item = template_defaults_item_data.to_dict()

                template_defaults.append(template_defaults_item)

        template_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template_policy, Unset):
            template_policy = self.template_policy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_regexes is not UNSET:
            field_dict["TemplateRegexes"] = template_regexes
        if template_defaults is not UNSET:
            field_dict["TemplateDefaults"] = template_defaults
        if template_policy is not UNSET:
            field_dict["TemplatePolicy"] = template_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template_regexes = []
        _template_regexes = d.pop("TemplateRegexes", UNSET)
        for template_regexes_item_data in _template_regexes or []:
            template_regexes_item = KeyfactorApiModelsTemplatesGlobalTemplateRegexResponse.from_dict(
                template_regexes_item_data
            )

            template_regexes.append(template_regexes_item)

        template_defaults = []
        _template_defaults = d.pop("TemplateDefaults", UNSET)
        for template_defaults_item_data in _template_defaults or []:
            template_defaults_item = KeyfactorApiModelsTemplatesGlobalTemplateDefaultResponse.from_dict(
                template_defaults_item_data
            )

            template_defaults.append(template_defaults_item)

        _template_policy = d.pop("TemplatePolicy", UNSET)
        template_policy: Union[Unset, KeyfactorApiModelsTemplatesGlobalTemplatePolicyResponse]
        if isinstance(_template_policy, Unset):
            template_policy = UNSET
        else:
            template_policy = KeyfactorApiModelsTemplatesGlobalTemplatePolicyResponse.from_dict(_template_policy)

        keyfactor_api_models_templates_global_template_settings_response = cls(
            template_regexes=template_regexes,
            template_defaults=template_defaults,
            template_policy=template_policy,
        )

        keyfactor_api_models_templates_global_template_settings_response.additional_properties = d
        return keyfactor_api_models_templates_global_template_settings_response

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
