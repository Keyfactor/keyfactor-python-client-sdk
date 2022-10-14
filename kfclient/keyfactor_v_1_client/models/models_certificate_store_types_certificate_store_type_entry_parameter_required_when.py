from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelsCertificateStoreTypesCertificateStoreTypeEntryParameterRequiredWhen")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreTypesCertificateStoreTypeEntryParameterRequiredWhen:
    """
    Example:
        {'HasPrivateKey': False, 'OnAdd': False, 'OnRemove': False, 'OnReenrollment': False}

    """

    additional_properties: Dict[str, bool] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        models_certificate_store_types_certificate_store_type_entry_parameter_required_when = cls()

        models_certificate_store_types_certificate_store_type_entry_parameter_required_when.additional_properties = d
        return models_certificate_store_types_certificate_store_type_entry_parameter_required_when

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
