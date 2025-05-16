from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sheet_type import SheetType
    from .solid_type import SolidType
    from .surface_type import SurfaceType

@dataclass
class JobPayloadFormatAdvancedIGES(AdditionalDataHolder, Parsable):
    """
    An object that contains advanced options for an IGES output.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .sheet_type import SheetType

    # The sheet body type to export as, when the output is IGES.  Possible values are:- ``open``-  ``shell`` - ``surface`` - (Default)- ``wireframe``
    sheet_type: Optional[SheetType] = SheetType("surface")
    from .solid_type import SolidType

    # The solid body type to export as, when the output is IGES. Possible values are: - ``solid`` - (Default)- ``surface``- ``wireframe``
    solid_type: Optional[SolidType] = SolidType("solid")
    from .surface_type import SurfaceType

    # Specifies the surface type to export as, when the output is IGES. Possible values are - ``bounded`` - (Default) Bounded surface- ``trimmed`` - Trimmed surface-  `wireframe`. Wireframe  surface.'
    surface_type: Optional[SurfaceType] = SurfaceType("bounded")
    # Possible values are between `0` and `1`. By default it is set at 0.001.
    tolerance: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatAdvancedIGES:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatAdvancedIGES
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatAdvancedIGES()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sheet_type import SheetType
        from .solid_type import SolidType
        from .surface_type import SurfaceType

        from .sheet_type import SheetType
        from .solid_type import SolidType
        from .surface_type import SurfaceType

        fields: dict[str, Callable[[Any], None]] = {
            "sheetType": lambda n : setattr(self, 'sheet_type', n.get_enum_value(SheetType)),
            "solidType": lambda n : setattr(self, 'solid_type', n.get_enum_value(SolidType)),
            "surfaceType": lambda n : setattr(self, 'surface_type', n.get_enum_value(SurfaceType)),
            "tolerance": lambda n : setattr(self, 'tolerance', n.get_float_value()),
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
        writer.write_enum_value("sheetType", self.sheet_type)
        writer.write_enum_value("solidType", self.solid_type)
        writer.write_enum_value("surfaceType", self.surface_type)
        writer.write_float_value("tolerance", self.tolerance)
        writer.write_additional_data_value(self.additional_data)
    

