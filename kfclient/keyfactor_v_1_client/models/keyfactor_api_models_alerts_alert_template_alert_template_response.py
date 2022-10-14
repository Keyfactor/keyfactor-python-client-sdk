from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, str]):
        forest_root (Union[Unset, str]):
        configuration_tenant (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    forest_root: Union[Unset, str] = UNSET
    configuration_tenant: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        forest_root = self.forest_root
        configuration_tenant = self.configuration_tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if forest_root is not UNSET:
            field_dict["ForestRoot"] = forest_root
        if configuration_tenant is not UNSET:
            field_dict["ConfigurationTenant"] = configuration_tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        forest_root = d.pop("ForestRoot", UNSET)

        configuration_tenant = d.pop("ConfigurationTenant", UNSET)

        keyfactor_api_models_alerts_alert_template_alert_template_response = cls(
            id=id,
            display_name=display_name,
            forest_root=forest_root,
            configuration_tenant=configuration_tenant,
        )

        keyfactor_api_models_alerts_alert_template_alert_template_response.additional_properties = d
        return keyfactor_api_models_alerts_alert_template_alert_template_response

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
