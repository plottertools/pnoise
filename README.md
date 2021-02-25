# *pnoise*

*pnoise* is a pure-Python, Numpy-based, vectorized port of Processing's `noise()` function. The `p` in *pnoise* stands for Processin, Perlin, Python, "port", and probably other things I haven't though of yet.

## Why?

I wrote this port before switching to [vnoise](https://github.com/plottertools/vnoise) and, although I'm no longer using it, I figured I would keep it around. 

## How does it compare to *vnoise*?

| | *pnoise* | *vnoise* |
| --- | --- | --- |
| Algorithm | "classic Perlin noise of 1983" | "Perlin improved
noise" |
| License | LGPL v2.1 | MIT |
| Scalar API | ✅ | ✅ |
| Vectorized API | ✅ | ✅ |
| 3D function | ✅ | ✅ |
| 2D function | ❌ (can be derived from 3D but slower) | ✅ |
| 1D function | ❌ (can be derived from 3D but slower) | ✅ |

See a performance comparison [here](https://github.com/plottertools/vnoise/tree/main/benchmarks).

## Installation

```
pip install git+https://github.com/plottertools/pnoise#egg=pnoise
```

## License

LGPL 2.1, see [LICENSE](LICENSE) file.
