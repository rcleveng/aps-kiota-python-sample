from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .payload import Payload
    from .specific_properties_payload_fields import SpecificPropertiesPayload_fields
    from .specific_properties_payload_pagination import SpecificPropertiesPayload_pagination
    from .specific_properties_payload_query import SpecificPropertiesPayload_query

@dataclass
class SpecificPropertiesPayload(AdditionalDataHolder, Parsable):
    """
    An object that represents the request body of a Fetch Specific Properties operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies what properties of the objects to return. If you do not specify this attribute, the response returns all properties.Possible values are:- ``properties`` - Return all properties.- ``properties.something``- Return the property named ``something`` and all its children.- ``properties.some*`` - Return all properties with names that begin with ``some`` and all their children.- ``properties.category.*`` - Return the property named ``category`` and all its children.- ``properties.*.property`` - Return any property named ``property`` regardless of its parent.
    fields: Optional[SpecificPropertiesPayload_fields] = None
    # Specifies how to split the response into multiple pages, and return the response one page at a time.
    pagination: Optional[SpecificPropertiesPayload_pagination] = None
    # Specifies the format for numeric values in the response body. Possible values:- ``text`` - (Default) Returns all properties requested in ``fields`` without applying any special formatting.- ``unit`` - Applies a filter and returns only the properties that contain numerical values. Additionally, it formats property values as ``##<VALUE_OF_PROPERTY><UNIT_OF_VALUE><PRECISION><SYSTEM_UNIT>``. For example ``##94.172{mm}[3]{m}``, where ``94.172`` is the value of the property, ``{mm}`` is the unit of the value, ``[3]`` is the precision, and ``{m}`` is the metric base unit for the measurement.
    payload: Optional[Payload] = None
    # Specifies what objects to query. Contains the parameters to pass to the search service. You can use one of the following forms: 
    query: Optional[SpecificPropertiesPayload_query] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecificPropertiesPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecificPropertiesPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecificPropertiesPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .payload import Payload
        from .specific_properties_payload_fields import SpecificPropertiesPayload_fields
        from .specific_properties_payload_pagination import SpecificPropertiesPayload_pagination
        from .specific_properties_payload_query import SpecificPropertiesPayload_query

        from .payload import Payload
        from .specific_properties_payload_fields import SpecificPropertiesPayload_fields
        from .specific_properties_payload_pagination import SpecificPropertiesPayload_pagination
        from .specific_properties_payload_query import SpecificPropertiesPayload_query

        fields: dict[str, Callable[[Any], None]] = {
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(SpecificPropertiesPayload_fields)),
            "pagination": lambda n : setattr(self, 'pagination', n.get_object_value(SpecificPropertiesPayload_pagination)),
            "payload": lambda n : setattr(self, 'payload', n.get_enum_value(Payload)),
            "query": lambda n : setattr(self, 'query', n.get_object_value(SpecificPropertiesPayload_query)),
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
        writer.write_object_value("fields", self.fields)
        writer.write_object_value("pagination", self.pagination)
        writer.write_enum_value("payload", self.payload)
        writer.write_object_value("query", self.query)
        writer.write_additional_data_value(self.additional_data)
    

