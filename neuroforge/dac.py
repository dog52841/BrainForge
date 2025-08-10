# Note: In a real application, you might need to handle potential circular imports
# if modules grow more complex. For now, this is fine.
from .ekf import EKFStore

class AdaptationEngine:
    """
    Dynamic Adaptation & Correction: Learns from errors and patches
    the Extended Knowledge Folder (EKF).
    """
    def __init__(self, ekf_store: EKFStore):
        print("AdaptationEngine initialized.")
        self.ekf = ekf_store

    def adapt(self, prompt: str, error: str, fix: str):
        """
        Adapts the EKF based on an error and a fix.
        This process is how the system "learns" from its mistakes.
        """
        print(f"DAC: Adapting from error for prompt '{prompt}'")
        print(f"DAC: Received Error='{error}', Fix='{fix}'")

        # The core logic: store the verified fix in the knowledge store.
        self.ekf.store(prompt, fix)

        print("DAC: Adaptation complete. New knowledge stored in EKF.")
