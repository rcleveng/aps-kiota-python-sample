from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
    from .json_api_link import Json_api_link
    from .relationship_links_data_meta_data import RelationshipLinks_data_meta_data

@dataclass
class RelationshipLinks_data_meta(AdditionalDataHolder, Parsable):
    """
    The meta-information of the links of this resource.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The object containing meta-information on the data of the links of this resource.
    data: Optional[RelationshipLinks_data_meta_data] = None
    # A container of additional properties that extends this resource.
    extension: Optional[Base_attributes_extension_object_with_schema_link] = None
    # An object containing the hyperlink to the referenced resource.
    link: Optional[Json_api_link] = None
    # The MIME type of the content of the resource.
    mime_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelationshipLinks_data_meta:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelationshipLinks_data_meta
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelationshipLinks_data_meta()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
        from .json_api_link import Json_api_link
        from .relationship_links_data_meta_data import RelationshipLinks_data_meta_data

        from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
        from .json_api_link import Json_api_link
        from .relationship_links_data_meta_data import RelationshipLinks_data_meta_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(RelationshipLinks_data_meta_data)),
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Base_attributes_extension_object_with_schema_link)),
            "link": lambda n : setattr(self, 'link', n.get_object_value(Json_api_link)),
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
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
        writer.write_object_value("data", self.data)
        writer.write_object_value("extension", self.extension)
        writer.write_object_value("link", self.link)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_additional_data_value(self.additional_data)
    

