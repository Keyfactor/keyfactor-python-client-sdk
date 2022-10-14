from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.models_ssh_access_logon_user_access_request import ModelsSSHAccessLogonUserAccessRequest

T = TypeVar("T", bound="ModelsSSHAccessServerGroupAccessRequest")


@attr.s(auto_attribs=True)
class ModelsSSHAccessServerGroupAccessRequest:
    """
    Attributes:
        server_group_id (str):  Example: 00000000-0000-0000-0000-000000000000.
        logon_users (List[ModelsSSHAccessLogonUserAccessRequest]):
    """

    server_group_id: str
    logon_users: List[ModelsSSHAccessLogonUserAccessRequest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_group_id = self.server_group_id
        logon_users = []
        for logon_users_item_data in self.logon_users:
            logon_users_item = logon_users_item_data.to_dict()

            logon_users.append(logon_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ServerGroupId": server_group_id,
                "LogonUsers": logon_users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_group_id = d.pop("ServerGroupId")

        logon_users = []
        _logon_users = d.pop("LogonUsers")
        for logon_users_item_data in _logon_users:
            logon_users_item = ModelsSSHAccessLogonUserAccessRequest.from_dict(logon_users_item_data)

            logon_users.append(logon_users_item)

        models_ssh_access_server_group_access_request = cls(
            server_group_id=server_group_id,
            logon_users=logon_users,
        )

        models_ssh_access_server_group_access_request.additional_properties = d
        return models_ssh_access_server_group_access_request

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
