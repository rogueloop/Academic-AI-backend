import numpy as np
import time
import torch
import torch.nn as nn
import torch.optim as optim
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
class StudyScheduleEnvironment:
    def __init__(self, daily_time_quota,task_pool):
        self.daily_time_quota = daily_time_quota
        self.state = daily_time_quota
        self.task_pool=task_pool
#         self.task_pool = [
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Systems of Linear Equations', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Gauss Elimination, Row Echelon Form, and Rank of a Matrix', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Systems of Linear Equations', 'deadline': 5},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Fundamental Theorem for Linear Systems', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Gauss Elimination, Row Echelon Form, and Rank of a Matrix', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Eigenvalues and Eigenvectors', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Fundamental Theorem for Linear Systems', 'deadline': 5},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Diagonalization of Matrices', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Eigenvalues and Eigenvectors', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Orthogonal Transformation, Quadratic Forms, and Canonical Forms', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Diagonalization of Matrices', 'deadline': 8},

#     # Module 2: Multivariable Calculus - Differentiation
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Limit and Continuity of Functions of Two Variables', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Partial Derivatives, Chain Rule, and Total Derivative', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Limit and Continuity of Functions of Two Variables', 'deadline': 5},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Relative Maxima and Minima', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Partial Derivatives, Chain Rule, and Total Derivative', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Absolute Maxima and Minima on Closed and Bounded Set', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Relative Maxima and Minima', 'deadline': 6},

#     # Module 3: Multivariable Calculus - Integration
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Double Integrals (Cartesian)', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Reversing the Order of Integration', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Double Integrals (Cartesian)', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Change of Coordinates (Cartesian to Polar)', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Reversing the Order of Integration', 'deadline': 8},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Finding Areas and Volume Using Double Integrals', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Change of Coordinates (Cartesian to Polar)', 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Mass and Centre of Gravity of Inhomogeneous Laminas Using Double Integral', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Finding Areas and Volume Using Double Integrals', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Triple Integrals', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Mass and Centre of Gravity of Inhomogeneous Laminas Using Double Integral', 'deadline': 8},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Volume Calculated as Triple Integral', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Triple Integrals', 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Triple Integral in Cylindrical and Spherical Coordinates', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Volume Calculated as Triple Integral', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Computations Involving Spheres, Cylinders', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Triple Integral in Cylindrical and Spherical Coordinates', 'deadline': 8},

#     # Module 4: Sequences and Series
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Convergence of Sequences and Series', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Convergence of Geometric Series and P-Series', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Convergence of Sequences and Series', 'deadline': 5},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Test of Convergence (Comparison, Ratio, and Root Tests)', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Convergence of Geometric Series and P-Series', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Alternating Series and Leibnitz Test', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Test of Convergence (Comparison, Ratio, and Root Tests)', 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Absolute and Conditional Convergence', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Alternating Series and Leibnitz Test', 'deadline': 8},

#     # Module 5: Series Representation of Functions
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Taylor Series', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': None, 'deadline': 5},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Binomial Series and Series Representation of Exponential, Trigonometric, Logarithmic Functions', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Taylor Series', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Fourier Series', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Binomial Series and Series Representation of Exponential, Trigonometric, Logarithmic Functions', 'deadline': 8},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Euler Formulas', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Fourier Series', 'deadline': 6},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Convergence of Fourier Series', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Euler Formulas', 'deadline': 7},
#     {'subject': 'Linear Algebra and Calculus', 'description': 'Half Range Sine and Cosine Series, Parseval’s Theorem', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Convergence of Fourier Series', 'deadline': 8},
    
    
#       # Module 1: Electrochemistry and Corrosion
#     {'subject': 'Engineering Chemistry', 'description': 'Introduction to Electrochemistry and Differences between Electrolytic and Electrochemical Cells', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'Electrochemical Cells and Redox Reactions', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Introduction to Electrochemistry and Differences between Electrolytic and Electrochemical Cells', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': 'Cell Representation and Types of Electrodes', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Electrochemical Cells and Redox Reactions', 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'Reference Electrodes and SHE', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Cell Representation and Types of Electrodes', 'deadline': 5},
#     # ... Continue adding topics for Module 1

#     # Module 2: Spectroscopic Techniques and Applications
#     {'subject': 'Engineering Chemistry', 'description': 'Introduction to Spectroscopic Techniques and Types of Spectrum', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'UV-Visible Spectroscopy Principles and Applications', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Introduction to Spectroscopic Techniques and Types of Spectrum', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': 'Molecular Energy Levels and Beer Lambert’s Law', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'UV-Visible Spectroscopy Principles and Applications', 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'IR-Spectroscopy Principles and Applications', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Molecular Energy Levels and Beer Lambert’s Law', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': '1H NMR Spectroscopy Principles and Applications', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'IR-Spectroscopy Principles and Applications', 'deadline': 6},
#     # ... Continue adding topics for Module 2

