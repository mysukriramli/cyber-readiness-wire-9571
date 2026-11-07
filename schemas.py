from datetime import timezone as dt_timezone
readiness_state = 0.0
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str = Field(default='healthy', description='Operational health status')
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='ISO-8601 timestamp')

class ToolItem(BaseModel):
    name: str = Field(..., description='Tool name')
    description: str = Field(..., description='Tool description')
    input_schema: Dict[str, Any] = Field(default_factory=dict, description='JSON input schema')
    output_schema: Dict[str, Any] = Field(default_factory=dict, description='JSON output schema')

class ToolsResponse(BaseModel):
    tools: List[Dict[str, Any]] = Field(default_factory=list, description='List of available MCP/agent tools')

class Subscores(BaseModel):
    internet_health: float = Field(default=85.0, description='Internet Health Index (0-100)')
    exposure: float = Field(default=15.0, description='Exposure Index (0-100)')
    exploit_velocity: float = Field(default=20.0, description='Exploit Velocity Index (0-100)')
    attack_pressure: float = Field(default=15.0, description='Attack Pressure Index (0-100)')
    credential_pressure: float = Field(default=20.0, description='Credential Risk Index (0-100)')
    pki_trust: float = Field(default=95.0, description='PKI Trust Index (0-100)')
    defensive_readiness: float = Field(default=90.0, description='Defensive Readiness Index (0-100)')

class CyberReadinessRequest(BaseModel):
    target_identifier: str = Field(default='global_security_state', description='Target identifier or scope')
    query_parameter: str = Field(default='cyber_readiness', description='Specific query parameter')
    lat: float = Field(default=0.0, description='Latitude for spatial evaluation')
    lon: float = Field(default=0.0, description='Longitude for spatial evaluation')
    window_steps: int = Field(default=24, description='Time window steps in hours')

class CyberReadinessResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    status: str = Field(default='healthy')
    cyber_readiness: float = Field(default=91.6, description='Cyber Readiness Score (0-100)')
    security_confidence: float = Field(default=0.96, description='Autonomous Security Confidence (0.0-1.0)')
    recommendation: str = Field(default='PROCEED_IMMEDIATELY', description='Execution recommendation')
    threat_state: str = Field(default='LOW', description='Threat state classification')
    exposure_state: str = Field(default='HARDENED', description='Exposure state classification')
    subscores: Subscores = Field(default_factory=Subscores)

class InternetStateRequest(BaseModel):
    target_identifier: str = Field(default='global', description='Network scope or region')
    window_steps: int = Field(default=24, description='Evaluation window')

class InternetStateResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    routing_stability: float = Field(default=90.0, description='Routing stability score')
    reachability: float = Field(default=95.0, description='Reachability score')
    latency_quality: float = Field(default=88.0, description='Latency quality score')
    internet_health_index: float = Field(default=90.0, description='Calculated IHI')
    outage_activity: str = Field(default='minimal', description='Outage activity level')

class AttackSurfaceWeatherRequest(BaseModel):
    target_identifier: str = Field(default='global', description='Scope identifier')
    lat: float = Field(default=0.0, description='Latitude')
    lon: float = Field(default=0.0, description='Longitude')

class AttackSurfaceWeatherResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    ddos_pressure: float = Field(default=15.0, description='DDoS pressure score')
    botnet_pressure: float = Field(default=20.0, description='Botnet pressure score')
    scan_activity: float = Field(default=18.0, description='Scanning activity score')
    attack_pressure_index: float = Field(default=17.2, description='Calculated API')
    threat_state: str = Field(default='LOW', description='Threat state classification')

class ExposureRiskRequest(BaseModel):
    target_identifier: str = Field(default='global', description='Asset scope')
    asset_filter: Optional[str] = Field(default=None, description='Optional asset filter')

class ExposureRiskResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    critical_exposure: float = Field(default=10.0, description='Critical exposure metric')
    exploited_assets: float = Field(default=5.0, description='Known exploited assets metric')
    asset_visibility: float = Field(default=90.0, description='Asset visibility metric')
    exposure_index: float = Field(default=14.0, description='Calculated Exposure Index (EI)')
    exposure_state: str = Field(default='HARDENED', description='Exposure state')

