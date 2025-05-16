from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .specify_references_payload_references_metadata import SpecifyReferencesPayload_references_metadata

@dataclass
class SpecifyReferencesPayload_references(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The file name of the referenced file. By default, it is set to ``""`` and the referenced file will be downloaded by its ``urn`` and placed relative to the top-level component using ``relativePath``.
    filename: Optional[str] = None
    # An object to hold custom metadata.
    metadata: Optional[SpecifyReferencesPayload_references_metadata] = None
    # The path to the referenced file, relative to the top level component. By default, it is set to ``""``, which means that the referenced file and top level component are in the same folder.
    relative_path: Optional[str] = None
    # The URN of the referenced file.
    urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecifyReferencesPayload_references:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecifyReferencesPayload_references
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecifyReferencesPayload_references()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .specify_references_payload_references_metadata import SpecifyReferencesPayload_references_metadata

        from .specify_references_payload_references_metadata import SpecifyReferencesPayload_references_metadata

        fields: dict[str, Callable[[Any], None]] = {
            "filename": lambda n : setattr(self, 'filename', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(SpecifyReferencesPayload_references_metadata)),
            "relativePath": lambda n : setattr(self, 'relative_path', n.get_str_value()),
            "urn": lambda n : setattr(self, 'urn', n.get_str_value()),
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
        writer.write_str_value("filename", self.filename)
        writer.write_object_value("metadata", self.metadata)
        writer.write_str_value("relativePath", self.relative_path)
        writer.write_str_value("urn", self.urn)
        writer.write_additional_data_value(self.additional_data)
    

