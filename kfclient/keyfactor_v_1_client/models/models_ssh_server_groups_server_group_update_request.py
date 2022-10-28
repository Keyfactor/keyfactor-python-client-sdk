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
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHServerGroupsServerGroupUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsSSHServerGroupsServerGroupUpdateRequest:
    """
    Attributes:
        id (str):  Example: 00000000-0000-0000-0000-000000000000.
        owner_name (str):
        group_name (str):
        under_management (bool):
        sync_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
    """

    id: str
    owner_name: str
    group_name: str
    under_management: bool
    sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        owner_name = self.owner_name
        group_name = self.group_name
        under_management = self.under_management
        sync_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_schedule, Unset):
            sync_schedule = self.sync_schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "OwnerName": owner_name,
                "GroupName": group_name,
                "UnderManagement": under_management,
            }
        )
        if sync_schedule is not UNSET:
            field_dict["SyncSchedule"] = sync_schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        owner_name = d.pop("OwnerName")

        group_name = d.pop("GroupName")

        under_management = d.pop("UnderManagement")

        _sync_schedule = d.pop("SyncSchedule", UNSET)
        sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_sync_schedule, Unset):
            sync_schedule = UNSET
        else:
            sync_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_sync_schedule)

        models_ssh_server_groups_server_group_update_request = cls(
            id=id,
            owner_name=owner_name,
            group_name=group_name,
            under_management=under_management,
            sync_schedule=sync_schedule,
        )

        models_ssh_server_groups_server_group_update_request.additional_properties = d
        return models_ssh_server_groups_server_group_update_request

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
