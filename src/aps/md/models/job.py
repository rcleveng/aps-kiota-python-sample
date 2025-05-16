from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_accepted_jobs import Job_acceptedJobs

@dataclass
class Job(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a Create Translation Job operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # List of the requested outputs.
    accepted_jobs: Optional[Job_acceptedJobs] = None
    # reporting success status
    result: Optional[str] = None
    # the urn identifier of the source file
    urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Job:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Job
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Job()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_accepted_jobs import Job_acceptedJobs

        from .job_accepted_jobs import Job_acceptedJobs

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedJobs": lambda n : setattr(self, 'accepted_jobs', n.get_object_value(Job_acceptedJobs)),
            "result": lambda n : setattr(self, 'result', n.get_str_value()),
            "urn": lambda n : setattr(self, 'urn', n.get_str_value()),
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
        writer.write_object_value("acceptedJobs", self.accepted_jobs)
        writer.write_str_value("result", self.result)
        writer.write_str_value("urn", self.urn)
        writer.write_additional_data_value(self.additional_data)
    

