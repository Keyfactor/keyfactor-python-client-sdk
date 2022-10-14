from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsRevocationSuspendedRevocationResponse")


@attr.s(auto_attribs=True)
class ModelsRevocationSuspendedRevocationResponse:
    """
    Attributes:
        cert_id (Union[Unset, int]):
        workflow_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        message (Union[Unset, str]):
    """

    cert_id: Union[Unset, int] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert_id = self.cert_id
        workflow_id = self.workflow_id
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_id is not UNSET:
            field_dict["CertId"] = cert_id
        if workflow_id is not UNSET:
            field_dict["WorkflowId"] = workflow_id
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert_id = d.pop("CertId", UNSET)

        workflow_id = d.pop("WorkflowId", UNSET)

        message = d.pop("Message", UNSET)

        models_revocation_suspended_revocation_response = cls(
            cert_id=cert_id,
            workflow_id=workflow_id,
            message=message,
        )

        models_revocation_suspended_revocation_response.additional_properties = d
        return models_revocation_suspended_revocation_response

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
