from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .object_tree_data_objects import ObjectTree_data_objects

@dataclass
class ObjectTree_data(AdditionalDataHolder, Parsable):
    """
    Envelope that contains the returned data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of "objects" that constitute the nodes of the object tree.
    objects: Optional[list[ObjectTree_data_objects]] = None
    # The type of data that is returned. Always ``objects``.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ObjectTree_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectTree_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ObjectTree_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .object_tree_data_objects import ObjectTree_data_objects

        from .object_tree_data_objects import ObjectTree_data_objects

        fields: dict[str, Callable[[Any], None]] = {
            "objects": lambda n : setattr(self, 'objects', n.get_collection_of_object_values(ObjectTree_data_objects)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_collection_of_object_values("objects", self.objects)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

