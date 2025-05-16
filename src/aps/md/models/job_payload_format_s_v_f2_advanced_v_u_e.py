from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hierarchy import Hierarchy

@dataclass
class JobPayloadFormatSVF2AdvancedVUE(AdditionalDataHolder, Parsable):
    """
    Advanced options for VUE inputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies how the hierarchy of items are determined. Applicable only when the source design is of type VUE.- ``Classic`` - (Default) Uses hardcoded rules to set the hierarchy of items.- ``SystemPath`` - Uses a linked XML or MDB2 properties file to set hierarchy of items. You can use this option to make the organization of items consistent with SmartPlant 3D.**Notes:**1. The functioning of the SystemPath depends on the default setting of the property SP3D_SystemPath or System Path.2. The pathing delimiter must be /.3. If you want to customize further, import the VUE file to Navisworks. After that, use POST job on the resulting Navisworks (nwc/nwd) file.
    hierarchy: Optional[Hierarchy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVF2AdvancedVUE:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVF2AdvancedVUE
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatSVF2AdvancedVUE()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hierarchy import Hierarchy

        from .hierarchy import Hierarchy

        fields: dict[str, Callable[[Any], None]] = {
            "hierarchy": lambda n : setattr(self, 'hierarchy', n.get_enum_value(Hierarchy)),
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
        writer.write_enum_value("hierarchy", self.hierarchy)
        writer.write_additional_data_value(self.additional_data)
    

