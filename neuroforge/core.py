from .ekf import EKFStore
from .hrm_agent import HRMAgent
from .verifier import Verifier
from .nis import NeurophaseScheduler
from .dac import AdaptationEngine

class NeuroForge:
    """
    The core of the NeuroForge system, orchestrating all components to
    process queries and learn over time.
    """
    def __init__(self):
        print("--- Initializing NeuroForge Engine ---")
        self.ekf = EKFStore(ram_limit=5000)
        self.hrm = HRMAgent()
        self.verifier = Verifier()
        self.nis = NeurophaseScheduler()
        self.dac = AdaptationEngine(self.ekf)
        print("--- NeuroForge Engine Ready ---")

    def query(self, prompt: str) -> str:
        """
        Processes a user query through the full reasoning and verification pipeline.
        """
        print(f"\n=== New Query Received: '{prompt}' ===")

        # Phase 1: Check EKF for a direct, known answer
        print("\n[Phase 1: Knowledge Retrieval]")
        fact = self.ekf.retrieve(prompt)
        if fact:
            print(">>> EKF provided a direct answer.")
            return fact

        # Phase 2: Decide reasoning path with NIS
        print("\n[Phase 2: Inference Scheduling]")
        mode = self.nis.decide_mode(prompt)

        # Phase 3: Reason with HRM Agent
        print("\n[Phase 3: Core Reasoning]")
        reasoning_output = self.hrm.reason(prompt, mode=mode)

        # Phase 4: Verify the output & Store in EKF if it passes
        print("\n[Phase 4: Verification & Learning]")
        if self.verifier.verify(reasoning_output):
            print(">>> Output Verified. Storing in EKF for future use.")
            self.ekf.store(prompt, reasoning_output)
        else:
            print(">>> Output Failed Verification. Discarding.")
            # In a real system, this might trigger an adaptation cycle
            return "Verification failed. I cannot provide a reliable answer."

        print("\n=== Query Processed Successfully ===")
        return reasoning_output

    def learn_from_error(self, prompt: str, error: str, fix: str):
        """
        Public method to allow supervised learning from mistakes,
        triggering the Dynamic Adaptation & Correction (DAC) engine.
        """
        print(f"\n=== Learning from Error for prompt: '{prompt}' ===")
        self.dac.adapt(prompt, error, fix)
