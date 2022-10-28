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
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.models_certificate_retrieval_response_cert_state import ModelsCertificateRetrievalResponseCertState
from ..models.models_certificate_retrieval_response_certificate_store_inventory_item_model import (
    ModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel,
)
from ..models.models_certificate_retrieval_response_certificate_store_location_detail_model import (
    ModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel,
)
from ..models.models_certificate_retrieval_response_crl_distribution_point_model import (
    ModelsCertificateRetrievalResponseCRLDistributionPointModel,
)
from ..models.models_certificate_retrieval_response_detailed_key_usage_model import (
    ModelsCertificateRetrievalResponseDetailedKeyUsageModel,
)
from ..models.models_certificate_retrieval_response_extended_key_usage_model import (
    ModelsCertificateRetrievalResponseExtendedKeyUsageModel,
)
from ..models.models_certificate_retrieval_response_key_type import ModelsCertificateRetrievalResponseKeyType
from ..models.models_certificate_retrieval_response_location_count_model import (
    ModelsCertificateRetrievalResponseLocationCountModel,
)
from ..models.models_certificate_retrieval_response_metadata import ModelsCertificateRetrievalResponseMetadata
from ..models.models_certificate_retrieval_response_revocation_reason import (
    ModelsCertificateRetrievalResponseRevocationReason,
)
from ..models.models_certificate_retrieval_response_subject_alternative_name_model import (
    ModelsCertificateRetrievalResponseSubjectAlternativeNameModel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateRetrievalResponse")


@attr.s(auto_attribs=True)
class ModelsCertificateRetrievalResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        thumbprint (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        issued_dn (Union[Unset, str]):
        issued_cn (Union[Unset, str]):
        import_date (Union[Unset, datetime.datetime]):
        not_before (Union[Unset, datetime.datetime]):
        not_after (Union[Unset, datetime.datetime]):
        issuer_dn (Union[Unset, str]):
        principal_id (Union[Unset, int]):
        template_id (Union[Unset, int]):
        cert_state (Union[Unset, ModelsCertificateRetrievalResponseCertState]):
        key_size_in_bits (Union[Unset, int]):
        key_type (Union[Unset, ModelsCertificateRetrievalResponseKeyType]):
        requester_id (Union[Unset, int]):
        issued_ou (Union[Unset, str]):
        issued_email (Union[Unset, str]):
        key_usage (Union[Unset, int]):
        signing_algorithm (Union[Unset, str]):
        cert_state_string (Union[Unset, str]):
        key_type_string (Union[Unset, str]):
        revocation_eff_date (Union[Unset, None, datetime.datetime]):
        revocation_reason (Union[Unset, None, ModelsCertificateRetrievalResponseRevocationReason]):
        revocation_comment (Union[Unset, None, str]):
        certificate_authority_id (Union[Unset, int]):
        certificate_authority_name (Union[Unset, str]):
        template_name (Union[Unset, str]): Full template display name.
        archived_key (Union[Unset, bool]):
        has_private_key (Union[Unset, bool]):
        principal_name (Union[Unset, str]):
        cert_request_id (Union[Unset, int]):
        requester_name (Union[Unset, str]):
        content_bytes (Union[Unset, str]):
        extended_key_usages (Union[Unset, List[ModelsCertificateRetrievalResponseExtendedKeyUsageModel]]):
        subject_alt_name_elements (Union[Unset, List[ModelsCertificateRetrievalResponseSubjectAlternativeNameModel]]):
        crl_distribution_points (Union[Unset, List[ModelsCertificateRetrievalResponseCRLDistributionPointModel]]):
        locations_count (Union[Unset, List[ModelsCertificateRetrievalResponseLocationCountModel]]):
        ssl_locations (Union[Unset, List[ModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel]]):
        locations (Union[Unset, List[ModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel]]):
        metadata (Union[Unset, ModelsCertificateRetrievalResponseMetadata]):
        certificate_key_id (Union[Unset, int]):
        ca_row_index (Union[Unset, int]):
        ca_record_id (Union[Unset, str]):
        detailed_key_usage (Union[Unset, ModelsCertificateRetrievalResponseDetailedKeyUsageModel]):
        key_recoverable (Union[Unset, bool]):
        curve (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    thumbprint: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    issued_dn: Union[Unset, str] = UNSET
    issued_cn: Union[Unset, str] = UNSET
    import_date: Union[Unset, datetime.datetime] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    principal_id: Union[Unset, int] = UNSET
    template_id: Union[Unset, int] = UNSET
    cert_state: Union[Unset, ModelsCertificateRetrievalResponseCertState] = UNSET
    key_size_in_bits: Union[Unset, int] = UNSET
    key_type: Union[Unset, ModelsCertificateRetrievalResponseKeyType] = UNSET
    requester_id: Union[Unset, int] = UNSET
    issued_ou: Union[Unset, str] = UNSET
    issued_email: Union[Unset, str] = UNSET
    key_usage: Union[Unset, int] = UNSET
    signing_algorithm: Union[Unset, str] = UNSET
    cert_state_string: Union[Unset, str] = UNSET
    key_type_string: Union[Unset, str] = UNSET
    revocation_eff_date: Union[Unset, None, datetime.datetime] = UNSET
    revocation_reason: Union[Unset, None, ModelsCertificateRetrievalResponseRevocationReason] = UNSET
    revocation_comment: Union[Unset, None, str] = UNSET
    certificate_authority_id: Union[Unset, int] = UNSET
    certificate_authority_name: Union[Unset, str] = UNSET
    template_name: Union[Unset, str] = UNSET
    archived_key: Union[Unset, bool] = UNSET
    has_private_key: Union[Unset, bool] = UNSET
    principal_name: Union[Unset, str] = UNSET
    cert_request_id: Union[Unset, int] = UNSET
    requester_name: Union[Unset, str] = UNSET
    content_bytes: Union[Unset, str] = UNSET
    extended_key_usages: Union[Unset, List[ModelsCertificateRetrievalResponseExtendedKeyUsageModel]] = UNSET
    subject_alt_name_elements: Union[Unset, List[ModelsCertificateRetrievalResponseSubjectAlternativeNameModel]] = UNSET
    crl_distribution_points: Union[Unset, List[ModelsCertificateRetrievalResponseCRLDistributionPointModel]] = UNSET
    locations_count: Union[Unset, List[ModelsCertificateRetrievalResponseLocationCountModel]] = UNSET
    ssl_locations: Union[Unset, List[ModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel]] = UNSET
    locations: Union[Unset, List[ModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel]] = UNSET
    metadata: Union[Unset, ModelsCertificateRetrievalResponseMetadata] = UNSET
    certificate_key_id: Union[Unset, int] = UNSET
    ca_row_index: Union[Unset, int] = UNSET
    ca_record_id: Union[Unset, str] = UNSET
    detailed_key_usage: Union[Unset, ModelsCertificateRetrievalResponseDetailedKeyUsageModel] = UNSET
    key_recoverable: Union[Unset, bool] = UNSET
    curve: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        thumbprint = self.thumbprint
        serial_number = self.serial_number
        issued_dn = self.issued_dn
        issued_cn = self.issued_cn
        import_date: Union[Unset, str] = UNSET
        if not isinstance(self.import_date, Unset):
            import_date = self.import_date.isoformat()[:-6]+'Z'

        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()[:-6]+'Z'

        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()[:-6]+'Z'

        issuer_dn = self.issuer_dn
        principal_id = self.principal_id
        template_id = self.template_id
        cert_state: Union[Unset, int] = UNSET
        if not isinstance(self.cert_state, Unset):
            cert_state = self.cert_state.value

        key_size_in_bits = self.key_size_in_bits
        key_type: Union[Unset, int] = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value

        requester_id = self.requester_id
        issued_ou = self.issued_ou
        issued_email = self.issued_email
        key_usage = self.key_usage
        signing_algorithm = self.signing_algorithm
        cert_state_string = self.cert_state_string
        key_type_string = self.key_type_string
        revocation_eff_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.revocation_eff_date, Unset):
            revocation_eff_date = self.revocation_eff_date.isoformat()[:-6]+'Z' if self.revocation_eff_date else None

        revocation_reason: Union[Unset, None, int] = UNSET
        if not isinstance(self.revocation_reason, Unset):
            revocation_reason = self.revocation_reason.value if self.revocation_reason else None

        revocation_comment = self.revocation_comment
        certificate_authority_id = self.certificate_authority_id
        certificate_authority_name = self.certificate_authority_name
        template_name = self.template_name
        archived_key = self.archived_key
        has_private_key = self.has_private_key
        principal_name = self.principal_name
        cert_request_id = self.cert_request_id
        requester_name = self.requester_name
        content_bytes = self.content_bytes
        extended_key_usages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extended_key_usages, Unset):
            extended_key_usages = []
            for extended_key_usages_item_data in self.extended_key_usages:
                extended_key_usages_item = extended_key_usages_item_data.to_dict()

                extended_key_usages.append(extended_key_usages_item)

        subject_alt_name_elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subject_alt_name_elements, Unset):
            subject_alt_name_elements = []
            for subject_alt_name_elements_item_data in self.subject_alt_name_elements:
                subject_alt_name_elements_item = subject_alt_name_elements_item_data.to_dict()

                subject_alt_name_elements.append(subject_alt_name_elements_item)

        crl_distribution_points: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.crl_distribution_points, Unset):
            crl_distribution_points = []
            for crl_distribution_points_item_data in self.crl_distribution_points:
                crl_distribution_points_item = crl_distribution_points_item_data.to_dict()

                crl_distribution_points.append(crl_distribution_points_item)

        locations_count: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations_count, Unset):
            locations_count = []
            for locations_count_item_data in self.locations_count:
                locations_count_item = locations_count_item_data.to_dict()

                locations_count.append(locations_count_item)

        ssl_locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ssl_locations, Unset):
            ssl_locations = []
            for ssl_locations_item_data in self.ssl_locations:
                ssl_locations_item = ssl_locations_item_data.to_dict()

                ssl_locations.append(ssl_locations_item)

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()

                locations.append(locations_item)

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        certificate_key_id = self.certificate_key_id
        ca_row_index = self.ca_row_index
        ca_record_id = self.ca_record_id
        detailed_key_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.detailed_key_usage, Unset):
            detailed_key_usage = self.detailed_key_usage.to_dict()

        key_recoverable = self.key_recoverable
        curve = self.curve

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if thumbprint is not UNSET:
            field_dict["Thumbprint"] = thumbprint
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if issued_dn is not UNSET:
            field_dict["IssuedDN"] = issued_dn
        if issued_cn is not UNSET:
            field_dict["IssuedCN"] = issued_cn
        if import_date is not UNSET:
            field_dict["ImportDate"] = import_date
        if not_before is not UNSET:
            field_dict["NotBefore"] = not_before
        if not_after is not UNSET:
            field_dict["NotAfter"] = not_after
        if issuer_dn is not UNSET:
            field_dict["IssuerDN"] = issuer_dn
        if principal_id is not UNSET:
            field_dict["PrincipalId"] = principal_id
        if template_id is not UNSET:
            field_dict["TemplateId"] = template_id
        if cert_state is not UNSET:
            field_dict["CertState"] = cert_state
        if key_size_in_bits is not UNSET:
            field_dict["KeySizeInBits"] = key_size_in_bits
        if key_type is not UNSET:
            field_dict["KeyType"] = key_type
        if requester_id is not UNSET:
            field_dict["RequesterId"] = requester_id
        if issued_ou is not UNSET:
            field_dict["IssuedOU"] = issued_ou
        if issued_email is not UNSET:
            field_dict["IssuedEmail"] = issued_email
        if key_usage is not UNSET:
            field_dict["KeyUsage"] = key_usage
        if signing_algorithm is not UNSET:
            field_dict["SigningAlgorithm"] = signing_algorithm
        if cert_state_string is not UNSET:
            field_dict["CertStateString"] = cert_state_string
        if key_type_string is not UNSET:
            field_dict["KeyTypeString"] = key_type_string
        if revocation_eff_date is not UNSET:
            field_dict["RevocationEffDate"] = revocation_eff_date
        if revocation_reason is not UNSET:
            field_dict["RevocationReason"] = revocation_reason
        if revocation_comment is not UNSET:
            field_dict["RevocationComment"] = revocation_comment
        if certificate_authority_id is not UNSET:
            field_dict["CertificateAuthorityId"] = certificate_authority_id
        if certificate_authority_name is not UNSET:
            field_dict["CertificateAuthorityName"] = certificate_authority_name
        if template_name is not UNSET:
            field_dict["TemplateName"] = template_name
        if archived_key is not UNSET:
            field_dict["ArchivedKey"] = archived_key
        if has_private_key is not UNSET:
            field_dict["HasPrivateKey"] = has_private_key
        if principal_name is not UNSET:
            field_dict["PrincipalName"] = principal_name
        if cert_request_id is not UNSET:
            field_dict["CertRequestId"] = cert_request_id
        if requester_name is not UNSET:
            field_dict["RequesterName"] = requester_name
        if content_bytes is not UNSET:
            field_dict["ContentBytes"] = content_bytes
        if extended_key_usages is not UNSET:
            field_dict["ExtendedKeyUsages"] = extended_key_usages
        if subject_alt_name_elements is not UNSET:
            field_dict["SubjectAltNameElements"] = subject_alt_name_elements
        if crl_distribution_points is not UNSET:
            field_dict["CRLDistributionPoints"] = crl_distribution_points
        if locations_count is not UNSET:
            field_dict["LocationsCount"] = locations_count
        if ssl_locations is not UNSET:
            field_dict["SSLLocations"] = ssl_locations
        if locations is not UNSET:
            field_dict["Locations"] = locations
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if certificate_key_id is not UNSET:
            field_dict["CertificateKeyId"] = certificate_key_id
        if ca_row_index is not UNSET:
            field_dict["CARowIndex"] = ca_row_index
        if ca_record_id is not UNSET:
            field_dict["CARecordId"] = ca_record_id
        if detailed_key_usage is not UNSET:
            field_dict["DetailedKeyUsage"] = detailed_key_usage
        if key_recoverable is not UNSET:
            field_dict["KeyRecoverable"] = key_recoverable
        if curve is not UNSET:
            field_dict["Curve"] = curve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        thumbprint = d.pop("Thumbprint", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        issued_dn = d.pop("IssuedDN", UNSET)

        issued_cn = d.pop("IssuedCN", UNSET)

        _import_date = d.pop("ImportDate", UNSET)
        import_date: Union[Unset, datetime.datetime]
        if isinstance(_import_date, Unset):
            import_date = UNSET
        else:
            import_date = isoparse(_import_date)

        _not_before = d.pop("NotBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _not_after = d.pop("NotAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        issuer_dn = d.pop("IssuerDN", UNSET)

        principal_id = d.pop("PrincipalId", UNSET)

        template_id = d.pop("TemplateId", UNSET)

        _cert_state = d.pop("CertState", UNSET)
        cert_state: Union[Unset, ModelsCertificateRetrievalResponseCertState]
        if isinstance(_cert_state, Unset):
            cert_state = UNSET
        else:
            cert_state = ModelsCertificateRetrievalResponseCertState(_cert_state)

        key_size_in_bits = d.pop("KeySizeInBits", UNSET)

        _key_type = d.pop("KeyType", UNSET)
        key_type: Union[Unset, ModelsCertificateRetrievalResponseKeyType]
        if isinstance(_key_type, Unset):
            key_type = UNSET
        else:
            key_type = ModelsCertificateRetrievalResponseKeyType(_key_type)

        requester_id = d.pop("RequesterId", UNSET)

        issued_ou = d.pop("IssuedOU", UNSET)

        issued_email = d.pop("IssuedEmail", UNSET)

        key_usage = d.pop("KeyUsage", UNSET)

        signing_algorithm = d.pop("SigningAlgorithm", UNSET)

        cert_state_string = d.pop("CertStateString", UNSET)

        key_type_string = d.pop("KeyTypeString", UNSET)

        _revocation_eff_date = d.pop("RevocationEffDate", UNSET)
        revocation_eff_date: Union[Unset, None, datetime.datetime]
        if _revocation_eff_date is None:
            revocation_eff_date = None
        elif isinstance(_revocation_eff_date, Unset):
            revocation_eff_date = UNSET
        else:
            revocation_eff_date = isoparse(_revocation_eff_date)

        _revocation_reason = d.pop("RevocationReason", UNSET)
        revocation_reason: Union[Unset, None, ModelsCertificateRetrievalResponseRevocationReason]
        if _revocation_reason is None:
            revocation_reason = None
        elif isinstance(_revocation_reason, Unset):
            revocation_reason = UNSET
        else:
            revocation_reason = ModelsCertificateRetrievalResponseRevocationReason(_revocation_reason)

        revocation_comment = d.pop("RevocationComment", UNSET)

        certificate_authority_id = d.pop("CertificateAuthorityId", UNSET)

        certificate_authority_name = d.pop("CertificateAuthorityName", UNSET)

        template_name = d.pop("TemplateName", UNSET)

        archived_key = d.pop("ArchivedKey", UNSET)

        has_private_key = d.pop("HasPrivateKey", UNSET)

        principal_name = d.pop("PrincipalName", UNSET)

        cert_request_id = d.pop("CertRequestId", UNSET)

        requester_name = d.pop("RequesterName", UNSET)

        content_bytes = d.pop("ContentBytes", UNSET)

        extended_key_usages = []
        _extended_key_usages = d.pop("ExtendedKeyUsages", UNSET)
        for extended_key_usages_item_data in _extended_key_usages or []:
            extended_key_usages_item = ModelsCertificateRetrievalResponseExtendedKeyUsageModel.from_dict(
                extended_key_usages_item_data
            )

            extended_key_usages.append(extended_key_usages_item)

        subject_alt_name_elements = []
        _subject_alt_name_elements = d.pop("SubjectAltNameElements", UNSET)
        for subject_alt_name_elements_item_data in _subject_alt_name_elements or []:
            subject_alt_name_elements_item = ModelsCertificateRetrievalResponseSubjectAlternativeNameModel.from_dict(
                subject_alt_name_elements_item_data
            )

            subject_alt_name_elements.append(subject_alt_name_elements_item)

        crl_distribution_points = []
        _crl_distribution_points = d.pop("CRLDistributionPoints", UNSET)
        for crl_distribution_points_item_data in _crl_distribution_points or []:
            crl_distribution_points_item = ModelsCertificateRetrievalResponseCRLDistributionPointModel.from_dict(
                crl_distribution_points_item_data
            )

            crl_distribution_points.append(crl_distribution_points_item)

        locations_count = []
        _locations_count = d.pop("LocationsCount", UNSET)
        for locations_count_item_data in _locations_count or []:
            locations_count_item = ModelsCertificateRetrievalResponseLocationCountModel.from_dict(
                locations_count_item_data
            )

            locations_count.append(locations_count_item)

        ssl_locations = []
        _ssl_locations = d.pop("SSLLocations", UNSET)
        for ssl_locations_item_data in _ssl_locations or []:
            ssl_locations_item = ModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel.from_dict(
                ssl_locations_item_data
            )

            ssl_locations.append(ssl_locations_item)

        locations = []
        _locations = d.pop("Locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = ModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel.from_dict(
                locations_item_data
            )

            locations.append(locations_item)

        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, ModelsCertificateRetrievalResponseMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelsCertificateRetrievalResponseMetadata.from_dict(_metadata)

        certificate_key_id = d.pop("CertificateKeyId", UNSET)

        ca_row_index = d.pop("CARowIndex", UNSET)

        ca_record_id = d.pop("CARecordId", UNSET)

        _detailed_key_usage = d.pop("DetailedKeyUsage", UNSET)
        detailed_key_usage: Union[Unset, ModelsCertificateRetrievalResponseDetailedKeyUsageModel]
        if isinstance(_detailed_key_usage, Unset):
            detailed_key_usage = UNSET
        else:
            detailed_key_usage = ModelsCertificateRetrievalResponseDetailedKeyUsageModel.from_dict(_detailed_key_usage)

        key_recoverable = d.pop("KeyRecoverable", UNSET)

        curve = d.pop("Curve", UNSET)

        models_certificate_retrieval_response = cls(
            id=id,
            thumbprint=thumbprint,
            serial_number=serial_number,
            issued_dn=issued_dn,
            issued_cn=issued_cn,
            import_date=import_date,
            not_before=not_before,
            not_after=not_after,
            issuer_dn=issuer_dn,
            principal_id=principal_id,
            template_id=template_id,
            cert_state=cert_state,
            key_size_in_bits=key_size_in_bits,
            key_type=key_type,
            requester_id=requester_id,
            issued_ou=issued_ou,
            issued_email=issued_email,
            key_usage=key_usage,
            signing_algorithm=signing_algorithm,
            cert_state_string=cert_state_string,
            key_type_string=key_type_string,
            revocation_eff_date=revocation_eff_date,
            revocation_reason=revocation_reason,
            revocation_comment=revocation_comment,
            certificate_authority_id=certificate_authority_id,
            certificate_authority_name=certificate_authority_name,
            template_name=template_name,
            archived_key=archived_key,
            has_private_key=has_private_key,
            principal_name=principal_name,
            cert_request_id=cert_request_id,
            requester_name=requester_name,
            content_bytes=content_bytes,
            extended_key_usages=extended_key_usages,
            subject_alt_name_elements=subject_alt_name_elements,
            crl_distribution_points=crl_distribution_points,
            locations_count=locations_count,
            ssl_locations=ssl_locations,
            locations=locations,
            metadata=metadata,
            certificate_key_id=certificate_key_id,
            ca_row_index=ca_row_index,
            ca_record_id=ca_record_id,
            detailed_key_usage=detailed_key_usage,
            key_recoverable=key_recoverable,
            curve=curve,
        )

        models_certificate_retrieval_response.additional_properties = d
        return models_certificate_retrieval_response

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
