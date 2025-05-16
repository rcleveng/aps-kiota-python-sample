from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .folder_payload_data_relationships_parent import FolderPayload_data_relationships_parent

@dataclass
class FolderPayload_data_relationships(AdditionalDataHolder, Parsable):
    """
    A container of links to resources that are related to the folder to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information about the parent of the new folder in the folder hierarchy.
    parent: Optional[FolderPayload_data_relationships_parent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderPayload_data_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderPayload_data_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderPayload_data_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .folder_payload_data_relationships_parent import FolderPayload_data_relationships_parent

        from .folder_payload_data_relationships_parent import FolderPayload_data_relationships_parent

        fields: dict[str, Callable[[Any], None]] = {
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(FolderPayload_data_relationships_parent)),
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
        writer.write_object_value("parent", self.parent)
        writer.write_additional_data_value(self.additional_data)
    

