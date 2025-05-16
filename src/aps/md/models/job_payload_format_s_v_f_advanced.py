from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_format_s_v_f_advanced_d_g_n import JobPayloadFormatSVFAdvancedDGN
    from .job_payload_format_s_v_f_advanced_d_w_g import JobPayloadFormatSVFAdvancedDWG
    from .job_payload_format_s_v_f_advanced_i_f_c import JobPayloadFormatSVFAdvancedIFC
    from .job_payload_format_s_v_f_advanced_n_w_d import JobPayloadFormatSVFAdvancedNWD
    from .job_payload_format_s_v_f_advanced_r_v_t import JobPayloadFormatSVFAdvancedRVT
    from .job_payload_format_s_v_f_advanced_v_u_e import JobPayloadFormatSVFAdvancedVUE

@dataclass
class JobPayloadFormatSVF_advanced(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes JobPayloadFormatSVFAdvancedDGN, JobPayloadFormatSVFAdvancedDWG, JobPayloadFormatSVFAdvancedIFC, JobPayloadFormatSVFAdvancedNWD, JobPayloadFormatSVFAdvancedRVT, JobPayloadFormatSVFAdvancedVUE
    """
    # Composed type representation for type JobPayloadFormatSVFAdvancedDGN
    job_payload_format_s_v_f_advanced_d_g_n: Optional[JobPayloadFormatSVFAdvancedDGN] = None
    # Composed type representation for type JobPayloadFormatSVFAdvancedDWG
    job_payload_format_s_v_f_advanced_d_w_g: Optional[JobPayloadFormatSVFAdvancedDWG] = None
    # Composed type representation for type JobPayloadFormatSVFAdvancedIFC
    job_payload_format_s_v_f_advanced_i_f_c: Optional[JobPayloadFormatSVFAdvancedIFC] = None
    # Composed type representation for type JobPayloadFormatSVFAdvancedNWD
    job_payload_format_s_v_f_advanced_n_w_d: Optional[JobPayloadFormatSVFAdvancedNWD] = None
    # Composed type representation for type JobPayloadFormatSVFAdvancedRVT
    job_payload_format_s_v_f_advanced_r_v_t: Optional[JobPayloadFormatSVFAdvancedRVT] = None
    # Composed type representation for type JobPayloadFormatSVFAdvancedVUE
    job_payload_format_s_v_f_advanced_v_u_e: Optional[JobPayloadFormatSVFAdvancedVUE] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVF_advanced:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVF_advanced
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = JobPayloadFormatSVF_advanced()
        if mapping_value and mapping_value.casefold() == "JobPayloadFormatSVFAdvancedDGN".casefold():
            from .job_payload_format_s_v_f_advanced_d_g_n import JobPayloadFormatSVFAdvancedDGN

            result.job_payload_format_s_v_f_advanced_d_g_n = JobPayloadFormatSVFAdvancedDGN()
        elif mapping_value and mapping_value.casefold() == "JobPayloadFormatSVFAdvancedDWG".casefold():
            from .job_payload_format_s_v_f_advanced_d_w_g import JobPayloadFormatSVFAdvancedDWG

            result.job_payload_format_s_v_f_advanced_d_w_g = JobPayloadFormatSVFAdvancedDWG()
        elif mapping_value and mapping_value.casefold() == "JobPayloadFormatSVFAdvancedIFC".casefold():
            from .job_payload_format_s_v_f_advanced_i_f_c import JobPayloadFormatSVFAdvancedIFC

            result.job_payload_format_s_v_f_advanced_i_f_c = JobPayloadFormatSVFAdvancedIFC()
        elif mapping_value and mapping_value.casefold() == "JobPayloadFormatSVFAdvancedNWD".casefold():
            from .job_payload_format_s_v_f_advanced_n_w_d import JobPayloadFormatSVFAdvancedNWD

            result.job_payload_format_s_v_f_advanced_n_w_d = JobPayloadFormatSVFAdvancedNWD()
        elif mapping_value and mapping_value.casefold() == "JobPayloadFormatSVFAdvancedRVT".casefold():
            from .job_payload_format_s_v_f_advanced_r_v_t import JobPayloadFormatSVFAdvancedRVT

            result.job_payload_format_s_v_f_advanced_r_v_t = JobPayloadFormatSVFAdvancedRVT()
        elif mapping_value and mapping_value.casefold() == "JobPayloadFormatSVFAdvancedVUE".casefold():
            from .job_payload_format_s_v_f_advanced_v_u_e import JobPayloadFormatSVFAdvancedVUE

            result.job_payload_format_s_v_f_advanced_v_u_e = JobPayloadFormatSVFAdvancedVUE()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_format_s_v_f_advanced_d_g_n import JobPayloadFormatSVFAdvancedDGN
        from .job_payload_format_s_v_f_advanced_d_w_g import JobPayloadFormatSVFAdvancedDWG
        from .job_payload_format_s_v_f_advanced_i_f_c import JobPayloadFormatSVFAdvancedIFC
        from .job_payload_format_s_v_f_advanced_n_w_d import JobPayloadFormatSVFAdvancedNWD
        from .job_payload_format_s_v_f_advanced_r_v_t import JobPayloadFormatSVFAdvancedRVT
        from .job_payload_format_s_v_f_advanced_v_u_e import JobPayloadFormatSVFAdvancedVUE

        if self.job_payload_format_s_v_f_advanced_d_g_n:
            return self.job_payload_format_s_v_f_advanced_d_g_n.get_field_deserializers()
        if self.job_payload_format_s_v_f_advanced_d_w_g:
            return self.job_payload_format_s_v_f_advanced_d_w_g.get_field_deserializers()
        if self.job_payload_format_s_v_f_advanced_i_f_c:
            return self.job_payload_format_s_v_f_advanced_i_f_c.get_field_deserializers()
        if self.job_payload_format_s_v_f_advanced_n_w_d:
            return self.job_payload_format_s_v_f_advanced_n_w_d.get_field_deserializers()
        if self.job_payload_format_s_v_f_advanced_r_v_t:
            return self.job_payload_format_s_v_f_advanced_r_v_t.get_field_deserializers()
        if self.job_payload_format_s_v_f_advanced_v_u_e:
            return self.job_payload_format_s_v_f_advanced_v_u_e.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.job_payload_format_s_v_f_advanced_d_g_n:
            writer.write_object_value(None, self.job_payload_format_s_v_f_advanced_d_g_n)
        elif self.job_payload_format_s_v_f_advanced_d_w_g:
            writer.write_object_value(None, self.job_payload_format_s_v_f_advanced_d_w_g)
        elif self.job_payload_format_s_v_f_advanced_i_f_c:
            writer.write_object_value(None, self.job_payload_format_s_v_f_advanced_i_f_c)
        elif self.job_payload_format_s_v_f_advanced_n_w_d:
            writer.write_object_value(None, self.job_payload_format_s_v_f_advanced_n_w_d)
        elif self.job_payload_format_s_v_f_advanced_r_v_t:
            writer.write_object_value(None, self.job_payload_format_s_v_f_advanced_r_v_t)
        elif self.job_payload_format_s_v_f_advanced_v_u_e:
            writer.write_object_value(None, self.job_payload_format_s_v_f_advanced_v_u_e)
    

