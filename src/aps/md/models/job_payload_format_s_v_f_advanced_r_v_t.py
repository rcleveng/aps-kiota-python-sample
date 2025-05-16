from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .extractor_version import ExtractorVersion
    from .material_mode import MaterialMode
    from .twod_view import TwodView

@dataclass
class JobPayloadFormatSVFAdvancedRVT(AdditionalDataHolder, Parsable):
    """
    Advanced options for Revit inputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies what version of the Revit translator/extractor to use. Applicable only when the source design is of type RVT. Possible values are:- ``next`` - Makes the translation job use the newest available version of the translator/extractor. This option is meant to be used by beta testers who wish to test a pre-release version of the translator. If no pre-release version is available, the system uses the current official release version.- ``previous`` - Makes the translation job use the previous official release version of the translator/extractor. This option is meant to be used as a workaround in case of regressions caused by a new official release of the translator/extractor. If this attribute is not specified, the system uses the current official release version.
    extractor_version: Optional[ExtractorVersion] = None
    # Generates master views when translating from the Revit input format to SVF. This option is ignored for all other input formats. This attribute defaults to false.Master views are 3D views that are generated for each phase of the Revit model. A master view contains all elements (including “room” elements) present in the host model for that phase. The display name of a master view defaults to the name of the phase it is generated from. However, if a view with that name already exists, the Model Derivative service appends a suffix to the default display name.**Notes:**1. Master views do not contain elements from linked models.2. Enabling this option can increase the time it takes to translate the model.
    generate_master_views: Optional[bool] = None
    # Specifies the materials to apply to the generated SVF derivatives. Applicable only when the source design is of type RVT. Possible values are:- ``auto`` - (Default) Use the current setting of the default view of the input file.- ``basic`` - Use basic materials.- ``autodesk`` - Use Autodesk materials.
    material_mode: Optional[MaterialMode] = None
    # The format that 2D views must be rendered to. Possible values are:- ``legacy`` - (Default) Render to a model derivative specific file format.- ``pdf`` - Render to the PDF file format. When the source design is of type Revit, applies only to Revit 2022 files and newer. If the source design is of type DWG, only properties with semantic values are extracted. 
    twodviews: Optional[TwodView] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVFAdvancedRVT:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVFAdvancedRVT
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatSVFAdvancedRVT()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .extractor_version import ExtractorVersion
        from .material_mode import MaterialMode
        from .twod_view import TwodView

        from .extractor_version import ExtractorVersion
        from .material_mode import MaterialMode
        from .twod_view import TwodView

        fields: dict[str, Callable[[Any], None]] = {
            "extractorVersion": lambda n : setattr(self, 'extractor_version', n.get_enum_value(ExtractorVersion)),
            "generateMasterViews": lambda n : setattr(self, 'generate_master_views', n.get_bool_value()),
            "materialMode": lambda n : setattr(self, 'material_mode', n.get_enum_value(MaterialMode)),
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
        writer.write_enum_value("extractorVersion", self.extractor_version)
        writer.write_bool_value("generateMasterViews", self.generate_master_views)
        writer.write_enum_value("materialMode", self.material_mode)
        writer.write_enum_value("2dviews", self.twodviews)
        writer.write_additional_data_value(self.additional_data)
    

