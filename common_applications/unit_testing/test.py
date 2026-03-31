# importing the packages
import pytest

# ===========================================================================


def unique_elements(lst):
    """Return a list of unique elements, preserving order."""
    return list(dict.fromkeys(lst))


def remove_first_element(lst):
    """Remove the first element of a list. Raises ValueError if empty."""
    if not lst:
        raise ValueError("List is empty")
    return lst[1:]


# ============================================================================
# test fixtures:


@pytest.fixture
def sample_list():
    """Fixture providing a sample list for tests."""
    print("\n[Fixture] Setting up sample list")
    data = [1, 2, 2, 3, 4, 4]
    yield data  # passed to test functions
    print("\n[Fixture] Teardown: sample list cleaned up")


# Fixture with multiple input variations
@pytest.fixture(params=[[1, 2, 2, 3], [5, 5, 5], []])
def sample_list_variants(request):
    """Fixture yielding different sample lists for parameterized tests."""
    return request.param


# ============================================================================
# test functions:


def test_unique_elements(sample_list):
    """Test unique_elements function on a standard sample list."""
    result = unique_elements(sample_list)
    assert result == [1, 2, 3, 4]


def test_sum_of_elements(sample_list):
    """Test summing elements of the sample list."""
    total = sum(sample_list)
    assert total == 16

# creating three different test parameters as input_list and expected:
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 2, 3], [1, 2, 3]),
        ([5, 5, 5], [5]),
        ([], []),
    ],
)
def test_unique_elements_param(input_list, expected):
    """Test unique_elements on multiple input lists using parameterization."""
    assert unique_elements(input_list) == expected


def test_unique_elements_empty():
    """Edge case: empty list should return empty list."""
    assert unique_elements([]) == []


def test_unique_elements_single_item():
    """Edge case: single-item list should return same single item."""
    assert unique_elements([42]) == [42]


def test_remove_first_element_raises():
    """Test that remove_first_element raises ValueError on empty list."""
    with pytest.raises(ValueError):
        remove_first_element([])


def test_unique_elements_variants(sample_list_variants):
    """Test unique_elements on multiple sample lists from fixture."""
    result = unique_elements(sample_list_variants)
    assert len(result) == len(set(sample_list_variants))