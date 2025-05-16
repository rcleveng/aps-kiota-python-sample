from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .manifest_resources_phase_ids import ManifestResources_phaseIds
    from .manifest_resources_phase_names import ManifestResources_phaseNames
    from .messages import Messages

@dataclass
class ManifestResources(AdditionalDataHolder, Parsable):
    """
    Represents a resource generated for a derivative.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The default viewpoint of a viewable 3D resource.
    camera: Optional[list[float]] = None
    # An optional array of objects, where each object (of type ``children``) represents another resource generated for this resource.
    children: Optional[list[ManifestResources]] = None
    # An ID that uniquely identifies the resource.
    guid: Optional[str] = None
    # - ``true``: There is a thumbnail for the resource.- ``false``: There is no thumbnail for the resource.
    has_thumbnail: Optional[str] = None
    # The messages property
    messages: Optional[list[Messages]] = None
    # MIME type of the content of the resource.
    mime: Optional[str] = None
    # The name of the resource.
    name: Optional[str] = None
    # The unique ID of the phase the resource file was generated from. This attribute is present only on Model Views (Viewables) generated from a Revit source design. This attribute can be a string (for Revit non-sheet 2D or 3D views) or an array of strings (for Revit sheet views).
    phase_ids: Optional[ManifestResources_phaseIds] = None
    # The name of the phase the resource file was generated from. This attribute is present only on Model Views (Viewables) generated from a Revit source design. This attribute can be a string (for Revit non-sheet 2D or 3D views) or an array of strings (for Revit sheet views).
    phase_names: Optional[ManifestResources_phaseNames] = None
    # Indicates the progress of the process generating this resource, as a percentage. Once complete, the value changes to ``complete``.
    progress: Optional[str] = None
    # An array of two integers where the first number represents the width of a thumbnail in pixels, and the second the height. Available only for thumbnail resources.
    resolution: Optional[list[int]] = None
    # File type of the resource.
    role: Optional[str] = None
    # Status of the task generating this resource; Possible values are:  ``pending``, ``inprogress``, ``success``, ``failed``, ``timeout``
    status: Optional[str] = None
    # Type of resource this JSON object represents.
    type: Optional[str] = None
    # The URN that you can use to access the resource.
    urn: Optional[str] = None
    # An ID assigned to a resource that can be displayed in a viewer.
    viewable_i_d: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManifestResources:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManifestResources
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManifestResources()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .manifest_resources_phase_ids import ManifestResources_phaseIds
        from .manifest_resources_phase_names import ManifestResources_phaseNames
        from .messages import Messages

        from .manifest_resources_phase_ids import ManifestResources_phaseIds
        from .manifest_resources_phase_names import ManifestResources_phaseNames
        from .messages import Messages

        fields: dict[str, Callable[[Any], None]] = {
            "camera": lambda n : setattr(self, 'camera', n.get_collection_of_primitive_values(float)),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(ManifestResources)),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "hasThumbnail": lambda n : setattr(self, 'has_thumbnail', n.get_str_value()),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(Messages)),
            "mime": lambda n : setattr(self, 'mime', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phaseIds": lambda n : setattr(self, 'phase_ids', n.get_object_value(ManifestResources_phaseIds)),
            "phaseNames": lambda n : setattr(self, 'phase_names', n.get_object_value(ManifestResources_phaseNames)),
            "progress": lambda n : setattr(self, 'progress', n.get_str_value()),
            "resolution": lambda n : setattr(self, 'resolution', n.get_collection_of_primitive_values(int)),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "urn": lambda n : setattr(self, 'urn', n.get_str_value()),
            "viewableID": lambda n : setattr(self, 'viewable_i_d', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("camera", self.camera)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("guid", self.guid)
        writer.write_str_value("hasThumbnail", self.has_thumbnail)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_str_value("mime", self.mime)
        writer.write_str_value("name", self.name)
        writer.write_object_value("phaseIds", self.phase_ids)
        writer.write_object_value("phaseNames", self.phase_names)
        writer.write_str_value("progress", self.progress)
        writer.write_collection_of_primitive_values("resolution", self.resolution)
        writer.write_str_value("role", self.role)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
        writer.write_str_value("urn", self.urn)
        writer.write_str_value("viewableID", self.viewable_i_d)
        writer.write_additional_data_value(self.additional_data)
    

