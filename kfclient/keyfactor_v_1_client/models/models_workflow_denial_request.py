from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsWorkflowDenialRequest")


@attr.s(auto_attribs=True)
class ModelsWorkflowDenialRequest:
    """
    Attributes:
        comment (Union[Unset, str]):
        certificate_request_ids (Union[Unset, List[int]]):
    """

    comment: Union[Unset, str] = UNSET
    certificate_request_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comment = self.comment
        certificate_request_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.certificate_request_ids, Unset):
            certificate_request_ids = self.certificate_request_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if certificate_request_ids is not UNSET:
            field_dict["CertificateRequestIds"] = certificate_request_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("Comment", UNSET)

        certificate_request_ids = cast(List[int], d.pop("CertificateRequestIds", UNSET))

        models_workflow_denial_request = cls(
            comment=comment,
            certificate_request_ids=certificate_request_ids,
        )

        models_workflow_denial_request.additional_properties = d
        return models_workflow_denial_request

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