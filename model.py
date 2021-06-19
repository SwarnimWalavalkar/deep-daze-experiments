from IPython.display import Image

from deep_daze import Imagine

from config import Config as config

import torch
torch.cuda.empty_cache()


model = Imagine(
    text=config.TEXT,
    num_layers=config.NUM_LAYERS,
    save_every=config.SAVE_EVERY,
    batch_size=config.BATCH_SIZE,
    gradient_accumulate_every=config.GRADIENT_ACCUMULATE_EVERY,
    image_width=config.IMAGE_WIDTH,
    lr=config.LEARNING_RATE,
    iterations=config.ITERATIONS,
    save_progress=config.SAVE_PROGRESS
)

for epoch in range(20):
    for i in range(config.ITERATIONS):
        model.train_step(epoch, i)

        if i % model.save_every != 0:
            continue

        filename = config.TEXT.replace(' ', '_')
        image = Image(f'./{filename}.jpg')
