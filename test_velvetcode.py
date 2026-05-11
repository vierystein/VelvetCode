# test_velvetcode.py
"""
Tests for VelvetCode module.
"""

import unittest
from velvetcode import VelvetCode

class TestVelvetCode(unittest.TestCase):
    """Test cases for VelvetCode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VelvetCode()
        self.assertIsInstance(instance, VelvetCode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VelvetCode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
