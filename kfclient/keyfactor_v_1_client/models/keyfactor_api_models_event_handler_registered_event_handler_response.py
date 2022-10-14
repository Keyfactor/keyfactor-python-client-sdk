from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, str]):
        use_handler (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    use_handler: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        use_handler = self.use_handler

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if use_handler is not UNSET:
            field_dict["UseHandler"] = use_handler

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        use_handler = d.pop("UseHandler", UNSET)

        keyfactor_api_models_event_handler_registered_event_handler_response = cls(
            id=id,
            display_name=display_name,
            use_handler=use_handler,
        )

        keyfactor_api_models_event_handler_registered_event_handler_response.additional_properties = d
        return keyfactor_api_models_event_handler_registered_event_handler_response

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
