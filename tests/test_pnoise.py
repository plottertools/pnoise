import pytest
from pnoise import Noise


@pytest.fixture(scope="module")
def noise():
    return Noise()


def test_noise3_dimensions(noise):
    # scalar
    assert isinstance(noise.perlin(1.5, 1.0, 1.5, grid_mode=True), float)
    assert isinstance(noise.perlin(1.5, 1.0, 1.5, grid_mode=False), float)

    # grid mode on
    assert noise.perlin([0, 1], [2, 3, 4], 4).shape == (2, 3)
    assert noise.perlin([0, 1], [2, 3, 4], [5, 6, 7, 8]).shape == (2, 3, 4)
    assert noise.perlin([1], [2, 3, 4], [5, 6, 7, 8]).shape == (1, 3, 4)
    assert noise.perlin([0, 1], 4, [5, 6, 7, 8]).shape == (2, 4)
    assert noise.perlin(4, 4, [5, 6, 7, 8]).shape == (4,)
    assert noise.perlin(4, [0, 1], [5, 6, 7, 8]).shape == (2, 4)

    # grid mode off
    assert noise.perlin([0, 1, 2], [3, 4, 5], [5, 6, 7], grid_mode=False).shape == (3,)
    assert noise.perlin([0], [3], [5], grid_mode=False).shape == (1,)

    with pytest.raises(ValueError):
        noise.perlin([0, 1, 2], [3, 4, 5, 6], [5, 6, 7], grid_mode=False)
