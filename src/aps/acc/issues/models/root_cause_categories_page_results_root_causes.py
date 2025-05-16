from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Root_cause_categories_page_results_rootCauses(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time the custom attribute was deleted, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    deleted_at: Optional[str] = None
    # The Autodesk ID of the user who deleted the custom attribute.
    deleted_by: Optional[str] = None
    # The ID of the issue root cause.
    id: Optional[str] = None
    # The description of the custom attribute.Max length: 500
    is_active: Optional[bool] = None
    # Not relevant
    permitted_actions: Optional[list[str]] = None
    # Not relevant
    permitted_attributes: Optional[list[str]] = None
    # The ID of the parent issue root cause category.
    root_cause_category_id: Optional[str] = None
    # The title of the issue root cause.Max length: 100
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Root_cause_categories_page_results_rootCauses:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Root_cause_categories_page_results_rootCauses
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Root_cause_categories_page_results_rootCauses()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_str_value()),
            "deletedBy": lambda n : setattr(self, 'deleted_by', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "permittedActions": lambda n : setattr(self, 'permitted_actions', n.get_collection_of_primitive_values(str)),
            "permittedAttributes": lambda n : setattr(self, 'permitted_attributes', n.get_collection_of_primitive_values(str)),
            "rootCauseCategoryId": lambda n : setattr(self, 'root_cause_category_id', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("deletedAt", self.deleted_at)
        writer.write_str_value("deletedBy", self.deleted_by)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_collection_of_primitive_values("permittedActions", self.permitted_actions)
        writer.write_collection_of_primitive_values("permittedAttributes", self.permitted_attributes)
        writer.write_str_value("rootCauseCategoryId", self.root_cause_category_id)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

