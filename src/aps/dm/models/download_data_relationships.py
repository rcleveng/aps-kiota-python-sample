from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_data_relationships_storage import DownloadData_relationships_storage

@dataclass
class DownloadData_relationships(AdditionalDataHolder, Parsable):
    """
    Contains links to the resources directly related to the download.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains information about the location of the download.
    storage: Optional[DownloadData_relationships_storage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadData_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadData_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadData_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_data_relationships_storage import DownloadData_relationships_storage

        from .download_data_relationships_storage import DownloadData_relationships_storage

        fields: dict[str, Callable[[Any], None]] = {
            "storage": lambda n : setattr(self, 'storage', n.get_object_value(DownloadData_relationships_storage)),
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
        writer.write_object_value("storage", self.storage)
        writer.write_additional_data_value(self.additional_data)
    