#     # Module 3: Instrumental Methods and Nanomaterials
#     {'subject': 'Engineering Chemistry', 'description': 'Principles of Thermal Analysis and Applications', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'Chromatographic Methods and Nanomaterials', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Principles of Thermal Analysis and Applications', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': 'TGA and DTA Principles and Applications', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Chromatographic Methods and Nanomaterials', 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'Basic Principles and Applications of Column Chromatography', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'TGA and DTA Principles and Applications', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': 'GC and HPLC Principles and Applications', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Basic Principles and Applications of Column Chromatography', 'deadline': 6},
#     # ... Continue adding topics for Module 3

#     # Module 4: Stereochemistry and Polymer Chemistry
#     {'subject': 'Engineering Chemistry', 'description': 'Isomerism and Representation of 3D Structures', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'Stereoisomerism and Conformational Analysis', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Isomerism and Representation of 3D Structures', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': 'Geometrical Isomerism and Optical Isomerism', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Stereoisomerism and Conformational Analysis', 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'R-S Notation and Optical Isomerism', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Geometrical Isomerism and Optical Isomerism', 'deadline': 5},
#     # ... Continue adding topics for Module 4

#     # Module 5: Water Chemistry and Sewage Water Treatment
#     {'subject': 'Engineering Chemistry', 'description': 'Water Characteristics and Hardness', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'Water Softening Methods and Reverse Osmosis', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Water Characteristics and Hardness', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': 'Disinfection Methods and Municipal Water Treatment', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Water Softening Methods and Reverse Osmosis', 'deadline': 6},
#     {'subject': 'Engineering Chemistry', 'description': 'Dissolved Oxygen and Water Treatment', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Disinfection Methods and Municipal Water Treatment', 'deadline': 5},
#     {'subject': 'Engineering Chemistry', 'description': 'Sewage Water Treatment and Flow Diagrams', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Dissolved Oxygen and Water Treatment', 'deadline': 6},
#     # ... Continue adding topics for Module 5
        
#       {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Relevance of Civil Engineering in Infrastructural Development', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Responsibility of an Engineer in Ensuring Safety', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Relevance of Civil Engineering in Infrastructural Development', 'deadline': 5},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Introduction to Major Disciplines of Civil Engineering', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Responsibility of an Engineer in Ensuring Safety', 'deadline': 6},
#     # ... Continue adding topics for Module 1

#     # Module 2: Surveying and Construction Materials
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Importance, Objectives, and Principles of Surveying', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Conventional Construction Materials: Bricks, Stones, Cement, Sand, and Timber', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Importance, Objectives, and Principles of Surveying', 'deadline': 5},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Cement Concrete and Steel: Constituents, Properties, and Types', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Conventional Construction Materials: Bricks, Stones, Cement, Sand, and Timber', 'deadline': 6},
#     # ... Continue adding topics for Module 2

#     # Module 3: Building Construction and Basic Infrastructure Services
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Foundations: Bearing Capacity, Functions, and Types', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Brick Masonry and Roofs/Floors: Types and Functions', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Foundations: Bearing Capacity, Functions, and Types', 'deadline': 5},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Basic Infrastructure Services: MEP, HVAC, Elevators, etc.', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'Brick Masonry and Roofs/Floors: Types and Functions', 'deadline': 6},
#     # ... Continue adding topics for Module 3

