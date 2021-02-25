# *pnoise*

*pnoise* is a pure-Python, Numpy-based, vectorized port of Processing's `noise()` function. 

## Why?

I wrote this port before switching to [vnoise](https://github.com/plottertools/vnoise) and although I'm no longer using it I figured I would keep it around.

## How does it compare to *vnoise*?

| | *pnoise* | *vnoise* |
| --- | --- | --- |
| Algorithm | "classic Perlin noise of 1983" | "Perlin improved
noise" |
| Scalar API | ✅ | ✅ |
| Vectorized API | ✅ | ✅ |
| 3D function | ✅ | ✅ |
| 2D function | ❌ (can be derived from 3D but slower) | ✅ |
| 1D function | ❌ (can be derived from 3D but slower) | ✅ |
| Scalar performance 3D (1 octave) | - | ~2x faster |
| Scalar performance 3D (4 octave) | ~2x faster | - |
| Vectorized performance 3D (1 octave) | - | ~2.5x faster |
| Vectorized performance 3D (4 octave) | ~2x faster | - |
| Vectorized performance 2D (1 octave) | - | ~5.5x faster |
| Vectorized performance 2D (4 octave) | - | ~30% faster |
| Vectorized performance 1D (1 octave) | - | ~8x faster |
| Vectorized performance 1D (4 octave) | similar | similar |


## Installation

```
pip install git+https://github.com/plottertools/pnoise#egg=pnoise
```

## License

LGPL 2.1, see [LICENSE](LICENSE) file.