# test_coreapex.py
"""
Tests for CoreApex module.
"""

import unittest
from coreapex import CoreApex

class TestCoreApex(unittest.TestCase):
    """Test cases for CoreApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreApex()
        self.assertIsInstance(instance, CoreApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
