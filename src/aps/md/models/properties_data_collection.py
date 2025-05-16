from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties_data_collection_properties import Properties_data_collection_properties

@dataclass
class Properties_data_collection(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A unique identifier of the object as defined in the source design. For example, ``UniqueID`` in Revit files.
    external_id: Optional[str] = None
    # Name of the object.
    name: Optional[str] = None
    # Unique identifier of the object.**Note:** The ``objectid`` is a non-persistent ID assigned to an object when a design file is translated to SVF or SVF2. So:- The ``objectid`` of an object can change if the design is translated to SVF or SVF2 again.- If you require a persistent ID to reference an object, use ``externalId``.
    objectid: Optional[float] = None
    # A JSON object containing dictionary objects (key value pairs), where the key is the property name and the value is the value of the property.
    properties: Optional[Properties_data_collection_properties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Properties_data_collection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Properties_data_collection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Properties_data_collection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .properties_data_collection_properties import Properties_data_collection_properties

        from .properties_data_collection_properties import Properties_data_collection_properties

        fields: dict[str, Callable[[Any], None]] = {
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objectid": lambda n : setattr(self, 'objectid', n.get_float_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(Properties_data_collection_properties)),
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
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("name", self.name)
        writer.write_float_value("objectid", self.objectid)
        writer.write_object_value("properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    

