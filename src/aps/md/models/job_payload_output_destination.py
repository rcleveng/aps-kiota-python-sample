from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobPayload_output_destination(AdditionalDataHolder, Parsable):
    """
    Specifies where to store generated derivatives.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies where to store generated derivatives. Possible values are:- ``US``: (Default) Store derivatives at a data center for the United States of America.- ``EMEA``: Store derivatives at a data center for the European Union. - ``APAC``: (Beta) Store derivatives at a data center for the Australia region. **Note**: Beta features are subject to change. Please avoid using them in production environments.
    region: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayload_output_destination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayload_output_destination
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayload_output_destination()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
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
        writer.write_str_value("region", self.region)
        writer.write_additional_data_value(self.additional_data)
    

