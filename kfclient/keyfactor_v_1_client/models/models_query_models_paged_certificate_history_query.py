from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.models_query_models_paged_certificate_history_query_sort_ascending import (
    ModelsQueryModelsPagedCertificateHistoryQuerySortAscending,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsQueryModelsPagedCertificateHistoryQuery")


@attr.s(auto_attribs=True)
class ModelsQueryModelsPagedCertificateHistoryQuery:
    """
    Attributes:
        page_returned (Union[Unset, int]): The current page within the result set to be returned
        return_limit (Union[Unset, int]): Maximum number of records to be returned in a single call
        sort_field (Union[Unset, str]): Field by which the results should be sorted (OperationStart, OperationEnd,
            UserName)
        sort_ascending (Union[Unset, ModelsQueryModelsPagedCertificateHistoryQuerySortAscending]): Field sort direction
            [0=ascending, 1=descending]
    """

    page_returned: Union[Unset, int] = UNSET
    return_limit: Union[Unset, int] = UNSET
    sort_field: Union[Unset, str] = UNSET
    sort_ascending: Union[Unset, ModelsQueryModelsPagedCertificateHistoryQuerySortAscending] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_returned = self.page_returned
        return_limit = self.return_limit
        sort_field = self.sort_field
        sort_ascending: Union[Unset, int] = UNSET
        if not isinstance(self.sort_ascending, Unset):
            sort_ascending = self.sort_ascending.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_returned is not UNSET:
            field_dict["PageReturned"] = page_returned
        if return_limit is not UNSET:
            field_dict["ReturnLimit"] = return_limit
        if sort_field is not UNSET:
            field_dict["SortField"] = sort_field
        if sort_ascending is not UNSET:
            field_dict["SortAscending"] = sort_ascending

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_returned = d.pop("PageReturned", UNSET)

        return_limit = d.pop("ReturnLimit", UNSET)

        sort_field = d.pop("SortField", UNSET)

        _sort_ascending = d.pop("SortAscending", UNSET)
        sort_ascending: Union[Unset, ModelsQueryModelsPagedCertificateHistoryQuerySortAscending]
        if isinstance(_sort_ascending, Unset):
            sort_ascending = UNSET
        else:
            sort_ascending = ModelsQueryModelsPagedCertificateHistoryQuerySortAscending(_sort_ascending)

        models_query_models_paged_certificate_history_query = cls(
            page_returned=page_returned,
            return_limit=return_limit,
            sort_field=sort_field,
            sort_ascending=sort_ascending,
        )

        models_query_models_paged_certificate_history_query.additional_properties = d
        return models_query_models_paged_certificate_history_query

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
