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

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse:
    """
    Attributes:
        agent_blueprint_store_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        agent_blueprint_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        store_path (Union[Unset, str]):
        container_id (Union[Unset, int]):
        cert_store_type (Union[Unset, int]):
        cert_store_type_name (Union[Unset, str]):
        approved (Union[Unset, bool]):
        create_if_missing (Union[Unset, bool]):
        properties (Union[Unset, str]):
    """

    agent_blueprint_store_id: Union[Unset, str] = UNSET
    agent_blueprint_id: Union[Unset, str] = UNSET
    store_path: Union[Unset, str] = UNSET
    container_id: Union[Unset, int] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    cert_store_type_name: Union[Unset, str] = UNSET
    approved: Union[Unset, bool] = UNSET
    create_if_missing: Union[Unset, bool] = UNSET
    properties: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_blueprint_store_id = self.agent_blueprint_store_id
        agent_blueprint_id = self.agent_blueprint_id
        store_path = self.store_path
        container_id = self.container_id
        cert_store_type = self.cert_store_type
        cert_store_type_name = self.cert_store_type_name
        approved = self.approved
        create_if_missing = self.create_if_missing
        properties = self.properties

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_blueprint_store_id is not UNSET:
            field_dict["AgentBlueprintStoreId"] = agent_blueprint_store_id
        if agent_blueprint_id is not UNSET:
            field_dict["AgentBlueprintId"] = agent_blueprint_id
        if store_path is not UNSET:
            field_dict["StorePath"] = store_path
        if container_id is not UNSET:
            field_dict["ContainerId"] = container_id
        if cert_store_type is not UNSET:
            field_dict["CertStoreType"] = cert_store_type
        if cert_store_type_name is not UNSET:
            field_dict["CertStoreTypeName"] = cert_store_type_name
        if approved is not UNSET:
            field_dict["Approved"] = approved
        if create_if_missing is not UNSET:
            field_dict["CreateIfMissing"] = create_if_missing
        if properties is not UNSET:
            field_dict["Properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_blueprint_store_id = d.pop("AgentBlueprintStoreId", UNSET)

        agent_blueprint_id = d.pop("AgentBlueprintId", UNSET)

        store_path = d.pop("StorePath", UNSET)

        container_id = d.pop("ContainerId", UNSET)

        cert_store_type = d.pop("CertStoreType", UNSET)

        cert_store_type_name = d.pop("CertStoreTypeName", UNSET)

        approved = d.pop("Approved", UNSET)

        create_if_missing = d.pop("CreateIfMissing", UNSET)

        properties = d.pop("Properties", UNSET)

        keyfactor_api_models_orchestrators_agent_blueprint_stores_response = cls(
            agent_blueprint_store_id=agent_blueprint_store_id,
            agent_blueprint_id=agent_blueprint_id,
            store_path=store_path,
            container_id=container_id,
            cert_store_type=cert_store_type,
            cert_store_type_name=cert_store_type_name,
            approved=approved,
            create_if_missing=create_if_missing,
            properties=properties,
        )

        keyfactor_api_models_orchestrators_agent_blueprint_stores_response.additional_properties = d
        return keyfactor_api_models_orchestrators_agent_blueprint_stores_response

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
