from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_accepted_jobs_output import Job_acceptedJobs_output

@dataclass
class Job_acceptedJobs(AdditionalDataHolder, Parsable):
    """
    List of the requested outputs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identical to the ``output`` object of the request body. For information on each attribute, see the request body structure description.
    output: Optional[Job_acceptedJobs_output] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Job_acceptedJobs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Job_acceptedJobs
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Job_acceptedJobs()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_accepted_jobs_output import Job_acceptedJobs_output

        from .job_accepted_jobs_output import Job_acceptedJobs_output

        fields: dict[str, Callable[[Any], None]] = {
            "output": lambda n : setattr(self, 'output', n.get_object_value(Job_acceptedJobs_output)),
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
        writer.write_object_value("output", self.output)
        writer.write_additional_data_value(self.additional_data)
    

