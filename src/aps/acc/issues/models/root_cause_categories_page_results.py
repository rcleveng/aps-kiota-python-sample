from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .root_cause_categories_page_results_root_causes import Root_cause_categories_page_results_rootCauses

@dataclass
class Root_cause_categories_page_results(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time the custom attribute was created, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    created_at: Optional[str] = None
    # The Autodesk ID of the user who created the custom attribute.
    created_by: Optional[str] = None
    # The date and time the custom attribute was deleted, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    deleted_at: Optional[str] = None
    # The Autodesk ID of the user who deleted the custom attribute.
    deleted_by: Optional[str] = None
    # The ID of the issue root cause category.
    id: Optional[str] = None
    # The description of the custom attribute.Max length: 500
    is_active: Optional[bool] = None
    # Not relevant
    permitted_actions: Optional[list[str]] = None
    # Not relevant
    permitted_attributes: Optional[list[str]] = None
    # The metadata object; only relevant for list custom attributes.
    root_causes: Optional[list[Root_cause_categories_page_results_rootCauses]] = None
    # The title of the custom attribute.Max length: 100
    title: Optional[str] = None
    # The last date and time the custom attribute was updated, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    updated_at: Optional[str] = None
    # The Autodesk ID of the user who last updated the custom attribute.
    updated_by: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Root_cause_categories_page_results:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Root_cause_categories_page_results
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Root_cause_categories_page_results()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .root_cause_categories_page_results_root_causes import Root_cause_categories_page_results_rootCauses

        from .root_cause_categories_page_results_root_causes import Root_cause_categories_page_results_rootCauses

        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_str_value()),
            "deletedBy": lambda n : setattr(self, 'deleted_by', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "permittedActions": lambda n : setattr(self, 'permitted_actions', n.get_collection_of_primitive_values(str)),
            "permittedAttributes": lambda n : setattr(self, 'permitted_attributes', n.get_collection_of_primitive_values(str)),
            "rootCauses": lambda n : setattr(self, 'root_causes', n.get_collection_of_object_values(Root_cause_categories_page_results_rootCauses)),
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
        writer.write_str_value("createdAt", self.created_at)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_str_value("deletedAt", self.deleted_at)
        writer.write_str_value("deletedBy", self.deleted_by)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_collection_of_primitive_values("permittedActions", self.permitted_actions)
        writer.write_collection_of_primitive_values("permittedAttributes", self.permitted_attributes)
        writer.write_collection_of_object_values("rootCauses", self.root_causes)
        writer.write_str_value("title", self.title)
        writer.write_str_value("updatedAt", self.updated_at)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_additional_data_value(self.additional_data)
    

