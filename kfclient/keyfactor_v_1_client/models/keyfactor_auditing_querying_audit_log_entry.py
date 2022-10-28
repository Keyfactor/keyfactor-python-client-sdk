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

from ..models.keyfactor_auditing_querying_audit_log_entry_level import KeyfactorAuditingQueryingAuditLogEntryLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorAuditingQueryingAuditLogEntry")


@attr.s(auto_attribs=True)
class KeyfactorAuditingQueryingAuditLogEntry:
    """
    Attributes:
        id (Union[Unset, int]):
        timestamp (Union[Unset, datetime.datetime]):
        message (Union[Unset, str]):
        signature (Union[Unset, str]):
        category (Union[Unset, int]):
        operation (Union[Unset, int]):
        level (Union[Unset, KeyfactorAuditingQueryingAuditLogEntryLevel]):
        user (Union[Unset, str]):
        entity_type (Union[Unset, str]):
        audit_identifier (Union[Unset, str]):
        immutable_identifier (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    message: Union[Unset, str] = UNSET
    signature: Union[Unset, str] = UNSET
    category: Union[Unset, int] = UNSET
    operation: Union[Unset, int] = UNSET
    level: Union[Unset, KeyfactorAuditingQueryingAuditLogEntryLevel] = UNSET
    user: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    audit_identifier: Union[Unset, str] = UNSET
    immutable_identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        message = self.message
        signature = self.signature
        category = self.category
        operation = self.operation
        level: Union[Unset, int] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        user = self.user
        entity_type = self.entity_type
        audit_identifier = self.audit_identifier
        immutable_identifier = self.immutable_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp
        if message is not UNSET:
            field_dict["Message"] = message
        if signature is not UNSET:
            field_dict["Signature"] = signature
        if category is not UNSET:
            field_dict["Category"] = category
        if operation is not UNSET:
            field_dict["Operation"] = operation
        if level is not UNSET:
            field_dict["Level"] = level
        if user is not UNSET:
            field_dict["User"] = user
        if entity_type is not UNSET:
            field_dict["EntityType"] = entity_type
        if audit_identifier is not UNSET:
            field_dict["AuditIdentifier"] = audit_identifier
        if immutable_identifier is not UNSET:
            field_dict["ImmutableIdentifier"] = immutable_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        _timestamp = d.pop("Timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        message = d.pop("Message", UNSET)

        signature = d.pop("Signature", UNSET)

        category = d.pop("Category", UNSET)

        operation = d.pop("Operation", UNSET)

        _level = d.pop("Level", UNSET)
        level: Union[Unset, KeyfactorAuditingQueryingAuditLogEntryLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = KeyfactorAuditingQueryingAuditLogEntryLevel(_level)

        user = d.pop("User", UNSET)

        entity_type = d.pop("EntityType", UNSET)

        audit_identifier = d.pop("AuditIdentifier", UNSET)

        immutable_identifier = d.pop("ImmutableIdentifier", UNSET)

        keyfactor_auditing_querying_audit_log_entry = cls(
            id=id,
            timestamp=timestamp,
            message=message,
            signature=signature,
            category=category,
            operation=operation,
            level=level,
            user=user,
            entity_type=entity_type,
            audit_identifier=audit_identifier,
            immutable_identifier=immutable_identifier,
        )

        keyfactor_auditing_querying_audit_log_entry.additional_properties = d
        return keyfactor_auditing_querying_audit_log_entry

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
