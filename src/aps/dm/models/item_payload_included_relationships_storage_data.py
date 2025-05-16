from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .type_object import Type_object

@dataclass
class ItemPayload_included_relationships_storage_data(AdditionalDataHolder, Parsable):
    """
    The data about the location of binary data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The URN indicating the location of the binary data. This is represented by the ``objectId``  returned when [uploading the file](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-PUT/).
    id: Optional[str] = None
    # The type of this resource. Possible values are ``objects``.
    type: Optional[Type_object] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemPayload_included_relationships_storage_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemPayload_included_relationships_storage_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemPayload_included_relationships_storage_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .type_object import Type_object

        from .type_object import Type_object

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_object)),
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
        writer.write_str_value("id", self.id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

