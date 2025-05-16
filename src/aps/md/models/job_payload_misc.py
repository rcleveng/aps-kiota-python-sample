from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_misc_workflow_attribute import JobPayload_misc_workflowAttribute

@dataclass
class JobPayload_misc(AdditionalDataHolder, Parsable):
    """
    A collection of miscellaneous parameters.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The workflow ID of the webhook that listens to Model Derivative events. It must be 36 characters or less and can only contain alphanumeric characters (A-Z, 0-9) and hyphens (-).
    workflow: Optional[str] = None
    # A user-defined JSON object, which you can use to set some custom workflow information. It must be less than 1KB and is ignored if ``misc.workflow`` is not specified.
    workflow_attribute: Optional[JobPayload_misc_workflowAttribute] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayload_misc:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayload_misc
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayload_misc()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_misc_workflow_attribute import JobPayload_misc_workflowAttribute

        from .job_payload_misc_workflow_attribute import JobPayload_misc_workflowAttribute

        fields: dict[str, Callable[[Any], None]] = {
            "workflow": lambda n : setattr(self, 'workflow', n.get_str_value()),
            "workflowAttribute": lambda n : setattr(self, 'workflow_attribute', n.get_object_value(JobPayload_misc_workflowAttribute)),
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
        writer.write_str_value("workflow", self.workflow)
        writer.write_object_value("workflowAttribute", self.workflow_attribute)
        writer.write_additional_data_value(self.additional_data)
    

