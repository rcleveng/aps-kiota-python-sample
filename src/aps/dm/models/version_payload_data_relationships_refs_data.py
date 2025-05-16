from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .type_version import Type_version
    from .version_payload_data_relationships_refs_data_meta import VersionPayload_data_relationships_refs_data_meta

@dataclass
class VersionPayload_data_relationships_refs_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The URN (Version ID) of the referenced version.
    id: Optional[str] = None
    # Contains meta information about the reference.
    meta: Optional[VersionPayload_data_relationships_refs_data_meta] = None
    # The type of the resource. Possible values are ``versions``.
    type: Optional[Type_version] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VersionPayload_data_relationships_refs_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VersionPayload_data_relationships_refs_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VersionPayload_data_relationships_refs_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .type_version import Type_version
        from .version_payload_data_relationships_refs_data_meta import VersionPayload_data_relationships_refs_data_meta

        from .type_version import Type_version
        from .version_payload_data_relationships_refs_data_meta import VersionPayload_data_relationships_refs_data_meta

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(VersionPayload_data_relationships_refs_data_meta)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_version)),
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
        writer.write_object_value("meta", self.meta)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

