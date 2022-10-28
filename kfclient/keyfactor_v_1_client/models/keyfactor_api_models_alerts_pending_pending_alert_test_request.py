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

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsAlertsPendingPendingAlertTestRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsAlertsPendingPendingAlertTestRequest:
    """
    Attributes:
        alert_id (Union[Unset, int]):
        send_alerts (Union[Unset, bool]):
    """

    alert_id: Union[Unset, int] = UNSET
    send_alerts: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_id = self.alert_id
        send_alerts = self.send_alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_id is not UNSET:
            field_dict["AlertId"] = alert_id
        if send_alerts is not UNSET:
            field_dict["SendAlerts"] = send_alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_id = d.pop("AlertId", UNSET)

        send_alerts = d.pop("SendAlerts", UNSET)

        keyfactor_api_models_alerts_pending_pending_alert_test_request = cls(
            alert_id=alert_id,
            send_alerts=send_alerts,
        )

        keyfactor_api_models_alerts_pending_pending_alert_test_request.additional_properties = d
        return keyfactor_api_models_alerts_pending_pending_alert_test_request

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
