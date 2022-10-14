from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHServerGroupsServerGroupCreationRequest")


@attr.s(auto_attribs=True)
class ModelsSSHServerGroupsServerGroupCreationRequest:
    """
    Attributes:
        owner_name (str):
        group_name (str):
        sync_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        under_management (Union[Unset, bool]):
    """

    owner_name: str
    group_name: str
    sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    under_management: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_name = self.owner_name
        group_name = self.group_name
        sync_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_schedule, Unset):
            sync_schedule = self.sync_schedule.to_dict()

        under_management = self.under_management

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OwnerName": owner_name,
                "GroupName": group_name,
            }
        )
        if sync_schedule is not UNSET:
            field_dict["SyncSchedule"] = sync_schedule
        if under_management is not UNSET:
            field_dict["UnderManagement"] = under_management

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner_name = d.pop("OwnerName")

        group_name = d.pop("GroupName")

        _sync_schedule = d.pop("SyncSchedule", UNSET)
        sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_sync_schedule, Unset):
            sync_schedule = UNSET
        else:
            sync_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_sync_schedule)

        under_management = d.pop("UnderManagement", UNSET)

        models_ssh_server_groups_server_group_creation_request = cls(
            owner_name=owner_name,
            group_name=group_name,
            sync_schedule=sync_schedule,
            under_management=under_management,
        )

        models_ssh_server_groups_server_group_creation_request.additional_properties = d
        return models_ssh_server_groups_server_group_creation_request

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
