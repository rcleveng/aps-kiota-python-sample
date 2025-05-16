from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_relationships_links_links import Json_api_relationships_links_links
    from .json_api_relationships_links_refs import Json_api_relationships_links_refs
    from .version_data_relationships_derivatives import VersionData_relationships_derivatives
    from .version_data_relationships_download_formats import VersionData_relationships_downloadFormats
    from .version_data_relationships_item import VersionData_relationships_item
    from .version_data_relationships_storage import VersionData_relationships_storage
    from .version_data_relationships_thumbnails import VersionData_relationships_thumbnails

@dataclass
class VersionData_relationships(AdditionalDataHolder, Parsable):
    """
    Contains information on other resources related to this resource.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains information you can use to retrieve the derivatives of this version.
    derivatives: Optional[VersionData_relationships_derivatives] = None
    # Contains the endpoint you can use to find out what formats the version can be downloaded as.
    download_formats: Optional[VersionData_relationships_downloadFormats] = None
    # Contains information about the item this is a version of.
    item: Optional[VersionData_relationships_item] = None
    # Information on the link resources found in this resource.
    links: Optional[Json_api_relationships_links_links] = None
    # Information on other resources that have a custom relationship with this resource.
    refs: Optional[Json_api_relationships_links_refs] = None
    # Contains information about the storage location that contains the binary data of this version.
    storage: Optional[VersionData_relationships_storage] = None
    # Contains the information required to retrieve thumbnails of this version from the Model Derivative service. 
    thumbnails: Optional[VersionData_relationships_thumbnails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VersionData_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VersionData_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VersionData_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_relationships_links_links import Json_api_relationships_links_links
        from .json_api_relationships_links_refs import Json_api_relationships_links_refs
        from .version_data_relationships_derivatives import VersionData_relationships_derivatives
        from .version_data_relationships_download_formats import VersionData_relationships_downloadFormats
        from .version_data_relationships_item import VersionData_relationships_item
        from .version_data_relationships_storage import VersionData_relationships_storage
        from .version_data_relationships_thumbnails import VersionData_relationships_thumbnails

        from .json_api_relationships_links_links import Json_api_relationships_links_links
        from .json_api_relationships_links_refs import Json_api_relationships_links_refs
        from .version_data_relationships_derivatives import VersionData_relationships_derivatives
        from .version_data_relationships_download_formats import VersionData_relationships_downloadFormats
        from .version_data_relationships_item import VersionData_relationships_item
        from .version_data_relationships_storage import VersionData_relationships_storage
        from .version_data_relationships_thumbnails import VersionData_relationships_thumbnails

        fields: dict[str, Callable[[Any], None]] = {
            "derivatives": lambda n : setattr(self, 'derivatives', n.get_object_value(VersionData_relationships_derivatives)),
            "downloadFormats": lambda n : setattr(self, 'download_formats', n.get_object_value(VersionData_relationships_downloadFormats)),
            "item": lambda n : setattr(self, 'item', n.get_object_value(VersionData_relationships_item)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_relationships_links_links)),
            "refs": lambda n : setattr(self, 'refs', n.get_object_value(Json_api_relationships_links_refs)),
            "storage": lambda n : setattr(self, 'storage', n.get_object_value(VersionData_relationships_storage)),
            "thumbnails": lambda n : setattr(self, 'thumbnails', n.get_object_value(VersionData_relationships_thumbnails)),
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
        writer.write_object_value("derivatives", self.derivatives)
        writer.write_object_value("downloadFormats", self.download_formats)
        writer.write_object_value("item", self.item)
        writer.write_object_value("links", self.links)
        writer.write_object_value("refs", self.refs)
        writer.write_object_value("storage", self.storage)
        writer.write_object_value("thumbnails", self.thumbnails)
        writer.write_additional_data_value(self.additional_data)
    

