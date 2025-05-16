from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_payload_data_attributes import DownloadPayload_data_attributes
    from .download_payload_data_relationships import DownloadPayload_data_relationships
    from .type_downloads import Type_downloads

@dataclass
class DownloadPayload_data(AdditionalDataHolder, Parsable):
    """
    Contains information about the desired download format and the version of the item to convert to this format.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains information about the desired download format.
    attributes: Optional[DownloadPayload_data_attributes] = None
    # Contains information about the version the download format is being created for. 
    relationships: Optional[DownloadPayload_data_relationships] = None
    # The type of this resource. Possible values are ``downloads``.
    type: Optional[Type_downloads] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadPayload_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadPayload_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadPayload_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_payload_data_attributes import DownloadPayload_data_attributes
        from .download_payload_data_relationships import DownloadPayload_data_relationships
        from .type_downloads import Type_downloads

        from .download_payload_data_attributes import DownloadPayload_data_attributes
        from .download_payload_data_relationships import DownloadPayload_data_relationships
        from .type_downloads import Type_downloads

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(DownloadPayload_data_attributes)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(DownloadPayload_data_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_downloads)),
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
    

