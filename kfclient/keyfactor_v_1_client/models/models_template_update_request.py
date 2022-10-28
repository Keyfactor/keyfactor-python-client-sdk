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

from ..models.models_template_update_request_allowed_enrollment_types import (
    ModelsTemplateUpdateRequestAllowedEnrollmentTypes,
)
from ..models.models_template_update_request_key_retention import ModelsTemplateUpdateRequestKeyRetention
from ..models.models_template_update_request_template_default_model import (
    ModelsTemplateUpdateRequestTemplateDefaultModel,
)
from ..models.models_template_update_request_template_enrollment_field_model import (
    ModelsTemplateUpdateRequestTemplateEnrollmentFieldModel,
)
from ..models.models_template_update_request_template_metadata_field_model import (
    ModelsTemplateUpdateRequestTemplateMetadataFieldModel,
)
from ..models.models_template_update_request_template_policy_model import ModelsTemplateUpdateRequestTemplatePolicyModel
from ..models.models_template_update_request_template_regex_model import ModelsTemplateUpdateRequestTemplateRegexModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTemplateUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsTemplateUpdateRequest:
    """
    Attributes:
        id (Union[Unset, int]):
        key_size (Union[Unset, str]):
        key_type (Union[Unset, str]):
        friendly_name (Union[Unset, str]):
        key_retention (Union[Unset, ModelsTemplateUpdateRequestKeyRetention]):
        key_retention_days (Union[Unset, int]):
        key_archival (Union[Unset, bool]):
        enrollment_fields (Union[Unset, List[ModelsTemplateUpdateRequestTemplateEnrollmentFieldModel]]):
        metadata_fields (Union[Unset, List[ModelsTemplateUpdateRequestTemplateMetadataFieldModel]]):
        allowed_enrollment_types (Union[Unset, ModelsTemplateUpdateRequestAllowedEnrollmentTypes]):
        template_regexes (Union[Unset, List[ModelsTemplateUpdateRequestTemplateRegexModel]]):
        template_defaults (Union[Unset, List[ModelsTemplateUpdateRequestTemplateDefaultModel]]):
        template_policy (Union[Unset, ModelsTemplateUpdateRequestTemplatePolicyModel]):
        use_allowed_requesters (Union[Unset, bool]):
        allowed_requesters (Union[Unset, List[str]]):
        requires_approval (Union[Unset, bool]):
        key_usage (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    key_size: Union[Unset, str] = UNSET
    key_type: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    key_retention: Union[Unset, ModelsTemplateUpdateRequestKeyRetention] = UNSET
    key_retention_days: Union[Unset, int] = UNSET
    key_archival: Union[Unset, bool] = UNSET
    enrollment_fields: Union[Unset, List[ModelsTemplateUpdateRequestTemplateEnrollmentFieldModel]] = UNSET
    metadata_fields: Union[Unset, List[ModelsTemplateUpdateRequestTemplateMetadataFieldModel]] = UNSET
    allowed_enrollment_types: Union[Unset, ModelsTemplateUpdateRequestAllowedEnrollmentTypes] = UNSET
    template_regexes: Union[Unset, List[ModelsTemplateUpdateRequestTemplateRegexModel]] = UNSET
    template_defaults: Union[Unset, List[ModelsTemplateUpdateRequestTemplateDefaultModel]] = UNSET
    template_policy: Union[Unset, ModelsTemplateUpdateRequestTemplatePolicyModel] = UNSET
    use_allowed_requesters: Union[Unset, bool] = UNSET
    allowed_requesters: Union[Unset, List[str]] = UNSET
    requires_approval: Union[Unset, bool] = UNSET
    key_usage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key_size = self.key_size
        key_type = self.key_type
        friendly_name = self.friendly_name
        key_retention: Union[Unset, int] = UNSET
        if not isinstance(self.key_retention, Unset):
            key_retention = self.key_retention.value

        key_retention_days = self.key_retention_days
        key_archival = self.key_archival
        enrollment_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enrollment_fields, Unset):
            enrollment_fields = []
            for enrollment_fields_item_data in self.enrollment_fields:
                enrollment_fields_item = enrollment_fields_item_data.to_dict()

                enrollment_fields.append(enrollment_fields_item)

        metadata_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_fields, Unset):
            metadata_fields = []
            for metadata_fields_item_data in self.metadata_fields:
                metadata_fields_item = metadata_fields_item_data.to_dict()

                metadata_fields.append(metadata_fields_item)

        allowed_enrollment_types: Union[Unset, int] = UNSET
        if not isinstance(self.allowed_enrollment_types, Unset):
            allowed_enrollment_types = self.allowed_enrollment_types.value

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

        use_allowed_requesters = self.use_allowed_requesters
        allowed_requesters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_requesters, Unset):
            allowed_requesters = self.allowed_requesters

        requires_approval = self.requires_approval
        key_usage = self.key_usage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if key_size is not UNSET:
            field_dict["KeySize"] = key_size
        if key_type is not UNSET:
            field_dict["KeyType"] = key_type
        if friendly_name is not UNSET:
            field_dict["FriendlyName"] = friendly_name
        if key_retention is not UNSET:
            field_dict["KeyRetention"] = key_retention
        if key_retention_days is not UNSET:
            field_dict["KeyRetentionDays"] = key_retention_days
        if key_archival is not UNSET:
            field_dict["KeyArchival"] = key_archival
        if enrollment_fields is not UNSET:
            field_dict["EnrollmentFields"] = enrollment_fields
        if metadata_fields is not UNSET:
            field_dict["MetadataFields"] = metadata_fields
        if allowed_enrollment_types is not UNSET:
            field_dict["AllowedEnrollmentTypes"] = allowed_enrollment_types
        if template_regexes is not UNSET:
            field_dict["TemplateRegexes"] = template_regexes
        if template_defaults is not UNSET:
            field_dict["TemplateDefaults"] = template_defaults
        if template_policy is not UNSET:
            field_dict["TemplatePolicy"] = template_policy
        if use_allowed_requesters is not UNSET:
            field_dict["UseAllowedRequesters"] = use_allowed_requesters
        if allowed_requesters is not UNSET:
            field_dict["AllowedRequesters"] = allowed_requesters
        if requires_approval is not UNSET:
            field_dict["RequiresApproval"] = requires_approval
        if key_usage is not UNSET:
            field_dict["KeyUsage"] = key_usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        key_size = d.pop("KeySize", UNSET)

        key_type = d.pop("KeyType", UNSET)

        friendly_name = d.pop("FriendlyName", UNSET)

        _key_retention = d.pop("KeyRetention", UNSET)
        key_retention: Union[Unset, ModelsTemplateUpdateRequestKeyRetention]
        if isinstance(_key_retention, Unset):
            key_retention = UNSET
        else:
            key_retention = ModelsTemplateUpdateRequestKeyRetention(_key_retention)

        key_retention_days = d.pop("KeyRetentionDays", UNSET)

        key_archival = d.pop("KeyArchival", UNSET)

        enrollment_fields = []
        _enrollment_fields = d.pop("EnrollmentFields", UNSET)
        for enrollment_fields_item_data in _enrollment_fields or []:
            enrollment_fields_item = ModelsTemplateUpdateRequestTemplateEnrollmentFieldModel.from_dict(
                enrollment_fields_item_data
            )

            enrollment_fields.append(enrollment_fields_item)

        metadata_fields = []
        _metadata_fields = d.pop("MetadataFields", UNSET)
        for metadata_fields_item_data in _metadata_fields or []:
            metadata_fields_item = ModelsTemplateUpdateRequestTemplateMetadataFieldModel.from_dict(
                metadata_fields_item_data
            )

            metadata_fields.append(metadata_fields_item)

        _allowed_enrollment_types = d.pop("AllowedEnrollmentTypes", UNSET)
        allowed_enrollment_types: Union[Unset, ModelsTemplateUpdateRequestAllowedEnrollmentTypes]
        if isinstance(_allowed_enrollment_types, Unset):
            allowed_enrollment_types = UNSET
        else:
            allowed_enrollment_types = ModelsTemplateUpdateRequestAllowedEnrollmentTypes(_allowed_enrollment_types)

        template_regexes = []
        _template_regexes = d.pop("TemplateRegexes", UNSET)
        for template_regexes_item_data in _template_regexes or []:
            template_regexes_item = ModelsTemplateUpdateRequestTemplateRegexModel.from_dict(template_regexes_item_data)

            template_regexes.append(template_regexes_item)

        template_defaults = []
        _template_defaults = d.pop("TemplateDefaults", UNSET)
        for template_defaults_item_data in _template_defaults or []:
            template_defaults_item = ModelsTemplateUpdateRequestTemplateDefaultModel.from_dict(
                template_defaults_item_data
            )

            template_defaults.append(template_defaults_item)

        _template_policy = d.pop("TemplatePolicy", UNSET)
        template_policy: Union[Unset, ModelsTemplateUpdateRequestTemplatePolicyModel]
        if isinstance(_template_policy, Unset):
            template_policy = UNSET
        else:
            template_policy = ModelsTemplateUpdateRequestTemplatePolicyModel.from_dict(_template_policy)

        use_allowed_requesters = d.pop("UseAllowedRequesters", UNSET)

        allowed_requesters = cast(List[str], d.pop("AllowedRequesters", UNSET))

        requires_approval = d.pop("RequiresApproval", UNSET)

        key_usage = d.pop("KeyUsage", UNSET)

        models_template_update_request = cls(
            id=id,
            key_size=key_size,
            key_type=key_type,
            friendly_name=friendly_name,
            key_retention=key_retention,
            key_retention_days=key_retention_days,
            key_archival=key_archival,
            enrollment_fields=enrollment_fields,
            metadata_fields=metadata_fields,
            allowed_enrollment_types=allowed_enrollment_types,
            template_regexes=template_regexes,
            template_defaults=template_defaults,
            template_policy=template_policy,
            use_allowed_requesters=use_allowed_requesters,
            allowed_requesters=allowed_requesters,
            requires_approval=requires_approval,
            key_usage=key_usage,
        )

        models_template_update_request.additional_properties = d
        return models_template_update_request

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
