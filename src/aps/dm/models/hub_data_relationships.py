from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hub_data_relationships_pim_collection import HubData_relationships_pimCollection
    from .hub_data_relationships_projects import HubData_relationships_projects

@dataclass
class HubData_relationships(AdditionalDataHolder, Parsable):
    """
    Contains links to resources that are directly related to this hub.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information on the ``id`` and ``type`` properties of a resource. This is available only for Fusion Team hubs and A360 Personal hubs.
    pim_collection: Optional[HubData_relationships_pimCollection] = None
    # Contains the endpoint you can use to list the projects in this hub.
    projects: Optional[HubData_relationships_projects] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HubData_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HubData_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HubData_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hub_data_relationships_pim_collection import HubData_relationships_pimCollection
        from .hub_data_relationships_projects import HubData_relationships_projects

        from .hub_data_relationships_pim_collection import HubData_relationships_pimCollection
        from .hub_data_relationships_projects import HubData_relationships_projects

        fields: dict[str, Callable[[Any], None]] = {
            "pimCollection": lambda n : setattr(self, 'pim_collection', n.get_object_value(HubData_relationships_pimCollection)),
            "projects": lambda n : setattr(self, 'projects', n.get_object_value(HubData_relationships_projects)),
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
        writer.write_object_value("pimCollection", self.pim_collection)
        writer.write_object_value("projects", self.projects)
        writer.write_additional_data_value(self.additional_data)
    

