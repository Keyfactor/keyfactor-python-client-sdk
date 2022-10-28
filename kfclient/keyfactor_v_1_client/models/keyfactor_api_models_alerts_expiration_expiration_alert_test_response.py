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

from ..models.keyfactor_api_models_alerts_expiration_expiration_alert_response import (
    KeyfactorApiModelsAlertsExpirationExpirationAlertResponse,
)
from ..models.keyfactor_api_models_alerts_expiration_expiration_alert_test_response_alert_build_result import (
    KeyfactorApiModelsAlertsExpirationExpirationAlertTestResponseAlertBuildResult,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsExpirationExpirationAlertTestResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsExpirationExpirationAlertTestResponse:
    """
    Attributes:
        expiration_alerts (Union[Unset, List[KeyfactorApiModelsAlertsExpirationExpirationAlertResponse]]):
        alert_build_result (Union[Unset,
            KeyfactorApiModelsAlertsExpirationExpirationAlertTestResponseAlertBuildResult]):
    """

    expiration_alerts: Union[Unset, List[KeyfactorApiModelsAlertsExpirationExpirationAlertResponse]] = UNSET
    alert_build_result: Union[
        Unset, KeyfactorApiModelsAlertsExpirationExpirationAlertTestResponseAlertBuildResult
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expiration_alerts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.expiration_alerts, Unset):
            expiration_alerts = []
            for expiration_alerts_item_data in self.expiration_alerts:
                expiration_alerts_item = expiration_alerts_item_data.to_dict()

                expiration_alerts.append(expiration_alerts_item)

        alert_build_result: Union[Unset, int] = UNSET
        if not isinstance(self.alert_build_result, Unset):
            alert_build_result = self.alert_build_result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiration_alerts is not UNSET:
            field_dict["ExpirationAlerts"] = expiration_alerts
        if alert_build_result is not UNSET:
            field_dict["AlertBuildResult"] = alert_build_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expiration_alerts = []
        _expiration_alerts = d.pop("ExpirationAlerts", UNSET)
        for expiration_alerts_item_data in _expiration_alerts or []:
            expiration_alerts_item = KeyfactorApiModelsAlertsExpirationExpirationAlertResponse.from_dict(
                expiration_alerts_item_data
            )

            expiration_alerts.append(expiration_alerts_item)

        _alert_build_result = d.pop("AlertBuildResult", UNSET)
        alert_build_result: Union[Unset, KeyfactorApiModelsAlertsExpirationExpirationAlertTestResponseAlertBuildResult]
        if isinstance(_alert_build_result, Unset):
            alert_build_result = UNSET
        else:
            alert_build_result = KeyfactorApiModelsAlertsExpirationExpirationAlertTestResponseAlertBuildResult(
                _alert_build_result
            )

        keyfactor_api_models_alerts_expiration_expiration_alert_test_response = cls(
            expiration_alerts=expiration_alerts,
            alert_build_result=alert_build_result,
        )

        keyfactor_api_models_alerts_expiration_expiration_alert_test_response.additional_properties = d
        return keyfactor_api_models_alerts_expiration_expiration_alert_test_response

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
