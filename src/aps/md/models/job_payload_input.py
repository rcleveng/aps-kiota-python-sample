from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobPayload_input(AdditionalDataHolder, Parsable):
    """
    An object describing the attributes of the source design.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # - ``true`` - Instructs the system to check for references, and if any exist, download all referenced files. Setting this parameter to ``true`` is mandatory when translating source designs consisting of multiple files. For example, Autodesk Inventor assemblies.- ``false`` - (Default) Instructs the system not to check for references.
    check_references: Optional[bool] = None
    # - ``true``: The source design is compressed as a zip file. If set to ``true``, you need to define the `rootFilename`.'- ``false``: (Default) The source design is not compressed.
    compressed_urn: Optional[bool] = None
    # The file name of the top-level component of the source design.  Mandatory if  ``compressedUrn`` is set to ``true``.
    root_filename: Optional[str] = None
    # The URL safe Base64 encoded URN of the source design. **Note:** The URN is returned as the ``objectID`` once you complete uploading the source design to APS. This value must be converted to a `Base64 (URL Safe) encoded <http://www.freeformatter.com/base64-encoder.html>`_ string before you can specify it for this attribute.
    urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayload_input:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayload_input
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayload_input()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checkReferences": lambda n : setattr(self, 'check_references', n.get_bool_value()),
            "compressedUrn": lambda n : setattr(self, 'compressed_urn', n.get_bool_value()),
            "rootFilename": lambda n : setattr(self, 'root_filename', n.get_str_value()),
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
        writer.write_bool_value("checkReferences", self.check_references)
        writer.write_bool_value("compressedUrn", self.compressed_urn)
        writer.write_str_value("rootFilename", self.root_filename)
        writer.write_str_value("urn", self.urn)
        writer.write_additional_data_value(self.additional_data)
    

