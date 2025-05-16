from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SpecifyReferences(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a Specify References operation. 
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The result of the operation. Always ``success`` for status ``200``.
    result: Optional[str] = None
    # The URN of the top level component.
    urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecifyReferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecifyReferences
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecifyReferences()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "result": lambda n : setattr(self, 'result', n.get_str_value()),
            "urn": lambda n : setattr(self, 'urn', n.get_str_value()),
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
        writer.write_str_value("result", self.result)
        writer.write_str_value("urn", self.urn)
        writer.write_additional_data_value(self.additional_data)
    

