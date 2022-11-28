from unittest import TestCase

import numpy as np
import torch
import tensorflow

from phi import math
from phi.torch import TORCH


class TestTorchBackend(TestCase):

    def test_as_tensor_stacking(self):
        data = [torch.tensor(1), torch.tensor(2)]
        tensor = TORCH.as_tensor(data, convert_external=True)
        self.assertIsInstance(tensor, torch.Tensor)
        self.assertEqual((2,), tensor.shape)

    def test_pad(self):
        a = np.random.rand(32, 32)
        a_np = np.pad(a, pad_width=1, mode='wrap')
        a_torch = TORCH.pad(torch.Tensor(a), pad_width=((1, 1), (1, 1)), mode='circular')
        np.array_equal(a_np, a_torch)

    def test_is_tensor(self):
        self.assertTrue(TORCH.is_tensor(1))
        self.assertTrue(TORCH.is_tensor([0, 1, 2, 3]))
        self.assertTrue(TORCH.is_tensor(torch.zeros(4)))
        self.assertTrue(TORCH.is_tensor(np.zeros(4)))
        self.assertFalse(TORCH.is_tensor(tensorflow.zeros(4)))
        # only native
        self.assertTrue(TORCH.is_tensor(torch.zeros(4), only_native=True))
        self.assertFalse(TORCH.is_tensor(tensorflow.zeros(4), only_native=True))
        self.assertFalse(TORCH.is_tensor([0, 1, 2, 3], only_native=True))
        self.assertFalse(TORCH.is_tensor(np.zeros(4), only_native=True))
        # Others
        self.assertFalse(TORCH.is_tensor('string'))
