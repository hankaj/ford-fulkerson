# Ford-Fulkerson

This is an implementation of [Ford-Fulkerson algorithm (FFA)](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm). FFA is a greedy algorithm used to compute the maximum flow of a flow network.


# Input file format

To compute the maximum flow in your network, describe the network in the following format and save it to a JSON file:

```
[
    source_node_id,
    sink_node_id,
    total_number_of_nodes,
    [
        [start_node_id, end_node_id, capacity],
        [start_node_id, end_node_id, capacity],
        ...
    ]
]
```

- Each `node_id` must be an integer from 0 (inclusive) to `total_number_of_nodes` (exclusive).
- Each `[start_node_id, end_node_id, capacity]` describes a directed edge with the maximum flow along this edge.

[Example of a valid input file](test_data.json)


# Usage

Clone this repository.

```
git clone https://github.com/hankaj/ford-fulkerson.git
```

Run the script and follow the instructions on the screen.

```
python main.py
```

To run the example, answer with the path to the test file.

```
Insert file path:
test_data.json
```

The script will print out the maximum flow of your flow network.
