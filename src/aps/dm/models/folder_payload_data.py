from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .folder_payload_data_attributes import FolderPayload_data_attributes
    from .folder_payload_data_relationships import FolderPayload_data_relationships
    from .type_folder import Type_folder

@dataclass
class FolderPayload_data(AdditionalDataHolder, Parsable):
    """
    The data that describes the folder to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The properties of the folder to be created.
    attributes: Optional[FolderPayload_data_attributes] = None
    # A container of links to resources that are related to the folder to be created.
    relationships: Optional[FolderPayload_data_relationships] = None
    # The type of the resource. Possible values are ``folders``.
    type: Optional[Type_folder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderPayload_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderPayload_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderPayload_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .folder_payload_data_attributes import FolderPayload_data_attributes
        from .folder_payload_data_relationships import FolderPayload_data_relationships
        from .type_folder import Type_folder

        from .folder_payload_data_attributes import FolderPayload_data_attributes
        from .folder_payload_data_relationships import FolderPayload_data_relationships
        from .type_folder import Type_folder

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(FolderPayload_data_attributes)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(FolderPayload_data_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_folder)),
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
        writer.write_object_value("relationships", self.relationships)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

