import argparse
import torch
from logger.log import LoggerService

logger = LoggerService.get_instance()


class ModelConfig:

    def __init__(self, args):
        self.batch_size: int = args.batch_size
        self.epoch: int = args.epoch
        self.device: str = args.device
        self.size: int = args.size
        self.learning_rate: float = args.learning_rate
        self.noise_dimension: int = args.noise_dimension
        self.number_of_classes: int = args.number_of_classes
        self.features_discriminator: int = args.features_discriminator
        self.features_generator: int = args.features_generator
        self.train_path: str = args.train_path
        self.val_path: str = args.val_path
        self.data_format: str = args.data_format
        self.kernel_size: int = args.kernel_size
        self.save: int = args.save
        self.load: int = args.load
        self.models_path = args.models_path


def process_args(args) -> ModelConfig:
    if torch.cuda.is_available() and args.device == 'cpu':
        logger.warn("You have a CUDA device, so you should probably run with -d cuda:0")
    config: ModelConfig = ModelConfig(args)
    return config


def parse_args() -> ModelConfig:
    parser = argparse.ArgumentParser(description='Run SimulatorGAN')

    parser.add_argument('-b', '--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('-e', '--epoch', type=int, default=10, help='Number of epochs')
    parser.add_argument('-d', '--device', type=str, default='cpu', help='Device (cpu, cuda:0 ...)')
    parser.add_argument('-s', '--size', type=int, default=50, help='Image size')
    parser.add_argument('-lr', '--learning-rate', type=float, default=3e-4, help='Learning Rate')
    parser.add_argument('-nd', '--noise-dimension', type=int, default=100, help='Noise dimension')
    parser.add_argument('-nc', '--number-of-classes', type=int, default=3, help='Number of classes')
    parser.add_argument('-fd', '--features-discriminator', type=int, default=64,
                        help='Scaling discriminator features factor')
    parser.add_argument('-fg', '--features-generator', type=int, default=64,
                        help='Scaling generator features factor')
    parser.add_argument('-tp', '--train-path', type=str, required=True, help='Training data path')
    parser.add_argument('-vp', '--val-path', type=str, required=True, help='Validation data path')
    parser.add_argument('-df', '--data-format', type=str, default='txt', help='Data type (txt, csv ...)')
    parser.add_argument('-ks', '--kernel-size', type=int, default='3', help='Convolution kernel size')
    parser.add_argument('--save', type=int, default='0', help='Save models')
    parser.add_argument('--load', type=int, default='0', help='Load models')
    parser.add_argument('--models_path', type=str, default='', help='Models path')

    args = parser.parse_args()
    conf = process_args(args)

    return conf
