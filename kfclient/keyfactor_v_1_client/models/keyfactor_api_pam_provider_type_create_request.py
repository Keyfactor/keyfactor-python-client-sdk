from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyfactor_api_pam_provider_type_parameter_create_request import (
    KeyfactorApiPAMProviderTypeParameterCreateRequest,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiPAMProviderTypeCreateRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiPAMProviderTypeCreateRequest:
    """
    Attributes:
        name (str):
        parameters (Union[Unset, List[KeyfactorApiPAMProviderTypeParameterCreateRequest]]):
    """

    name: str
    parameters: Union[Unset, List[KeyfactorApiPAMProviderTypeParameterCreateRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()

                parameters.append(parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
            }
        )
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        parameters = []
        _parameters = d.pop("Parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = KeyfactorApiPAMProviderTypeParameterCreateRequest.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        keyfactor_api_pam_provider_type_create_request = cls(
            name=name,
            parameters=parameters,
        )

        keyfactor_api_pam_provider_type_create_request.additional_properties = d
        return keyfactor_api_pam_provider_type_create_request

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
