from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_protocol import ApplicationProtocol

@dataclass
class JobPayloadFormatAdvancedSTEP(AdditionalDataHolder, Parsable):
    """
    An object that contains advanced options for a STEP output.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .application_protocol import ApplicationProtocol

    # Specifies the application protocol to use when the output type is STEP. Possible values are: - ``203`` - Configuration controlled design.- ``214`` - (Default) Core data for automotive mechanical design processes. - ``242`` - Managed model based 3D engineering. 
    application_protocol: Optional[ApplicationProtocol] = ApplicationProtocol("214")
    # Possible values are between `0` and `1`. By default it is set at 0.001.
    tolerance: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatAdvancedSTEP:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatAdvancedSTEP
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatAdvancedSTEP()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_protocol import ApplicationProtocol

        from .application_protocol import ApplicationProtocol

        fields: dict[str, Callable[[Any], None]] = {
            "applicationProtocol": lambda n : setattr(self, 'application_protocol', n.get_enum_value(ApplicationProtocol)),
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
        writer.write_enum_value("applicationProtocol", self.application_protocol)
        writer.write_float_value("tolerance", self.tolerance)
        writer.write_additional_data_value(self.additional_data)
    

