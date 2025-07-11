# test_blockchainnftvalidator.py
"""
Tests for BlockchainNFTValidator module.
"""

import unittest
from blockchainnftvalidator import BlockchainNFTValidator

class TestBlockchainNFTValidator(unittest.TestCase):
    """Test cases for BlockchainNFTValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTValidator()
        self.assertIsInstance(instance, BlockchainNFTValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
