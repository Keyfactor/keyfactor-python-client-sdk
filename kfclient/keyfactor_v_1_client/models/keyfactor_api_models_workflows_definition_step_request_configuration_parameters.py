from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.keyfactor_api_models_workflows_definition_step_request_configuration_parameters_additional_property import (
    KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParametersAdditionalProperty,
)

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters:
    """ """

    additional_properties: Dict[
        str, KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParametersAdditionalProperty
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyfactor_api_models_workflows_definition_step_request_configuration_parameters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParametersAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        keyfactor_api_models_workflows_definition_step_request_configuration_parameters.additional_properties = (
            additional_properties
        )
        return keyfactor_api_models_workflows_definition_step_request_configuration_parameters

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParametersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParametersAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
