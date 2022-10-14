from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyfactor_api_models_license_license_response_license import (
    KeyfactorApiModelsLicenseLicenseResponseLicense,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsLicenseLicenseResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsLicenseLicenseResponse:
    """
    Attributes:
        keyfactor_version (Union[Unset, str]):
        license_data (Union[Unset, KeyfactorApiModelsLicenseLicenseResponseLicense]):
    """

    keyfactor_version: Union[Unset, str] = UNSET
    license_data: Union[Unset, KeyfactorApiModelsLicenseLicenseResponseLicense] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keyfactor_version = self.keyfactor_version
        license_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_data, Unset):
            license_data = self.license_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyfactor_version is not UNSET:
            field_dict["KeyfactorVersion"] = keyfactor_version
        if license_data is not UNSET:
            field_dict["LicenseData"] = license_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyfactor_version = d.pop("KeyfactorVersion", UNSET)

        _license_data = d.pop("LicenseData", UNSET)
        license_data: Union[Unset, KeyfactorApiModelsLicenseLicenseResponseLicense]
        if isinstance(_license_data, Unset):
            license_data = UNSET
        else:
            license_data = KeyfactorApiModelsLicenseLicenseResponseLicense.from_dict(_license_data)

        keyfactor_api_models_license_license_response = cls(
            keyfactor_version=keyfactor_version,
            license_data=license_data,
        )

        keyfactor_api_models_license_license_response.additional_properties = d
        return keyfactor_api_models_license_license_response

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
