from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSSHLogonsLogonAccessRequest")


@attr.s(auto_attribs=True)
class ModelsSSHLogonsLogonAccessRequest:
    """
    Attributes:
        logon_id (int):
        user_ids (Union[Unset, List[int]]):
    """

    logon_id: int
    user_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logon_id = self.logon_id
        user_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "LogonId": logon_id,
            }
        )
        if user_ids is not UNSET:
            field_dict["UserIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        logon_id = d.pop("LogonId")

        user_ids = cast(List[int], d.pop("UserIds", UNSET))

        models_ssh_logons_logon_access_request = cls(
            logon_id=logon_id,
            user_ids=user_ids,
        )

        models_ssh_logons_logon_access_request.additional_properties = d
        return models_ssh_logons_logon_access_request

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
