from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SpecificPropertiesPayload_pagination(AdditionalDataHolder, Parsable):
    """
    Specifies how to split the response into multiple pages, and return the response one page at a time.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The maximum number of properties to return in a single page. Use this attribute with the ``offset`` attribute to split the properties into multiple pages. To fetch the first page, specify ``offset`` =0 (do not skip any properties). To fetch the second page, specify ``offset`` = value of ``limit`` you specified for the first page. So, the server skips the search results returned on the first page. In general, ``offset`` = ``previous_offset`` + ``previous_limit``. This attribute is 20 by default. The minimum value is 1 and the maximum is 1000.
    limit: Optional[float] = None
    # The number of properties to skip. Use this attribute with the ``limit`` attribute to split the properties into multiple pages. To fetch the first page, specify ``offset`` =0 (do not skip any properties). To fetch the second page, specify ``offset`` = value of ``limit`` you specified for the first page. So, the server skips the properties returned on the first page. In general, ``offset`` = ``previous_offset`` + ``previous_limit``. This attribute is 0 by default. The minimum value is 0.
    offset: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecificPropertiesPayload_pagination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecificPropertiesPayload_pagination
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecificPropertiesPayload_pagination()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "limit": lambda n : setattr(self, 'limit', n.get_float_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_float_value()),
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
        writer.write_additional_data_value(self.additional_data)
    

