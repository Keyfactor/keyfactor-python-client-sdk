from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCustomReportUpdateRequest")


@attr.s(auto_attribs=True)
class ModelsCustomReportUpdateRequest:
    """The CustomReport can be used to create and update a custom report.

    Attributes:
        id (int):
        custom_url (Union[Unset, str]):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        in_navigator (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    id: int
    custom_url: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    in_navigator: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        custom_url = self.custom_url
        display_name = self.display_name
        description = self.description
        in_navigator = self.in_navigator
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
            }
        )
        if custom_url is not UNSET:
            field_dict["CustomURL"] = custom_url
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if description is not UNSET:
            field_dict["Description"] = description
        if in_navigator is not UNSET:
            field_dict["InNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["Favorite"] = favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        custom_url = d.pop("CustomURL", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        description = d.pop("Description", UNSET)

        in_navigator = d.pop("InNavigator", UNSET)

        favorite = d.pop("Favorite", UNSET)

        models_custom_report_update_request = cls(
            id=id,
            custom_url=custom_url,
            display_name=display_name,
            description=description,
            in_navigator=in_navigator,
            favorite=favorite,
        )

        models_custom_report_update_request.additional_properties = d
        return models_custom_report_update_request

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
