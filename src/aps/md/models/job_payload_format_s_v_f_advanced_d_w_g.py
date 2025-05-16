from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .twod_view import TwodView

@dataclass
class JobPayloadFormatSVFAdvancedDWG(AdditionalDataHolder, Parsable):
    """
    Advanced options for DWG inputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The format that 2D views must be rendered to. Possible values are:- ``legacy`` - (Default) Render to a model derivative specific file format.- ``pdf`` - Render to the PDF file format. When the source design is of type Revit, applies only to Revit 2022 files and newer. If the source design is of type DWG, only properties with semantic values are extracted. 
    twodviews: Optional[TwodView] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVFAdvancedDWG:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVFAdvancedDWG
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatSVFAdvancedDWG()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .twod_view import TwodView

        from .twod_view import TwodView

        fields: dict[str, Callable[[Any], None]] = {
            "2dviews": lambda n : setattr(self, 'twodviews', n.get_enum_value(TwodView)),
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
        writer.write_enum_value("2dviews", self.twodviews)
        writer.write_additional_data_value(self.additional_data)
    

