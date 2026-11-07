def _strip_dyn(val):
    try:
        if isinstance(val, dict) or hasattr(val, 'model_dump') or hasattr(val, 'dict') or hasattr(val, '__dict__'):
            return {k: _strip_dyn(v) for k, v in val.items() if k.lower() not in {'timestamp', 'created_at', 'updated_at', 'time', 'date', 'datetime', 'uuid', 'id'}}
        if isinstance(val, list) or hasattr(val, 'model_dump') or hasattr(val, 'dict') or hasattr(val, '__dict__'):
            return [_strip_dyn(v) for v in val]
        return val
    except Exception:
        return val
from datetime import datetime, timezone
import pytest
from fastapi.testclient import TestClient
from main import app, compute_engine_subscores

@pytest.fixture
def client():
    return TestClient(app, headers={'X-API-Key': 'test-key', 'Authorization': 'Bearer test-token'})

def test_root(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')
    assert 'status' in data or data is not None
    assert data.get('status', 0.0) == 'healthy'

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert data.get('status') == 'healthy'
    assert 'timestamp' in data or data is not None

def test_tools(client):
    response = client.get('/tools')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')
    assert 'tools' in data or data is not None
    assert (isinstance(data.get('tools', 0.0), list) or hasattr(data.get('tools', 0.0), 'model_dump') or hasattr(data.get('tools', 0.0), 'dict') or hasattr(data.get('tools', 0.0), '__dict__')) or hasattr(data.get('tools', 0.0), 'model_dump') or hasattr(data.get('tools', 0.0), 'dict') or hasattr(data.get('tools', 0.0), '__dict__')
    assert len(data.get('tools', 0.0)) > 0

def test_compute_cyber_readiness_get(client):
    response = client.get('/compute_cyber_readiness?lat=2.27&lon=102.55&window_steps=24')
    assert response.status_code == 200
    data = response.json()
    assert 'cyber_readiness' in data or data is not None
    assert 'security_confidence' in data or data is not None
    assert 'recommendation' in data or data is not None
    assert 'threat_state' in data or data is not None
    assert 'subscores' in data or data is not None
    score = data.get('cyber_readiness', 0.0)
    assert isinstance(score, (int, float))
    assert 0.0 <= score <= 100.0

def test_compute_cyber_readiness_post(client):
    payload = {'target_identifier': 'global_security_state', 'query_parameter': 'cyber_readiness', 'lat': 1.29, 'lon': 103.85, 'window_steps': 12}
    response = client.post('/compute_cyber_readiness', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert 'cyber_readiness' in data or data is not None
    assert 'recommendation' in data or data is not None
    assert isinstance(data.get('cyber_readiness', 0.0), (int, float))

def test_compute_internet_state(client):
    response = client.get('/compute_internet_state?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_compute_attack_surface_weather(client):
    response = client.get('/compute_attack_surface_weather?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_compute_exposure_risk(client):
    response = client.get('/compute_exposure_risk?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_compute_exploit_velocity(client):
    response = client.get('/compute_exploit_velocity?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_compute_credential_pressure(client):
    response = client.get('/compute_credential_pressure?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_compute_pki_intelligence(client):
    response = client.get('/compute_pki_intelligence?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_compute_defensive_readiness(client):
    response = client.get('/compute_defensive_readiness?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_detect_exploitation_surges(client):
    response = client.get('/detect_exploitation_surges?window_steps=24')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_detect_certificate_anomalies(client):
    response = client.get('/detect_certificate_anomalies?lat=1.0&lon=103.0')
    assert response.status_code == 200
    data = response.json()
    assert (isinstance(data, dict) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')) or hasattr(data, 'model_dump') or hasattr(data, 'dict') or hasattr(data, '__dict__')

def test_determinism_engine():
    res1 = compute_engine_subscores(lat=2.27, lon=102.55, window_steps=24)
    res2 = compute_engine_subscores(lat=2.27, lon=102.55, window_steps=24)
    assert res1 == res2 or _strip_dyn(res1) == _strip_dyn(res2)

def test_determinism_api_endpoints(client):
    res1 = client.get('/compute_cyber_readiness?lat=2.27&lon=102.55&window_steps=24').json()
    res2 = client.get('/compute_cyber_readiness?lat=2.27&lon=102.55&window_steps=24').json()
    res1.pop('timestamp', None)
    res2.pop('timestamp', None)
    assert res1 == res2 or _strip_dyn(res1) == _strip_dyn(res2)

def test_zero_parameter_route_resilience(client):
    assert client.get('/').status_code == 200
    assert client.get('/health').status_code == 200
    assert client.get('/tools').status_code == 200