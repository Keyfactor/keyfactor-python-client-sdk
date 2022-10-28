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
from ..models.models_extended_key_usage import ModelsExtendedKeyUsage
from ..models.models_template_enrollment_field import ModelsTemplateEnrollmentField
from ..models.models_template_metadata_field import ModelsTemplateMetadataField
from ..models.models_template_regex import ModelsTemplateRegex
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoreModelsEnrollmentEnrollmentTemplate")


@attr.s(auto_attribs=True)
class CoreModelsEnrollmentEnrollmentTemplate:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        forest (Union[Unset, str]):
        key_size (Union[Unset, str]):
        key_type (Union[Unset, str]):
        requires_approval (Union[Unset, bool]):
        rfc_enforcement (Union[Unset, bool]):
        c_as (Union[Unset, List[CoreModelsEnrollmentEnrollmentCA]]):
        enrollment_fields (Union[Unset, List[ModelsTemplateEnrollmentField]]):
        metadata_fields (Union[Unset, List[ModelsTemplateMetadataField]]):
        regexes (Union[Unset, List[ModelsTemplateRegex]]):
        extended_key_usages (Union[Unset, List[ModelsExtendedKeyUsage]]):
        curve (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    forest: Union[Unset, str] = UNSET
    key_size: Union[Unset, str] = UNSET
    key_type: Union[Unset, str] = UNSET
    requires_approval: Union[Unset, bool] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    c_as: Union[Unset, List[CoreModelsEnrollmentEnrollmentCA]] = UNSET
    enrollment_fields: Union[Unset, List[ModelsTemplateEnrollmentField]] = UNSET
    metadata_fields: Union[Unset, List[ModelsTemplateMetadataField]] = UNSET
    regexes: Union[Unset, List[ModelsTemplateRegex]] = UNSET
    extended_key_usages: Union[Unset, List[ModelsExtendedKeyUsage]] = UNSET
    curve: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        forest = self.forest
        key_size = self.key_size
        key_type = self.key_type
        requires_approval = self.requires_approval
        rfc_enforcement = self.rfc_enforcement
        c_as: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.c_as, Unset):
            c_as = []
            for c_as_item_data in self.c_as:
                c_as_item = c_as_item_data.to_dict()

                c_as.append(c_as_item)

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

        regexes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regexes, Unset):
            regexes = []
            for regexes_item_data in self.regexes:
                regexes_item = regexes_item_data.to_dict()

                regexes.append(regexes_item)

        extended_key_usages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extended_key_usages, Unset):
            extended_key_usages = []
            for extended_key_usages_item_data in self.extended_key_usages:
                extended_key_usages_item = extended_key_usages_item_data.to_dict()

                extended_key_usages.append(extended_key_usages_item)

        curve = self.curve

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if forest is not UNSET:
            field_dict["Forest"] = forest
        if key_size is not UNSET:
            field_dict["KeySize"] = key_size
        if key_type is not UNSET:
            field_dict["KeyType"] = key_type
        if requires_approval is not UNSET:
            field_dict["RequiresApproval"] = requires_approval
        if rfc_enforcement is not UNSET:
            field_dict["RFCEnforcement"] = rfc_enforcement
        if c_as is not UNSET:
            field_dict["CAs"] = c_as
        if enrollment_fields is not UNSET:
            field_dict["EnrollmentFields"] = enrollment_fields
        if metadata_fields is not UNSET:
            field_dict["MetadataFields"] = metadata_fields
        if regexes is not UNSET:
            field_dict["Regexes"] = regexes
        if extended_key_usages is not UNSET:
            field_dict["ExtendedKeyUsages"] = extended_key_usages
        if curve is not UNSET:
            field_dict["Curve"] = curve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        forest = d.pop("Forest", UNSET)

        key_size = d.pop("KeySize", UNSET)

        key_type = d.pop("KeyType", UNSET)

        requires_approval = d.pop("RequiresApproval", UNSET)

        rfc_enforcement = d.pop("RFCEnforcement", UNSET)

        c_as = []
        _c_as = d.pop("CAs", UNSET)
        for c_as_item_data in _c_as or []:
            c_as_item = CoreModelsEnrollmentEnrollmentCA.from_dict(c_as_item_data)

            c_as.append(c_as_item)

        enrollment_fields = []
        _enrollment_fields = d.pop("EnrollmentFields", UNSET)
        for enrollment_fields_item_data in _enrollment_fields or []:
            enrollment_fields_item = ModelsTemplateEnrollmentField.from_dict(enrollment_fields_item_data)

            enrollment_fields.append(enrollment_fields_item)

        metadata_fields = []
        _metadata_fields = d.pop("MetadataFields", UNSET)
        for metadata_fields_item_data in _metadata_fields or []:
            metadata_fields_item = ModelsTemplateMetadataField.from_dict(metadata_fields_item_data)

            metadata_fields.append(metadata_fields_item)

        regexes = []
        _regexes = d.pop("Regexes", UNSET)
        for regexes_item_data in _regexes or []:
            regexes_item = ModelsTemplateRegex.from_dict(regexes_item_data)

            regexes.append(regexes_item)

        extended_key_usages = []
        _extended_key_usages = d.pop("ExtendedKeyUsages", UNSET)
        for extended_key_usages_item_data in _extended_key_usages or []:
            extended_key_usages_item = ModelsExtendedKeyUsage.from_dict(extended_key_usages_item_data)

            extended_key_usages.append(extended_key_usages_item)

        curve = d.pop("Curve", UNSET)

        core_models_enrollment_enrollment_template = cls(
            id=id,
            name=name,
            display_name=display_name,
            forest=forest,
            key_size=key_size,
            key_type=key_type,
            requires_approval=requires_approval,
            rfc_enforcement=rfc_enforcement,
            c_as=c_as,
            enrollment_fields=enrollment_fields,
            metadata_fields=metadata_fields,
            regexes=regexes,
            extended_key_usages=extended_key_usages,
            curve=curve,
        )

        core_models_enrollment_enrollment_template.additional_properties = d
        return core_models_enrollment_enrollment_template

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
