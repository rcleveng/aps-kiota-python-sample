from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_relationships_links_folder_parent import Json_api_relationships_links_folder_parent
    from .json_api_relationships_links_internal import Json_api_relationships_links_internal
    from .json_api_relationships_links_links import Json_api_relationships_links_links
    from .json_api_relationships_links_refs import Json_api_relationships_links_refs

@dataclass
class FolderData_relationships(AdditionalDataHolder, Parsable):
    """
    Contains links to resources that are directly related to this folder.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information on resources that are found under this resource.
    contents: Optional[Json_api_relationships_links_internal] = None
    # Information on the link resources found in this resource.
    links: Optional[Json_api_relationships_links_links] = None
    # Information on the parent of this resource in the folder hierarchy.
    parent: Optional[Json_api_relationships_links_folder_parent] = None
    # Information on other resources that have a custom relationship with this resource.
    refs: Optional[Json_api_relationships_links_refs] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderData_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderData_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderData_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_relationships_links_folder_parent import Json_api_relationships_links_folder_parent
        from .json_api_relationships_links_internal import Json_api_relationships_links_internal
        from .json_api_relationships_links_links import Json_api_relationships_links_links
        from .json_api_relationships_links_refs import Json_api_relationships_links_refs

        from .json_api_relationships_links_folder_parent import Json_api_relationships_links_folder_parent
        from .json_api_relationships_links_internal import Json_api_relationships_links_internal
        from .json_api_relationships_links_links import Json_api_relationships_links_links
        from .json_api_relationships_links_refs import Json_api_relationships_links_refs

        fields: dict[str, Callable[[Any], None]] = {
            "contents": lambda n : setattr(self, 'contents', n.get_object_value(Json_api_relationships_links_internal)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_relationships_links_links)),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(Json_api_relationships_links_folder_parent)),
            "refs": lambda n : setattr(self, 'refs', n.get_object_value(Json_api_relationships_links_refs)),
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
        writer.write_object_value("contents", self.contents)
        writer.write_object_value("links", self.links)
        writer.write_object_value("parent", self.parent)
        writer.write_object_value("refs", self.refs)
        writer.write_additional_data_value(self.additional_data)
    

