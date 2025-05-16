from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .region import Region
    from .specify_references_payload_references import SpecifyReferencesPayload_references

@dataclass
class SpecifyReferencesPayload(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a Specify References operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The file name of the top level component. By default, it is set to ``""`` and the file will be download with its ``urn``.
    filename: Optional[str] = None
    # An array of objects, where each object represents a referenced file.
    references: Optional[list[SpecifyReferencesPayload_references]] = None
    # Specifies where the referenced files are stored. Possible values are:     - ``US`` - Data center for the US region.- ``EMEA`` - Data center for the European Union, Middle East, and Africa. - ``AUS`` - (Beta) Data center for the Australia region.**Note**: Beta features are subject to change. Please avoid using them in production environments.
    region: Optional[Region] = None
    # The URL safe Base64 encoded URN of the source design. Mandatory if the Base64 encoded urn in the request URL is a logical URN.
    urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecifyReferencesPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecifyReferencesPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecifyReferencesPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .region import Region
        from .specify_references_payload_references import SpecifyReferencesPayload_references

        from .region import Region
        from .specify_references_payload_references import SpecifyReferencesPayload_references

        fields: dict[str, Callable[[Any], None]] = {
            "filename": lambda n : setattr(self, 'filename', n.get_str_value()),
            "references": lambda n : setattr(self, 'references', n.get_collection_of_object_values(SpecifyReferencesPayload_references)),
            "region": lambda n : setattr(self, 'region', n.get_enum_value(Region)),
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
        writer.write_collection_of_object_values("references", self.references)
        writer.write_enum_value("region", self.region)
        writer.write_str_value("urn", self.urn)
        writer.write_additional_data_value(self.additional_data)
    

