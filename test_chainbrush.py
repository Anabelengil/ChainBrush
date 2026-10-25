# test_chainbrush.py
"""
Tests for ChainBrush module.
"""

import unittest
from chainbrush import ChainBrush

class TestChainBrush(unittest.TestCase):
    """Test cases for ChainBrush class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainBrush()
        self.assertIsInstance(instance, ChainBrush)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainBrush()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
