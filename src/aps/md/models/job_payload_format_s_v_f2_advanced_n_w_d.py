from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobPayloadFormatSVF2AdvancedNWD(AdditionalDataHolder, Parsable):
    """
    Advanced options for NWD inputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies how to handle Autodesk material properties.  Applicable only when the source design type is Navisworks.- ``true``: Extract properties for Autodesk materials.- ``false``: (Default) Do not extract properties for Autodesk materials.
    autodesk_material_properties: Optional[bool] = None
    # Specifies whether basic material properties must be extracted or not.  Applicable only when the source design type is Navisworks.- ``true``: Extract properties for basic materials.- ``false``: (Default) Do not extract properties for basic materials.
    basic_material_properties: Optional[bool] = None
    # Specifies whether hidden objects must be extracted or not. Applicable only when the source design type is Navisworks.- ``true``: Extract hidden objects from the input file.- ``false``: (Default) Do not extract hidden objects from the input file.
    hidden_objects: Optional[bool] = None
    # Specifies whether timeliner properties must be extracted or not.  Applicable only when the source design type is Navisworks.- ``true``: Extract timeliner properties.- ``false``: (Default) Do not extract timeliner properties.
    timeliner_properties: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVF2AdvancedNWD:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVF2AdvancedNWD
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatSVF2AdvancedNWD()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "autodeskMaterialProperties": lambda n : setattr(self, 'autodesk_material_properties', n.get_bool_value()),
            "basicMaterialProperties": lambda n : setattr(self, 'basic_material_properties', n.get_bool_value()),
            "hiddenObjects": lambda n : setattr(self, 'hidden_objects', n.get_bool_value()),
            "timelinerProperties": lambda n : setattr(self, 'timeliner_properties', n.get_bool_value()),
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
        writer.write_bool_value("autodeskMaterialProperties", self.autodesk_material_properties)
        writer.write_bool_value("basicMaterialProperties", self.basic_material_properties)
        writer.write_bool_value("hiddenObjects", self.hidden_objects)
        writer.write_bool_value("timelinerProperties", self.timeliner_properties)
        writer.write_additional_data_value(self.additional_data)
    

