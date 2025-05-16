from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .type_commandtype_list_items import Type_commandtype_ListItems

@dataclass
class ListItems_attributes_extension(AdditionalDataHolder, Parsable):
    """
    An object that contains properties specific to the ListItems command,  extending the default properties of a command.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Type ID of the schema used for extending properties. Must be ``commands:autodesk.core:ListItems`` for the ListItems command.
    type: Optional[Type_commandtype_ListItems] = None
    # The version of the schema. Must be ``1.0.0`` for the ListItems command. 
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListItems_attributes_extension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListItems_attributes_extension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListItems_attributes_extension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .type_commandtype_list_items import Type_commandtype_ListItems

        from .type_commandtype_list_items import Type_commandtype_ListItems

        fields: dict[str, Callable[[Any], None]] = {
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_commandtype_ListItems)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_enum_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

