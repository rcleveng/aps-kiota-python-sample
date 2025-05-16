from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_version import Json_api_version
    from .pagination_info import PaginationInfo
    from .project_data import ProjectData

@dataclass
class Projects(AdditionalDataHolder, Parsable):
    """
    An object representing a collection of projects within a hub.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects where each object represents a project.
    data: Optional[list[ProjectData]] = None
    # The JSON API object.
    jsonapi: Optional[Json_api_version] = None
    # An object that is returned with responses that can be split across multiple pages. "Next," "Previous," and "First" are available only if the response is split across multiple pages.
    links: Optional[PaginationInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Projects:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Projects
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Projects()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_version import Json_api_version
        from .pagination_info import PaginationInfo
        from .project_data import ProjectData

        from .json_api_version import Json_api_version
        from .pagination_info import PaginationInfo
        from .project_data import ProjectData

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(ProjectData)),
            "jsonapi": lambda n : setattr(self, 'jsonapi', n.get_object_value(Json_api_version)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(PaginationInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("data", self.data)
        writer.write_object_value("jsonapi", self.jsonapi)
        writer.write_object_value("links", self.links)
        writer.write_additional_data_value(self.additional_data)
    

