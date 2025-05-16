from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_data_relationships_storage_data import DownloadData_relationships_storage_data
    from .download_data_relationships_storage_meta import DownloadData_relationships_storage_meta

@dataclass
class DownloadData_relationships_storage(AdditionalDataHolder, Parsable):
    """
    Contains information about the location of the download.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains information about the storage location of the download.
    data: Optional[DownloadData_relationships_storage_data] = None
    # Meta information about the storage location of the download.
    meta: Optional[DownloadData_relationships_storage_meta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadData_relationships_storage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadData_relationships_storage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadData_relationships_storage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_data_relationships_storage_data import DownloadData_relationships_storage_data
        from .download_data_relationships_storage_meta import DownloadData_relationships_storage_meta

        from .download_data_relationships_storage_data import DownloadData_relationships_storage_data
        from .download_data_relationships_storage_meta import DownloadData_relationships_storage_meta

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(DownloadData_relationships_storage_data)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(DownloadData_relationships_storage_meta)),
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
    

