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

from ..models.models_certificate_store_entry_job_fields import ModelsCertificateStoreEntryJobFields
from ..models.models_keyfactor_api_secret import ModelsKeyfactorAPISecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateStoreEntry")


@attr.s(auto_attribs=True)
class ModelsCertificateStoreEntry:
    """
    Attributes:
        certificate_store_id (str):  Example: 00000000-0000-0000-0000-000000000000.
        alias (Union[Unset, str]):
        job_fields (Union[Unset, ModelsCertificateStoreEntryJobFields]):
        overwrite (Union[Unset, bool]):
        entry_password (Union[Unset, ModelsKeyfactorAPISecret]):
        pfx_password (Union[Unset, str]): The PFX password.
        include_private_key (Union[Unset, bool]):
    """

    certificate_store_id: str
    alias: Union[Unset, str] = UNSET
    job_fields: Union[Unset, ModelsCertificateStoreEntryJobFields] = UNSET
    overwrite: Union[Unset, bool] = UNSET
    entry_password: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    pfx_password: Union[Unset, str] = UNSET
    include_private_key: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_store_id = self.certificate_store_id
        alias = self.alias
        job_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = self.job_fields.to_dict()

        overwrite = self.overwrite
        entry_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry_password, Unset):
            entry_password = self.entry_password.to_dict()

        pfx_password = self.pfx_password
        include_private_key = self.include_private_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CertificateStoreId": certificate_store_id,
            }
        )
        if alias is not UNSET:
            field_dict["Alias"] = alias
        if job_fields is not UNSET:
            field_dict["JobFields"] = job_fields
        if overwrite is not UNSET:
            field_dict["Overwrite"] = overwrite
        if entry_password is not UNSET:
            field_dict["EntryPassword"] = entry_password
        if pfx_password is not UNSET:
            field_dict["PfxPassword"] = pfx_password
        if include_private_key is not UNSET:
            field_dict["IncludePrivateKey"] = include_private_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_store_id = d.pop("CertificateStoreId")

        alias = d.pop("Alias", UNSET)

        _job_fields = d.pop("JobFields", UNSET)
        job_fields: Union[Unset, ModelsCertificateStoreEntryJobFields]
        if isinstance(_job_fields, Unset):
            job_fields = UNSET
        else:
            job_fields = ModelsCertificateStoreEntryJobFields.from_dict(_job_fields)

        overwrite = d.pop("Overwrite", UNSET)

        _entry_password = d.pop("EntryPassword", UNSET)
        entry_password: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_entry_password, Unset):
            entry_password = UNSET
        else:
            entry_password = ModelsKeyfactorAPISecret.from_dict(_entry_password)

        pfx_password = d.pop("PfxPassword", UNSET)

        include_private_key = d.pop("IncludePrivateKey", UNSET)

        models_certificate_store_entry = cls(
            certificate_store_id=certificate_store_id,
            alias=alias,
            job_fields=job_fields,
            overwrite=overwrite,
            entry_password=entry_password,
            pfx_password=pfx_password,
            include_private_key=include_private_key,
        )

        models_certificate_store_entry.additional_properties = d
        return models_certificate_store_entry

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
