from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse")


@attr.s(auto_attribs=True)
class KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse:
    """
    Attributes:
        successful_stores (Union[Unset, List[str]]):
        failed_stores (Union[Unset, List[str]]):
    """

    successful_stores: Union[Unset, List[str]] = UNSET
    failed_stores: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        successful_stores: Union[Unset, List[str]] = UNSET
        if not isinstance(self.successful_stores, Unset):
            successful_stores = self.successful_stores

        failed_stores: Union[Unset, List[str]] = UNSET
        if not isinstance(self.failed_stores, Unset):
            failed_stores = self.failed_stores

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if successful_stores is not UNSET:
            field_dict["SuccessfulStores"] = successful_stores
        if failed_stores is not UNSET:
            field_dict["FailedStores"] = failed_stores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        successful_stores = cast(List[str], d.pop("SuccessfulStores", UNSET))

        failed_stores = cast(List[str], d.pop("FailedStores", UNSET))

        keyfactor_api_models_enrollment_enrollment_management_response = cls(
            successful_stores=successful_stores,
            failed_stores=failed_stores,
        )

        keyfactor_api_models_enrollment_enrollment_management_response.additional_properties = d
        return keyfactor_api_models_enrollment_enrollment_management_response

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