from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateDownloadRequest")


@attr.s(auto_attribs=True)
class ModelsCertificateDownloadRequest:
    """
    Attributes:
        cert_id (Union[Unset, int]):
        serial_number (Union[Unset, str]):
        issuer_dn (Union[Unset, str]):
        thumbprint (Union[Unset, str]):
        include_chain (Union[Unset, bool]):
    """

    cert_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    include_chain: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert_id = self.cert_id
        serial_number = self.serial_number
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        include_chain = self.include_chain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_id is not UNSET:
            field_dict["CertID"] = cert_id
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if include_chain is not UNSET:
            field_dict["IncludeChain"] = include_chain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert_id = d.pop("CertID", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        issuer_dn = d.pop("IssuerDN", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        include_chain = d.pop("IncludeChain", UNSET)

        models_certificate_download_request = cls(
            cert_id=cert_id,
            serial_number=serial_number,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            include_chain=include_chain,
        )

        models_certificate_download_request.additional_properties = d
        return models_certificate_download_request

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
