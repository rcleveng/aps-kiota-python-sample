from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .type_folder import Type_folder

@dataclass
class FolderPayload_data_relationships_parent_data(AdditionalDataHolder, Parsable):
    """
    The data about the parent of the folder to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The URN of the parent folder. For information on how to find the URN, see the initial steps of the [Download a File](/en/docs/data/v2/tutorials/download-file/) tutorial.Note that for BIM 360 Docs, new folders must be created within an existing folder (e.g., the Plans or Project Files folders), and not directly within the root folder. Permissions, visibility (e.g., ``items:autodesk.bim360:Document`` or ``items:autodesk.bim360:File``), and actions (e.g., OCR) are inherited from the existing parent folder. New folders also inherit subscriptions such as the notifications sent when files are added to a folder.
    id: Optional[str] = None
    # The type of the resource. Possible values are ``folders``.
    type: Optional[Type_folder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderPayload_data_relationships_parent_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderPayload_data_relationships_parent_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderPayload_data_relationships_parent_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .type_folder import Type_folder

        from .type_folder import Type_folder

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

