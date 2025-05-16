from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .messages_message import Messages_message

@dataclass
class Messages(AdditionalDataHolder, Parsable):
    """
    An array of objects where each object represents a message logged to the manifest during translation. For example, error messages and warning messages.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ID of the message. For example, the error code reported by an error message.
    code: Optional[str] = None
    # A human-readable explanation of the event being reported. Can be a string or an array of string.
    message: Optional[Messages_message] = None
    # Indicates the type of the message. For example, warning indicates a warning message and error indicates an error message.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Messages:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Messages
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Messages()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .messages_message import Messages_message

        from .messages_message import Messages_message

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_object_value(Messages_message)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("code", self.code)
        writer.write_object_value("message", self.message)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

