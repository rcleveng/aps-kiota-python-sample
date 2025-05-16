from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_format_s_v_f2_advanced import JobPayloadFormatSVF2_advanced
    from .output_type import OutputType
    from .view import View

@dataclass
class JobPayloadFormatSVF2(AdditionalDataHolder, Parsable):
    """
    Options for SVF2 outputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Advanced options for ``svf2`` output types. The available options depend on the input type.
    advanced: Optional[JobPayloadFormatSVF2_advanced] = None
    # The requested output types. Possible values include `svf`, `svf2`, `thumbnail`, `stl`, `step`, `iges`, `obj`, `ifc` or `dwg`. For a list of supported types, call the [GET formats](/en/docs/model-derivative/v2/reference/http/formats-GET) endpoint.
    type: Optional[OutputType] = None
    # Specifies the type of view to generate. Possible values are `2d` and `3d`.
    views: Optional[list[View]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVF2:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVF2
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatSVF2()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_format_s_v_f2_advanced import JobPayloadFormatSVF2_advanced
        from .output_type import OutputType
        from .view import View

        from .job_payload_format_s_v_f2_advanced import JobPayloadFormatSVF2_advanced
        from .output_type import OutputType
        from .view import View

        fields: dict[str, Callable[[Any], None]] = {
            "advanced": lambda n : setattr(self, 'advanced', n.get_object_value(JobPayloadFormatSVF2_advanced)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(OutputType)),
            "views": lambda n : setattr(self, 'views', n.get_collection_of_enum_values(View)),
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
        writer.write_enum_value("type", self.type)
        writer.write_collection_of_enum_values("views", self.views)
        writer.write_additional_data_value(self.additional_data)
    

