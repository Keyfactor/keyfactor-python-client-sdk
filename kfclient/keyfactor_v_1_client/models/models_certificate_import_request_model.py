# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.models_certificate_import_request_model_metadata import ModelsCertificateImportRequestModelMetadata
from ..models.models_enrollment_management_store_type import ModelsEnrollmentManagementStoreType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateImportRequestModel")


@attr.s(auto_attribs=True)
class ModelsCertificateImportRequestModel:
    """Class representing a request to import a certificate into Keyfactor Command

    Example:
        {'Certificate': '<base64 cert>', 'Password': '<pfx password>', 'Metadata': {'Email-Contact': 'user@domain.com'},
            'StoreIds': ['00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000'], 'StoreTypes':
            [{'StoreTypeId': 0, 'Alias': '<store alias>', 'Overwrite': True, 'Properties': []}], 'Schedule':
            datetime.datetime(2022, 9, 23, 18, 9, 16, 594227, tzinfo=datetime.timezone.utc), 'ImportMetadata': True}

    Attributes:
        certificate (str): Base64-encoded certificate contents
        password (Union[Unset, str]): Optional password associated if required for a PFX
        metadata (Union[Unset, ModelsCertificateImportRequestModelMetadata]): Colleciton of metadata to be associated
            with the imported certificate
        store_ids (Union[Unset, List[str]]): List of the Keyfactor certificate store identifiers (GUID) with which the
            imported certificate should be associated
        store_types (Union[Unset, List[ModelsEnrollmentManagementStoreType]]): List of the certificate store types with
            with the imported certificate should be associated
        schedule (Union[Unset, datetime.datetime]): Schedule on which the certificate should be imported
        import_metadata (Union[Unset, bool]): Whether or not we should validate and import the certificate's metadata.
    """

    certificate: str
    password: Union[Unset, str] = UNSET
    metadata: Union[Unset, ModelsCertificateImportRequestModelMetadata] = UNSET
    store_ids: Union[Unset, List[str]] = UNSET
    store_types: Union[Unset, List[ModelsEnrollmentManagementStoreType]] = UNSET
    schedule: Union[Unset, datetime.datetime] = UNSET
    import_metadata: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate = self.certificate
        password = self.password
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        store_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.store_ids, Unset):
            store_ids = self.store_ids

        store_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.store_types, Unset):
            store_types = []
            for store_types_item_data in self.store_types:
                store_types_item = store_types_item_data.to_dict()

                store_types.append(store_types_item)

        schedule: Union[Unset, str] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.isoformat()[:-6]+'Z'

        import_metadata = self.import_metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Certificate": certificate,
            }
        )
        if password is not UNSET:
            field_dict["Password"] = password
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if store_ids is not UNSET:
            field_dict["StoreIds"] = store_ids
        if store_types is not UNSET:
            field_dict["StoreTypes"] = store_types
        if schedule is not UNSET:
            field_dict["Schedule"] = schedule
        if import_metadata is not UNSET:
            field_dict["ImportMetadata"] = import_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate = d.pop("Certificate")

        password = d.pop("Password", UNSET)

        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, ModelsCertificateImportRequestModelMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsCertificateImportRequestModelMetadata.from_dict(_metadata)

        store_ids = cast(List[str], d.pop("StoreIds", UNSET))

        store_types = []
        _store_types = d.pop("StoreTypes", UNSET)
        for store_types_item_data in _store_types or []:
            store_types_item = ModelsEnrollmentManagementStoreType.from_dict(store_types_item_data)

            store_types.append(store_types_item)

        _schedule = d.pop("Schedule", UNSET)
        schedule: Union[Unset, datetime.datetime]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = isoparse(_schedule)

        import_metadata = d.pop("ImportMetadata", UNSET)

        models_certificate_import_request_model = cls(
            certificate=certificate,
            password=password,
            metadata=metadata,
            store_ids=store_ids,
            store_types=store_types,
            schedule=schedule,
            import_metadata=import_metadata,
        )

        models_certificate_import_request_model.additional_properties = d
        return models_certificate_import_request_model

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
