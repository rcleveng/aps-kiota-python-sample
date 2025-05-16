from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .types_page_results_subtypes import Types_page_results_subtypes

@dataclass
class Types_page_results(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Not relevant
    container_id: Optional[str] = None
    # The date and time the issue was created, in ISO8601 format.
    created_at: Optional[str] = None
    # The unique identifier of the user who created the issue type.
    created_by: Optional[str] = None
    # The date and time the issue type was deleted, in ISO8601 format.
    deleted_at: Optional[str] = None
    # The unique identifier of the user who deleted the issue type.
    deleted_by: Optional[str] = None
    # The ID of the issue type.
    id: Optional[str] = None
    # States whether the issue type is active.
    is_active: Optional[bool] = None
    # Not relevant
    order_index: Optional[int] = None
    # Not relevant
    permitted_actions: Optional[list[str]] = None
    # Not relevant
    permitted_attributes: Optional[list[str]] = None
    # Not relevant
    status_set: Optional[str] = None
    # A list of subtypes of the specific issue type.
    subtypes: Optional[list[Types_page_results_subtypes]] = None
    # Max length: 250
    title: Optional[str] = None
    # The date and time the issue type was updated, in ISO8601 format.
    updated_at: Optional[str] = None
    # The unique identifier of the user who updated the issue type.
    updated_by: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Types_page_results:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Types_page_results
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Types_page_results()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .types_page_results_subtypes import Types_page_results_subtypes

        from .types_page_results_subtypes import Types_page_results_subtypes

        fields: dict[str, Callable[[Any], None]] = {
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_str_value()),
            "deletedBy": lambda n : setattr(self, 'deleted_by', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "orderIndex": lambda n : setattr(self, 'order_index', n.get_int_value()),
            "permittedActions": lambda n : setattr(self, 'permitted_actions', n.get_collection_of_primitive_values(str)),
            "permittedAttributes": lambda n : setattr(self, 'permitted_attributes', n.get_collection_of_primitive_values(str)),
            "statusSet": lambda n : setattr(self, 'status_set', n.get_str_value()),
            "subtypes": lambda n : setattr(self, 'subtypes', n.get_collection_of_object_values(Types_page_results_subtypes)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_str_value()),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_str_value()),
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
        writer.write_str_value("containerId", self.container_id)
        writer.write_str_value("createdAt", self.created_at)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_str_value("deletedAt", self.deleted_at)
        writer.write_str_value("deletedBy", self.deleted_by)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_int_value("orderIndex", self.order_index)
        writer.write_collection_of_primitive_values("permittedActions", self.permitted_actions)
        writer.write_collection_of_primitive_values("permittedAttributes", self.permitted_attributes)
        writer.write_str_value("statusSet", self.status_set)
        writer.write_collection_of_object_values("subtypes", self.subtypes)
        writer.write_str_value("title", self.title)
        writer.write_str_value("updatedAt", self.updated_at)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_additional_data_value(self.additional_data)
    

