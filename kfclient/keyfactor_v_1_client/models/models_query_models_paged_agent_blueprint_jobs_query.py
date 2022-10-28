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

from ..models.models_query_models_paged_agent_blueprint_jobs_query_sort_ascending import (
    ModelsQueryModelsPagedAgentBlueprintJobsQuerySortAscending,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsQueryModelsPagedAgentBlueprintJobsQuery")


@attr.s(auto_attribs=True)
class ModelsQueryModelsPagedAgentBlueprintJobsQuery:
    """
    Attributes:
        page_returned (Union[Unset, int]): The current page within the result set to be returned
        skip_count (Union[Unset, int]): Number of records to be skipped before inclusion in the result set
        return_limit (Union[Unset, int]): Maximum number of records to be returned in a single call
        sort_field (Union[Unset, str]): Field by which the results should be sorted (OperationStart, OperationEnd,
            UserName)
        sort_ascending (Union[Unset, ModelsQueryModelsPagedAgentBlueprintJobsQuerySortAscending]): Field sort direction
            [0=ascending, 1=descending]
    """

    page_returned: Union[Unset, int] = UNSET
    skip_count: Union[Unset, int] = UNSET
    return_limit: Union[Unset, int] = UNSET
    sort_field: Union[Unset, str] = UNSET
    sort_ascending: Union[Unset, ModelsQueryModelsPagedAgentBlueprintJobsQuerySortAscending] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_returned = self.page_returned
        skip_count = self.skip_count
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
        if skip_count is not UNSET:
            field_dict["SkipCount"] = skip_count
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

        skip_count = d.pop("SkipCount", UNSET)

        return_limit = d.pop("ReturnLimit", UNSET)

        sort_field = d.pop("SortField", UNSET)

        _sort_ascending = d.pop("SortAscending", UNSET)
        sort_ascending: Union[Unset, ModelsQueryModelsPagedAgentBlueprintJobsQuerySortAscending]
        if isinstance(_sort_ascending, Unset):
            sort_ascending = UNSET
        else:
            sort_ascending = ModelsQueryModelsPagedAgentBlueprintJobsQuerySortAscending(_sort_ascending)

        models_query_models_paged_agent_blueprint_jobs_query = cls(
            page_returned=page_returned,
            skip_count=skip_count,
            return_limit=return_limit,
            sort_field=sort_field,
            sort_ascending=sort_ascending,
        )

        models_query_models_paged_agent_blueprint_jobs_query.additional_properties = d
        return models_query_models_paged_agent_blueprint_jobs_query

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
