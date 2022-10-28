# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.keyfactor_api_models_templates_global_template_default_request import (
    KeyfactorApiModelsTemplatesGlobalTemplateDefaultRequest,
)
from ..models.keyfactor_api_models_templates_global_template_policy_request import (
    KeyfactorApiModelsTemplatesGlobalTemplatePolicyRequest,
)
from ..models.keyfactor_api_models_templates_global_template_regex_request import (
    KeyfactorApiModelsTemplatesGlobalTemplateRegexRequest,
)

T = TypeVar("T", bound="KeyfactorApiModelsTemplatesGlobalTemplateSettingsRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsTemplatesGlobalTemplateSettingsRequest:
    """
    Attributes:
        template_regexes (List[KeyfactorApiModelsTemplatesGlobalTemplateRegexRequest]): The regular expressions to use
            for validation during enrollment.
        template_defaults (List[KeyfactorApiModelsTemplatesGlobalTemplateDefaultRequest]): The default values to use
            during enrollment.
        template_policy (KeyfactorApiModelsTemplatesGlobalTemplatePolicyRequest):
    """

    template_regexes: List[KeyfactorApiModelsTemplatesGlobalTemplateRegexRequest]
    template_defaults: List[KeyfactorApiModelsTemplatesGlobalTemplateDefaultRequest]
    template_policy: KeyfactorApiModelsTemplatesGlobalTemplatePolicyRequest
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_regexes = []
        for template_regexes_item_data in self.template_regexes:
            template_regexes_item = template_regexes_item_data.to_dict()

            template_regexes.append(template_regexes_item)

        template_defaults = []
        for template_defaults_item_data in self.template_defaults:
            template_defaults_item = template_defaults_item_data.to_dict()

            template_defaults.append(template_defaults_item)

        template_policy = self.template_policy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TemplateRegexes": template_regexes,
                "TemplateDefaults": template_defaults,
                "TemplatePolicy": template_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template_regexes = []
        _template_regexes = d.pop("TemplateRegexes")
        for template_regexes_item_data in _template_regexes:
            template_regexes_item = KeyfactorApiModelsTemplatesGlobalTemplateRegexRequest.from_dict(
                template_regexes_item_data
            )

            template_regexes.append(template_regexes_item)

        template_defaults = []
        _template_defaults = d.pop("TemplateDefaults")
        for template_defaults_item_data in _template_defaults:
            template_defaults_item = KeyfactorApiModelsTemplatesGlobalTemplateDefaultRequest.from_dict(
                template_defaults_item_data
            )

            template_defaults.append(template_defaults_item)

        template_policy = KeyfactorApiModelsTemplatesGlobalTemplatePolicyRequest.from_dict(d.pop("TemplatePolicy"))

        keyfactor_api_models_templates_global_template_settings_request = cls(
            template_regexes=template_regexes,
            template_defaults=template_defaults,
            template_policy=template_policy,
        )

        keyfactor_api_models_templates_global_template_settings_request.additional_properties = d
        return keyfactor_api_models_templates_global_template_settings_request

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
