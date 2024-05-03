import pytest
import os
from gendiff.diff_builder import generate_diff


TEST_FILES_DIR = os.path.join('tests', 'fixtures')


@pytest.fixture
def json_plain_1():
    return os.path.join(TEST_FILES_DIR, 'file1.json')


@pytest.fixture
def json_plain_2():
    return os.path.join(TEST_FILES_DIR, 'file2.json')


@pytest.fixture
def yaml_plain_1():
    return os.path.join(TEST_FILES_DIR, 'file1.yaml')


@pytest.fixture
def yaml_plain_2():
    return os.path.join(TEST_FILES_DIR, 'file2.yaml')


@pytest.fixture
def json_nested_1():
    return os.path.join(TEST_FILES_DIR, 'file3.json')


@pytest.fixture
def json_nested_2():
    return os.path.join(TEST_FILES_DIR, 'file4.json')


@pytest.fixture
def yaml_nested_1():
    return os.path.join(TEST_FILES_DIR, 'file3.yaml')


@pytest.fixture
def yaml_nested_2():
    return os.path.join(TEST_FILES_DIR, 'file4.yaml')


@pytest.fixture
def expected_diff_plain():
    path = os.path.join(TEST_FILES_DIR, 'expected_plain.txt')
    with open(path) as file:
        expected = file.read()
    return expected


@pytest.fixture
def expected_diff_nested():
    path = os.path.join(TEST_FILES_DIR, 'expected_nested.txt')
    with open(path) as file:
        expected = file.read()
    return expected


def test_plain_json(json_plain_1, json_plain_2, expected_diff_plain):
    diff = generate_diff(json_plain_1, json_plain_2)
    assert diff == expected_diff_plain


def test_plain_yaml(yaml_plain_1, yaml_plain_2, expected_diff_plain):
    diff = generate_diff(yaml_plain_1, yaml_plain_2)
    assert diff == expected_diff_plain


def test_nested_json(json_nested_1, json_nested_2, expected_diff_nested):
    diff = generate_diff(json_nested_1, json_nested_2)
    assert diff == expected_diff_nested


def test_nested_yaml(yaml_nested_1, yaml_nested_2, expected_diff_nested):
    diff = generate_diff(yaml_nested_1, yaml_nested_2)
    assert diff == expected_diff_nested
