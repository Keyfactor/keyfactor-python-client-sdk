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

T = TypeVar("T", bound="ModelsCertificateStoresCertificateStoreCreateRequest")


@attr.s(auto_attribs=True)
class ModelsCertificateStoresCertificateStoreCreateRequest:
    """
    Attributes:
        container_id (Union[Unset, int]):
        client_machine (Union[Unset, str]):
        storepath (Union[Unset, str]):
        cert_store_type (Union[Unset, int]):
        create_if_missing (Union[Unset, bool]):
        properties (Union[Unset, str]):
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        agent_assigned (Union[Unset, bool]):
        inventory_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        password (Union[Unset, ModelsKeyfactorAPISecret]):
    """

    container_id: Union[Unset, int] = UNSET
    client_machine: Union[Unset, str] = UNSET
    storepath: Union[Unset, str] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    create_if_missing: Union[Unset, bool] = UNSET
    properties: Union[Unset, str] = UNSET
    agent_id: Union[Unset, str] = UNSET
    agent_assigned: Union[Unset, bool] = UNSET
    inventory_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    password: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_id = self.container_id
        client_machine = self.client_machine
        storepath = self.storepath
        cert_store_type = self.cert_store_type
        create_if_missing = self.create_if_missing
        properties = self.properties
        agent_id = self.agent_id
        agent_assigned = self.agent_assigned
        inventory_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_schedule, Unset):
            inventory_schedule = self.inventory_schedule.to_dict()

        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_id is not UNSET:
            field_dict["ContainerId"] = container_id
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if storepath is not UNSET:
            field_dict["Storepath"] = storepath
        if cert_store_type is not UNSET:
            field_dict["CertStoreType"] = cert_store_type
        if create_if_missing is not UNSET:
            field_dict["CreateIfMissing"] = create_if_missing
        if properties is not UNSET:
            field_dict["Properties"] = properties
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if agent_assigned is not UNSET:
            field_dict["AgentAssigned"] = agent_assigned
        if inventory_schedule is not UNSET:
            field_dict["InventorySchedule"] = inventory_schedule
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        container_id = d.pop("ContainerId", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        storepath = d.pop("Storepath", UNSET)

        cert_store_type = d.pop("CertStoreType", UNSET)

        create_if_missing = d.pop("CreateIfMissing", UNSET)

        properties = d.pop("Properties", UNSET)

        agent_id = d.pop("AgentId", UNSET)

        agent_assigned = d.pop("AgentAssigned", UNSET)

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

        models_certificate_stores_certificate_store_create_request = cls(
            container_id=container_id,
            client_machine=client_machine,
            storepath=storepath,
            cert_store_type=cert_store_type,
            create_if_missing=create_if_missing,
            properties=properties,
            agent_id=agent_id,
            agent_assigned=agent_assigned,
            inventory_schedule=inventory_schedule,
            password=password,
        )

        models_certificate_stores_certificate_store_create_request.additional_properties = d
        return models_certificate_stores_certificate_store_create_request

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
