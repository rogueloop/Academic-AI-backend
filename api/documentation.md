# Study Schedule Reinforcement Learning System

This system implements a reinforcement learning (RL) approach to generate study schedules for students. It utilizes Q-learning, a popular RL algorithm, to train an agent to select study tasks based on available study time and task priorities.

## Contents

- [Introduction](#introduction)
- [Classes](#classes)
  - [StudyScheduleEnvironment](#studyscheduleenvironment-class)
  - [QLearningAgent](#qlearningagent-class)
  - [Scheduler](#scheduler-class)
- [Usage](#usage)
- [Documentation](#documentation)
- [License](#license)

## Introduction

The system consists of the following main components:

### StudyScheduleEnvironment

Represents the environment in which the agent operates. It defines the state space, action space, rewards, and transitions.

### QLearningAgent

Implements the Q-learning algorithm to train an agent to select study tasks optimally based on the environment's state and rewards.

### Scheduler

Provides a high-level interface for training the agent and generating study schedules using the trained agent.

## Classes

### StudyScheduleEnvironment Class

This class defines the environment in which the agent operates. It represents a student's study schedule, where the student has a daily time quota for studying and a pool of study tasks to choose from.

**Attributes:**

- `daily_time_quota`: The daily time quota (in hours) available for studying.
- `task_pool`: A list of study tasks, each represented as a dictionary containing information such as subject, description, minimum and maximum study time, priority, prerequisite, and deadline.
- `completed_topics`: A set containing the subjects/topics that have been completed by the student.

**Methods:**

- `reset()`: Resets the environment to its initial state.
- `is_episode_done()`: Checks if the episode (study session) is done based on the available study time.
- `step(action)`: Executes a step in the environment based on the selected action (study task). Returns the next state and the reward obtained from taking the action.

### QLearningAgent Class

This class implements the Q-learning algorithm to train an agent to select study tasks optimally based on the environment's state and rewards.

**Attributes:**

- `env`: The environment in which the agent operates.
- `learning_rate`: The learning rate for updating the Q-values.
- `gamma`: The discount factor for future rewards.
- `epsilon`: The exploration rate for epsilon-greedy action selection.
- `num_epochs`: The number of training epochs.

**Methods:**

- `select_action(state)`: Selects an action (study task) based on the current state using an epsilon-greedy policy.
- `train()`: Trains the agent using Q-learning to learn the optimal policy for selecting study tasks.

### Scheduler Class

This class provides a high-level interface for training the agent and generating study schedules using the trained agent.

**Attributes:**

- `daily_time_quota`: The daily time quota (in hours) available for studying.
- `learning_rate`: The learning rate for updating the Q-values during training.
- `gamma`: The discount factor for future rewards during training.
- `epsilon`: The exploration rate for epsilon-greedy action selection during training.
- `num_epochs`: The number of training epochs.
- `env`: An instance of the StudyScheduleEnvironment class.
- `agent`: An instance of the QLearningAgent class.

**Methods:**

- `train()`: Trains the agent using Q-learning based on the provided parameters.
- `generate_study_schedule()`: Generates a study schedule using the trained agent and returns the schedule as a list of dictionaries containing study tasks and their corresponding study times.

## Usage

To use the study schedule reinforcement learning system:

1. Define the study tasks and their attributes in the `task_pool` list within the `StudyScheduleEnvironment` class.
2. Create an instance of the `Scheduler` class with the desired parameters.
3. Train the agent using the `train()` method.
4. Generate study schedules using the `generate_study_schedule()` method.

**Example:**

```python
# Define study tasks and their attributes
task_pool = [...]

# Create a Scheduler instance
scheduler = Scheduler(daily_time_quota=8, learning_rate=0.001, gamma=0.9, epsilon=0.1, num_epochs=100, task_pool=task_pool)

# Train the agent
scheduler.train()

# Generate a study schedule
study_schedule = scheduler.generate_study_schedule()
