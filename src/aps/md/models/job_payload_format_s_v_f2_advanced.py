from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_format_s_v_f2_advanced_d_g_n import JobPayloadFormatSVF2AdvancedDGN
    from .job_payload_format_s_v_f2_advanced_d_w_g import JobPayloadFormatSVF2AdvancedDWG
    from .job_payload_format_s_v_f2_advanced_i_f_c import JobPayloadFormatSVF2AdvancedIFC
    from .job_payload_format_s_v_f2_advanced_n_w_d import JobPayloadFormatSVF2AdvancedNWD
    from .job_payload_format_s_v_f2_advanced_r_v_t import JobPayloadFormatSVF2AdvancedRVT
    from .job_payload_format_s_v_f2_advanced_v_u_e import JobPayloadFormatSVF2AdvancedVUE

@dataclass
class JobPayloadFormatSVF2_advanced(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes JobPayloadFormatSVF2AdvancedDGN, JobPayloadFormatSVF2AdvancedDWG, JobPayloadFormatSVF2AdvancedIFC, JobPayloadFormatSVF2AdvancedNWD, JobPayloadFormatSVF2AdvancedRVT, JobPayloadFormatSVF2AdvancedVUE
    """
    # Composed type representation for type JobPayloadFormatSVF2AdvancedDGN
    job_payload_format_s_v_f2_advanced_d_g_n: Optional[JobPayloadFormatSVF2AdvancedDGN] = None
    # Composed type representation for type JobPayloadFormatSVF2AdvancedDWG
    job_payload_format_s_v_f2_advanced_d_w_g: Optional[JobPayloadFormatSVF2AdvancedDWG] = None
    # Composed type representation for type JobPayloadFormatSVF2AdvancedIFC
    job_payload_format_s_v_f2_advanced_i_f_c: Optional[JobPayloadFormatSVF2AdvancedIFC] = None
    # Composed type representation for type JobPayloadFormatSVF2AdvancedNWD
    job_payload_format_s_v_f2_advanced_n_w_d: Optional[JobPayloadFormatSVF2AdvancedNWD] = None
    # Composed type representation for type JobPayloadFormatSVF2AdvancedRVT
    job_payload_format_s_v_f2_advanced_r_v_t: Optional[JobPayloadFormatSVF2AdvancedRVT] = None
    # Composed type representation for type JobPayloadFormatSVF2AdvancedVUE
    job_payload_format_s_v_f2_advanced_v_u_e: Optional[JobPayloadFormatSVF2AdvancedVUE] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatSVF2_advanced:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatSVF2_advanced
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = JobPayloadFormatSVF2_advanced()
        from .job_payload_format_s_v_f2_advanced_d_g_n import JobPayloadFormatSVF2AdvancedDGN

        result.job_payload_format_s_v_f2_advanced_d_g_n = JobPayloadFormatSVF2AdvancedDGN()
        from .job_payload_format_s_v_f2_advanced_d_w_g import JobPayloadFormatSVF2AdvancedDWG

        result.job_payload_format_s_v_f2_advanced_d_w_g = JobPayloadFormatSVF2AdvancedDWG()
        from .job_payload_format_s_v_f2_advanced_i_f_c import JobPayloadFormatSVF2AdvancedIFC

        result.job_payload_format_s_v_f2_advanced_i_f_c = JobPayloadFormatSVF2AdvancedIFC()
        from .job_payload_format_s_v_f2_advanced_n_w_d import JobPayloadFormatSVF2AdvancedNWD

        result.job_payload_format_s_v_f2_advanced_n_w_d = JobPayloadFormatSVF2AdvancedNWD()
        from .job_payload_format_s_v_f2_advanced_r_v_t import JobPayloadFormatSVF2AdvancedRVT

        result.job_payload_format_s_v_f2_advanced_r_v_t = JobPayloadFormatSVF2AdvancedRVT()
        from .job_payload_format_s_v_f2_advanced_v_u_e import JobPayloadFormatSVF2AdvancedVUE

        result.job_payload_format_s_v_f2_advanced_v_u_e = JobPayloadFormatSVF2AdvancedVUE()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_format_s_v_f2_advanced_d_g_n import JobPayloadFormatSVF2AdvancedDGN
        from .job_payload_format_s_v_f2_advanced_d_w_g import JobPayloadFormatSVF2AdvancedDWG
        from .job_payload_format_s_v_f2_advanced_i_f_c import JobPayloadFormatSVF2AdvancedIFC
        from .job_payload_format_s_v_f2_advanced_n_w_d import JobPayloadFormatSVF2AdvancedNWD
        from .job_payload_format_s_v_f2_advanced_r_v_t import JobPayloadFormatSVF2AdvancedRVT
        from .job_payload_format_s_v_f2_advanced_v_u_e import JobPayloadFormatSVF2AdvancedVUE

        if self.job_payload_format_s_v_f2_advanced_d_g_n or self.job_payload_format_s_v_f2_advanced_d_w_g or self.job_payload_format_s_v_f2_advanced_i_f_c or self.job_payload_format_s_v_f2_advanced_n_w_d or self.job_payload_format_s_v_f2_advanced_r_v_t or self.job_payload_format_s_v_f2_advanced_v_u_e:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.job_payload_format_s_v_f2_advanced_d_g_n, self.job_payload_format_s_v_f2_advanced_d_w_g, self.job_payload_format_s_v_f2_advanced_i_f_c, self.job_payload_format_s_v_f2_advanced_n_w_d, self.job_payload_format_s_v_f2_advanced_r_v_t, self.job_payload_format_s_v_f2_advanced_v_u_e)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value(None, self.job_payload_format_s_v_f2_advanced_d_g_n, self.job_payload_format_s_v_f2_advanced_d_w_g, self.job_payload_format_s_v_f2_advanced_i_f_c, self.job_payload_format_s_v_f2_advanced_n_w_d, self.job_payload_format_s_v_f2_advanced_r_v_t, self.job_payload_format_s_v_f2_advanced_v_u_e)
    

