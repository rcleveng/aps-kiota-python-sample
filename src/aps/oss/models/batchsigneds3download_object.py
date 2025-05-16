from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .batchsigneds3download_object_requests import Batchsigneds3download_object_requests

@dataclass
class Batchsigneds3download_object(AdditionalDataHolder, Parsable):
    """
    The response to a Batch Generate Signed S3 Download URLs operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array where each element is an object containing information needed to generate a signed S3 download URL.
    requests: Optional[list[Batchsigneds3download_object_requests]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Batchsigneds3download_object:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Batchsigneds3download_object
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Batchsigneds3download_object()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .batchsigneds3download_object_requests import Batchsigneds3download_object_requests

        from .batchsigneds3download_object_requests import Batchsigneds3download_object_requests

        fields: dict[str, Callable[[Any], None]] = {
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(Batchsigneds3download_object_requests)),
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
        writer.write_collection_of_object_values("requests", self.requests)
        writer.write_additional_data_value(self.additional_data)
    

