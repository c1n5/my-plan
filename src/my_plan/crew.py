from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class MyPlanCrew():
    """Meal Planning Crew for Personalized Nutrition and Shopping"""

    @agent
    def dietary_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['dietary_analyst'],
#            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def menu_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['menu_planner'],
#            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def shopping_list_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['shopping_list_optimizer'],
 #           tools=[SerperDevTool()],
            verbose=True
        )

    @task
    def dietary_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['dietary_analyst_task'],
            output_file='01 dietary_preference_report.md'
        )

    @task
    def menu_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['menu_planner_task'],
            output_file='02 weekly_menu_plan.md'
        )

    @task
    def shopping_list_optimizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['shopping_list_optimizer_task'],
            output_file='03 shopping_list.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Meal Planning crew with sequential processing"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
