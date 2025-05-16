from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .equals_to_eq import EqualsTo_Eq

@dataclass
class EqualsTo(AdditionalDataHolder, Parsable):
    """
    Use this to retrieve only the properties of objects where a specified property is exactly equal to a specified value.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Returns only the objects where the value of the specified attribute (``name`` attribute or any numerical property) is exactly equal to the specified value.The first element of the array contains the name of the attribute. This can be the ``name`` attribute or the name of a numerical property. The second element of the array must be the value to match. If the first element is ``name``, must be a string value. If the first element is a numerical property, must be a numeric. The array can only be two elements long.For example, if you specify an array as: ``"$eq":["name","Rectangular"]``, the request will only return the properties of the object named ``Rectangular``. if you specify an array as: ``"$eq":["properties.Dimensions.Width1",0.6]``, the request will return the properties of all objects whose ``properties.Dimensions.Width1`` property is exactly equal to ``0.6``.**Note:** We recommend that you  use ``$between``  instead of ``$eq`` when testing non-integer numeric values for equality. Using ``between`` mitigates floating-point errors.
    eq: Optional[list[EqualsTo_Eq]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EqualsTo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EqualsTo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EqualsTo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .equals_to_eq import EqualsTo_Eq

        from .equals_to_eq import EqualsTo_Eq

        fields: dict[str, Callable[[Any], None]] = {
            "$eq": lambda n : setattr(self, 'eq', n.get_collection_of_object_values(EqualsTo_Eq)),
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
        writer.write_collection_of_object_values("$eq", self.eq)
        writer.write_additional_data_value(self.additional_data)
    

