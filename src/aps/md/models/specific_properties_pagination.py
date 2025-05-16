from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SpecificProperties_pagination(AdditionalDataHolder, Parsable):
    """
    Envelope that contains pagination information.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The maximum number of properties you requested for this page.
    limit: Optional[float] = None
    # The number of items skipped (because they were returned in previous pages) when returning this page.
    offset: Optional[float] = None
    # The total number of properties to be returned.
    total_results: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecificProperties_pagination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecificProperties_pagination
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecificProperties_pagination()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "limit": lambda n : setattr(self, 'limit', n.get_float_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_float_value()),
            "totalResults": lambda n : setattr(self, 'total_results', n.get_float_value()),
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
        writer.write_float_value("limit", self.limit)
        writer.write_float_value("offset", self.offset)
        writer.write_float_value("totalResults", self.total_results)
        writer.write_additional_data_value(self.additional_data)
    

