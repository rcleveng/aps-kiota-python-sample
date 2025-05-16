from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .folder_contents_data import FolderContents_data
    from .folder_contents_links import FolderContents_links
    from .json_api_version import Json_api_version
    from .version_data import VersionData

@dataclass
class FolderContents(AdditionalDataHolder, Parsable):
    """
    Successful retrieval of the folder contents collection associated with a specific folder.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The properties of an item or folder, as the case may be.
    data: Optional[list[FolderContents_data]] = None
    # An array of objects, where each element represents a resource included within this resource.
    included: Optional[list[VersionData]] = None
    # The JSON API object.
    jsonapi: Optional[Json_api_version] = None
    # Information on links for this resource. ``first``, ``prev``, and ``next`` are available only when the response is paginated.
    links: Optional[FolderContents_links] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderContents:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderContents
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderContents()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .folder_contents_data import FolderContents_data
        from .folder_contents_links import FolderContents_links
        from .json_api_version import Json_api_version
        from .version_data import VersionData

        from .folder_contents_data import FolderContents_data
        from .folder_contents_links import FolderContents_links
        from .json_api_version import Json_api_version
        from .version_data import VersionData

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(FolderContents_data)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(VersionData)),
            "jsonapi": lambda n : setattr(self, 'jsonapi', n.get_object_value(Json_api_version)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(FolderContents_links)),
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
        writer.write_collection_of_object_values("included", self.included)
        writer.write_object_value("jsonapi", self.jsonapi)
        writer.write_object_value("links", self.links)
        writer.write_additional_data_value(self.additional_data)
    

