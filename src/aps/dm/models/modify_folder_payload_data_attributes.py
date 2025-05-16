from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ModifyFolderPayload_data_attributes(AdditionalDataHolder, Parsable):
    """
    The properties of the folder that can be modified.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ``true`` : Delete a BIM 360 Docs folder.``false`` : Restore a BIM 360 Docs folder.
    hidden: Optional[bool] = None
    # The new folder name (1-255 characters). Avoid using the following reserved characters in the name: ``<``, ``>``, ``:``, ``"``, ``/``, ``/``, ``|``, ``?``, ``*``, ``'``, ``/n``, ``/r``, ``/t``, ``/0``, ``/f``, ``¢``, ``™``, ``$``, ``®``. When a deleted folder is restored, it keeps its original name. However, if a name conflict occurs, you must provide a new unique name for it. 
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModifyFolderPayload_data_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModifyFolderPayload_data_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModifyFolderPayload_data_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

