import torch.nn as nn


class Generator(nn.Module):
    def __init__(self, noise_dimension, image_channels, features_g):
        super(Generator, self).__init__()
        # Based on  DCGAN paper
        self.network = nn.Sequential(
            self._block(noise_dimension, features_g * 16, 4, 1, 0),
            self._block(features_g * 16, features_g * 8, 4, 2, 1),
            self._block(features_g * 8, features_g * 4, 4, 2, 1),
            self._block(features_g * 4, features_g * 2, 4, 2, 1),
            nn.ConvTranspose2d(features_g * 2, image_channels, kernel_size=4, stride=2, padding=1),
            nn.Tanh()  # Image pixels between -1 and 1
        )

    @staticmethod
    def _block(in_channels, out_channels, kernel_size, stride, padding):
        return nn.Sequential(
            nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding, bias=False),
            # Bias false for batch norm
            nn.BatchNorm2d(out_channels),
            nn.ReLU()
        )

    def forward(self, x):
        return self.network(x)
