from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_meta_link import Json_api_meta_link
    from .json_api_type_id import Json_api_type_id

@dataclass
class VersionData_relationships_storage(AdditionalDataHolder, Parsable):
    """
    Contains information about the storage location that contains the binary data of this version.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object containing the ``id`` and ``type`` properties of a resource.
    data: Optional[Json_api_type_id] = None
    # Meta-information on links to this resource.
    meta: Optional[Json_api_meta_link] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VersionData_relationships_storage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VersionData_relationships_storage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VersionData_relationships_storage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_meta_link import Json_api_meta_link
        from .json_api_type_id import Json_api_type_id

        from .json_api_meta_link import Json_api_meta_link
        from .json_api_type_id import Json_api_type_id

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(Json_api_type_id)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(Json_api_meta_link)),
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
        writer.write_object_value("meta", self.meta)
        writer.write_additional_data_value(self.additional_data)
    

