from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .publish_model_payload_attributes import PublishModelPayload_attributes
    from .publish_model_payload_relationships import PublishModelPayload_relationships
    from .type_commands import Type_commands

@dataclass
class PublishModelPayload(AdditionalDataHolder, Parsable):
    """
    An object that contains the input required to execute the PublishModel command.The PublishModel Command publishes the latest version of a Collaboration for Revit (C4R) model to BIM 360 Docs.  See the [Developer's Guide topic on the PublishModel command](/en/docs/data/v2/developers_guide/commands/publishmodel/) for more information.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container of the inputs for the command.
    attributes: Optional[PublishModelPayload_attributes] = None
    # Contains a list of resources required for execution of the command.
    relationships: Optional[PublishModelPayload_relationships] = None
    # The type of this resource. Possible values are ``commands``.
    type: Optional[Type_commands] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PublishModelPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PublishModelPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PublishModelPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .publish_model_payload_attributes import PublishModelPayload_attributes
        from .publish_model_payload_relationships import PublishModelPayload_relationships
        from .type_commands import Type_commands

        from .publish_model_payload_attributes import PublishModelPayload_attributes
        from .publish_model_payload_relationships import PublishModelPayload_relationships
        from .type_commands import Type_commands

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(PublishModelPayload_attributes)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(PublishModelPayload_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_commands)),
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
    

