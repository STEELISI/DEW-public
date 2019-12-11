# XXX We need to redo the directory structure so core functions (like Scenario parsing) are more central.
# In the meantime:
import os.path
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.abspath(os.path.join(cwd, os.pardir))
sys.path.insert(0, parentDir + '/UI/HighLevelBehaviorLanguage/')
sys.path.insert(0, parentDir + '/UI/')
from hlb_parser import HLBParser, ConstraintParser

class GeneralGenerator(object):
    # scenario and constraints given as a list.
    def __init__(self, scenario, constraints=None, name='Generic Class'):
        # For debugging. Subclass should set this to something meaningful. e.g. "bash"
        self.name = name

        # A list of DEW constraints. E.g. ['num actorA 3', 'os actorB ubuntu']
        self.constraints = constraints

        # A list of Scenario statements. E.g. ['Scenario statement 1', 'Scenario statement 2']
        # The order of the list is not meaningful.
        self.scenario = scenario

        # Imported from hlb_parser.
        self.HLBparser = HLBParser()
        self.ConstParser = ConstraintParser()

        # After we parse statements, we store them as a list of tuples (one tuple per statement).
        self.scenario_parsed = []
        self.constraints_parsed = []

    def parse(self):
        # For each item in our scenario/constraints lists, make sure we can parse it and
        # turn it into tuplets.
        # Scenario -> ['trigger events', 'actors', 'action', 'emit events', 'wait time']
        # (note, some of these can be None)

        # Constraints -> ['constraint type', 'target', 'value' ] (some of these can be None)
        for c in self.constraints:
            try:
                parsedTuple = self.ConstParser.parse_stmt(c)
            except:
                print("ERROR:\tCannot parse the following constraint: %s\n" % c)
                return False
            # Because we use parsing for UI suggestions, we don't throw exceptions
            # when we can't parse a statement, instead the parser returns a tuplet of Nones.
            if all(x == None for x in parsedTuple):
                print("ERROR:\tUnparsable constraint: %s\n" % c)
                return False

            # XXX Right now, for generation we only care about 'num' constraints.
            # XXX At some point we may care about others, like 'os'.
            if 'num' == parsedTuple[0]:
                self.constraints_parsed.append(parsedTuple)

        for s in self.scenario:
            try:
                parsedTuple = self.HLBparser.parse_stmt(s)
            except:
                print("ERROR:\tCannot parse the following Scenario statement: %s\n" % s)
                return False
            # See above comment - we return all Nones if statement is un-parsable.
            if all(x == None for x in parsedTuple):
                print("ERROR:\tUnparsable Scenario statement: %s\n" % s)
                return False
            self.scenario_parsed.append(parsedTuple)


    def graphDependency(self):
        # We only need dependencies for Scenario.
        pass


    def generate(self):
        # Parse all our Scenario and Constraints.
        if not self.parse():
            exit()

        # Figure out dependencies
        # XXX For now, this is its own code here, BUT we should not duplicate functionality
        # XXX between the generator and the UI that shows the dependency graph.
        if not self.graphDependency():
            exit()


    def translate(self):
        # THIS FUNCTION SHOULD BE OVERRIDDEN BY SPECIFIC GENERATOR.
        # XXX We may find that we need more info than this group by group approach:
        # XXX but for now, we tranlate a set of Scenario commands at a time which can be
        # started at the same time.
        # Any constraints that apply to the targets (Scenario actors) in the commands
        # are also packaged with the Scenario command set.
        pass


    def output(self, filename=None):
        pass


