from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_relationships_links_internal_resource import Json_api_relationships_links_internal_resource
    from .json_api_relationships_links_only_bim import Json_api_relationships_links_only_bim
    from .json_api_relationships_links_root_folder import Json_api_relationships_links_root_folder
    from .project_data_relationships_top_folders import ProjectData_relationships_topFolders

@dataclass
class ProjectData_relationships(AdditionalDataHolder, Parsable):
    """
    Contains links to resources related to this project.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains links to resources that are external to the data domain service. This is available only with BIM360.
    checklists: Optional[Json_api_relationships_links_only_bim] = None
    # Contains links to resources that are external to the data domain service. This is available only with BIM360.
    cost: Optional[Json_api_relationships_links_only_bim] = None
    # Information on the resources above this resource in the hierarchy.
    hub: Optional[Json_api_relationships_links_internal_resource] = None
    # Contains links to resources that are external to the data domain service. This is available only with BIM360.
    issues: Optional[Json_api_relationships_links_only_bim] = None
    # Contains links to resources that are external to the data domain service. This is available only with BIM360.
    locations: Optional[Json_api_relationships_links_only_bim] = None
    # Contains links to resources that are external to the data domain service. This is available only with BIM360.
    markups: Optional[Json_api_relationships_links_only_bim] = None
    # Contains links to resources that are external to the data domain service. This is available only with BIM360.
    rfis: Optional[Json_api_relationships_links_only_bim] = None
    # Information about the root folder of a project.
    root_folder: Optional[Json_api_relationships_links_root_folder] = None
    # Contains links to resources that are external to the data domain service. This is available only with BIM360.
    submittals: Optional[Json_api_relationships_links_only_bim] = None
    # Information about the highest level folders you have access to.
    top_folders: Optional[ProjectData_relationships_topFolders] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProjectData_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProjectData_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProjectData_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_relationships_links_internal_resource import Json_api_relationships_links_internal_resource
        from .json_api_relationships_links_only_bim import Json_api_relationships_links_only_bim
        from .json_api_relationships_links_root_folder import Json_api_relationships_links_root_folder
        from .project_data_relationships_top_folders import ProjectData_relationships_topFolders

        from .json_api_relationships_links_internal_resource import Json_api_relationships_links_internal_resource
        from .json_api_relationships_links_only_bim import Json_api_relationships_links_only_bim
        from .json_api_relationships_links_root_folder import Json_api_relationships_links_root_folder
        from .project_data_relationships_top_folders import ProjectData_relationships_topFolders

        fields: dict[str, Callable[[Any], None]] = {
            "checklists": lambda n : setattr(self, 'checklists', n.get_object_value(Json_api_relationships_links_only_bim)),
            "cost": lambda n : setattr(self, 'cost', n.get_object_value(Json_api_relationships_links_only_bim)),
            "hub": lambda n : setattr(self, 'hub', n.get_object_value(Json_api_relationships_links_internal_resource)),
            "issues": lambda n : setattr(self, 'issues', n.get_object_value(Json_api_relationships_links_only_bim)),
            "locations": lambda n : setattr(self, 'locations', n.get_object_value(Json_api_relationships_links_only_bim)),
            "markups": lambda n : setattr(self, 'markups', n.get_object_value(Json_api_relationships_links_only_bim)),
            "rfis": lambda n : setattr(self, 'rfis', n.get_object_value(Json_api_relationships_links_only_bim)),
            "rootFolder": lambda n : setattr(self, 'root_folder', n.get_object_value(Json_api_relationships_links_root_folder)),
            "submittals": lambda n : setattr(self, 'submittals', n.get_object_value(Json_api_relationships_links_only_bim)),
            "topFolders": lambda n : setattr(self, 'top_folders', n.get_object_value(ProjectData_relationships_topFolders)),
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
        writer.write_object_value("checklists", self.checklists)
        writer.write_object_value("cost", self.cost)
        writer.write_object_value("hub", self.hub)
        writer.write_object_value("issues", self.issues)
        writer.write_object_value("locations", self.locations)
        writer.write_object_value("markups", self.markups)
        writer.write_object_value("rfis", self.rfis)
        writer.write_object_value("rootFolder", self.root_folder)
        writer.write_object_value("submittals", self.submittals)
        writer.write_object_value("topFolders", self.top_folders)
        writer.write_additional_data_value(self.additional_data)
    

