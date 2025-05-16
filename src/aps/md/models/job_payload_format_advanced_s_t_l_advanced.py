from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .export_file_structure import ExportFileStructure
    from .format import Format

@dataclass
class JobPayloadFormatAdvancedSTL_advanced(AdditionalDataHolder, Parsable):
    """
    Advanced options for `stl` type.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .export_file_structure import ExportFileStructure

    # Specifies the structure of the derivative, when the specified output is STL. Possible values are: - ``single`` (Default) Create one STL file for all the input files (assembly file).- ``multiple``: Create a separate STL file for each object
    export_file_structure: Optional[ExportFileStructure] = ExportFileStructure("single")
    from .format import Format

    # Specifies the format of the file to create, when the specified output is STL.  Possible values are:- ``ascii`` - Create derivative as an ASCII STL file.- ``binary`` - (Default) Create derivative as a binary STL file.  
    format: Optional[Format] = Format("binary")
    # Color is exported by default. If set to ``true``, color is exported. If set to `false`, color is not exported.
    export_color: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatAdvancedSTL_advanced:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatAdvancedSTL_advanced
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatAdvancedSTL_advanced()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .export_file_structure import ExportFileStructure
        from .format import Format

        from .export_file_structure import ExportFileStructure
        from .format import Format

        fields: dict[str, Callable[[Any], None]] = {
            "exportColor": lambda n : setattr(self, 'export_color', n.get_bool_value()),
            "exportFileStructure": lambda n : setattr(self, 'export_file_structure', n.get_enum_value(ExportFileStructure)),
            "format": lambda n : setattr(self, 'format', n.get_enum_value(Format)),
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
        writer.write_bool_value("exportColor", self.export_color)
        writer.write_enum_value("exportFileStructure", self.export_file_structure)
        writer.write_enum_value("format", self.format)
        writer.write_additional_data_value(self.additional_data)
    

