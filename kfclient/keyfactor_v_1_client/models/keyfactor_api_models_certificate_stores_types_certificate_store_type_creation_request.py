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

from ..models.keyfactor_api_models_certificate_stores_types_certificate_store_type_creation_request_custom_alias_allowed import (
    KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestCustomAliasAllowed,
)
from ..models.keyfactor_api_models_certificate_stores_types_certificate_store_type_creation_request_private_key_allowed import (
    KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestPrivateKeyAllowed,
)
from ..models.models_cert_store_type_password_options import ModelsCertStoreTypePasswordOptions
from ..models.models_cert_store_type_supported_operations import ModelsCertStoreTypeSupportedOperations
from ..models.models_certificate_store_type_property import ModelsCertificateStoreTypeProperty
from ..models.models_certificate_store_types_certificate_store_type_entry_parameter import (
    ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequest")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequest:
    """
    Attributes:
        name (str):
        short_name (str):
        capability (Union[Unset, str]):
        local_store (Union[Unset, bool]):
        supported_operations (Union[Unset, ModelsCertStoreTypeSupportedOperations]):
        properties (Union[Unset, List[ModelsCertificateStoreTypeProperty]]):
        password_options (Union[Unset, ModelsCertStoreTypePasswordOptions]):
        store_path_type (Union[Unset, str]):
        store_path_value (Union[Unset, str]):
        private_key_allowed (Union[Unset,
            KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestPrivateKeyAllowed]):
        server_required (Union[Unset, bool]):
        power_shell (Union[Unset, bool]):
        blueprint_allowed (Union[Unset, bool]):
        custom_alias_allowed (Union[Unset,
            KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestCustomAliasAllowed]):
        server_registration (Union[Unset, int]):
        inventory_endpoint (Union[Unset, str]):
        inventory_job_type_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        management_job_type_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        discovery_job_type_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        enrollment_job_type_id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        entry_parameters (Union[Unset, List[ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter]]):
    """

    name: str
    short_name: str
    capability: Union[Unset, str] = UNSET
    local_store: Union[Unset, bool] = UNSET
    supported_operations: Union[Unset, ModelsCertStoreTypeSupportedOperations] = UNSET
    properties: Union[Unset, List[ModelsCertificateStoreTypeProperty]] = UNSET
    password_options: Union[Unset, ModelsCertStoreTypePasswordOptions] = UNSET
    store_path_type: Union[Unset, str] = UNSET
    store_path_value: Union[Unset, str] = UNSET
    private_key_allowed: Union[
        Unset, KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestPrivateKeyAllowed
    ] = UNSET
    server_required: Union[Unset, bool] = UNSET
    power_shell: Union[Unset, bool] = UNSET
    blueprint_allowed: Union[Unset, bool] = UNSET
    custom_alias_allowed: Union[
        Unset, KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestCustomAliasAllowed
    ] = UNSET
    server_registration: Union[Unset, int] = UNSET
    inventory_endpoint: Union[Unset, str] = UNSET
    inventory_job_type_id: Union[Unset, str] = UNSET
    management_job_type_id: Union[Unset, str] = UNSET
    discovery_job_type_id: Union[Unset, str] = UNSET
    enrollment_job_type_id: Union[Unset, str] = UNSET
    entry_parameters: Union[Unset, List[ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        short_name = self.short_name
        capability = self.capability
        local_store = self.local_store
        supported_operations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supported_operations, Unset):
            supported_operations = self.supported_operations.to_dict()

        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()

                properties.append(properties_item)

        password_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password_options, Unset):
            password_options = self.password_options.to_dict()

        store_path_type = self.store_path_type
        store_path_value = self.store_path_value
        private_key_allowed: Union[Unset, int] = UNSET
        if not isinstance(self.private_key_allowed, Unset):
            private_key_allowed = self.private_key_allowed.value

        server_required = self.server_required
        power_shell = self.power_shell
        blueprint_allowed = self.blueprint_allowed
        custom_alias_allowed: Union[Unset, int] = UNSET
        if not isinstance(self.custom_alias_allowed, Unset):
            custom_alias_allowed = self.custom_alias_allowed.value

        server_registration = self.server_registration
        inventory_endpoint = self.inventory_endpoint
        inventory_job_type_id = self.inventory_job_type_id
        management_job_type_id = self.management_job_type_id
        discovery_job_type_id = self.discovery_job_type_id
        enrollment_job_type_id = self.enrollment_job_type_id
        entry_parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry_parameters, Unset):
            entry_parameters = []
            for entry_parameters_item_data in self.entry_parameters:
                entry_parameters_item = entry_parameters_item_data.to_dict()

                entry_parameters.append(entry_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Name": name,
                "ShortName": short_name,
            }
        )
        if capability is not UNSET:
            field_dict["Capability"] = capability
        if local_store is not UNSET:
            field_dict["LocalStore"] = local_store
        if supported_operations is not UNSET:
            field_dict["SupportedOperations"] = supported_operations
        if properties is not UNSET:
            field_dict["Properties"] = properties
        if password_options is not UNSET:
            field_dict["PasswordOptions"] = password_options
        if store_path_type is not UNSET:
            field_dict["StorePathType"] = store_path_type
        if store_path_value is not UNSET:
            field_dict["StorePathValue"] = store_path_value
        if private_key_allowed is not UNSET:
            field_dict["PrivateKeyAllowed"] = private_key_allowed
        if server_required is not UNSET:
            field_dict["ServerRequired"] = server_required
        if power_shell is not UNSET:
            field_dict["PowerShell"] = power_shell
        if blueprint_allowed is not UNSET:
            field_dict["BlueprintAllowed"] = blueprint_allowed
        if custom_alias_allowed is not UNSET:
            field_dict["CustomAliasAllowed"] = custom_alias_allowed
        if server_registration is not UNSET:
            field_dict["ServerRegistration"] = server_registration
        if inventory_endpoint is not UNSET:
            field_dict["InventoryEndpoint"] = inventory_endpoint
        if inventory_job_type_id is not UNSET:
            field_dict["InventoryJobTypeId"] = inventory_job_type_id
        if management_job_type_id is not UNSET:
            field_dict["ManagementJobTypeId"] = management_job_type_id
        if discovery_job_type_id is not UNSET:
            field_dict["DiscoveryJobTypeId"] = discovery_job_type_id
        if enrollment_job_type_id is not UNSET:
            field_dict["EnrollmentJobTypeId"] = enrollment_job_type_id
        if entry_parameters is not UNSET:
            field_dict["EntryParameters"] = entry_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        short_name = d.pop("ShortName")

        capability = d.pop("Capability", UNSET)

        local_store = d.pop("LocalStore", UNSET)

        _supported_operations = d.pop("SupportedOperations", UNSET)
        supported_operations: Union[Unset, ModelsCertStoreTypeSupportedOperations]
        if isinstance(_supported_operations, Unset):
            supported_operations = UNSET
        else:
            supported_operations = ModelsCertStoreTypeSupportedOperations.from_dict(_supported_operations)

        properties = []
        _properties = d.pop("Properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = ModelsCertificateStoreTypeProperty.from_dict(properties_item_data)

            properties.append(properties_item)

        _password_options = d.pop("PasswordOptions", UNSET)
        password_options: Union[Unset, ModelsCertStoreTypePasswordOptions]
        if isinstance(_password_options, Unset):
            password_options = UNSET
        else:
            password_options = ModelsCertStoreTypePasswordOptions.from_dict(_password_options)

        store_path_type = d.pop("StorePathType", UNSET)

        store_path_value = d.pop("StorePathValue", UNSET)

        _private_key_allowed = d.pop("PrivateKeyAllowed", UNSET)
        private_key_allowed: Union[
            Unset, KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestPrivateKeyAllowed
        ]
        if isinstance(_private_key_allowed, Unset):
            private_key_allowed = UNSET
        else:
            private_key_allowed = (
                KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestPrivateKeyAllowed(
                    _private_key_allowed
                )
            )

        server_required = d.pop("ServerRequired", UNSET)

        power_shell = d.pop("PowerShell", UNSET)

        blueprint_allowed = d.pop("BlueprintAllowed", UNSET)

        _custom_alias_allowed = d.pop("CustomAliasAllowed", UNSET)
        custom_alias_allowed: Union[
            Unset, KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestCustomAliasAllowed
        ]
        if isinstance(_custom_alias_allowed, Unset):
            custom_alias_allowed = UNSET
        else:
            custom_alias_allowed = (
                KeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeCreationRequestCustomAliasAllowed(
                    _custom_alias_allowed
                )
            )

        server_registration = d.pop("ServerRegistration", UNSET)

        inventory_endpoint = d.pop("InventoryEndpoint", UNSET)

        inventory_job_type_id = d.pop("InventoryJobTypeId", UNSET)

        management_job_type_id = d.pop("ManagementJobTypeId", UNSET)

        discovery_job_type_id = d.pop("DiscoveryJobTypeId", UNSET)

        enrollment_job_type_id = d.pop("EnrollmentJobTypeId", UNSET)

        entry_parameters = []
        _entry_parameters = d.pop("EntryParameters", UNSET)
        for entry_parameters_item_data in _entry_parameters or []:
            entry_parameters_item = ModelsCertificateStoreTypesCertificateStoreTypeEntryParameter.from_dict(
                entry_parameters_item_data
            )

            entry_parameters.append(entry_parameters_item)

        keyfactor_api_models_certificate_stores_types_certificate_store_type_creation_request = cls(
            name=name,
            short_name=short_name,
            capability=capability,
            local_store=local_store,
            supported_operations=supported_operations,
            properties=properties,
            password_options=password_options,
            store_path_type=store_path_type,
            store_path_value=store_path_value,
            private_key_allowed=private_key_allowed,
            server_required=server_required,
            power_shell=power_shell,
            blueprint_allowed=blueprint_allowed,
            custom_alias_allowed=custom_alias_allowed,
            server_registration=server_registration,
            inventory_endpoint=inventory_endpoint,
            inventory_job_type_id=inventory_job_type_id,
            management_job_type_id=management_job_type_id,
            discovery_job_type_id=discovery_job_type_id,
            enrollment_job_type_id=enrollment_job_type_id,
            entry_parameters=entry_parameters,
        )

        keyfactor_api_models_certificate_stores_types_certificate_store_type_creation_request.additional_properties = d
        return keyfactor_api_models_certificate_stores_types_certificate_store_type_creation_request

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
