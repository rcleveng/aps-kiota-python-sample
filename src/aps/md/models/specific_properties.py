from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties import Properties
    from .specific_properties_pagination import SpecificProperties_pagination

@dataclass
class SpecificProperties(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a Fetch Specific Properties operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object that represents a successful response to a Fetch All Properties operation.
    data: Optional[Properties] = None
    # Envelope that contains pagination information.
    pagination: Optional[SpecificProperties_pagination] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecificProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecificProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecificProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .properties import Properties
        from .specific_properties_pagination import SpecificProperties_pagination

        from .properties import Properties
        from .specific_properties_pagination import SpecificProperties_pagination

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(Properties)),
            "pagination": lambda n : setattr(self, 'pagination', n.get_object_value(SpecificProperties_pagination)),
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
        writer.write_object_value("pagination", self.pagination)
        writer.write_additional_data_value(self.additional_data)
    

