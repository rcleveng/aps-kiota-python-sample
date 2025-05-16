from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_to_type import AssignedToType
    from .issue_payload_custom_attributes import IssuePayload_customAttributes
    from .issue_payload_gps_coordinates import IssuePayload_gpsCoordinates
    from .issue_payload_permitted_actions import IssuePayload_permittedActions
    from .status import Status

@dataclass
class IssuePayload(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Autodesk ID of the member, role, or company you want to assign to the issue. Note that if you select an assignee ID, you also need to select a type (assignedToType).
    assigned_to: Optional[str] = None
    # The assignedToType property
    assigned_to_type: Optional[AssignedToType] = None
    # A list of custom attributes of the specific issue.
    custom_attributes: Optional[list[IssuePayload_customAttributes]] = None
    # The description and purpose of the issue.Max length: 10000
    description: Optional[str] = None
    # The due date of the issue, in ISO8601 format.
    due_date: Optional[str] = None
    # A GPS Coordinate which represents the geo location of the issue.
    gps_coordinates: Optional[IssuePayload_gpsCoordinates] = None
    # The unique identifier of the subtype of the issue.
    issue_subtype_id: Optional[str] = None
    # The unique identifier of the type of root cause for the issue.
    issue_template_id: Optional[str] = None
    # The location as plain text that relates to the issue.Max length: 8300
    location_details: Optional[str] = None
    # The unique LBS (Location Breakdown Structure) identifier that relates to the issue.
    location_id: Optional[str] = None
    # The list of actions permitted for the user for this issue in its current state.Note that if a user with Create for my company permissions attempts to assign a user from a another company to the issue, it will return an error.Possible Values: assign_all (can assign another user from another company to the issue), assign_same_company (can only assign another user from the same company to the issue), clear_assignee, delete, add_comment, add_attachment, remove_attachment.The following values are not relevant: add_attachment, remove_attachment.
    permitted_actions: Optional[IssuePayload_permittedActions] = None
    # States whether the issue is published. Default value: false (e.g. unpublished).
    published: Optional[bool] = None
    # The unique identifier of the type of root cause for the issue.
    root_cause_id: Optional[str] = None
    # Not relevant
    snapshot_urn: Optional[str] = None
    # The start date of the issue, in ISO8601 format.
    start_date: Optional[str] = None
    # The current status of the issue. To check the available statuses for the project, call GET users/me and check the permitted statuses list (issue.new.permittedStatuses). For more information about statuses, see the Help documentation.
    status: Optional[Status] = None
    # The description and purpose of the issue.Max length: 10000
    title: Optional[str] = None
    # The Autodesk ID of the member you want to assign as a watcher for the issue.
    watchers: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IssuePayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IssuePayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IssuePayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_to_type import AssignedToType
        from .issue_payload_custom_attributes import IssuePayload_customAttributes
        from .issue_payload_gps_coordinates import IssuePayload_gpsCoordinates
        from .issue_payload_permitted_actions import IssuePayload_permittedActions
        from .status import Status

        from .assigned_to_type import AssignedToType
        from .issue_payload_custom_attributes import IssuePayload_customAttributes
        from .issue_payload_gps_coordinates import IssuePayload_gpsCoordinates
        from .issue_payload_permitted_actions import IssuePayload_permittedActions
        from .status import Status

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "assignedToType": lambda n : setattr(self, 'assigned_to_type', n.get_enum_value(AssignedToType)),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(IssuePayload_customAttributes)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_str_value()),
            "gpsCoordinates": lambda n : setattr(self, 'gps_coordinates', n.get_object_value(IssuePayload_gpsCoordinates)),
            "issueSubtypeId": lambda n : setattr(self, 'issue_subtype_id', n.get_str_value()),
            "issueTemplateId": lambda n : setattr(self, 'issue_template_id', n.get_str_value()),
            "locationDetails": lambda n : setattr(self, 'location_details', n.get_str_value()),
            "locationId": lambda n : setattr(self, 'location_id', n.get_str_value()),
            "permittedActions": lambda n : setattr(self, 'permitted_actions', n.get_object_value(IssuePayload_permittedActions)),
            "published": lambda n : setattr(self, 'published', n.get_bool_value()),
            "rootCauseId": lambda n : setattr(self, 'root_cause_id', n.get_str_value()),
            "snapshotUrn": lambda n : setattr(self, 'snapshot_urn', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Status)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "watchers": lambda n : setattr(self, 'watchers', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_enum_value("assignedToType", self.assigned_to_type)
        writer.write_collection_of_object_values("customAttributes", self.custom_attributes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("dueDate", self.due_date)
        writer.write_object_value("gpsCoordinates", self.gps_coordinates)
        writer.write_str_value("issueSubtypeId", self.issue_subtype_id)
        writer.write_str_value("issueTemplateId", self.issue_template_id)
        writer.write_str_value("locationDetails", self.location_details)
        writer.write_str_value("locationId", self.location_id)
        writer.write_object_value("permittedActions", self.permitted_actions)
        writer.write_bool_value("published", self.published)
        writer.write_str_value("rootCauseId", self.root_cause_id)
        writer.write_str_value("snapshotUrn", self.snapshot_urn)
        writer.write_str_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_primitive_values("watchers", self.watchers)
        writer.write_additional_data_value(self.additional_data)
    

