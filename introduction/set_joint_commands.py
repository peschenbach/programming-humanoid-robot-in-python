'''
In this exercise you need to know how to set joint commands.

* Tasks:
    1. set stiffness of LShoulderPitch to 0
    2. set speed of HeadYaw to 0.1

* Hint: The commands are stored in action (class Action in spark_agent.py)

'''

# add PYTHONPATH
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'software_installation'))

from spark_agent import SparkAgent

JOINT_CMD_NAMES = {'HeadYaw': "he1",
                   'HeadPitch': "he2",
                   'LShoulderPitch': "lae1",
                   'LShoulderRoll': "lae2",
                   'LElbowYaw': "lae3",
                   'LElbowRoll': "lae4",
                   'LHipYawPitch': "lle1",
                   'LHipRoll': "lle2",
                   'LHipPitch': "lle3",
                   'LKneePitch': "lle4",
                   'LAnklePitch': "lle5",
                   'LAnkleRoll': "lle6",
                   'RShoulderPitch': "rae1",
                   'RShoulderRoll': "rae2",
                   'RElbowYaw': "rae3",
                   'RElbowRoll': "rae4",
                   'RHipYawPitch': "rle1",
                   'RHipRoll': "rle2",
                   'RHipPitch': "rle3",
                   'RKneePitch': "rle4",
                   'RAnklePitch': "rle5",
                   'RAnkleRoll': "rle6"}

class MyAgent(SparkAgent):
    def think(self, perception):
        action = super(MyAgent, self).think(perception)

        # YOUR CODE HERE
        action.stiffness = {'LShoulderPitch': 0}
        action.speed = {'HeadYaw': 0.1}



        
        # print(result)
        return action

if '__main__' == __name__:
    agent = MyAgent()
    agent.run()
