from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest:
    """
    Attributes:
        id (int):
        use_handler (bool):
    """

    id: int
    use_handler: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        use_handler = self.use_handler

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "UseHandler": use_handler,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id")

        use_handler = d.pop("UseHandler")

        keyfactor_api_models_event_handler_registered_event_handler_request = cls(
            id=id,
            use_handler=use_handler,
        )

        keyfactor_api_models_event_handler_registered_event_handler_request.additional_properties = d
        return keyfactor_api_models_event_handler_registered_event_handler_request

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
