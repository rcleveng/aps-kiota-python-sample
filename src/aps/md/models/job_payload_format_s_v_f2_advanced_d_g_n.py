from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobPayloadFormatSVF2AdvancedDGN(AdditionalDataHolder, Parsable):
    """
    Advanced options for DGN inputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array containing user data linkage IDs of the linkage data to be extracted from the DGN file. Linkage data is not extracted if you do not specify this attribute.
    requested_linkage_i_ds: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVF2AdvancedDGN:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVF2AdvancedDGN
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatSVF2AdvancedDGN()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "requestedLinkageIDs": lambda n : setattr(self, 'requested_linkage_i_ds', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("requestedLinkageIDs", self.requested_linkage_i_ds)
        writer.write_additional_data_value(self.additional_data)
    

