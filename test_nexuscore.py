# test_nexuscore.py
"""
Tests for NexusCore module.
"""

import unittest
from nexuscore import NexusCore

class TestNexusCore(unittest.TestCase):
    """Test cases for NexusCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NexusCore()
        self.assertIsInstance(instance, NexusCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NexusCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
