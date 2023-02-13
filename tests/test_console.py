#!/usr/bin/env python3
"""
A unit test module for testing ``console.py`` module.
"""

from console import HBNBCommand 
import unittest
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """
    Test the basic features of the Console.
    """

    def test_console_helper(self):
        """
        Testing the console helper method, being one of the
        default available command that come with cmd.Cmd.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            print(output)
        self.assertIn("Documented commands", output)
