class Config(object):
    TEXT = 'an apple on a wooden table'  # @param {type:"string"}
    NUM_LAYERS = 32  # @param {type:"number"}
    SAVE_EVERY = 20  # @param {type:"number"}
    BATCH_SIZE = 2  # @param {type: "number"}
    GRADIENT_ACCUMULATE_EVERY = 8  # @param {type: "number"}
    IMAGE_WIDTH = 256  # @param {type:"number"}
    SAVE_PROGRESS = True  # @param {type:"boolean"}
    LEARNING_RATE = 1e-5  # @param {type:"number"}
    ITERATIONS = 1050  # @param {type:"number"}
