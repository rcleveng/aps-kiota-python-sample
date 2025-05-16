from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item403_error_meta_warnings import Item403Error_meta_warnings

@dataclass
class Item403Error_meta(AdditionalDataHolder, Parsable):
    """
    Contains information about the error that occurred.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects, where each element of the array represents a warning.
    warnings: Optional[list[Item403Error_meta_warnings]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Item403Error_meta:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Item403Error_meta
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Item403Error_meta()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item403_error_meta_warnings import Item403Error_meta_warnings

        from .item403_error_meta_warnings import Item403Error_meta_warnings

        fields: dict[str, Callable[[Any], None]] = {
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_object_values(Item403Error_meta_warnings)),
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
        writer.write_collection_of_object_values("warnings", self.warnings)
        writer.write_additional_data_value(self.additional_data)
    

