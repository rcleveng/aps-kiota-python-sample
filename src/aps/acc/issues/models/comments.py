from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Comments(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The comment content. A /n indicates a new line, e.g.: Hey/nAharon will be a 2 lines comment.Max length: 10000
    body: Optional[str] = None
    # Not relevant
    client_created_at: Optional[str] = None
    # Not relevant
    client_updated_at: Optional[str] = None
    # The date and time the custom attribute was created, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    created_at: Optional[str] = None
    # The Autodesk ID of the user who created the comment.
    created_by: Optional[str] = None
    # Not relevant
    deleted_at: Optional[str] = None
    # The comment ID.
    id: Optional[str] = None
    # Not relevant
    permitted_actions: Optional[list[str]] = None
    # Not relevant
    permitted_attributes: Optional[list[str]] = None
    # Not relevant
    updated_at: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Comments:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Comments
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Comments()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_str_value()),
            "clientCreatedAt": lambda n : setattr(self, 'client_created_at', n.get_str_value()),
            "clientUpdatedAt": lambda n : setattr(self, 'client_updated_at', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "permittedActions": lambda n : setattr(self, 'permitted_actions', n.get_collection_of_primitive_values(str)),
            "permittedAttributes": lambda n : setattr(self, 'permitted_attributes', n.get_collection_of_primitive_values(str)),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_str_value()),
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
        writer.write_str_value("body", self.body)
        writer.write_str_value("clientCreatedAt", self.client_created_at)
        writer.write_str_value("clientUpdatedAt", self.client_updated_at)
        writer.write_str_value("createdAt", self.created_at)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_str_value("deletedAt", self.deleted_at)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_primitive_values("permittedActions", self.permitted_actions)
        writer.write_collection_of_primitive_values("permittedAttributes", self.permitted_attributes)
        writer.write_str_value("updatedAt", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

