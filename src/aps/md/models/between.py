from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .between_between import Between_Between

@dataclass
class Between(AdditionalDataHolder, Parsable):
    """
    Use this to retrieve only the properties of objects where a specified attribute is between two specified values.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Returns only the objects where the value of the specified numerical property lies between the specified values.The first element of the array contains the name of the property. The next two elements specify the values that the property must lie between. The array can only be three elements long.For example, if you specify an array as: ``"$between":["properties.Dimensions.Width1",1,10]``, the request returns the properties of all objects whose ``properties.Dimensions.Width1`` property is between ``1`` and ``10``.**Note:** The Model Derivative service converts numeric values from their native units to metric base units for comparison. So, you must specify the values to compare with in metric base units. For example, if the property you are comparing is a length measurement, you must specify the values  in ``m``.  Not in ``cm``, ``mm``, or ``ft``.
    between: Optional[list[Between_Between]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Between:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Between
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Between()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .between_between import Between_Between

        from .between_between import Between_Between

        fields: dict[str, Callable[[Any], None]] = {
            "$between": lambda n : setattr(self, 'between', n.get_collection_of_object_values(Between_Between)),
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
        writer.write_collection_of_object_values("$between", self.between)
        writer.write_additional_data_value(self.additional_data)
    

