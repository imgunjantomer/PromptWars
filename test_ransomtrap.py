import os
import math
import unittest
import tempfile
from collections import Counter


def calculate_shannon_entropy(data: bytes) -> float:
    """Calculates Shannon entropy to detect encrypted high-entropy payloads."""
    if not data:
        return 0.0
    counts = Counter(data)
    length = len(data)
    return -sum((count / length) * math.log2(count / length) for count in counts.values())


def classify_threat_triage(canary_touched: bool, entropy_score: float, burst_rate: int) -> dict:
    """AI-assisted heuristic triage classifier for PS06 Cybersecurity Triage."""
    if canary_touched and entropy_score >= 7.0:
        return {"severity": "CRITICAL", "action": "TERMINATE_PROCESS", "confidence": 0.98}
    elif canary_touched or burst_rate > 15:
        return {"severity": "HIGH", "action": "ISOLATE_AND_ALERT", "confidence": 0.87}
    return {"severity": "LOW", "action": "MONITOR", "confidence": 0.95}


class TestRansomTrapCore(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.canary_path = os.path.join(self.test_dir.name, "!0_passwords.txt")
        with open(self.canary_path, "w", encoding="utf-8") as f:
            f.write("DECOY_CANARY_TOKEN_DO_NOT_MODIFY")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_canary_file_deployment(self):
        self.assertTrue(os.path.exists(self.canary_path))

    def test_entropy_detection_encrypted_vs_plain(self):
        plain_data = b"Normal user document text with low randomness." * 10
        encrypted_data = os.urandom(512)
        self.assertLess(calculate_shannon_entropy(plain_data), 5.0)
        self.assertGreater(calculate_shannon_entropy(encrypted_data), 7.2)

    def test_triage_critical_classification(self):
        result = classify_threat_triage(canary_touched=True, entropy_score=7.8, burst_rate=25)
        self.assertEqual(result["severity"], "CRITICAL")
        self.assertEqual(result["action"], "TERMINATE_PROCESS")

    def test_triage_low_classification(self):
        result = classify_threat_triage(canary_touched=False, entropy_score=3.2, burst_rate=2)
        self.assertEqual(result["severity"], "LOW")


if __name__ == "__main__":
    unittest.main()