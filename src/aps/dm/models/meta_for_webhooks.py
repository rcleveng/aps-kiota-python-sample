from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MetaForWebhooks(AdditionalDataHolder, Parsable):
    """
    Meta information required for webhooks.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Workflow ID of a webhook that listens to Model Derivative events. Must be less than 36 characters. Only ASCII characters (a-z, A-Z, 0-9), periods (.), and hyphens (-) are accepted.See the [Creating a Webhook and Listening to Events](/en/docs/webhooks/v1/tutorials/create-a-hook-model-derivative) tutorial for more information.**Note**: This attribute applies to BIM 360 Docs only.
    workflow: Optional[str] = None
    # A user defined JSON object containing custom workflow information for the specified webhook event. Must be less than 1KB.**Note**: Applicable only if a valid value has been specified for ``meta.workflow``. 
    workflow_attribute: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MetaForWebhooks:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MetaForWebhooks
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MetaForWebhooks()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "workflow": lambda n : setattr(self, 'workflow', n.get_str_value()),
            "workflowAttribute": lambda n : setattr(self, 'workflow_attribute', n.get_str_value()),
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
        writer.write_str_value("workflowAttribute", self.workflow_attribute)
        writer.write_additional_data_value(self.additional_data)
    

