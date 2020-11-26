from gym.envs.registration import register

register(
    id='Planar5DoF-v0',
    entry_point='gym_dof5.envs:GazeboPlanar5DofEnv',
)

