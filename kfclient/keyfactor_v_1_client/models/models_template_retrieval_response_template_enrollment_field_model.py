from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.models_template_retrieval_response_template_enrollment_field_model_data_type import (
    ModelsTemplateRetrievalResponseTemplateEnrollmentFieldModelDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTemplateRetrievalResponseTemplateEnrollmentFieldModel")


@attr.s(auto_attribs=True)
class ModelsTemplateRetrievalResponseTemplateEnrollmentFieldModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        options (Union[Unset, List[str]]):
        data_type (Union[Unset, ModelsTemplateRetrievalResponseTemplateEnrollmentFieldModelDataType]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    options: Union[Unset, List[str]] = UNSET
    data_type: Union[Unset, ModelsTemplateRetrievalResponseTemplateEnrollmentFieldModelDataType] = UNSET
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
        data_type: Union[Unset, ModelsTemplateRetrievalResponseTemplateEnrollmentFieldModelDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = ModelsTemplateRetrievalResponseTemplateEnrollmentFieldModelDataType(_data_type)

        models_template_retrieval_response_template_enrollment_field_model = cls(
            id=id,
            name=name,
            options=options,
            data_type=data_type,
        )

        models_template_retrieval_response_template_enrollment_field_model.additional_properties = d
        return models_template_retrieval_response_template_enrollment_field_model

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
