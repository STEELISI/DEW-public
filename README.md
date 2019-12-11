# DEW (Doer!): Distributed Eperiment Workflows Representation

DEW unifies behavior and topology of an experiment, but captures only relevant topological details. 

# Design overview 

DEW has several design goals:

## High-level representation

It was important to us that DEW contains a human-readable, short
description of what the experiment is supposed to do.  Such a
description facilitates reuse, because researchers could, at a glance,
understand the experiment's actions and judge if this experiment is useful
to them.  Moreover, expressing what an experiment will do in broad strokes
captures the process, which so far has existed only in the researcher's
mind, and eases experiment design.

## Generic language

DEW should support many diverse experiments, and thus its language must be
expressive enough to be broadly applicable, regardless of the experiment's
goal or testbed infrastructure where it will be realized.

## Self-contained representation

We wanted DEW to contain sufficient details to facilitate automated
generation of experimental topologies and scripts, which would run on these
topologies.  If we could achieve this, then researchers could work with
experiments at a high level, delegating tedious, detail-oriented and
error-prone tasks to machines.  This would further facilitate generation of
topologies and scripts in many different languages, and for many different
testbed infrastructures, enabling portability.

## Decouple behavior from topology

We wanted to decouple the intended behavior from the topology where it will
be realized, thus enabling the same experiment to be scaled up and down
easily, by changing a few lines of DEW.  Our goal was to capture only the
necessary topology details in the form of constraints the behavior must
place on resources.

## Structured representation

We wanted to impose some natural structure on DEW, enabling researchers to
easily locate and focus on the important pieces for their goal(s).  This
structure should facilitate experiment design and running, which are aligned
with human cognitive process.

# Installing

You'll need:
	- Python (either 2.x or 3.x)
	- pyparsing
	- networkx 2+
	- Enum
	- numpy

Optionally you'll also want:
	- spaCy (for Natural Language Processing)
	- spaCy english model (en)
	- CEFTB Xir description language (for constraint processing
	and saving experiment descriptions)

See the readme in the Constraints directory for setting up and using the
constraint server. 

For spaCY install and model install instructions see:
	https://spacy.io/usage/
	https://spacy.io/usage/models

For installing Xir see:
	https://github.com/ceftb/xir
	https://github.com/ceftb/xir/tree/master/lang/python

# Running

To run the GUI: % python dew_gui.py

# Organization

You can find the BNF notation of DEW in BNF folder.

Folder UI has our UI implementation

Folder translators will house translators from other representations into DEW


