from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .issue_custom_attributes import Issue_customAttributes
    from .issue_gps_coordinates import Issue_gpsCoordinates
    from .issue_linked_documents import Issue_linkedDocuments
    from .issue_links import Issue_links
    from .issue_official_response import Issue_officialResponse
    from .issue_permitted_actions import Issue_permittedActions

@dataclass
class Issue(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Autodesk ID of the member, role, or company you want to assign to the issue. Note that if you select an assignee ID, you also need to select a type (assignedToType).
    assigned_to: Optional[str] = None
    # The type of the current assignee of this issue. Possible values: user, company, role, null. Note that if you select a type, you also need to select the assignee ID (assignedTo).
    assigned_to_type: Optional[str] = None
    # Not relevant
    attachment_count: Optional[int] = None
    # The date and time the issue was closed, in ISO8601 format.
    closed_at: Optional[str] = None
    # The unique identifier of the user who closed the issue.
    closed_by: Optional[str] = None
    # The number of comments in this issue.
    comment_count: Optional[int] = None
    # Not relevant
    container_id: Optional[str] = None
    # The date and time the issue was created, in ISO8601 format.
    created_at: Optional[str] = None
    # The unique identifier of the user who created the issue
    created_by: Optional[str] = None
    # A list of custom attributes of the specific issue.
    custom_attributes: Optional[list[Issue_customAttributes]] = None
    # States whether the issue was deleted. Default value: false.
    deleted: Optional[bool] = None
    # The date and time the issue was deleted, in ISO8601 format. This is only relevant for deleted issues.
    deleted_at: Optional[str] = None
    # The Autodesk ID of the user who deleted the issue. This is only relevant for deleted issues.
    deleted_by: Optional[str] = None
    # The description and purpose of the issue.Max length: 10000
    description: Optional[str] = None
    # The chronological user-friendly identifier of the issue.
    display_id: Optional[int] = None
    # The due date of the issue, in ISO8601 format.
    due_date: Optional[str] = None
    # A GPS Coordinate which represents the geo location of the issue.
    gps_coordinates: Optional[Issue_gpsCoordinates] = None
    # The unique identifier of the issue.
    id: Optional[str] = None
    # The unique identifier of the subtype of the issue.
    issue_subtype_id: Optional[str] = None
    # Not relevant
    issue_template_id: Optional[str] = None
    # The unique identifier of the type of the issue.
    issue_type_id: Optional[str] = None
    # Information about the files associated with issues (pushpins).
    linked_documents: Optional[list[Issue_linkedDocuments]] = None
    # Not relevant
    links: Optional[list[Issue_links]] = None
    # The location as plain text that relates to the issue.Max length: 8300
    location_details: Optional[str] = None
    # The unique LBS (Location Breakdown Structure) identifier that relates to the issue.
    location_id: Optional[str] = None
    # Not relevant
    official_response: Optional[Issue_officialResponse] = None
    # Not relevant
    opened_at: Optional[str] = None
    # Not relevant
    opened_by: Optional[str] = None
    # Not relevant
    owner_id: Optional[str] = None
    # The list of actions permitted for the user for this issue in its current state.Note that if a user with Create for my company permissions attempts to assign a user from a another company to the issue, it will return an error.Possible Values: assign_all (can assign another user from another company to the issue), assign_same_company (can only assign another user from the same company to the issue), clear_assignee, delete, add_comment, add_attachment, remove_attachment.The following values are not relevant: add_attachment, remove_attachment.
    permitted_actions: Optional[Issue_permittedActions] = None
    # A list of attributes the current user can manipulate in the current context. issueTypeId, linkedDocument, links, ownerId, officialResponse, rootCauseId, snapshotUrn are not applicable.
    permitted_attributes: Optional[list[str]] = None
    # A list of statuses accessible to the current user, this is based on the current status of the issue and the user permissions.Possible Values: open, pending, in_review, closed.
    permitted_statuses: Optional[list[str]] = None
    # States whether the issue is published. Default value: false (e.g. unpublished).
    published: Optional[bool] = None
    # The unique identifier of the type of root cause for the issue.
    root_cause_id: Optional[str] = None
    # Not relevant
    snapshot_has_markups: Optional[bool] = None
    # Not relevant
    snapshot_urn: Optional[str] = None
    # The start date of the issue, in ISO8601 format.
    start_date: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The description and purpose of the issue.Max length: 10000
    title: Optional[str] = None
    # The date and time the issue was updated, in ISO8601 format.
    updated_at: Optional[str] = None
    # The unique identifier of the user who updated the issue.
    updated_by: Optional[str] = None
    # The Autodesk ID of the member you want to assign as a watcher for the issue.
    watchers: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Issue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Issue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Issue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .issue_custom_attributes import Issue_customAttributes
        from .issue_gps_coordinates import Issue_gpsCoordinates
        from .issue_linked_documents import Issue_linkedDocuments
        from .issue_links import Issue_links
        from .issue_official_response import Issue_officialResponse
        from .issue_permitted_actions import Issue_permittedActions

        from .issue_custom_attributes import Issue_customAttributes
        from .issue_gps_coordinates import Issue_gpsCoordinates
        from .issue_linked_documents import Issue_linkedDocuments
        from .issue_links import Issue_links
        from .issue_official_response import Issue_officialResponse
        from .issue_permitted_actions import Issue_permittedActions

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "assignedToType": lambda n : setattr(self, 'assigned_to_type', n.get_str_value()),
            "attachmentCount": lambda n : setattr(self, 'attachment_count', n.get_int_value()),
            "closedAt": lambda n : setattr(self, 'closed_at', n.get_str_value()),
            "closedBy": lambda n : setattr(self, 'closed_by', n.get_str_value()),
            "commentCount": lambda n : setattr(self, 'comment_count', n.get_int_value()),
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(Issue_customAttributes)),
            "deleted": lambda n : setattr(self, 'deleted', n.get_bool_value()),
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_str_value()),
            "deletedBy": lambda n : setattr(self, 'deleted_by', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayId": lambda n : setattr(self, 'display_id', n.get_int_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_str_value()),
            "gpsCoordinates": lambda n : setattr(self, 'gps_coordinates', n.get_object_value(Issue_gpsCoordinates)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "issueSubtypeId": lambda n : setattr(self, 'issue_subtype_id', n.get_str_value()),
            "issueTemplateId": lambda n : setattr(self, 'issue_template_id', n.get_str_value()),
            "issueTypeId": lambda n : setattr(self, 'issue_type_id', n.get_str_value()),
            "linkedDocuments": lambda n : setattr(self, 'linked_documents', n.get_collection_of_object_values(Issue_linkedDocuments)),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(Issue_links)),
            "locationDetails": lambda n : setattr(self, 'location_details', n.get_str_value()),
            "locationId": lambda n : setattr(self, 'location_id', n.get_str_value()),
            "officialResponse": lambda n : setattr(self, 'official_response', n.get_object_value(Issue_officialResponse)),
            "openedAt": lambda n : setattr(self, 'opened_at', n.get_str_value()),
            "openedBy": lambda n : setattr(self, 'opened_by', n.get_str_value()),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_str_value()),
            "permittedActions": lambda n : setattr(self, 'permitted_actions', n.get_object_value(Issue_permittedActions)),
            "permittedAttributes": lambda n : setattr(self, 'permitted_attributes', n.get_collection_of_primitive_values(str)),
            "permittedStatuses": lambda n : setattr(self, 'permitted_statuses', n.get_collection_of_primitive_values(str)),
            "published": lambda n : setattr(self, 'published', n.get_bool_value()),
            "rootCauseId": lambda n : setattr(self, 'root_cause_id', n.get_str_value()),
            "snapshotHasMarkups": lambda n : setattr(self, 'snapshot_has_markups', n.get_bool_value()),
            "snapshotUrn": lambda n : setattr(self, 'snapshot_urn', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_str_value()),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_str_value()),
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
        writer.write_str_value("assignedToType", self.assigned_to_type)
        writer.write_int_value("attachmentCount", self.attachment_count)
        writer.write_str_value("closedAt", self.closed_at)
        writer.write_str_value("closedBy", self.closed_by)
        writer.write_int_value("commentCount", self.comment_count)
        writer.write_str_value("containerId", self.container_id)
        writer.write_str_value("createdAt", self.created_at)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_collection_of_object_values("customAttributes", self.custom_attributes)
        writer.write_bool_value("deleted", self.deleted)
        writer.write_str_value("deletedAt", self.deleted_at)
        writer.write_str_value("deletedBy", self.deleted_by)
        writer.write_str_value("description", self.description)
        writer.write_int_value("displayId", self.display_id)
        writer.write_str_value("dueDate", self.due_date)
        writer.write_object_value("gpsCoordinates", self.gps_coordinates)
        writer.write_str_value("id", self.id)
        writer.write_str_value("issueSubtypeId", self.issue_subtype_id)
        writer.write_str_value("issueTemplateId", self.issue_template_id)
        writer.write_str_value("issueTypeId", self.issue_type_id)
        writer.write_collection_of_object_values("linkedDocuments", self.linked_documents)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_str_value("locationDetails", self.location_details)
        writer.write_str_value("locationId", self.location_id)
        writer.write_object_value("officialResponse", self.official_response)
        writer.write_str_value("openedAt", self.opened_at)
        writer.write_str_value("openedBy", self.opened_by)
        writer.write_str_value("ownerId", self.owner_id)
        writer.write_object_value("permittedActions", self.permitted_actions)
        writer.write_collection_of_primitive_values("permittedAttributes", self.permitted_attributes)
        writer.write_collection_of_primitive_values("permittedStatuses", self.permitted_statuses)
        writer.write_bool_value("published", self.published)
        writer.write_str_value("rootCauseId", self.root_cause_id)
        writer.write_bool_value("snapshotHasMarkups", self.snapshot_has_markups)
        writer.write_str_value("snapshotUrn", self.snapshot_urn)
        writer.write_str_value("startDate", self.start_date)
        writer.write_str_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_str_value("updatedAt", self.updated_at)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_collection_of_primitive_values("watchers", self.watchers)
        writer.write_additional_data_value(self.additional_data)
    

