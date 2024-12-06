#!/usr/bin/env python
import sys
from my_plan.crew import MyPlanCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'dietary_requirement': 'Gluten-Free, Dairy-Free',
        'ingredients': 'Chicken, Celery, Carrot, Almond Milk, Apple Cider Vinegar, Hummus, Pork Loin, Broccoli', 
        'health_goals': 'Support weight loss, improve gut health'
    }
    MyPlanCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'dietary_requirement': 'Gluten-Free, Dairy-Free',
        'ingredients': 'Chicken, Celery, Carrot, Almond Milk, Apple Cider Vinegar, Hummus, Pork Loin, Broccoli', 
        'health_goals': 'Support weight loss, improve gut health'
    }
    try:
        MyPlanCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyPlanCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'dietary_requirement': 'Gluten-Free, Dairy-Free',
        'ingredients': 'Chicken, Celery, Carrot, Almond Milk, Apple Cider Vinegar, Hummus, Pork Loin, Broccoli', 
        'health_goals': 'Support weight loss, improve gut health'
    }
    try:
        MyPlanCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
