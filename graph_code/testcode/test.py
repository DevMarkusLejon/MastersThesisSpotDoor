

joint_pos=[0.1, 0.9, -1.5, -0.1, 0.9, -1.5, 0.1, 1.1, -1.5, -0.1, 1.1, -1.5, 0, 3.13, -3,13, 1.57, 0, -1.57, 0]
joint_vel = [5]*19
last_action = [6]*12

obs = []

obs += [0, 0, 0]
obs += [1,1,1]
obs += [2,2,2]
obs += [3,3,3]
obs += joint_pos[0:12]
obs += joint_vel[0:12]
obs += last_action[0:12]

print(len(obs))
print(obs)
def print_observations(observations: list[float], USED_DOF: int = 19):
    """debug function to print out the observation data used as model input

    arguments
    observations -- list of float values ready to be passed into the model
    """
    
    print("base_linear_velocity:", observations[0:3])
    print("base_angular_velocity:", observations[3:6])
    print("projected_gravity:", observations[6:9])
    print("commanded_vel:", observations[9:12])
    print("joint_positions:", observations[12:12+USED_DOF])
    print("joint_velocity:", observations[12+USED_DOF:12+USED_DOF*2])
    print("last_action:", observations[12+USED_DOF*2:12+USED_DOF*3])

print_observations(obs, 12)
