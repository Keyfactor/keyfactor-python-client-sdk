from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyfactor_api_models_workflows_condition_configuration_request import (
    KeyfactorApiModelsWorkflowsConditionConfigurationRequest,
)
from ..models.keyfactor_api_models_workflows_definition_step_request_configuration_parameters import (
    KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters,
)
from ..models.keyfactor_api_models_workflows_definition_step_request_outputs import (
    KeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs,
)
from ..models.keyfactor_api_models_workflows_signal_configuration_request import (
    KeyfactorApiModelsWorkflowsSignalConfigurationRequest,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionStepRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionStepRequest:
    """
    Example:
        [{'ExtensionName': 'NOOPStep', 'UniqueName': 'StartNOOP', 'DisplayName': 'Start-NOOP', 'Enabled': True,
            'Signals': [], 'Outputs': {'continue': 'Example Unique Name'}}, {'ExtensionName': '<Extension name>',
            'UniqueName': '<Example Unique Name>', 'DisplayName': '<Display name of step>', 'Enabled': True,
            'ConfigurationParameters': {'Subject': 'Subject Value', 'Message': 'Message Value', 'CyberArkSecret':
            {'Parameters': {'Folder': '<CyberArk Safe Folder>', 'Object': '<CyberArk Secret Object>'}, 'Provider':
            '<Keyfactor PAM Provider ID>'}, 'DelineaSecret': {'Parameters': {'SecretId': '<Delinea Secret ID>'}, 'Provider':
            '<Keyfactor PAM Provider ID>'}}, 'Signals': [], 'Outputs': {'continue': 'EndNOOP'}}, {'ExtensionName':
            'NOOPStep', 'UniqueName': 'EndNOOP', 'DisplayName': 'End-Step', 'Enabled': True, 'Signals': []}]

    Attributes:
        extension_name (Union[Unset, str]):
        unique_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        configuration_parameters (Union[Unset,
            KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters]):
        signals (Union[Unset, List[KeyfactorApiModelsWorkflowsSignalConfigurationRequest]]):
        conditions (Union[Unset, List[KeyfactorApiModelsWorkflowsConditionConfigurationRequest]]):
        outputs (Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs]):
    """

    extension_name: Union[Unset, str] = UNSET
    unique_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    configuration_parameters: Union[
        Unset, KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters
    ] = UNSET
    signals: Union[Unset, List[KeyfactorApiModelsWorkflowsSignalConfigurationRequest]] = UNSET
    conditions: Union[Unset, List[KeyfactorApiModelsWorkflowsConditionConfigurationRequest]] = UNSET
    outputs: Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extension_name = self.extension_name
        unique_name = self.unique_name
        display_name = self.display_name
        enabled = self.enabled
        configuration_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = self.configuration_parameters.to_dict()

        signals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signals, Unset):
            signals = []
            for signals_item_data in self.signals:
                signals_item = signals_item_data.to_dict()

                signals.append(signals_item)

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()

                conditions.append(conditions_item)

        outputs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extension_name is not UNSET:
            field_dict["ExtensionName"] = extension_name
        if unique_name is not UNSET:
            field_dict["UniqueName"] = unique_name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if configuration_parameters is not UNSET:
            field_dict["ConfigurationParameters"] = configuration_parameters
        if signals is not UNSET:
            field_dict["Signals"] = signals
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if outputs is not UNSET:
            field_dict["Outputs"] = outputs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        extension_name = d.pop("ExtensionName", UNSET)

        unique_name = d.pop("UniqueName", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        enabled = d.pop("Enabled", UNSET)

        _configuration_parameters = d.pop("ConfigurationParameters", UNSET)
        configuration_parameters: Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters]
        if isinstance(_configuration_parameters, Unset):
            configuration_parameters = UNSET
        else:
            configuration_parameters = (
                KeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters.from_dict(
                    _configuration_parameters
                )
            )

        signals = []
        _signals = d.pop("Signals", UNSET)
        for signals_item_data in _signals or []:
            signals_item = KeyfactorApiModelsWorkflowsSignalConfigurationRequest.from_dict(signals_item_data)

            signals.append(signals_item)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = KeyfactorApiModelsWorkflowsConditionConfigurationRequest.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        _outputs = d.pop("Outputs", UNSET)
        outputs: Union[Unset, KeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = KeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs.from_dict(_outputs)

        keyfactor_api_models_workflows_definition_step_request = cls(
            extension_name=extension_name,
            unique_name=unique_name,
            display_name=display_name,
            enabled=enabled,
            configuration_parameters=configuration_parameters,
            signals=signals,
            conditions=conditions,
            outputs=outputs,
        )

        keyfactor_api_models_workflows_definition_step_request.additional_properties = d
        return keyfactor_api_models_workflows_definition_step_request

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
