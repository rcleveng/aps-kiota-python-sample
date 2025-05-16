from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .modify_folder_payload_data_attributes import ModifyFolderPayload_data_attributes
    from .modify_folder_payload_data_relationships import ModifyFolderPayload_data_relationships
    from .type_folder import Type_folder

@dataclass
class ModifyFolderPayload_data(AdditionalDataHolder, Parsable):
    """
    The data that describes what must be modified.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The properties of the folder that can be modified.
    attributes: Optional[ModifyFolderPayload_data_attributes] = None
    # The URN of the folder.For information on how to find the URN, see the initial steps of the [Download a File](/en/docs/data/v2/tutorials/download-file/) tutorial.Note that this should NOT be URL-encoded.
    id: Optional[str] = None
    # Contains links to resources that are directly related to this folder.
    relationships: Optional[ModifyFolderPayload_data_relationships] = None
    # The type of the resource. Possible values are ``folders``.
    type: Optional[Type_folder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModifyFolderPayload_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModifyFolderPayload_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModifyFolderPayload_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .modify_folder_payload_data_attributes import ModifyFolderPayload_data_attributes
        from .modify_folder_payload_data_relationships import ModifyFolderPayload_data_relationships
        from .type_folder import Type_folder

        from .modify_folder_payload_data_attributes import ModifyFolderPayload_data_attributes
        from .modify_folder_payload_data_relationships import ModifyFolderPayload_data_relationships
        from .type_folder import Type_folder

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(ModifyFolderPayload_data_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(ModifyFolderPayload_data_relationships)),
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
        writer.write_str_value("id", self.id)
        writer.write_object_value("relationships", self.relationships)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