#     # Module 4: Analysis of Thermodynamic Cycles and IC Engines
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Analysis of Thermodynamic Cycles: Carnot, Otto, Diesel', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': None, 'deadline': 6},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'IC Engines: CI, SI, 2-Stroke, 4-Stroke', 'min_study_time': 3, 'max_study_time': 5, 'priority': 4, 'prerequisite': 'Analysis of Thermodynamic Cycles: Carnot, Otto, Diesel', 'deadline': 5},
#     {'subject': 'Basics of Civil & Mechanical Engineering', 'description': 'Efficiencies of IC Engines and Systems', 'min_study_time': 2, 'max_study_time': 4, 'priority': 3, 'prerequisite': 'IC Engines: CI, SI, 2-Stroke, 4-Stroke', 'deadline': 6},   
#       # Add more topics as needed
# ]

        self.completed_topics = set()

    def reset(self):
        self.state = self.daily_time_quota
        self.completed_topics = set()
        return self.state
    def is_episode_done(self):
        # Check if the available study time for the day is exhausted
        return self.state <= 0  

    def step(self, action):
        task = self.task_pool[action]
        
        # Check if the task has a prerequisite
        # if task['prerequisite'] and task['prerequisite'] not in self.completed_topics:
        #     return self.state, 0  # Can't study this topic if the prerequisite is not completed

        # Check if the same subject topic has already been studied on the same day
        if task['subject'] in self.completed_topics:
            # Check if the deadline is close, allowing the same subject topic on the same day
            if task['deadline'] <= 2:  # You can adjust the threshold for a close deadline
                pass
            else:
                return self.state, 0  # Can't study the same subject on the same day

        task_time = np.random.randint(task['min_study_time'], task['max_study_time'] + 1)
        reward = 0

        if task_time <= self.state:
            self.state -= task_time
            reward = task['priority']
            self.completed_topics.add(task['subject'])

        return self.state, reward

seed = 42  # Choose any seed value
np.random.seed(seed)
torch.manual_seed(seed)
 
class QNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, output_size)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

class QLearningAgent:
    def __init__(self, env, learning_rate, gamma, epsilon, num_epochs):
        self.env = env
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_epochs = num_epochs

        # Create Q-network
        self.q_network = QNetwork(1, len(env.task_pool)).to(device)
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=learning_rate)
        self.criterion = nn.MSELoss()

    def select_action(self, state):
        f=np.random.rand()
        if f < self.epsilon:
            # print("random selection is too short\n",f)
            return np.random.choice(len(self.env.task_pool))
        else:
            with torch.no_grad():
                q_values = self.q_network(torch.tensor([state], dtype=torch.float32))
                # print("qvalues: ",q_values)
                return torch.argmax(q_values).item()
           

    def train(self):
        for epoch in range(self.num_epochs):
            state = self.env.reset()
            total_reward = 0
            
            self.env.completed_topics = set()  # Reset completed topics for each epoch
            max_steps = 1000  # Adjust as needed
            step_count = 0
            while step_count < max_steps:
                action = self.select_action(state)
                next_state, reward = self.env.step(action)

                with torch.no_grad():
                    q_values_next = self.q_network(torch.tensor([next_state], dtype=torch.float32))
                    max_q_value_next = torch.max(q_values_next).item()

                target_q_value = reward + self.gamma * max_q_value_next
                current_q_value = self.q_network(torch.tensor([state], dtype=torch.float32))[action]

                loss = self.criterion(current_q_value, torch.tensor(target_q_value))

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                total_reward += reward
                state = next_state
                step_count+=1
                if self.env.is_episode_done():
                    break
                

            print(f'Epoch {epoch + 1}/{self.num_epochs}, Total Reward: {total_reward}')
        torch.save(self.q_network.state_dict(), "qnetwork.pth")
        print(self.q_network.state_dict())

# Set parameters

class Scheduler:
    
    def __init__(self,daily_time_quota,learning_rate, gamma, epsilon, num_epochs,task_pool):
        self.daily_time_quota=daily_time_quota
        self.learning_rate=learning_rate
        self.gamma=gamma
        self.epsilon=epsilon
        self.num_epochs=num_epochs
        self.env = StudyScheduleEnvironment(daily_time_quota,task_pool)
        self.agent = QLearningAgent(self.env, learning_rate, gamma, epsilon, num_epochs)
# Create environment and agent
    def train(self):

        start_time = time.time()
        print(self.agent.q_network)
        print("reached the training phase")
# Train the agent
        self.agent.train()


        training_time = time.time() - start_time
        print(f"Training completed successfully. Training Time: {training_time} seconds")


    def generate_study_schedule(self):
        state = self.env.reset()
        schedule = []
        selected_tasks = set()

        while state > 0:
            action = self.agent.select_action(state)

        # Check if the task has already been selected
            if action in selected_tasks:
                continue

            task = self.env.task_pool[action]
            task_time = np.random.randint(task['min_study_time'], task['max_study_time'] + 1)

            if task_time <= state:
                schedule.append({'Subject': task['subject'], 'Task': task['description'], 'StudyTime': task_time})
                state -= task_time

            # Add the index to the set of selected tasks
                selected_tasks.add(action)
        
        for entry in schedule:
            print(f"Subject: {entry['Subject']}, Task: {entry['Task']}, Study Time: {entry['StudyTime']} hours")
        return schedule


# Generate a study schedule using the trained agent
    

# Print the study schedule

