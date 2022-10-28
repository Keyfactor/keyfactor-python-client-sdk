# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
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
