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
from ..models.models_reenrollment_status import ModelsReenrollmentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStore")


@attr.s(auto_attribs=True)
class ModelsCertificateStore:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        display_name (Union[Unset, str]):
        container_id (Union[Unset, int]):
        client_machine (Union[Unset, str]):
        storepath (Union[Unset, str]):
        cert_store_inventory_job_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        cert_store_type (Union[Unset, int]):
        approved (Union[Unset, bool]):
        create_if_missing (Union[Unset, bool]):
        properties (Union[Unset, str]):
        agent_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        agent_assigned (Union[Unset, bool]):
        container_name (Union[Unset, str]):
        inventory_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        reenrollment_status (Union[Unset, ModelsReenrollmentStatus]):
        set_new_password_allowed (Union[Unset, bool]):
        password (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    container_id: Union[Unset, int] = UNSET
    client_machine: Union[Unset, str] = UNSET
    storepath: Union[Unset, str] = UNSET
    cert_store_inventory_job_id: Union[Unset, str] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    approved: Union[Unset, bool] = UNSET
    create_if_missing: Union[Unset, bool] = UNSET
    properties: Union[Unset, str] = UNSET
    agent_id: Union[Unset, str] = UNSET
    agent_assigned: Union[Unset, bool] = UNSET
    container_name: Union[Unset, str] = UNSET
    inventory_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    reenrollment_status: Union[Unset, ModelsReenrollmentStatus] = UNSET
    set_new_password_allowed: Union[Unset, bool] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        container_id = self.container_id
        client_machine = self.client_machine
        storepath = self.storepath
        cert_store_inventory_job_id = self.cert_store_inventory_job_id
        cert_store_type = self.cert_store_type
        approved = self.approved
        create_if_missing = self.create_if_missing
        properties = self.properties
        agent_id = self.agent_id
        agent_assigned = self.agent_assigned
        container_name = self.container_name
        inventory_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_schedule, Unset):
            inventory_schedule = self.inventory_schedule.to_dict()

        reenrollment_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reenrollment_status, Unset):
            reenrollment_status = self.reenrollment_status.to_dict()

        set_new_password_allowed = self.set_new_password_allowed
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if container_id is not UNSET:
            field_dict["ContainerId"] = container_id
        if client_machine is not UNSET:
            field_dict["ClientMachine"] = client_machine
        if storepath is not UNSET:
            field_dict["Storepath"] = storepath
        if cert_store_inventory_job_id is not UNSET:
            field_dict["CertStoreInventoryJobId"] = cert_store_inventory_job_id
        if cert_store_type is not UNSET:
            field_dict["CertStoreType"] = cert_store_type
        if approved is not UNSET:
            field_dict["Approved"] = approved
        if create_if_missing is not UNSET:
            field_dict["CreateIfMissing"] = create_if_missing
        if properties is not UNSET:
            field_dict["Properties"] = properties
        if agent_id is not UNSET:
            field_dict["AgentId"] = agent_id
        if agent_assigned is not UNSET:
            field_dict["AgentAssigned"] = agent_assigned
        if container_name is not UNSET:
            field_dict["ContainerName"] = container_name
        if inventory_schedule is not UNSET:
            field_dict["InventorySchedule"] = inventory_schedule
        if reenrollment_status is not UNSET:
            field_dict["ReenrollmentStatus"] = reenrollment_status
        if set_new_password_allowed is not UNSET:
            field_dict["SetNewPasswordAllowed"] = set_new_password_allowed
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        container_id = d.pop("ContainerId", UNSET)

        client_machine = d.pop("ClientMachine", UNSET)

        storepath = d.pop("Storepath", UNSET)

        cert_store_inventory_job_id = d.pop("CertStoreInventoryJobId", UNSET)

        cert_store_type = d.pop("CertStoreType", UNSET)

        approved = d.pop("Approved", UNSET)

        create_if_missing = d.pop("CreateIfMissing", UNSET)

        properties = d.pop("Properties", UNSET)

        agent_id = d.pop("AgentId", UNSET)

        agent_assigned = d.pop("AgentAssigned", UNSET)

        container_name = d.pop("ContainerName", UNSET)

        _inventory_schedule = d.pop("InventorySchedule", UNSET)
        inventory_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_inventory_schedule, Unset):
            inventory_schedule = UNSET
        else:
            inventory_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_inventory_schedule)

        _reenrollment_status = d.pop("ReenrollmentStatus", UNSET)
        reenrollment_status: Union[Unset, ModelsReenrollmentStatus]
        if isinstance(_reenrollment_status, Unset):
            reenrollment_status = UNSET
        else:
            reenrollment_status = ModelsReenrollmentStatus.from_dict(_reenrollment_status)

        set_new_password_allowed = d.pop("SetNewPasswordAllowed", UNSET)

        password = d.pop("Password", UNSET)

        models_certificate_store = cls(
            id=id,
            display_name=display_name,
            container_id=container_id,
            client_machine=client_machine,
            storepath=storepath,
            cert_store_inventory_job_id=cert_store_inventory_job_id,
            cert_store_type=cert_store_type,
            approved=approved,
            create_if_missing=create_if_missing,
            properties=properties,
            agent_id=agent_id,
            agent_assigned=agent_assigned,
            container_name=container_name,
            inventory_schedule=inventory_schedule,
            reenrollment_status=reenrollment_status,
            set_new_password_allowed=set_new_password_allowed,
            password=password,
        )

        models_certificate_store.additional_properties = d
        return models_certificate_store

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
