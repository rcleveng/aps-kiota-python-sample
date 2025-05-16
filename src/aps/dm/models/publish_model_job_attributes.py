from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .command_execution_status import Command_execution_status
    from .publish_model_job_attributes_extension import PublishModelJob_attributes_extension

@dataclass
class PublishModelJob_attributes(AdditionalDataHolder, Parsable):
    """
    Contains the properties of the responseto the GetPublishModelJob command.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object that contains properties specific to the GetPublishModelJob command,  extending the default properties of a command.
    extension: Optional[PublishModelJob_attributes_extension] = None
    # The current stage of the command execution process. Possible values:- ``accepted`` - The command is ready to be executed. - ``committed`` - The command is currently being executed.- ``complete`` - The command was successfully executed.- ``failed`` - There was an error and command execution was stopped prematurely.
    status: Optional[Command_execution_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PublishModelJob_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PublishModelJob_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PublishModelJob_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .command_execution_status import Command_execution_status
        from .publish_model_job_attributes_extension import PublishModelJob_attributes_extension

        from .command_execution_status import Command_execution_status
        from .publish_model_job_attributes_extension import PublishModelJob_attributes_extension

        fields: dict[str, Callable[[Any], None]] = {
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(PublishModelJob_attributes_extension)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Command_execution_status)),
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
        writer.write_object_value("extension", self.extension)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

