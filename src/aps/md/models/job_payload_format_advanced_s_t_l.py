from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_format_advanced_s_t_l_advanced import JobPayloadFormatAdvancedSTL_advanced

@dataclass
class JobPayloadFormatAdvancedSTL(AdditionalDataHolder, Parsable):
    """
    An object that contains advanced options for a STL output.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Advanced options for `stl` type.
    advanced: Optional[JobPayloadFormatAdvancedSTL_advanced] = None
    # The requested output type. ``stl`` in this case.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatAdvancedSTL:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatAdvancedSTL
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatAdvancedSTL()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_format_advanced_s_t_l_advanced import JobPayloadFormatAdvancedSTL_advanced

        from .job_payload_format_advanced_s_t_l_advanced import JobPayloadFormatAdvancedSTL_advanced

        fields: dict[str, Callable[[Any], None]] = {
            "advanced": lambda n : setattr(self, 'advanced', n.get_object_value(JobPayloadFormatAdvancedSTL_advanced)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_object_value("advanced", self.advanced)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

