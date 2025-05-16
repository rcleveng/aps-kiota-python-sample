from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class User_issues_new(AdditionalDataHolder, Parsable):
    """
    If this object appears in the response, it indicates that the user can create and modify issues.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Not relevant
    permitted_actions: Optional[list[str]] = None
    # Not relevant
    permitted_attributes: Optional[list[str]] = None
    # Not relevant
    permitted_statuses: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> User_issues_new:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: User_issues_new
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return User_issues_new()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "permitted_actions": lambda n : setattr(self, 'permitted_actions', n.get_collection_of_primitive_values(str)),
            "permitted_attributes": lambda n : setattr(self, 'permitted_attributes', n.get_collection_of_primitive_values(str)),
            "permitted_statuses": lambda n : setattr(self, 'permitted_statuses', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("permitted_actions", self.permitted_actions)
        writer.write_collection_of_primitive_values("permitted_attributes", self.permitted_attributes)
        writer.write_collection_of_primitive_values("permitted_statuses", self.permitted_statuses)
        writer.write_additional_data_value(self.additional_data)
    

