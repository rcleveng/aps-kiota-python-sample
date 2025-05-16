from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .manifest_derivative import ManifestDerivative

@dataclass
class Manifest(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a Fetch Manifest operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects, where each object represents a derivative of the source design.
    derivatives: Optional[list[ManifestDerivative]] = None
    # - ``true``: There is a thumbnail for the source design.- ``false``: There is no thumbnail for the source design.
    has_thumbnail: Optional[str] = None
    # Indicates the overall progress of all translation jobs, as a percentage. Once all requested derivatives are generated, the value changes to ``complete``.
    progress: Optional[str] = None
    # Specifies the data center where the manifest, derivatives, and references are stored. Possible values are: - ``US`` - Data center for the US region.- ``EMEA`` - Data center for European Union, Middle East, and Africa. - ``APAC`` - Data center for the Australia region.
    region: Optional[str] = None
    # Overall status of all translation jobs for the source design. Possible values are: ``pending``, ``success``, ``inprogress``, ``failed``, ``timeout``.
    status: Optional[str] = None
    # The type of data that is returned. Always ``manifest``.
    type: Optional[str] = None
    # The URL-safe Base64 encoded URN of the source design.
    urn: Optional[str] = None
    # Indicates the version of the schema that the manifest is based on.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Manifest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Manifest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Manifest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .manifest_derivative import ManifestDerivative

        from .manifest_derivative import ManifestDerivative

        fields: dict[str, Callable[[Any], None]] = {
            "derivatives": lambda n : setattr(self, 'derivatives', n.get_collection_of_object_values(ManifestDerivative)),
            "hasThumbnail": lambda n : setattr(self, 'has_thumbnail', n.get_str_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "urn": lambda n : setattr(self, 'urn', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_collection_of_object_values("derivatives", self.derivatives)
        writer.write_str_value("hasThumbnail", self.has_thumbnail)
        writer.write_str_value("progress", self.progress)
        writer.write_str_value("region", self.region)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
        writer.write_str_value("urn", self.urn)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

