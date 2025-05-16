from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .version_payload_data_relationships_item import VersionPayload_data_relationships_item
    from .version_payload_data_relationships_refs import VersionPayload_data_relationships_refs
    from .version_payload_data_relationships_storage import VersionPayload_data_relationships_storage

@dataclass
class VersionPayload_data_relationships(AdditionalDataHolder, Parsable):
    """
    A container of links to resources that are related to the version to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains information about the item this is a version of.
    item: Optional[VersionPayload_data_relationships_item] = None
    # Information on other resources that will share a custom relationship with the version being created.
    refs: Optional[VersionPayload_data_relationships_refs] = None
    # Contains the information about the storage location that contains the binary data of this version.
    storage: Optional[VersionPayload_data_relationships_storage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VersionPayload_data_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VersionPayload_data_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VersionPayload_data_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .version_payload_data_relationships_item import VersionPayload_data_relationships_item
        from .version_payload_data_relationships_refs import VersionPayload_data_relationships_refs
        from .version_payload_data_relationships_storage import VersionPayload_data_relationships_storage

        from .version_payload_data_relationships_item import VersionPayload_data_relationships_item
        from .version_payload_data_relationships_refs import VersionPayload_data_relationships_refs
        from .version_payload_data_relationships_storage import VersionPayload_data_relationships_storage

        fields: dict[str, Callable[[Any], None]] = {
            "item": lambda n : setattr(self, 'item', n.get_object_value(VersionPayload_data_relationships_item)),
            "refs": lambda n : setattr(self, 'refs', n.get_object_value(VersionPayload_data_relationships_refs)),
            "storage": lambda n : setattr(self, 'storage', n.get_object_value(VersionPayload_data_relationships_storage)),
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
        writer.write_object_value("item", self.item)
        writer.write_object_value("refs", self.refs)
        writer.write_object_value("storage", self.storage)
        writer.write_additional_data_value(self.additional_data)
    

