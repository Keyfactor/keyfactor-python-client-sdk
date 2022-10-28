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

from ..models.keyfactor_api_models_alerts_pending_pending_alert_response import (
    KeyfactorApiModelsAlertsPendingPendingAlertResponse,
)
from ..models.keyfactor_api_models_alerts_pending_pending_alert_test_response_alert_build_result import (
    KeyfactorApiModelsAlertsPendingPendingAlertTestResponseAlertBuildResult,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsPendingPendingAlertTestResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsPendingPendingAlertTestResponse:
    """
    Attributes:
        pending_alerts (Union[Unset, List[KeyfactorApiModelsAlertsPendingPendingAlertResponse]]):
        alert_build_result (Union[Unset, KeyfactorApiModelsAlertsPendingPendingAlertTestResponseAlertBuildResult]):
    """

    pending_alerts: Union[Unset, List[KeyfactorApiModelsAlertsPendingPendingAlertResponse]] = UNSET
    alert_build_result: Union[Unset, KeyfactorApiModelsAlertsPendingPendingAlertTestResponseAlertBuildResult] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pending_alerts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pending_alerts, Unset):
            pending_alerts = []
            for pending_alerts_item_data in self.pending_alerts:
                pending_alerts_item = pending_alerts_item_data.to_dict()

                pending_alerts.append(pending_alerts_item)

        alert_build_result: Union[Unset, int] = UNSET
        if not isinstance(self.alert_build_result, Unset):
            alert_build_result = self.alert_build_result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pending_alerts is not UNSET:
            field_dict["PendingAlerts"] = pending_alerts
        if alert_build_result is not UNSET:
            field_dict["AlertBuildResult"] = alert_build_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pending_alerts = []
        _pending_alerts = d.pop("PendingAlerts", UNSET)
        for pending_alerts_item_data in _pending_alerts or []:
            pending_alerts_item = KeyfactorApiModelsAlertsPendingPendingAlertResponse.from_dict(
                pending_alerts_item_data
            )

            pending_alerts.append(pending_alerts_item)

        _alert_build_result = d.pop("AlertBuildResult", UNSET)
        alert_build_result: Union[Unset, KeyfactorApiModelsAlertsPendingPendingAlertTestResponseAlertBuildResult]
        if isinstance(_alert_build_result, Unset):
            alert_build_result = UNSET
        else:
            alert_build_result = KeyfactorApiModelsAlertsPendingPendingAlertTestResponseAlertBuildResult(
                _alert_build_result
            )

        keyfactor_api_models_alerts_pending_pending_alert_test_response = cls(
            pending_alerts=pending_alerts,
            alert_build_result=alert_build_result,
        )

        keyfactor_api_models_alerts_pending_pending_alert_test_response.additional_properties = d
        return keyfactor_api_models_alerts_pending_pending_alert_test_response

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
