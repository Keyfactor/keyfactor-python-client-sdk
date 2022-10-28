import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsEnrollmentRenewalRequest")


@attr.s(auto_attribs=True)
class ModelsEnrollmentRenewalRequest:
    """
    Example:
        {'CertificateId': 0, 'Thumbprint': '<hex thumbprint>', 'CertificateAuthority': '<host>\\<logical>', 'Template':
            '<template name>', 'Timestamp': datetime.datetime(2022, 9, 22, 14, 9, 16, 734610,
            tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))}

    Attributes:
        certificate_id (Union[Unset, int]):
        thumbprint (Union[Unset, str]):
        certificate_authority (Union[Unset, str]):
        template (Union[Unset, str]):
        timestamp (Union[Unset, datetime.datetime]):
    """

    certificate_id: Union[Unset, int] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    certificate_authority: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_id = self.certificate_id
        thumbprint = self.thumbprint
        certificate_authority = self.certificate_authority
        template = self.template
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_id is not UNSET:
            field_dict["CertificateId"] = certificate_id
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if certificate_authority is not UNSET:
            field_dict["CertificateAuthority"] = certificate_authority
        if template is not UNSET:
            field_dict["Template"] = template
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_id = d.pop("CertificateId", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        certificate_authority = d.pop("CertificateAuthority", UNSET)

        template = d.pop("Template", UNSET)

        _timestamp = d.pop("Timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        models_enrollment_renewal_request = cls(
            certificate_id=certificate_id,
            thumbprint=thumbprint,
            certificate_authority=certificate_authority,
            template=template,
            timestamp=timestamp,
        )

        models_enrollment_renewal_request.additional_properties = d
        return models_enrollment_renewal_request

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