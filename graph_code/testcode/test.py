

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
