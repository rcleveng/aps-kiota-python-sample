from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .model_views_data_metadata import ModelViews_data_metadata

@dataclass
class ModelViews_data(AdditionalDataHolder, Parsable):
    """
    An envelope that contains the return data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects, where each object represents a Model View.
    metadata: Optional[list[ModelViews_data_metadata]] = None
    # The type of data that is returned.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelViews_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelViews_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelViews_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .model_views_data_metadata import ModelViews_data_metadata

        from .model_views_data_metadata import ModelViews_data_metadata

        fields: dict[str, Callable[[Any], None]] = {
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(ModelViews_data_metadata)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

