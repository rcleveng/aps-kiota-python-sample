from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_type_id import Json_api_type_id

@dataclass
class HubData_relationships_pimCollection(AdditionalDataHolder, Parsable):
    """
    Information on the ``id`` and ``type`` properties of a resource. This is available only for Fusion Team hubs and A360 Personal hubs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object containing the ``id`` and ``type`` properties of a resource.
    data: Optional[Json_api_type_id] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HubData_relationships_pimCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HubData_relationships_pimCollection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HubData_relationships_pimCollection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_type_id import Json_api_type_id

        from .json_api_type_id import Json_api_type_id

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(Json_api_type_id)),
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
        writer.write_additional_data_value(self.additional_data)
    

