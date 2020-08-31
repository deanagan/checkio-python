# Welcome to the GridLand. All the citizens here are connected through the global internal network because the main way for communication here is via
# email. Every new district of the city starts with building a node – center of the district. All citizens are connected to this node in order to send
# and receive emails. All nodes of GridLand are connected so one node can send emails between the connected nodes. In such a way, no matter how big
# the
# city is all users can send messages to each other as long as all of the nodes are connected.

# The Mayor of GridLand is using this network to quickly send emergency emails to all citizens when necessary. But the system is not perfect. When one
# of city nodes gets crushed it may leave the citizens of this node district disconnected from these emergency emails. It may also leave districts
# around the crushed node disconnected if their nodes do not have other ways to connect. To resolve this occurrence, the Mayor uses mail-pigeons – an
# old method of sending mail that was invented before the global internal network. All of the citizens still connected to the network receive the
# emergency emails, but the disconnected citizens receive their messages from these pigeons.

# Your mission is to figure out how many pigeons you need when some of the nodes are crushed.

# Input: Four arguments: network structure (as a list of connections between the nodes), users of each node (as dict where keys are the node-names and
# user_counts are the amounts of users), name of the node that sends email, and the list of crashed nodes.

# Output: Int. The amount of users that won't receive an email.


import pytest
from disconnected_users import disconnected_users


def test_disconnectedusers():
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    assert disconnected_users([
        ["A", "B"],
        ["B", "C"],
        ["C", "D"]
    ], {
        "A": 10,
        "B": 20,
        "C": 30,
        "D": 40
    },
        'A', ['A']) == 100, "Nobody will get a mesage if node that sends emails is crushed"
