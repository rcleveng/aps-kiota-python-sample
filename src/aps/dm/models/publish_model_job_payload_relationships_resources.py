from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .publish_model_job_payload_relationships_resources_data import PublishModelJobPayload_relationships_resources_data

@dataclass
class PublishModelJobPayload_relationships_resources(AdditionalDataHolder, Parsable):
    """
    Contains the list of items to check.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects, where each object represents an item to check. 
    data: Optional[list[PublishModelJobPayload_relationships_resources_data]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PublishModelJobPayload_relationships_resources:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PublishModelJobPayload_relationships_resources
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PublishModelJobPayload_relationships_resources()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .publish_model_job_payload_relationships_resources_data import PublishModelJobPayload_relationships_resources_data

        from .publish_model_job_payload_relationships_resources_data import PublishModelJobPayload_relationships_resources_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(PublishModelJobPayload_relationships_resources_data)),
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
        writer.write_collection_of_object_values("data", self.data)
        writer.write_additional_data_value(self.additional_data)
    

