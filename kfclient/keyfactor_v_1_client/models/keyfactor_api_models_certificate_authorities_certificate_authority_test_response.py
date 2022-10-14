from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificateAuthoritiesCertificateAuthorityTestResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificateAuthoritiesCertificateAuthorityTestResponse:
    """A DTO for CA tests.

    Attributes:
        success (Union[Unset, bool]): Whether the test succeeded or failed.
        message (Union[Unset, str]): The message returned by the test.
    """

    success: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["Success"] = success
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("Success", UNSET)

        message = d.pop("Message", UNSET)

        keyfactor_api_models_certificate_authorities_certificate_authority_test_response = cls(
            success=success,
            message=message,
        )

        keyfactor_api_models_certificate_authorities_certificate_authority_test_response.additional_properties = d
        return keyfactor_api_models_certificate_authorities_certificate_authority_test_response

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
