"""pnoise library"""
"""
Ported from the Processing project - http://processing.org
Copyright (c) 2021 Antoine Beyeler
Copyright (c) 2012-15 The Processing Foundation
Copyright (c) 2004-12 Ben Fry and Casey Reas
Copyright (c) 2001-04 Massachusetts Institute of Technology

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation, version 2.1.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with this library; if not, write to the
Free Software Foundation, Inc., 59 Temple Place, Suite 330,
Boston, MA  02111-1307  USA
"""

import math
from numbers import Number
from typing import Sequence, Union

import numpy as np

PERLIN_YWRAPB = 4
PERLIN_YWRAP = 1 << PERLIN_YWRAPB
PERLIN_ZWRAPB = 8
PERLIN_ZWRAP = 1 << PERLIN_ZWRAPB
PERLIN_SIZE = 4095


class Noise:
    def __init__(self):
        self._perlin = np.random.random(PERLIN_SIZE + 1)
        self.octaves: int = 4
        self.amp_falloff: float = 0.5

    def seed(self, seed: int) -> None:
        rng = np.random.default_rng(seed)
        self._perlin = rng.random(PERLIN_SIZE + 1)

    # noinspection DuplicatedCode
    def perlin(
        self,
        x: Union[Number, Sequence[Number]],
        y: Union[Number, Sequence[Number]],
        z: Union[Number, Sequence[Number]],
        grid_mode: bool = True,
    ) -> np.ndarray:
        """Compute perlin noise for a range of values.

        Each of the x, y, and z argument may be 1D sequence of float. Perlin noise will be
        computed for each combination of each of the input argument and returns them in a
        Numpy array of shape (len(x), len(y), len(z)). If any of the input are scalar, they are
        interpreted as a length-1 array.
        """

        single = isinstance(x, Number) and isinstance(y, Number) and isinstance(z, Number)

        if not grid_mode or single:
            grid = np.array([x, y, z], dtype=float)
        else:
            grid = np.array(np.meshgrid(x, y, z, indexing="ij", copy=False), dtype=float)

        np.abs(grid, out=grid)
        grid_i = grid.astype(int)
        grid = grid - grid_i  # faster than in place for small matrices

        r = np.zeros(shape=grid.shape[1:])
        ampl = 0.5

        for _ in range(self.octaves):
            of = (
                grid_i[0, ...]
                + (grid_i[1, ...] << PERLIN_YWRAPB)
                + (grid_i[2, ...] << PERLIN_ZWRAPB)
            )

            r_f = 0.5 * (1.0 - np.cos(grid * math.pi))

            n1 = self._perlin[of % PERLIN_SIZE]
            n1 += r_f[0, ...] * (self._perlin[(of + 1) % PERLIN_SIZE] - n1)
            n2 = self._perlin[(of + PERLIN_YWRAP) % PERLIN_SIZE]
            n2 += r_f[0, ...] * (self._perlin[(of + PERLIN_YWRAP + 1) % PERLIN_SIZE] - n2)
            n1 += r_f[1, ...] * (n2 - n1)

            of += PERLIN_ZWRAP
            n2 = self._perlin[of % PERLIN_SIZE]
            n2 += r_f[0, ...] * (self._perlin[(of + 1) % PERLIN_SIZE] - n2)
            n3 = self._perlin[(of + PERLIN_YWRAP) % PERLIN_SIZE]
            n3 += r_f[0, ...] * (self._perlin[(of + PERLIN_YWRAP + 1) % PERLIN_SIZE] - n3)
            n2 += r_f[1, ...] * (n3 - n2)

            n1 += r_f[2, ...] * (n2 - n1)

            r += n1 * ampl
            ampl *= self.amp_falloff

            grid_i <<= 1
            grid *= 2

            idx = grid >= 1.0
            grid_i[idx] += 1
            grid[idx] -= 1.0

        if single:
            return np.asscalar(r)
        elif not grid_mode:
            return r
        else:
            return r[
                0 if isinstance(x, Number) else slice(None),
                0 if isinstance(y, Number) else slice(None),
                0 if isinstance(z, Number) else slice(None),
            ]
