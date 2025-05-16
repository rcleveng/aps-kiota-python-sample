from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .issue_linked_documents_details import Issue_linkedDocuments_details

@dataclass
class Issue_linkedDocuments(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time the pushpin issue was closed, in ISO8601 format.
    closed_at: Optional[str] = None
    # The version of the file when the pushpin issue was closed.
    closed_at_version: Optional[int] = None
    # The Autodesk ID of the user who closed the pushpin issue.
    closed_by: Optional[str] = None
    # The date and time the pushpin was created, in ISO8601 format.
    created_at: Optional[str] = None
    # The version of the file the pushin issue was added to. For information about file versions, see the Data Management API.
    created_at_version: Optional[int] = None
    # The Autodesk ID of the user who created the pushpin issue.
    created_by: Optional[str] = None
    # Information about the individual viewable.
    details: Optional[Issue_linkedDocuments_details] = None
    # The type of file. Possible values:TwoDVectorPushpin (3D models) TwoDRasterPushpin (2D sheets and views)
    type: Optional[str] = None
    # The ID of the file associated with the issue (pushpin). Note the we do not currently support data associated with the ACC Build Sheet tool.
    urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Issue_linkedDocuments:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Issue_linkedDocuments
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Issue_linkedDocuments()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .issue_linked_documents_details import Issue_linkedDocuments_details

        from .issue_linked_documents_details import Issue_linkedDocuments_details

        fields: dict[str, Callable[[Any], None]] = {
            "closedAt": lambda n : setattr(self, 'closed_at', n.get_str_value()),
            "closedAtVersion": lambda n : setattr(self, 'closed_at_version', n.get_int_value()),
            "closedBy": lambda n : setattr(self, 'closed_by', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "createdAtVersion": lambda n : setattr(self, 'created_at_version', n.get_int_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(Issue_linkedDocuments_details)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("closedAt", self.closed_at)
        writer.write_int_value("closedAtVersion", self.closed_at_version)
        writer.write_str_value("closedBy", self.closed_by)
        writer.write_str_value("createdAt", self.created_at)
        writer.write_int_value("createdAtVersion", self.created_at_version)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_object_value("details", self.details)
        writer.write_str_value("type", self.type)
        writer.write_str_value("urn", self.urn)
        writer.write_additional_data_value(self.additional_data)
    

