from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .greater_than_ge import GreaterThan_Ge

@dataclass
class GreaterThan(AdditionalDataHolder, Parsable):
    """
    Use this to retrieve only the properties of objects where a specified property is greater than a specified value. 
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Returns only the objects where the value of the specified numerical property is greater than or equal to the specified value.The first element of the array contains the name of the property. The next element specifies the values that the property must be greater than or equal to. The array can only be two elements long.For example, if you specify an array as: ``"$ge":["properties.Dimensions.Width1",0.1]``, the request returns the properties of all objects whose ``properties.Dimensions.Width1`` property is greater than or equal to  ``0.1``.**Note:** The Model Derivative service converts numeric values from their native units to metric base units for comparison. So, the value to compare with must be specified in metric base units. For example, if the property you are comparing is a length measurement, you must specify the value  in ``m``.  Not in ``cm``, ``mm``, or ``ft``.
    ge: Optional[list[GreaterThan_Ge]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GreaterThan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GreaterThan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GreaterThan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .greater_than_ge import GreaterThan_Ge

        from .greater_than_ge import GreaterThan_Ge

        fields: dict[str, Callable[[Any], None]] = {
            "$ge": lambda n : setattr(self, 'ge', n.get_collection_of_object_values(GreaterThan_Ge)),
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
        writer.write_collection_of_object_values("$ge", self.ge)
        writer.write_additional_data_value(self.additional_data)
    

