from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHUsersSshUserUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsSSHUsersSshUserUpdateRequest:
    """
    Attributes:
        id (int):
        logon_ids (Union[Unset, List[int]]):
    """

    id: int
    logon_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        logon_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.logon_ids, Unset):
            logon_ids = self.logon_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
            }
        )
        if logon_ids is not UNSET:
            field_dict["LogonIds"] = logon_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        logon_ids = cast(List[int], d.pop("LogonIds", UNSET))

        models_ssh_users_ssh_user_update_request = cls(
            id=id,
            logon_ids=logon_ids,
        )

        models_ssh_users_ssh_user_update_request.additional_properties = d
        return models_ssh_users_ssh_user_update_request

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
