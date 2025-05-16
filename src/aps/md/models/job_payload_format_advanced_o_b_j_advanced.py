from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .export_file_structure import ExportFileStructure
    from .unit import Unit

@dataclass
class JobPayloadFormatAdvancedOBJ_advanced(AdditionalDataHolder, Parsable):
    """
    Advanced options for OBJ output type.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .export_file_structure import ExportFileStructure

    # Specifies the structure of the derivative, when the specified output is STL. Possible values are: - ``single`` (Default) Create one STL file for all the input files (assembly file).- ``multiple``: Create a separate STL file for each object
    export_file_structure: Optional[ExportFileStructure] = ExportFileStructure("single")
    # Required for geometry extractions. Specifies the ID of the Model View that contains the geometry to extract.
    model_guid: Optional[str] = None
    # Required for geometry extractions. Specifies the IDs of the objects (``objectID) to extract. -1 will extract the entire model.
    object_ids: Optional[list[int]] = None
    # The units the models must be translated to, when the output type is OBJ. For example, from millimeters (10, 123, 31) to centimeters (1.0, 12.3, 3.1). If the source unit or the unit you are translating to is not supported, the values remain unchanged.Possible values are: - ``meter``- ``decimeter``- ``centimeter``- ``millimeter``- ``micrometer``- ``nanometer``- ``yard``- ``foot``- ``inch``- ``mil``- ``microinch``**Note:** Not supported when the source design is F3D.
    unit: Optional[Unit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatAdvancedOBJ_advanced:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatAdvancedOBJ_advanced
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatAdvancedOBJ_advanced()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .export_file_structure import ExportFileStructure
        from .unit import Unit

        from .export_file_structure import ExportFileStructure
        from .unit import Unit

        fields: dict[str, Callable[[Any], None]] = {
            "exportFileStructure": lambda n : setattr(self, 'export_file_structure', n.get_enum_value(ExportFileStructure)),
            "modelGuid": lambda n : setattr(self, 'model_guid', n.get_str_value()),
            "objectIds": lambda n : setattr(self, 'object_ids', n.get_collection_of_primitive_values(int)),
            "unit": lambda n : setattr(self, 'unit', n.get_enum_value(Unit)),
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
        writer.write_enum_value("exportFileStructure", self.export_file_structure)
        writer.write_str_value("modelGuid", self.model_guid)
        writer.write_collection_of_primitive_values("objectIds", self.object_ids)
        writer.write_enum_value("unit", self.unit)
        writer.write_additional_data_value(self.additional_data)
    

