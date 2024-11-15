import math
from Module.Equasions import calc_atoms, decay_constant, decay

def test_calc_atoms():
    # Test with known values
    result = calc_atoms(0.00001, 89.907)
    expected = (0.00001 / 89.907) * 6.02214076e23
    assert pytest.approx(result, rel=1e-6) == expected, f"Expected {expected}, got {result}"
    
    # Edge case: zero grams
    assert calc_atoms(0, 89.907) == 0, "Expected 0 atoms for 0 grams"

    # Edge case: zero isotope weight (should raise an error)
    with pytest.raises(ZeroDivisionError):
        calc_atoms(0.00001, 0)

def test_decay_constant():
    # Test with known half-life in years
    result = decay_constant(28.9, 'Yr')
    expected_conversion = 365 * 24 * 60 * 60  # Year to seconds
    expected_time_hl = 28.9 * expected_conversion
    expected = math.log(2) / expected_time_hl
    assert pytest.approx(result, rel=1e-6) == expected, f"Expected {expected}, got {result}"

    # Test with seconds (no conversion)
    result_sec = decay_constant(28.9, 'sec')
    expected_sec = math.log(2) / 28.9
    assert pytest.approx(result_sec, rel=1e-6) == expected_sec, f"Expected {expected_sec}, got {result_sec}"

    # Edge case: invalid units should raise a ValueError
    with pytest.raises(ValueError):
        decay_constant(28.9, 'unknown')

def test_decay():
    # Basic test for decay calculation with example values
    constant = decay_constant(28.9, 'Yr')
    atoms = calc_atoms(0.00001, 89.907)
    result = decay(constant, atoms)
    
    # Assuming the expected formula is provided for decay (e.g., atoms * constant or other)
    # Replace `expected_decay` with the correct formula for your function
    expected_decay = (atoms * constant) / 3.7e10 # Example if decay is atoms * constant
    assert pytest.approx(result, rel=1e-6) == expected_decay, f"Expected {expected_decay}, got {result}"

    # Edge case: zero atoms
    assert decay(constant, 0) == 0, "Expected 0 decay for 0 atoms"
