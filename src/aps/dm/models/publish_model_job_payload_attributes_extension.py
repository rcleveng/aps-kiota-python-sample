from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .type_commandtype_get_publish_model_job import Type_commandtype_GetPublishModelJob

@dataclass
class PublishModelJobPayload_attributes_extension(AdditionalDataHolder, Parsable):
    """
    An object that contains properties specific to the GetPublishModelJob command,  extending the default properties of a command.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Type ID of the schema used for extending properties. Must be ``commands:autodesk.bim360:C4RModelGetPublishJob`` for the GetPublishModelJob command.
    type: Optional[Type_commandtype_GetPublishModelJob] = None
    # The version of the schema. Must be ``1.0.0`` for the GetPublishModelJob command. 
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PublishModelJobPayload_attributes_extension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PublishModelJobPayload_attributes_extension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PublishModelJobPayload_attributes_extension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .type_commandtype_get_publish_model_job import Type_commandtype_GetPublishModelJob

        from .type_commandtype_get_publish_model_job import Type_commandtype_GetPublishModelJob

        fields: dict[str, Callable[[Any], None]] = {
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_commandtype_GetPublishModelJob)),
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
    

