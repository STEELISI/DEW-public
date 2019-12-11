import os.path
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.abspath(os.path.join(cwd, os.pardir))
sys.path.insert(0, parentDir)
from generator import GeneralGenerator

class Generator(GeneralGenerator):
    def __init__(self, *args, **kwargs):
        super(Generator, self).__init__(*args, name="bash", **kwargs)
        self.scenario = args[0]
        self.constraints = kwargs['constraints']

    # def parse(self):
    #     print("Scenario:")
    #     for scenario in self.scenario:
    #         print("\t" + scenario)
    #     print("Constraints:")
    #     print("\t" + str(self.constraints))
