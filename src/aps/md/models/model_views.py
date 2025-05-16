from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .model_views_data import ModelViews_data

@dataclass
class ModelViews(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a List Model Views operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An envelope that contains the return data.
    data: Optional[ModelViews_data] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelViews:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelViews
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelViews()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .model_views_data import ModelViews_data

        from .model_views_data import ModelViews_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(ModelViews_data)),
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
        writer.write_additional_data_value(self.additional_data)
    

