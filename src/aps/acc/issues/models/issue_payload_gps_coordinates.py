from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IssuePayload_gpsCoordinates(AdditionalDataHolder, Parsable):
    """
    A GPS Coordinate which represents the geo location of the issue.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The latitude property
    latitude: Optional[float] = None
    # The longitude property
    longitude: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IssuePayload_gpsCoordinates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IssuePayload_gpsCoordinates
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IssuePayload_gpsCoordinates()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
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
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_additional_data_value(self.additional_data)
    

