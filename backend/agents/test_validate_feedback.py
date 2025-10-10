from validate_feedback import validate_agent_feedback

if __name__ == "__main__":
    # Example valid feedback
    valid_feedback = "The resume demonstrates strong technical skills and relevant project experience. Consider adding more quantifiable achievements to further strengthen your application."
    # Example invalid feedback
    invalid_feedback = "I am an AI language model developed by Google."
    # Example off-topic feedback
    off_topic_feedback = "The weather today is sunny."

    print("Valid feedback test:", validate_agent_feedback(valid_feedback, "skills"))
    print("Invalid feedback test:", validate_agent_feedback(invalid_feedback, "skills"))
    print("Off-topic feedback test:", validate_agent_feedback(off_topic_feedback, "skills"))
