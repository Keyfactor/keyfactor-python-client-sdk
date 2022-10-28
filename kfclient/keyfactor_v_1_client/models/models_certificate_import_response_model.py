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

from ..models.models_certificate_import_response_model_import_status import (
    ModelsCertificateImportResponseModelImportStatus,
)
from ..models.models_certificate_import_response_model_job_status import ModelsCertificateImportResponseModelJobStatus
from ..models.models_invalid_keystore import ModelsInvalidKeystore
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateImportResponseModel")


@attr.s(auto_attribs=True)
class ModelsCertificateImportResponseModel:
    """
    Attributes:
        import_status (Union[Unset, ModelsCertificateImportResponseModelImportStatus]):
        job_status (Union[Unset, ModelsCertificateImportResponseModelJobStatus]):
        invalid_keystores (Union[Unset, List[ModelsInvalidKeystore]]):
        thumbprint (Union[Unset, str]):
    """

    import_status: Union[Unset, ModelsCertificateImportResponseModelImportStatus] = UNSET
    job_status: Union[Unset, ModelsCertificateImportResponseModelJobStatus] = UNSET
    invalid_keystores: Union[Unset, List[ModelsInvalidKeystore]] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_status: Union[Unset, int] = UNSET
        if not isinstance(self.import_status, Unset):
            import_status = self.import_status.value

        job_status: Union[Unset, int] = UNSET
        if not isinstance(self.job_status, Unset):
            job_status = self.job_status.value

        invalid_keystores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_keystores, Unset):
            invalid_keystores = []
            for invalid_keystores_item_data in self.invalid_keystores:
                invalid_keystores_item = invalid_keystores_item_data.to_dict()

                invalid_keystores.append(invalid_keystores_item)

        thumbprint = self.thumbprint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_status is not UNSET:
            field_dict["ImportStatus"] = import_status
        if job_status is not UNSET:
            field_dict["JobStatus"] = job_status
        if invalid_keystores is not UNSET:
            field_dict["InvalidKeystores"] = invalid_keystores
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _import_status = d.pop("ImportStatus", UNSET)
        import_status: Union[Unset, ModelsCertificateImportResponseModelImportStatus]
        if isinstance(_import_status, Unset):
            import_status = UNSET
        else:
            import_status = ModelsCertificateImportResponseModelImportStatus(_import_status)

        _job_status = d.pop("JobStatus", UNSET)
        job_status: Union[Unset, ModelsCertificateImportResponseModelJobStatus]
        if isinstance(_job_status, Unset):
            job_status = UNSET
        else:
            job_status = ModelsCertificateImportResponseModelJobStatus(_job_status)

        invalid_keystores = []
        _invalid_keystores = d.pop("InvalidKeystores", UNSET)
        for invalid_keystores_item_data in _invalid_keystores or []:
            invalid_keystores_item = ModelsInvalidKeystore.from_dict(invalid_keystores_item_data)

            invalid_keystores.append(invalid_keystores_item)

        thumbprint = d.pop("Thumbprint", UNSET)

        models_certificate_import_response_model = cls(
            import_status=import_status,
            job_status=job_status,
            invalid_keystores=invalid_keystores,
            thumbprint=thumbprint,
        )

        models_certificate_import_response_model.additional_properties = d
        return models_certificate_import_response_model

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
