from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
from ..models.models_certificate_authorities_certificate_authority_request_allowed_enrollment_types import (
    ModelsCertificateAuthoritiesCertificateAuthorityRequestAllowedEnrollmentTypes,
)
from ..models.models_certificate_authorities_certificate_authority_request_ca_type import (
    ModelsCertificateAuthoritiesCertificateAuthorityRequestCAType,
)
from ..models.models_certificate_authorities_certificate_authority_request_key_retention import (
    ModelsCertificateAuthoritiesCertificateAuthorityRequestKeyRetention,
)
from ..models.models_keyfactor_api_secret import ModelsKeyfactorAPISecret
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCertificateAuthoritiesCertificateAuthorityRequest")


@attr.s(auto_attribs=True)
class ModelsCertificateAuthoritiesCertificateAuthorityRequest:
    """
    Attributes:
        id (Union[Unset, int]):
        logical_name (Union[Unset, str]):
        host_name (Union[Unset, str]):
        delegate (Union[Unset, bool]):
        delegate_enrollment (Union[Unset, bool]):
        forest_root (Union[Unset, str]):
        configuration_tenant (Union[Unset, str]):
        remote (Union[Unset, bool]):
        agent (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        standalone (Union[Unset, bool]):
        monitor_thresholds (Union[Unset, bool]):
        issuance_max (Union[Unset, int]):
        issuance_min (Union[Unset, int]):
        failure_max (Union[Unset, int]):
        rfc_enforcement (Union[Unset, bool]):
        properties (Union[Unset, str]):
        allowed_enrollment_types (Union[Unset,
            ModelsCertificateAuthoritiesCertificateAuthorityRequestAllowedEnrollmentTypes]):
        key_retention (Union[Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestKeyRetention]):
        key_retention_days (Union[Unset, int]):
        explicit_credentials (Union[Unset, bool]):
        subscriber_terms (Union[Unset, bool]):
        explicit_user (Union[Unset, str]):
        explicit_password (Union[Unset, ModelsKeyfactorAPISecret]):
        use_allowed_requesters (Union[Unset, bool]):
        allowed_requesters (Union[Unset, List[str]]):
        full_scan (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        incremental_scan (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        threshold_check (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        auth_certificate_password (Union[Unset, ModelsKeyfactorAPISecret]):
        auth_certificate (Union[Unset, ModelsKeyfactorAPISecret]):
        ca_type (Union[Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestCAType]):
        enforce_unique_dn (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    logical_name: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    delegate: Union[Unset, bool] = UNSET
    delegate_enrollment: Union[Unset, bool] = UNSET
    forest_root: Union[Unset, str] = UNSET
    configuration_tenant: Union[Unset, str] = UNSET
    remote: Union[Unset, bool] = UNSET
    agent: Union[Unset, str] = UNSET
    standalone: Union[Unset, bool] = UNSET
    monitor_thresholds: Union[Unset, bool] = UNSET
    issuance_max: Union[Unset, int] = UNSET
    issuance_min: Union[Unset, int] = UNSET
    failure_max: Union[Unset, int] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    properties: Union[Unset, str] = UNSET
    allowed_enrollment_types: Union[
        Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestAllowedEnrollmentTypes
    ] = UNSET
    key_retention: Union[Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestKeyRetention] = UNSET
    key_retention_days: Union[Unset, int] = UNSET
    explicit_credentials: Union[Unset, bool] = UNSET
    subscriber_terms: Union[Unset, bool] = UNSET
    explicit_user: Union[Unset, str] = UNSET
    explicit_password: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    use_allowed_requesters: Union[Unset, bool] = UNSET
    allowed_requesters: Union[Unset, List[str]] = UNSET
    full_scan: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    incremental_scan: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    threshold_check: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule] = UNSET
    auth_certificate_password: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    auth_certificate: Union[Unset, ModelsKeyfactorAPISecret] = UNSET
    ca_type: Union[Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestCAType] = UNSET
    enforce_unique_dn: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        logical_name = self.logical_name
        host_name = self.host_name
        delegate = self.delegate
        delegate_enrollment = self.delegate_enrollment
        forest_root = self.forest_root
        configuration_tenant = self.configuration_tenant
        remote = self.remote
        agent = self.agent
        standalone = self.standalone
        monitor_thresholds = self.monitor_thresholds
        issuance_max = self.issuance_max
        issuance_min = self.issuance_min
        failure_max = self.failure_max
        rfc_enforcement = self.rfc_enforcement
        properties = self.properties
        allowed_enrollment_types: Union[Unset, int] = UNSET
        if not isinstance(self.allowed_enrollment_types, Unset):
            allowed_enrollment_types = self.allowed_enrollment_types.value

        key_retention: Union[Unset, int] = UNSET
        if not isinstance(self.key_retention, Unset):
            key_retention = self.key_retention.value

        key_retention_days = self.key_retention_days
        explicit_credentials = self.explicit_credentials
        subscriber_terms = self.subscriber_terms
        explicit_user = self.explicit_user
        explicit_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.explicit_password, Unset):
            explicit_password = self.explicit_password.to_dict()

        use_allowed_requesters = self.use_allowed_requesters
        allowed_requesters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_requesters, Unset):
            allowed_requesters = self.allowed_requesters

        full_scan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full_scan, Unset):
            full_scan = self.full_scan.to_dict()

        incremental_scan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incremental_scan, Unset):
            incremental_scan = self.incremental_scan.to_dict()

        threshold_check: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.threshold_check, Unset):
            threshold_check = self.threshold_check.to_dict()

        auth_certificate_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_certificate_password, Unset):
            auth_certificate_password = self.auth_certificate_password.to_dict()

        auth_certificate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_certificate, Unset):
            auth_certificate = self.auth_certificate.to_dict()

        ca_type: Union[Unset, int] = UNSET
        if not isinstance(self.ca_type, Unset):
            ca_type = self.ca_type.value

        enforce_unique_dn = self.enforce_unique_dn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if logical_name is not UNSET:
            field_dict["LogicalName"] = logical_name
        if host_name is not UNSET:
            field_dict["HostName"] = host_name
        if delegate is not UNSET:
            field_dict["Delegate"] = delegate
        if delegate_enrollment is not UNSET:
            field_dict["DelegateEnrollment"] = delegate_enrollment
        if forest_root is not UNSET:
            field_dict["ForestRoot"] = forest_root
        if configuration_tenant is not UNSET:
            field_dict["ConfigurationTenant"] = configuration_tenant
        if remote is not UNSET:
            field_dict["Remote"] = remote
        if agent is not UNSET:
            field_dict["Agent"] = agent
        if standalone is not UNSET:
            field_dict["Standalone"] = standalone
        if monitor_thresholds is not UNSET:
            field_dict["MonitorThresholds"] = monitor_thresholds
        if issuance_max is not UNSET:
            field_dict["IssuanceMax"] = issuance_max
        if issuance_min is not UNSET:
            field_dict["IssuanceMin"] = issuance_min
        if failure_max is not UNSET:
            field_dict["FailureMax"] = failure_max
        if rfc_enforcement is not UNSET:
            field_dict["RFCEnforcement"] = rfc_enforcement
        if properties is not UNSET:
            field_dict["Properties"] = properties
        if allowed_enrollment_types is not UNSET:
            field_dict["AllowedEnrollmentTypes"] = allowed_enrollment_types
        if key_retention is not UNSET:
            field_dict["KeyRetention"] = key_retention
        if key_retention_days is not UNSET:
            field_dict["KeyRetentionDays"] = key_retention_days
        if explicit_credentials is not UNSET:
            field_dict["ExplicitCredentials"] = explicit_credentials
        if subscriber_terms is not UNSET:
            field_dict["SubscriberTerms"] = subscriber_terms
        if explicit_user is not UNSET:
            field_dict["ExplicitUser"] = explicit_user
        if explicit_password is not UNSET:
            field_dict["ExplicitPassword"] = explicit_password
        if use_allowed_requesters is not UNSET:
            field_dict["UseAllowedRequesters"] = use_allowed_requesters
        if allowed_requesters is not UNSET:
            field_dict["AllowedRequesters"] = allowed_requesters
        if full_scan is not UNSET:
            field_dict["FullScan"] = full_scan
        if incremental_scan is not UNSET:
            field_dict["IncrementalScan"] = incremental_scan
        if threshold_check is not UNSET:
            field_dict["ThresholdCheck"] = threshold_check
        if auth_certificate_password is not UNSET:
            field_dict["AuthCertificatePassword"] = auth_certificate_password
        if auth_certificate is not UNSET:
            field_dict["AuthCertificate"] = auth_certificate
        if ca_type is not UNSET:
            field_dict["CAType"] = ca_type
        if enforce_unique_dn is not UNSET:
            field_dict["EnforceUniqueDN"] = enforce_unique_dn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        logical_name = d.pop("LogicalName", UNSET)

        host_name = d.pop("HostName", UNSET)

        delegate = d.pop("Delegate", UNSET)

        delegate_enrollment = d.pop("DelegateEnrollment", UNSET)

        forest_root = d.pop("ForestRoot", UNSET)

        configuration_tenant = d.pop("ConfigurationTenant", UNSET)

        remote = d.pop("Remote", UNSET)

        agent = d.pop("Agent", UNSET)

        standalone = d.pop("Standalone", UNSET)

        monitor_thresholds = d.pop("MonitorThresholds", UNSET)

        issuance_max = d.pop("IssuanceMax", UNSET)

        issuance_min = d.pop("IssuanceMin", UNSET)

        failure_max = d.pop("FailureMax", UNSET)

        rfc_enforcement = d.pop("RFCEnforcement", UNSET)

        properties = d.pop("Properties", UNSET)

        _allowed_enrollment_types = d.pop("AllowedEnrollmentTypes", UNSET)
        allowed_enrollment_types: Union[
            Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestAllowedEnrollmentTypes
        ]
        if isinstance(_allowed_enrollment_types, Unset):
            allowed_enrollment_types = UNSET
        else:
            allowed_enrollment_types = ModelsCertificateAuthoritiesCertificateAuthorityRequestAllowedEnrollmentTypes(
                _allowed_enrollment_types
            )

        _key_retention = d.pop("KeyRetention", UNSET)
        key_retention: Union[Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestKeyRetention]
        if isinstance(_key_retention, Unset):
            key_retention = UNSET
        else:
            key_retention = ModelsCertificateAuthoritiesCertificateAuthorityRequestKeyRetention(_key_retention)

        key_retention_days = d.pop("KeyRetentionDays", UNSET)

        explicit_credentials = d.pop("ExplicitCredentials", UNSET)

        subscriber_terms = d.pop("SubscriberTerms", UNSET)

        explicit_user = d.pop("ExplicitUser", UNSET)

        _explicit_password = d.pop("ExplicitPassword", UNSET)
        explicit_password: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_explicit_password, Unset):
            explicit_password = UNSET
        else:
            explicit_password = ModelsKeyfactorAPISecret.from_dict(_explicit_password)

        use_allowed_requesters = d.pop("UseAllowedRequesters", UNSET)

        allowed_requesters = cast(List[str], d.pop("AllowedRequesters", UNSET))

        _full_scan = d.pop("FullScan", UNSET)
        full_scan: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_full_scan, Unset):
            full_scan = UNSET
        else:
            full_scan = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_full_scan)

        _incremental_scan = d.pop("IncrementalScan", UNSET)
        incremental_scan: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_incremental_scan, Unset):
            incremental_scan = UNSET
        else:
            incremental_scan = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_incremental_scan)

        _threshold_check = d.pop("ThresholdCheck", UNSET)
        threshold_check: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_threshold_check, Unset):
            threshold_check = UNSET
        else:
            threshold_check = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_threshold_check)

        _auth_certificate_password = d.pop("AuthCertificatePassword", UNSET)
        auth_certificate_password: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_auth_certificate_password, Unset):
            auth_certificate_password = UNSET
        else:
            auth_certificate_password = ModelsKeyfactorAPISecret.from_dict(_auth_certificate_password)

        _auth_certificate = d.pop("AuthCertificate", UNSET)
        auth_certificate: Union[Unset, ModelsKeyfactorAPISecret]
        if isinstance(_auth_certificate, Unset):
            auth_certificate = UNSET
        else:
            auth_certificate = ModelsKeyfactorAPISecret.from_dict(_auth_certificate)

        _ca_type = d.pop("CAType", UNSET)
        ca_type: Union[Unset, ModelsCertificateAuthoritiesCertificateAuthorityRequestCAType]
        if isinstance(_ca_type, Unset):
            ca_type = UNSET
        else:
            ca_type = ModelsCertificateAuthoritiesCertificateAuthorityRequestCAType(_ca_type)

        enforce_unique_dn = d.pop("EnforceUniqueDN", UNSET)

        models_certificate_authorities_certificate_authority_request = cls(
            id=id,
            logical_name=logical_name,
            host_name=host_name,
            delegate=delegate,
            delegate_enrollment=delegate_enrollment,
            forest_root=forest_root,
            configuration_tenant=configuration_tenant,
            remote=remote,
            agent=agent,
            standalone=standalone,
            monitor_thresholds=monitor_thresholds,
            issuance_max=issuance_max,
            issuance_min=issuance_min,
            failure_max=failure_max,
            rfc_enforcement=rfc_enforcement,
            properties=properties,
            allowed_enrollment_types=allowed_enrollment_types,
            key_retention=key_retention,
            key_retention_days=key_retention_days,
            explicit_credentials=explicit_credentials,
            subscriber_terms=subscriber_terms,
            explicit_user=explicit_user,
            explicit_password=explicit_password,
            use_allowed_requesters=use_allowed_requesters,
            allowed_requesters=allowed_requesters,
            full_scan=full_scan,
            incremental_scan=incremental_scan,
            threshold_check=threshold_check,
            auth_certificate_password=auth_certificate_password,
            auth_certificate=auth_certificate,
            ca_type=ca_type,
            enforce_unique_dn=enforce_unique_dn,
        )

        models_certificate_authorities_certificate_authority_request.additional_properties = d
        return models_certificate_authorities_certificate_authority_request

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
