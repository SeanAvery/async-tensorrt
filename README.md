# async-tensorrt

![async overview](async_overview.png)

## Overview

The challenge is trying to maintain a 30 fps camera stream when inference time alone takes 40 miliseconds. To solve this, you can create a child thread for processing frames. This allows the main thread to run without being blocked by the Cuda execution.


## Materials

1. [Linux machine with Cuda (see tutorial 0)](https://seanavery.github.io/jetson-nano-box/#/)
2. [JK Jung's TensorRT Demos](https://github.com/jkjung-avt/tensorrt_demos)
3. [Multithreaded Python](https://docs.python.org/3.6/library/threading.html)
4. [TensorRT Documentation](https://docs.nvidia.com/deeplearning/tensorrt/api/index.html#python)
5. [PyCuda Documentation](https://documen.tician.de/pycuda/)


The code is a modification from the async exeuction in [JK Jung's TensorRT Demos](https://github.com/jkjung-avt/tensorrt_demos/blob/master/trt_ssd_async.py). In my code the main thread is responsible for Video Capture and Display, and the child thread handles inference and processing. This allows inference to execute modulus the incoming frames.

- [x] 1. Create Python thread
- [x] 2. Initialize Cuda context inside thread
- [x] 3. Camera capture in main thread
- [x] 4. Queue and modulus to throttle inference
- [x] 5. Locking and global variables
- [x] 6. Visualize inference results from shared state
