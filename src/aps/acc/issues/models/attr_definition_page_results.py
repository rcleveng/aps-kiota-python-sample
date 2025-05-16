from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attr_definition_page_results_metadata import Attr_definition_page_results_metadata
    from .data_type import DataType

@dataclass
class Attr_definition_page_results(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Not relevant
    container_id: Optional[str] = None
    # The date and time the custom attribute was created, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    created_at: Optional[str] = None
    # The Autodesk ID of the user who created the custom attribute.
    created_by: Optional[str] = None
    # Retrieves issue custom attribute definitions with the specified data type
    data_type: Optional[DataType] = None
    # The date and time the custom attribute was deleted, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    deleted_at: Optional[str] = None
    # The Autodesk ID of the user who deleted the custom attribute.
    deleted_by: Optional[str] = None
    # The description of the custom attribute.
    description: Optional[str] = None
    # The ID of the custom attribute.
    id: Optional[str] = None
    # The ID of the item (type, or subtype) the custom attribute is mapped to.
    mapped_item_id: Optional[str] = None
    # The mappedItemType property
    mapped_item_type: Optional[str] = None
    # The metadata object; only relevant for list custom attributes.
    metadata: Optional[Attr_definition_page_results_metadata] = None
    # The order that the custom attributes were mapped to the item (type, subtype). This is only relevant to non-inherited mappings.
    order: Optional[int] = None
    # Not relevant
    permitted_actions: Optional[list[str]] = None
    # Not relevant
    permitted_attributes: Optional[list[str]] = None
    # The title of the custom attribute.
    title: Optional[str] = None
    # The last date and time the custom attribute was updated, in the following format: YYYY-MM-DDThh:mm:ss.sz.
    updated_at: Optional[str] = None
    # The Autodesk ID of the user who last updated the custom attribute.
    updated_by: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Attr_definition_page_results:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Attr_definition_page_results
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Attr_definition_page_results()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attr_definition_page_results_metadata import Attr_definition_page_results_metadata
        from .data_type import DataType

        from .attr_definition_page_results_metadata import Attr_definition_page_results_metadata
        from .data_type import DataType

        fields: dict[str, Callable[[Any], None]] = {
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "dataType": lambda n : setattr(self, 'data_type', n.get_enum_value(DataType)),
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_str_value()),
            "deletedBy": lambda n : setattr(self, 'deleted_by', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "mappedItemId": lambda n : setattr(self, 'mapped_item_id', n.get_str_value()),
            "mappedItemType": lambda n : setattr(self, 'mapped_item_type', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(Attr_definition_page_results_metadata)),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "permittedActions": lambda n : setattr(self, 'permitted_actions', n.get_collection_of_primitive_values(str)),
            "permittedAttributes": lambda n : setattr(self, 'permitted_attributes', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("dataType", self.data_type)
        writer.write_str_value("deletedAt", self.deleted_at)
        writer.write_str_value("deletedBy", self.deleted_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("id", self.id)
        writer.write_str_value("mappedItemId", self.mapped_item_id)
        writer.write_str_value("mappedItemType", self.mapped_item_type)
        writer.write_object_value("metadata", self.metadata)
        writer.write_int_value("order", self.order)
        writer.write_collection_of_primitive_values("permittedActions", self.permitted_actions)
        writer.write_collection_of_primitive_values("permittedAttributes", self.permitted_attributes)
        writer.write_str_value("title", self.title)
        writer.write_str_value("updatedAt", self.updated_at)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_additional_data_value(self.additional_data)
    

