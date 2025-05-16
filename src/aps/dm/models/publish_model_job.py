from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .publish_model_job_attributes import PublishModelJob_attributes
    from .type_commands import Type_commands

@dataclass
class PublishModelJob(AdditionalDataHolder, Parsable):
    """
    The ``data`` object returned by the GetPublishModelJob command, if the model needs publishing. If the model is already published, the ``data`` object will bed ``null``. 
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains the properties of the responseto the GetPublishModelJob command.
    attributes: Optional[PublishModelJob_attributes] = None
    # A unique ID assigned to the process executing the command.
    id: Optional[str] = None
    # The type of this resource. Possible values are ``commands``.
    type: Optional[Type_commands] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PublishModelJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PublishModelJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PublishModelJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .publish_model_job_attributes import PublishModelJob_attributes
        from .type_commands import Type_commands

        from .publish_model_job_attributes import PublishModelJob_attributes
        from .type_commands import Type_commands

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(PublishModelJob_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

