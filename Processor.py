import tensorrt as trt
import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np

class SSD():
    def __init__(self):
        # initialize logger for debugging
        trt_logger = trt.Logger(trt.Logger.INFO)
        
        # load libnvinfer plugins
        # https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/
        trt.init_libnvinfer_plugins(trt_logger, '')
        
        # instantiate TensorRT engine
        trt_model = 'models/ssd-mobilenet-v2-coco.trt'
        with open(trt_model, 'rb') as f, trt.Runtime(trt_logger) as runtime:
            engine = runtime.deserialize_cuda_engine(f.read())
        
        # create context
        context = engine.create_execution_context()
        stream = cuda.Stream()

        # memory allocations for input/output layers
        # binding Input
        # binding NMS
        # binding NMS_1
        self.inputs = []
        self.outputs = []
        self.bindings = []
        for binding in engine:
            size = trt.volume(engine.get_binding_shape(binding))
            host_mem = cuda.pagelocked_empty(size, np.float32)   
            cuda_mem = cuda.mem_alloc(host_mem.nbytes)
            if engine.binding_is_input(binding):
                self.inputs.append({ 'host': host_mem, 'cuda': cuda_mem })
            else:
                self.outputs.append({ 'host': host_mem, 'cuda': cuda_mem })
