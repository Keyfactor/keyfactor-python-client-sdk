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

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..models.models_keyfactor_api_secret import ModelsKeyfactorAPISecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStoresCertificateStoreUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsCertificateStoresCertificateStoreUpdateRequest:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        container_id (Union[Unset, int]):
        create_if_missing (Union[Unset, bool]):
        properties (Union[Unset, str]):
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        inventory_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        password (Union[Unset, ModelsKeyfactorAPISecret]):
    """

    id: Union[Unset, str] = UNSET
    container_id: Union[Unset, int] = UNSET
    create_if_missing: Union[Unset, bool] = UNSET
    properties: Union[Unset, str] = UNSET
    agent_id: Union[Unset, str] = UNSET
    inventory_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    password: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        container_id = self.container_id
        create_if_missing = self.create_if_missing
        properties = self.properties
        agent_id = self.agent_id
        inventory_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_schedule, Unset):
            inventory_schedule = self.inventory_schedule.to_dict()

        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if container_id is not UNSET:
            field_dict["ContainerId"] = container_id
        if create_if_missing is not UNSET:
            field_dict["CreateIfMissing"] = create_if_missing
        if properties is not UNSET:
            field_dict["Properties"] = properties
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if inventory_schedule is not UNSET:
            field_dict["InventorySchedule"] = inventory_schedule
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        container_id = d.pop("ContainerId", UNSET)

        create_if_missing = d.pop("CreateIfMissing", UNSET)

        properties = d.pop("Properties", UNSET)

        agent_id = d.pop("AgentId", UNSET)

        _inventory_schedule = d.pop("InventorySchedule", UNSET)
        inventory_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_inventory_schedule, Unset):
            inventory_schedule = UNSET
        else:
            inventory_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_inventory_schedule)

        _password = d.pop("Password", UNSET)
        password: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = ModelsKeyfactorAPISecret.from_dict(_password)

        models_certificate_stores_certificate_store_update_request = cls(
            id=id,
            container_id=container_id,
            create_if_missing=create_if_missing,
            properties=properties,
            agent_id=agent_id,
            inventory_schedule=inventory_schedule,
            password=password,
        )

        models_certificate_stores_certificate_store_update_request.additional_properties = d
        return models_certificate_stores_certificate_store_update_request

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
