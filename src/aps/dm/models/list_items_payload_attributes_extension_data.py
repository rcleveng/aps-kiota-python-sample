from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ListItemsPayload_attributes_extension_data(AdditionalDataHolder, Parsable):
    """
    Contains the custom properties specific to the ListItems command.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specify whether to return the ``pathInProject`` attribute in response for BIM 360 Docs projects. ``pathInProject`` is the path to the item relative to the project’s root folder.- ``true``: Response will contain the ``pathInProject`` attribute for BIM 360 Docs projects.- ``false``: (Default) response will not contain the ``pathInProject`` attribute for BIM 360 Docs projects.Setting this parameter to ``true`` on a non-BIM 360 Docs project results in an error.
    include_path_in_project: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListItemsPayload_attributes_extension_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListItemsPayload_attributes_extension_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListItemsPayload_attributes_extension_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "includePathInProject": lambda n : setattr(self, 'include_path_in_project', n.get_bool_value()),
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
        writer.write_bool_value("includePathInProject", self.include_path_in_project)
        writer.write_additional_data_value(self.additional_data)
    

