# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response import (
    KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse,
)
from ..models.keyfactor_api_models_alerts_key_rotation_key_rotation_alert_test_response_alert_build_result import (
    KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponseAlertBuildResult,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponse:
    """
    Attributes:
        key_rotation_alerts (Union[Unset, List[KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse]]):
        alert_build_result (Union[Unset,
            KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponseAlertBuildResult]):
    """

    key_rotation_alerts: Union[Unset, List[KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse]] = UNSET
    alert_build_result: Union[
        Unset, KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponseAlertBuildResult
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_rotation_alerts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.key_rotation_alerts, Unset):
            key_rotation_alerts = []
            for key_rotation_alerts_item_data in self.key_rotation_alerts:
                key_rotation_alerts_item = key_rotation_alerts_item_data.to_dict()

                key_rotation_alerts.append(key_rotation_alerts_item)

        alert_build_result: Union[Unset, int] = UNSET
        if not isinstance(self.alert_build_result, Unset):
            alert_build_result = self.alert_build_result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_rotation_alerts is not UNSET:
            field_dict["KeyRotationAlerts"] = key_rotation_alerts
        if alert_build_result is not UNSET:
            field_dict["AlertBuildResult"] = alert_build_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_rotation_alerts = []
        _key_rotation_alerts = d.pop("KeyRotationAlerts", UNSET)
        for key_rotation_alerts_item_data in _key_rotation_alerts or []:
            key_rotation_alerts_item = KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse.from_dict(
                key_rotation_alerts_item_data
            )

            key_rotation_alerts.append(key_rotation_alerts_item)

        _alert_build_result = d.pop("AlertBuildResult", UNSET)
        alert_build_result: Union[
            Unset, KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponseAlertBuildResult
        ]
        if isinstance(_alert_build_result, Unset):
            alert_build_result = UNSET
        else:
            alert_build_result = KeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponseAlertBuildResult(
                _alert_build_result
            )

        keyfactor_api_models_alerts_key_rotation_key_rotation_alert_test_response = cls(
            key_rotation_alerts=key_rotation_alerts,
            alert_build_result=alert_build_result,
        )

        keyfactor_api_models_alerts_key_rotation_key_rotation_alert_test_response.additional_properties = d
        return keyfactor_api_models_alerts_key_rotation_key_rotation_alert_test_response

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
