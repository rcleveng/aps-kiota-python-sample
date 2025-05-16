from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .manifest_derivative_properties import ManifestDerivative_properties
    from .manifest_resources import ManifestResources
    from .messages import Messages

@dataclass
class ManifestDerivative(AdditionalDataHolder, Parsable):
    """
    Represents a derivative generated for the source design.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects, where each object represents a resource generated for the derivative. For example, a Model View (Viewable) of the source design.
    children: Optional[list[ManifestResources]] = None
    # - ``true``: The derivative has a thumbnail.- ``false``: The derivative does not have a thumbnail.
    has_thumbnail: Optional[str] = None
    # The messages property
    messages: Optional[list[Messages]] = None
    # The name of the resource.
    name: Optional[str] = None
    # The file type/format of the derivative. Possible values are: ``dwg``, ``fbx``, ``ifc``, ``iges``, ``obj`` , ``step``, ``stl``, ``svf``, ``svf2``,  ``thumbnail``.
    output_type: Optional[str] = None
    # Indicates the progress of the process generating this derivative, as a percentage. Once complete, the value changes to ``complete``.
    progress: Optional[str] = None
    # A JSON object containing metadata extracted from the source design. This metadata provides valuable information about the model, such as its author, client name, project status, and other relevant details.**Note:** This metadata is currently returned for the following source design types:- RVT - Revit models- NWD - Navisworks models- DWG - AutoCAD models        
    properties: Optional[ManifestDerivative_properties] = None
    # Status of the task generating this derivative. Possible values are: ``pending``, ``inprogress``, ``success``, ``failed``, ``timeout``.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManifestDerivative:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManifestDerivative
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManifestDerivative()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .manifest_derivative_properties import ManifestDerivative_properties
        from .manifest_resources import ManifestResources
        from .messages import Messages

        from .manifest_derivative_properties import ManifestDerivative_properties
        from .manifest_resources import ManifestResources
        from .messages import Messages

        fields: dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(ManifestResources)),
            "hasThumbnail": lambda n : setattr(self, 'has_thumbnail', n.get_str_value()),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(Messages)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "outputType": lambda n : setattr(self, 'output_type', n.get_str_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(ManifestDerivative_properties)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("hasThumbnail", self.has_thumbnail)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_str_value("name", self.name)
        writer.write_str_value("outputType", self.output_type)
        writer.write_str_value("progress", self.progress)
        writer.write_object_value("properties", self.properties)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

