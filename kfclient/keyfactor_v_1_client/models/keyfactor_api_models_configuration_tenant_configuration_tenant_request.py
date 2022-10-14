from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsConfigurationTenantConfigurationTenantRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsConfigurationTenantConfigurationTenantRequest:
    """
    Attributes:
        configuration_tenant (Union[Unset, str]):
    """

    configuration_tenant: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        configuration_tenant = self.configuration_tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_tenant is not UNSET:
            field_dict["ConfigurationTenant"] = configuration_tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        configuration_tenant = d.pop("ConfigurationTenant", UNSET)

        keyfactor_api_models_configuration_tenant_configuration_tenant_request = cls(
            configuration_tenant=configuration_tenant,
        )

        keyfactor_api_models_configuration_tenant_configuration_tenant_request.additional_properties = d
        return keyfactor_api_models_configuration_tenant_configuration_tenant_request

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
