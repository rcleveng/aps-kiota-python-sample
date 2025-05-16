from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
    from .project_data_attributes import ProjectData_attributes
    from .project_data_relationships import ProjectData_relationships
    from .type_project import Type_project

@dataclass
class ProjectData(AdditionalDataHolder, Parsable):
    """
    A container of data describing a project.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The properties of the project.
    attributes: Optional[ProjectData_attributes] = None
    # The ID that uniquely identifies the project.
    id: Optional[str] = None
    # Information on links to this resource.
    links: Optional[Json_api_links_self_and_web_view] = None
    # Contains links to resources related to this project.
    relationships: Optional[ProjectData_relationships] = None
    # The type of the resource. Possible values are ``projects``.
    type: Optional[Type_project] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProjectData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProjectData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProjectData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
        from .project_data_attributes import ProjectData_attributes
        from .project_data_relationships import ProjectData_relationships
        from .type_project import Type_project

        from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
        from .project_data_attributes import ProjectData_attributes
        from .project_data_relationships import ProjectData_relationships
        from .type_project import Type_project

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(ProjectData_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_links_self_and_web_view)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(ProjectData_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_project)),
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
        writer.write_object_value("attributes", self.attributes)
        writer.write_str_value("id", self.id)
        writer.write_object_value("links", self.links)
        writer.write_object_value("relationships", self.relationships)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

