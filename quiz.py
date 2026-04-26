from helpers import parse_response

def generate_context(topic, query_engine):
    return query_engine.query(f"Provide relevant information about {topic} in under 80 words")

def generate_question(topic, context, query_engine):
    prompt = f"""
    Generate ONE short-answer question based ONLY on the topic and context.

    Topic: {topic}

    Context (max 80 words):
    {context}

    Return ONLY valid JSON:
    {{
        "question": "...",
        "answer": "..."
    }}
    """

    return parse_response(query_engine.query(prompt))

def evaluate_answer(question, correct_answer, user_answer, query_engine):
    prompt = f"""
    Evaluate the student's answer briefly.

    Question: {question}
    Correct Answer: {correct_answer}
    Student Answer: {user_answer}

    Return ONLY valid JSON:
    {{
        "score": 0 or 1,
        "feedback": "short feedback (max 20 words)",
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
    Generate ONE {difficulty} question on the topic.

    Topic: {topic}

    Context (max 80 words):
    {context}

    Focus on this weakness (max 10 words):
    {weakness}

    Return ONLY valid JSON:
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