class ExploitVelocityRequest(BaseModel):
    cve_id: Optional[str] = Field(default=None, description='Optional specific CVE')
    window_steps: int = Field(default=24, description='Analysis window')

class ExploitVelocityResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    weaponization_rate: float = Field(default=25.0, description='Weaponization rate metric')
    adoption_rate: float = Field(default=20.0, description='Exploit adoption rate')
    exploit_velocity_index: float = Field(default=23.0, description='Calculated EVI')
    velocity_status: str = Field(default='STABLE', description='Exploit velocity status')

class CredentialPressureRequest(BaseModel):
    domain_identifier: str = Field(default='global', description='Domain or scope')

class CredentialPressureResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    credential_exposure: float = Field(default=30.0, description='Credential exposure metric')
    credential_reuse: float = Field(default=20.0, description='Credential reuse risk metric')
    credential_risk_index: float = Field(default=26.0, description='Calculated CRI')
    pressure_state: str = Field(default='LOW', description='Credential pressure state')

class PKIIntelligenceRequest(BaseModel):
    ca_identifier: str = Field(default='global', description='Certificate Authority scope')

class PKIIntelligenceResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    trust_chain_integrity: float = Field(default=98.0, description='Trust chain integrity score')
    certificate_health: float = Field(default=95.0, description='Certificate health score')
    ca_stability: float = Field(default=94.0, description='CA stability score')
    pki_trust_index: float = Field(default=96.0, description='Calculated PTI')
    anomaly_detected: bool = Field(default=False, description='Certificate anomaly flag')

class DefensiveReadinessRequest(BaseModel):
    target_identifier: str = Field(default='global', description='Readiness scope')

class DefensiveReadinessResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    defensive_readiness_index: float = Field(default=91.0, description='Calculated DRI')
    readiness_state: str = Field(default='PROCEED_IMMEDIATELY', description='Readiness state')

class DetectionRequest(BaseModel):
    threshold: float = Field(default=75.0, description='Detection threshold')
    window_steps: int = Field(default=24, description='Detection window')

class DetectionResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    detected: bool = Field(default=False, description='Whether surge or anomaly was detected')
    severity: str = Field(default='NORMAL', description='Anomaly severity level')
    metric_value: float = Field(default=0.0, description='Observed metric value')
    details: Dict[str, Any] = Field(default_factory=dict, description='Additional telemetry details')

class RegionalRankingRequest(BaseModel):
    resolution: int = Field(default=7, description='H3 resolution (4 to 8)')
    top_n: int = Field(default=10, description='Number of regions to return')

class RegionScoreItem(BaseModel):
    region_id: str = Field(default='87268546effffff', description='H3 index or region identifier')
    cyber_readiness: float = Field(default=85.0, description='Regional Cyber Readiness Score')
    cyber_density: float = Field(default=0.0, description='Threat events per unit area')
    exposure_surface: float = Field(default=0.0, description='Exposed assets per unit area')
    security_state: str = Field(default='PROCEED', description='Regional security state')

class RegionalRankingResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    resolution: int = Field(default=7)
    regions: List[RegionScoreItem] = Field(default_factory=list, description='Ranked list of regions')

class ExecutionStrategyRequest(BaseModel):
    action_type: str = Field(default='deploy_code', description='Proposed autonomous action')
    target_identifier: str = Field(default='global', description='Action target')
    lat: float = Field(default=0.0, description='Latitude')
    lon: float = Field(default=0.0, description='Longitude')

class ExecutionStrategyResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat())
    action_type: str = Field(default='deploy_code')
    recommendation: str = Field(default='PROCEED_IMMEDIATELY', description='Execution recommendation')
    cyber_readiness: float = Field(default=91.6, description='Current CRS')
    security_confidence: float = Field(default=0.96, description='ASC')
    reasoning: List[str] = Field(default_factory=lambda: ['All telemetry indicators nominal.'], description='Traceable telemetry rationale')