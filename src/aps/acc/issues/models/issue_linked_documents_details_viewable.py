from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Issue_linkedDocuments_details_viewable(AdditionalDataHolder, Parsable):
    """
    The individual viewable associated with the issue (pushpin). This is relevant for both individual 2D sheets and views within a 3D model, and individual PDF sheets within a multi-sheet PDF file. It is only relevant if the issue is associated with a file.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ID of the viewable (guid).
    guid: Optional[str] = None
    # Not relevant
    id: Optional[str] = None
    # True if it is a 3D viewable false if it is a 2D viewable
    is3_d: Optional[bool] = None
    # The name of the viewable.Max length: 1000
    name: Optional[str] = None
    # Not relevant
    viewable_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Issue_linkedDocuments_details_viewable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Issue_linkedDocuments_details_viewable
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Issue_linkedDocuments_details_viewable()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is3D": lambda n : setattr(self, 'is3_d', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "viewableId": lambda n : setattr(self, 'viewable_id', n.get_str_value()),
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
        writer.write_str_value("guid", self.guid)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("is3D", self.is3_d)
        writer.write_str_value("name", self.name)
        writer.write_str_value("viewableId", self.viewable_id)
        writer.write_additional_data_value(self.additional_data)
    

