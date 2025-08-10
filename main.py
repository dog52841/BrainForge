from neuroforge.core import NeuroForge

def main():
    """
    An example script to demonstrate the functionality of the NeuroForge system.
    This script showcases both the query processing and the learning capabilities.
    """
    # 1. Initialize the NeuroForge AI engine.
    # This will print the initialization sequence of all components.
    nf = NeuroForge()

    # 2. Simulate asking a question for the first time.
    # Since the Extended Knowledge Folder (EKF) is empty, this query
    # will proceed through the full pipeline: NIS -> HRM -> Verifier.
    question = "How do I fix a Python MemoryError in pandas?"
    response = nf.query(question)
    print(f"\n>>> Final Answer for '{question}':\n{response}")
    print("\n" + "="*50 + "\n")

    # 3. Simulate a scenario where the system made a mistake and is now learning.
    # We provide the prompt, the incorrect output (the "error"), and the
    # verified correct output (the "fix").
    error_prompt = "How to install a specific version of a package with pip?"
    error_output = "Just use 'pip install package'"  # An incomplete/wrong answer
    correct_fix = "To install a specific version, use 'pip install package==1.2.3'"

    nf.learn_from_error(
        prompt=error_prompt,
        error=error_output,
        fix=correct_fix
    )
    print("\n" + "="*50 + "\n")

    # 4. Ask the same question again.
    # In a fully implemented system with a persistent EKF, the retrieve()
    # method would now return the 'correct_fix' immediately. Our placeholder
    # will simply show the query flow again.
    response_after_learning = nf.query(error_prompt)
    print(f"\n>>> Final Answer for '{error_prompt}' (after learning cycle):\n{response_after_learning}")


if __name__ == "__main__":
    main()
