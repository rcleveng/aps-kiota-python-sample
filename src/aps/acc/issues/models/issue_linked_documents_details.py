from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .issue_linked_documents_details_position import Issue_linkedDocuments_details_position
    from .issue_linked_documents_details_viewable import Issue_linkedDocuments_details_viewable
    from .issue_linked_documents_details_viewer_state import Issue_linkedDocuments_details_viewerState

@dataclass
class Issue_linkedDocuments_details(AdditionalDataHolder, Parsable):
    """
    Information about the individual viewable.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An external identifier of the element the pushpin is associated with in the viewable.
    external_id: Optional[str] = None
    # The ID of the element the pushpin is associated with in the viewable.
    object_id: Optional[int] = None
    # The position of the pushpin in the viewable.
    position: Optional[Issue_linkedDocuments_details_position] = None
    # The individual viewable associated with the issue (pushpin). This is relevant for both individual 2D sheets and views within a 3D model, and individual PDF sheets within a multi-sheet PDF file. It is only relevant if the issue is associated with a file.
    viewable: Optional[Issue_linkedDocuments_details_viewable] = None
    # The viewer state at the time the pushpin was created. Maximum length: 2,500,000 characters. You can get the viewer state object by calling ViewerState.getState(). To restore the viewer instance use ViewerState.restoreState(). See the `Viewer API documentation https://developer.autodesk.com/en/docs/viewer/v2/reference/javascript/viewerstate/`_ for more details.
    viewer_state: Optional[Issue_linkedDocuments_details_viewerState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Issue_linkedDocuments_details:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Issue_linkedDocuments_details
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Issue_linkedDocuments_details()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .issue_linked_documents_details_position import Issue_linkedDocuments_details_position
        from .issue_linked_documents_details_viewable import Issue_linkedDocuments_details_viewable
        from .issue_linked_documents_details_viewer_state import Issue_linkedDocuments_details_viewerState

        from .issue_linked_documents_details_position import Issue_linkedDocuments_details_position
        from .issue_linked_documents_details_viewable import Issue_linkedDocuments_details_viewable
        from .issue_linked_documents_details_viewer_state import Issue_linkedDocuments_details_viewerState

        fields: dict[str, Callable[[Any], None]] = {
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_int_value()),
            "position": lambda n : setattr(self, 'position', n.get_object_value(Issue_linkedDocuments_details_position)),
            "viewable": lambda n : setattr(self, 'viewable', n.get_object_value(Issue_linkedDocuments_details_viewable)),
            "viewerState": lambda n : setattr(self, 'viewer_state', n.get_object_value(Issue_linkedDocuments_details_viewerState)),
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
        writer.write_str_value("externalId", self.external_id)
        writer.write_int_value("objectId", self.object_id)
        writer.write_object_value("position", self.position)
        writer.write_object_value("viewable", self.viewable)
        writer.write_object_value("viewerState", self.viewer_state)
        writer.write_additional_data_value(self.additional_data)
    

