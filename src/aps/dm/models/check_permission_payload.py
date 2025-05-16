from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission_payload_attributes import CheckPermissionPayload_attributes
    from .check_permission_payload_relationships import CheckPermissionPayload_relationships
    from .type_commands import Type_commands

@dataclass
class CheckPermissionPayload(AdditionalDataHolder, Parsable):
    """
    An object that contains the input data required to execute the CheckPermission command.The CheckPermission command checks if a user has permission to perform specified actions on specified resources.The user’s identity is derived from the ``x-user-id`` header (in a 2-Legged call), or from the access token (in a 3-Legged call). See the [Developer's Guide topic on the CheckPermission command](/en/docs/data/v2/developers_guide/commands/checkpermission/) for more information.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container of the inputs for the command.
    attributes: Optional[CheckPermissionPayload_attributes] = None
    # Contains a list of resources required for execution of the command.
    relationships: Optional[CheckPermissionPayload_relationships] = None
    # The type of this resource. Possible values are ``commands``.
    type: Optional[Type_commands] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPermissionPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPermissionPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPermissionPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission_payload_attributes import CheckPermissionPayload_attributes
        from .check_permission_payload_relationships import CheckPermissionPayload_relationships
        from .type_commands import Type_commands

        from .check_permission_payload_attributes import CheckPermissionPayload_attributes
        from .check_permission_payload_relationships import CheckPermissionPayload_relationships
        from .type_commands import Type_commands

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(CheckPermissionPayload_attributes)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(CheckPermissionPayload_relationships)),
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
    

