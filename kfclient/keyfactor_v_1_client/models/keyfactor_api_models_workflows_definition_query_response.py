from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorApiModelsWorkflowsDefinitionQueryResponse")


@attr.s(auto_attribs=True)
class KeyfactorApiModelsWorkflowsDefinitionQueryResponse:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 00000000-0000-0000-0000-000000000000.
        display_name (Union[Unset, str]):
        key (Union[Unset, str]):
        key_display_name (Union[Unset, str]):
        workflow_type (Union[Unset, str]):
        draft_version (Union[Unset, int]):
        published_version (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    key_display_name: Union[Unset, str] = UNSET
    workflow_type: Union[Unset, str] = UNSET
    draft_version: Union[Unset, int] = UNSET
    published_version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        key = self.key
        key_display_name = self.key_display_name
        workflow_type = self.workflow_type
        draft_version = self.draft_version
        published_version = self.published_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if key is not UNSET:
            field_dict["Key"] = key
        if key_display_name is not UNSET:
            field_dict["KeyDisplayName"] = key_display_name
        if workflow_type is not UNSET:
            field_dict["WorkflowType"] = workflow_type
        if draft_version is not UNSET:
            field_dict["DraftVersion"] = draft_version
        if published_version is not UNSET:
            field_dict["PublishedVersion"] = published_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        key = d.pop("Key", UNSET)

        key_display_name = d.pop("KeyDisplayName", UNSET)

        workflow_type = d.pop("WorkflowType", UNSET)

        draft_version = d.pop("DraftVersion", UNSET)

        published_version = d.pop("PublishedVersion", UNSET)

        keyfactor_api_models_workflows_definition_query_response = cls(
            id=id,
            display_name=display_name,
            key=key,
            key_display_name=key_display_name,
            workflow_type=workflow_type,
            draft_version=draft_version,
            published_version=published_version,
        )

        keyfactor_api_models_workflows_definition_query_response.additional_properties = d
        return keyfactor_api_models_workflows_definition_query_response

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
