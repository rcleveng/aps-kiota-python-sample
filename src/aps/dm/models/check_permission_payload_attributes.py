from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission_payload_attributes_extension import CheckPermissionPayload_attributes_extension

@dataclass
class CheckPermissionPayload_attributes(AdditionalDataHolder, Parsable):
    """
    A container of the inputs for the command.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object that contains properties specific to the CheckPermission command,  extending the default properties of a command.
    extension: Optional[CheckPermissionPayload_attributes_extension] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPermissionPayload_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPermissionPayload_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPermissionPayload_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission_payload_attributes_extension import CheckPermissionPayload_attributes_extension

        from .check_permission_payload_attributes_extension import CheckPermissionPayload_attributes_extension

        fields: dict[str, Callable[[Any], None]] = {
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(CheckPermissionPayload_attributes_extension)),
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
        writer.write_additional_data_value(self.additional_data)
    

