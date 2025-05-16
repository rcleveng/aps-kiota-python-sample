from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_data_attributes import Job_data_attributes
    from .json_api_links_self import Json_api_links_self
    from .type_job import Type_job

@dataclass
class Job_data(AdditionalDataHolder, Parsable):
    """
    Contains information about the download creation job.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains the properties that indicate the current status of the job.
    attributes: Optional[Job_data_attributes] = None
    # The Job ID of the job creating the download.
    id: Optional[str] = None
    # An object containing the URI of the endpoint to access this resource.
    links: Optional[Json_api_links_self] = None
    # The type of this resource. Possible values are ``jobs``.
    type: Optional[Type_job] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Job_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Job_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Job_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_data_attributes import Job_data_attributes
        from .json_api_links_self import Json_api_links_self
        from .type_job import Type_job

        from .job_data_attributes import Job_data_attributes
        from .json_api_links_self import Json_api_links_self
        from .type_job import Type_job

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(Job_data_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_links_self)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_job)),
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
        writer.write_object_value("attributes", self.attributes)
        writer.write_str_value("id", self.id)
        writer.write_object_value("links", self.links)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

