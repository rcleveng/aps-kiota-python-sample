from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission_relationships_resources import CheckPermission_relationships_resources

@dataclass
class CheckPermission_relationships(AdditionalDataHolder, Parsable):
    """
    Contains the list of resources checked for permission.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains the list of resources checked for permission.
    resources: Optional[CheckPermission_relationships_resources] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPermission_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPermission_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPermission_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission_relationships_resources import CheckPermission_relationships_resources

        from .check_permission_relationships_resources import CheckPermission_relationships_resources

        fields: dict[str, Callable[[Any], None]] = {
            "resources": lambda n : setattr(self, 'resources', n.get_object_value(CheckPermission_relationships_resources)),
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
        writer.write_object_value("resources", self.resources)
        writer.write_additional_data_value(self.additional_data)
    

