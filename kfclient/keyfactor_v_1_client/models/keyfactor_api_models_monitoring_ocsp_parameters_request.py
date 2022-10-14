from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsMonitoringOCSPParametersRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsMonitoringOCSPParametersRequest:
    """
    Example:
        {'CertificateContents': '<Certificate Content>', 'CertificateAuthorityId': 1}

    Attributes:
        certificate_contents (Union[Unset, str]):
        certificate_authority_id (Union[Unset, int]):
        authority_name (Union[Unset, str]):
        authority_name_id (Union[Unset, str]):
        authority_key_id (Union[Unset, str]):
        sample_serial_number (Union[Unset, str]):
    """

    certificate_contents: Union[Unset, str] = UNSET
    certificate_authority_id: Union[Unset, int] = UNSET
    authority_name: Union[Unset, str] = UNSET
    authority_name_id: Union[Unset, str] = UNSET
    authority_key_id: Union[Unset, str] = UNSET
    sample_serial_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_contents = self.certificate_contents
        certificate_authority_id = self.certificate_authority_id
        authority_name = self.authority_name
        authority_name_id = self.authority_name_id
        authority_key_id = self.authority_key_id
        sample_serial_number = self.sample_serial_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_contents is not UNSET:
            field_dict["CertificateContents"] = certificate_contents
        if certificate_authority_id is not UNSET:
            field_dict["CertificateAuthorityId"] = certificate_authority_id
        if authority_name is not UNSET:
            field_dict["AuthorityName"] = authority_name
        if authority_name_id is not UNSET:
            field_dict["AuthorityNameId"] = authority_name_id
        if authority_key_id is not UNSET:
            field_dict["AuthorityKeyId"] = authority_key_id
        if sample_serial_number is not UNSET:
            field_dict["SampleSerialNumber"] = sample_serial_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_contents = d.pop("CertificateContents", UNSET)

        certificate_authority_id = d.pop("CertificateAuthorityId", UNSET)

        authority_name = d.pop("AuthorityName", UNSET)

        authority_name_id = d.pop("AuthorityNameId", UNSET)

        authority_key_id = d.pop("AuthorityKeyId", UNSET)

        sample_serial_number = d.pop("SampleSerialNumber", UNSET)

        keyfactor_api_models_monitoring_ocsp_parameters_request = cls(
            certificate_contents=certificate_contents,
            certificate_authority_id=certificate_authority_id,
            authority_name=authority_name,
            authority_name_id=authority_name_id,
            authority_key_id=authority_key_id,
            sample_serial_number=sample_serial_number,
        )

        keyfactor_api_models_monitoring_ocsp_parameters_request.additional_properties = d
        return keyfactor_api_models_monitoring_ocsp_parameters_request

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
