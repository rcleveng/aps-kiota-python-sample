from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .batchsigneds3download_response_results import Batchsigneds3download_response_results

@dataclass
class Batchsigneds3download_response(AdditionalDataHolder, Parsable):
    """
    The response to a Batch Generate Signed S3 Download URLs operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A map of the returned results; each key in the map corresponds to an object key in the batch, and the value includes the results for that object.
    results: Optional[Batchsigneds3download_response_results] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Batchsigneds3download_response:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Batchsigneds3download_response
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Batchsigneds3download_response()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .batchsigneds3download_response_results import Batchsigneds3download_response_results

        from .batchsigneds3download_response_results import Batchsigneds3download_response_results

        fields: dict[str, Callable[[Any], None]] = {
            "results": lambda n : setattr(self, 'results', n.get_object_value(Batchsigneds3download_response_results)),
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
        writer.write_object_value("results", self.results)
        writer.write_additional_data_value(self.additional_data)
    

