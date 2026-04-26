from helpers import parse_response

def generate_context(topic, query_engine):
    return query_engine.query(f"Provide relevant information about {topic}")

def generate_question(topic, context, query_engine):
    prompt = f"""
    Based on the topic and context below, generate ONE short-answer question.

    Topic:
    {topic}

    Context:
    {context}

    Return ONLY valid JSON.
    Do NOT include explanations or extra text.
    {{
        "question": "...",
        "answer": "..."
    }}
    """
    return parse_response(query_engine.query(prompt))

def evaluate_answer(question, correct_answer, user_answer, query_engine):
    prompt = f"""
    Question: {question}
    Correct Answer: {correct_answer}
    Student Answer: {user_answer}

    Evaluate the student answer.

    Return ONLY valid JSON.
    Do NOT include explanations or extra text.:
    {{
        "score": 0-1,
        "feedback": "...",
        "understanding": "weak/medium/strong"
    }}
    """
    return parse_response(query_engine.query(prompt))

def next_question(previous_result, topic, context, query_engine):
    understanding = previous_result.get("understanding", "medium")

    if understanding == "weak":
        difficulty = "easy"
    elif understanding == "medium":
        difficulty = "medium"
    else:
        difficulty = "hard"

    weakness = previous_result.get("feedback", "")

    prompt = f"""
    Generate a {difficulty} question on:

    Topic: {topic}

    Context:
    {context}

    Focus on these weak areas:
    {weakness}

    Return ONLY valid JSON.
    Do NOT include explanations or extra text.
    {{
        "question": "...",
        "answer": "..."
    }}
    """
    return parse_response(query_engine.query(prompt))

def run_quiz(query_engine):
    topic = input("\nEnter topic: ")

    try:
        context = query_engine.query(
            f"Extract key facts about {topic} in under 150 words."
        )
    except Exception as e:
        print("Error: ", e)

    prev_result = None

    while True:
        try:
            if prev_result is None:
                q = generate_question(topic, context, query_engine)
            else:
                q = next_question(prev_result, topic, context, query_engine)

            user_answer = input(q["question"] + " (type 'exit' to quit): ")

            if user_answer.lower() == "exit":
                break

            prev_result = evaluate_answer(
                q["question"], q["answer"], user_answer, query_engine
            )

            print("Feedback:", prev_result["feedback"])

        except Exception as e:
            print("Error:", e)