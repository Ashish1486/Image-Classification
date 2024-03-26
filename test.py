# test_config.py
# Define test suites
from __future__ import annotations
TEST_SUITES = {
    'unit_tests': [
        'tests.unit.test_module1',
        'tests.unit.test_module2',
    ],
    'integration_tests': [
        'tests.integration.test_module3',
        'tests.integration.test_module4',
    ],
    'end_to_end_tests': [
        'tests.end_to_end.test_module5',
        'tests.end_to_end.test_module6',
    ],
}

# Define test case paths
TEST_CASE_PATHS = [
    'tests/unit',
    'tests/integration',
    'tests/end_to_end',
]

# Define test dependencies
TEST_DEPENDENCIES = {
    'unit_tests': [
        'mock',
        'pytest',
    ],
    'integration_tests': [
        'pytest',
        'requests',
    ],
    'end_to_end_tests': [
        'pytest',
        'selenium',
    ],
}

# Define test configuration options
TEST_CONFIG_OPTIONS = {
    'verbose': True,
    'log_file': 'test_logs.txt',
    'timeout': 300,  # in seconds
}
