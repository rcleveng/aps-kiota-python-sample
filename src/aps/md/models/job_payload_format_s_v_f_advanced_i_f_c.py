from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .building_storeys import BuildingStoreys
    from .conversion_method import ConversionMethod
    from .opening_elements import OpeningElements
    from .spaces import Spaces

@dataclass
class JobPayloadFormatSVFAdvancedIFC(AdditionalDataHolder, Parsable):
    """
    Advanced options for IFC inputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies how storeys are translated. Applicable only when the source design is of type IFC. Possible values are:- ``hide`` - (Default) Storeys are translated but not visible by default.- ``show`` - Storeys are translated and are visible by default.- ``skip`` - Storeys are not translated.**Note:** These options are applicable only when ``conversionMethod`` is set to ``modern`` or ``v3``.
    building_storeys: Optional[BuildingStoreys] = None
    # Specifies what IFC loader to use during translation. Applicable only when the source design is of type IFC. Possible values are:- ``legacy`` - Use IFC loader version 1, which is based on the Navisworks IFC loader. - ``modern`` - Use IFC loader version 2, which is based on the Revit IFC loader. - ``v3`` - Use IFC loader version 3, which is based on the Revit IFC loader.- ``v4`` - **(Recommended)** Use IFC loader version 4, which is a native solution specifically designed for Autodesk Platform Services (APS). It does not depend on Navisworks or Revit. 
    conversion_method: Optional[ConversionMethod] = None
    # Specifies how openings are translated. Applicable only when the source design is of type IFC. Possible values are:- ``hide`` - (Default) Openings are translated but are not visible by default.- ``show`` - Openings are translated and are visible by default.- ``skip`` - Openings are not translated.**Note:** These options are applicable only when conversionMethod is set to ``modern`` or ``v3``.
    opening_elements: Optional[OpeningElements] = None
    # Specifies how spaces are translated. Applicable only when the source design is of type IFC. Possible values are:- ``hide`` - (Default) spaces are translated but are not visible by default.- ``show`` - Spaces are translated and are visible by default.- ``skip`` - Spaces are not translated.**Note:** These options are applicable only when ``conversionMethod`` is set to ``modern`` or ``v3``.
    spaces: Optional[Spaces] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVFAdvancedIFC:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVFAdvancedIFC
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatSVFAdvancedIFC()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .building_storeys import BuildingStoreys
        from .conversion_method import ConversionMethod
        from .opening_elements import OpeningElements
        from .spaces import Spaces

        from .building_storeys import BuildingStoreys
        from .conversion_method import ConversionMethod
        from .opening_elements import OpeningElements
        from .spaces import Spaces

        fields: dict[str, Callable[[Any], None]] = {
            "buildingStoreys": lambda n : setattr(self, 'building_storeys', n.get_enum_value(BuildingStoreys)),
            "conversionMethod": lambda n : setattr(self, 'conversion_method', n.get_enum_value(ConversionMethod)),
            "openingElements": lambda n : setattr(self, 'opening_elements', n.get_enum_value(OpeningElements)),
            "spaces": lambda n : setattr(self, 'spaces', n.get_enum_value(Spaces)),
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
        writer.write_enum_value("buildingStoreys", self.building_storeys)
        writer.write_enum_value("conversionMethod", self.conversion_method)
        writer.write_enum_value("openingElements", self.opening_elements)
        writer.write_enum_value("spaces", self.spaces)
        writer.write_additional_data_value(self.additional_data)
    

