from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DownloadPayload_data_attributes_format(AdditionalDataHolder, Parsable):
    """
    Specifies the desired download format.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The file name extension of the desired download format. Must be one of the supported file name extensions returned by the [List Supported Download Formats](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-downloadFormats-GET/) operation for the specified version.
    file_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadPayload_data_attributes_format:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadPayload_data_attributes_format
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadPayload_data_attributes_format()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
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
        writer.write_str_value("fileType", self.file_type)
        writer.write_additional_data_value(self.additional_data)
    

