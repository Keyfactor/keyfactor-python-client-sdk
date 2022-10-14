from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.models_template_collection_retrieval_response_allowed_enrollment_types import (
    ModelsTemplateCollectionRetrievalResponseAllowedEnrollmentTypes,
)
from ..models.models_template_collection_retrieval_response_extended_key_usage_model import (
    ModelsTemplateCollectionRetrievalResponseExtendedKeyUsageModel,
)
from ..models.models_template_collection_retrieval_response_key_retention import (
    ModelsTemplateCollectionRetrievalResponseKeyRetention,
)
from ..models.models_template_collection_retrieval_response_template_enrollment_field_model import (
    ModelsTemplateCollectionRetrievalResponseTemplateEnrollmentFieldModel,
)
from ..models.models_template_collection_retrieval_response_template_regex_model import (
    ModelsTemplateCollectionRetrievalResponseTemplateRegexModel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTemplateCollectionRetrievalResponse")


@attr.s(auto_attribs=True)
class ModelsTemplateCollectionRetrievalResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        common_name (Union[Unset, str]):
        template_name (Union[Unset, str]):
        oid (Union[Unset, str]):
        key_size (Union[Unset, str]):
        key_type (Union[Unset, str]):
        forest_root (Union[Unset, str]):
        configuration_tenant (Union[Unset, str]):
        friendly_name (Union[Unset, str]):
        key_retention (Union[Unset, ModelsTemplateCollectionRetrievalResponseKeyRetention]):
        key_retention_days (Union[Unset, int]):
        key_archival (Union[Unset, bool]):
        enrollment_fields (Union[Unset, List[ModelsTemplateCollectionRetrievalResponseTemplateEnrollmentFieldModel]]):
        allowed_enrollment_types (Union[Unset, ModelsTemplateCollectionRetrievalResponseAllowedEnrollmentTypes]):
        template_regexes (Union[Unset, List[ModelsTemplateCollectionRetrievalResponseTemplateRegexModel]]):
        use_allowed_requesters (Union[Unset, bool]):
        allowed_requesters (Union[Unset, List[str]]):
        display_name (Union[Unset, str]):
        requires_approval (Union[Unset, bool]):
        key_usage (Union[Unset, int]):
        extended_key_usages (Union[Unset, List[ModelsTemplateCollectionRetrievalResponseExtendedKeyUsageModel]]):
    """

    id: Union[Unset, int] = UNSET
    common_name: Union[Unset, str] = UNSET
    template_name: Union[Unset, str] = UNSET
    oid: Union[Unset, str] = UNSET
    key_size: Union[Unset, str] = UNSET
    key_type: Union[Unset, str] = UNSET
    forest_root: Union[Unset, str] = UNSET
    configuration_tenant: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    key_retention: Union[Unset, ModelsTemplateCollectionRetrievalResponseKeyRetention] = UNSET
    key_retention_days: Union[Unset, int] = UNSET
    key_archival: Union[Unset, bool] = UNSET
    enrollment_fields: Union[Unset, List[ModelsTemplateCollectionRetrievalResponseTemplateEnrollmentFieldModel]] = UNSET
    allowed_enrollment_types: Union[Unset, ModelsTemplateCollectionRetrievalResponseAllowedEnrollmentTypes] = UNSET
    template_regexes: Union[Unset, List[ModelsTemplateCollectionRetrievalResponseTemplateRegexModel]] = UNSET
    use_allowed_requesters: Union[Unset, bool] = UNSET
    allowed_requesters: Union[Unset, List[str]] = UNSET
    display_name: Union[Unset, str] = UNSET
    requires_approval: Union[Unset, bool] = UNSET
    key_usage: Union[Unset, int] = UNSET
    extended_key_usages: Union[Unset, List[ModelsTemplateCollectionRetrievalResponseExtendedKeyUsageModel]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        common_name = self.common_name
        template_name = self.template_name
        oid = self.oid
        key_size = self.key_size
        key_type = self.key_type
        forest_root = self.forest_root
        configuration_tenant = self.configuration_tenant
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

        allowed_enrollment_types: Union[Unset, int] = UNSET
        if not isinstance(self.allowed_enrollment_types, Unset):
            allowed_enrollment_types = self.allowed_enrollment_types.value

        template_regexes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.template_regexes, Unset):
            template_regexes = []
            for template_regexes_item_data in self.template_regexes:
                template_regexes_item = template_regexes_item_data.to_dict()

                template_regexes.append(template_regexes_item)

        use_allowed_requesters = self.use_allowed_requesters
        allowed_requesters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_requesters, Unset):
            allowed_requesters = self.allowed_requesters

        display_name = self.display_name
        requires_approval = self.requires_approval
        key_usage = self.key_usage
        extended_key_usages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extended_key_usages, Unset):
            extended_key_usages = []
            for extended_key_usages_item_data in self.extended_key_usages:
                extended_key_usages_item = extended_key_usages_item_data.to_dict()

                extended_key_usages.append(extended_key_usages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if common_name is not UNSET:
            field_dict["CommonName"] = common_name
        if template_name is not UNSET:
            field_dict["TemplateName"] = template_name
        if oid is not UNSET:
            field_dict["Oid"] = oid
        if key_size is not UNSET:
            field_dict["KeySize"] = key_size
        if key_type is not UNSET:
            field_dict["KeyType"] = key_type
        if forest_root is not UNSET:
            field_dict["ForestRoot"] = forest_root
        if configuration_tenant is not UNSET:
            field_dict["ConfigurationTenant"] = configuration_tenant
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
        if allowed_enrollment_types is not UNSET:
            field_dict["AllowedEnrollmentTypes"] = allowed_enrollment_types
        if template_regexes is not UNSET:
            field_dict["TemplateRegexes"] = template_regexes
        if use_allowed_requesters is not UNSET:
            field_dict["UseAllowedRequesters"] = use_allowed_requesters
        if allowed_requesters is not UNSET:
            field_dict["AllowedRequesters"] = allowed_requesters
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if requires_approval is not UNSET:
            field_dict["RequiresApproval"] = requires_approval
        if key_usage is not UNSET:
            field_dict["KeyUsage"] = key_usage
        if extended_key_usages is not UNSET:
            field_dict["ExtendedKeyUsages"] = extended_key_usages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        common_name = d.pop("CommonName", UNSET)

        template_name = d.pop("TemplateName", UNSET)

        oid = d.pop("Oid", UNSET)

        key_size = d.pop("KeySize", UNSET)

        key_type = d.pop("KeyType", UNSET)

        forest_root = d.pop("ForestRoot", UNSET)

        configuration_tenant = d.pop("ConfigurationTenant", UNSET)

        friendly_name = d.pop("FriendlyName", UNSET)

        _key_retention = d.pop("KeyRetention", UNSET)
        key_retention: Union[Unset, ModelsTemplateCollectionRetrievalResponseKeyRetention]
        if isinstance(_key_retention, Unset):
            key_retention = UNSET
        else:
            key_retention = ModelsTemplateCollectionRetrievalResponseKeyRetention(_key_retention)

        key_retention_days = d.pop("KeyRetentionDays", UNSET)

        key_archival = d.pop("KeyArchival", UNSET)

        enrollment_fields = []
        _enrollment_fields = d.pop("EnrollmentFields", UNSET)
        for enrollment_fields_item_data in _enrollment_fields or []:
            enrollment_fields_item = ModelsTemplateCollectionRetrievalResponseTemplateEnrollmentFieldModel.from_dict(
                enrollment_fields_item_data
            )

            enrollment_fields.append(enrollment_fields_item)

        _allowed_enrollment_types = d.pop("AllowedEnrollmentTypes", UNSET)
        allowed_enrollment_types: Union[Unset, ModelsTemplateCollectionRetrievalResponseAllowedEnrollmentTypes]
        if isinstance(_allowed_enrollment_types, Unset):
            allowed_enrollment_types = UNSET
        else:
            allowed_enrollment_types = ModelsTemplateCollectionRetrievalResponseAllowedEnrollmentTypes(
                _allowed_enrollment_types
            )

        template_regexes = []
        _template_regexes = d.pop("TemplateRegexes", UNSET)
        for template_regexes_item_data in _template_regexes or []:
            template_regexes_item = ModelsTemplateCollectionRetrievalResponseTemplateRegexModel.from_dict(
                template_regexes_item_data
            )

            template_regexes.append(template_regexes_item)

        use_allowed_requesters = d.pop("UseAllowedRequesters", UNSET)

        allowed_requesters = cast(List[str], d.pop("AllowedRequesters", UNSET))

        display_name = d.pop("DisplayName", UNSET)

        requires_approval = d.pop("RequiresApproval", UNSET)

        key_usage = d.pop("KeyUsage", UNSET)

        extended_key_usages = []
        _extended_key_usages = d.pop("ExtendedKeyUsages", UNSET)
        for extended_key_usages_item_data in _extended_key_usages or []:
            extended_key_usages_item = ModelsTemplateCollectionRetrievalResponseExtendedKeyUsageModel.from_dict(
                extended_key_usages_item_data
            )

            extended_key_usages.append(extended_key_usages_item)

        models_template_collection_retrieval_response = cls(
            id=id,
            common_name=common_name,
            template_name=template_name,
            oid=oid,
            key_size=key_size,
            key_type=key_type,
            forest_root=forest_root,
            configuration_tenant=configuration_tenant,
            friendly_name=friendly_name,
            key_retention=key_retention,
            key_retention_days=key_retention_days,
            key_archival=key_archival,
            enrollment_fields=enrollment_fields,
            allowed_enrollment_types=allowed_enrollment_types,
            template_regexes=template_regexes,
            use_allowed_requesters=use_allowed_requesters,
            allowed_requesters=allowed_requesters,
            display_name=display_name,
            requires_approval=requires_approval,
            key_usage=key_usage,
            extended_key_usages=extended_key_usages,
        )

        models_template_collection_retrieval_response.additional_properties = d
        return models_template_collection_retrieval_response

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
