# test_pulseblock.py
"""
Tests for PulseBlock module.
"""

import unittest
from pulseblock import PulseBlock

class TestPulseBlock(unittest.TestCase):
    """Test cases for PulseBlock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseBlock()
        self.assertIsInstance(instance, PulseBlock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseBlock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
