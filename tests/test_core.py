import unittest
import sys
import os

# This allows the test to be run from the root directory (e.g., 'python -m unittest discover')
# or directly (e.g., 'python tests/test_core.py') by ensuring the 'neuroforge'
# package is on the Python path.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from neuroforge.core import NeuroForge

class TestNeuroForgeIntegration(unittest.TestCase):
    """
    A basic integration test for the NeuroForge system.

    This test ensures that the main NeuroForge class can be instantiated
    and that its public methods (`query` and `learn_from_error`) can be
    executed without raising any exceptions. It serves as a "smoke test"
    to confirm that all components are wired together correctly.
    """

    def setUp(self):
        """
        Set up a new NeuroForge instance before each test method runs.
        This ensures that tests are isolated from each other.
        """
        # Note: The print statements from the application will appear during the test run.
        # This is expected for this stage of development.
        self.nf = NeuroForge()

    def test_query_pipeline_executes(self):
        """
        Tests that the `query` method can be called and returns a string.
        """
        print("\n--- Running test: test_query_pipeline_executes ---")
        response = self.nf.query("This is a test query for the integration test.")
        self.assertIsInstance(response, str, "The query method should return a string.")
        # In our placeholder, the output should not be a verification failure message.
        self.assertNotIn("Verification failed", response)

    def test_learning_pipeline_executes(self):
        """
        Tests that the `learn_from_error` method can be called without error.
        """
        print("\n--- Running test: test_learning_pipeline_executes ---")
        try:
            self.nf.learn_from_error(
                prompt="Test prompt for learning",
                error="This was the incorrect output.",
                fix="This is the correct fix to be stored."
            )
        except Exception as e:
            self.fail(f"learn_from_error() raised an exception unexpectedly: {e}")

if __name__ == '__main__':
    # Allows the test to be run directly from the command line
    unittest.main()
