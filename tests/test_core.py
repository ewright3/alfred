import unittest
from ..casey import core

class TestCore(unittest.TestCase):
    def test_read_instructions(self):
        message = "test message"
        self.assertEqual(core.read_instruction("test message"), message)
        self.assertEqual(core.read_instruction(1), 1)
        self.assertEqual(core.read_instruction(True), True)

    def test_values(self):
        self.assertRaises(ValueError, core.read_instruction, None)
        self.assertRaises(ValueError, core.read_instruction, False)    
