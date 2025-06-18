__author__ = 'ShiningZec'

WELC_DOC = """Welcome to Smart Navigation.

Enter "help" to get helps.
Enter "tutor" to get started.
Enter "load -d" to load graph from default.

Wish you have a nice day.
"""

HELP_DOC = """Help: get-help\t alias: ?, help

Usage:
get-help [<function>]

Example:
get-help get-alias

Function:
get-alias, load-graph, display,
add-node, del-node, query-nodedata, set-nodetime,
query-edge, add-edge, del-edge, set-edgeDist,
judge-connectivity, connect-component, judge-eularpath,
get-shortestPath, get-mst, find-tour

"""

TUTOR_DOC = """Tutorial

Some functions(alias) you may want to know about:
load -d\t load nodes and edges from default files
dis\t decides which position to display
qn\t query node data
qe\t query edge data
jc -a\t judge connectivity, and connect components
je -p\t judge eular path existence
gsp sourcery targeted\t get shortest path from sourcery to targeted ndoe
gmst\t generate minimal spanning tree
f-tour yourtype\t find tour passing by all nodes with yourtype

"""

HELP_ALIAS = """Help: get-alias\t alias: alias

Usage: get-alias [<function>]

Example:
get-alias load-graph

get-alias load

"""

HELP_DIS = """Help: display\t alias: dis, show

Decides where to display the value.

Usage: display [position_tag] <display>

position_tag: [cli | main | sub]

Examples:
display-graph cli get-alias load

display-graph main query-node my_node

display-graph sub query-edge -a

"""

HELP_LOAD = """Help: load

Usage: load [[-d] | [-n <file_path>][-e <file_path>]]

\t -d\t\t load from default path(customized in config.json)
\t -n, --nodes\t load nodes from "file_path"(.csv file)
\t -e, --edges\t load edges from "file_path"(.csv file)

Examples:
load\t\t load from default path

load -d\t\t load from default path

load -n <node_path> -e <edge_path>
\t\t load nodes from node_path and edges from edge_path

"""

HELP_EXIT = """! exit:

Do not enter "exit", but press down key-bind <Control-d> to exit cli.
"""

HELP_QUERY_NODE = """Help: query-nodedata\t alias: qn

Usage: query-nodedata [-a | [-n <node_name>] | [-t <node_type>]]

\t -a\t\t get data from all nodes
\t -n, --name\t get data from all node with the name
\t -t, --type\t get data from all node with the type

Examples:
query-nodedata -a
query-nodedata -n my_node

query-nodedata -t my_type

"""

HELP_ADD_NODE = """Help: add-node\t alias: an, in

Usage: add-node <node_name> <node_type> <node_time>

Examples:
add-node my_node my_type 5

"""

HELP_DEL_NODE = """Help: del-node\t alias: dn

Usage: del-node [-a | [<node_name>]]

\t -a\t\t remove all nodes from graph
\t <node_name>\t remove the targeted node

Examples:
del-node -a

del-node my_node

"""

HELP_SET_NODE_TIME = """Help: set-nodeTime\t alias: sn, setnode

Usage: set-nodeTime <node_name> <time>

Examples:
set-nodeTime my_node 5

sn my_node 5

"""

HELP_QUERY_EDGE = """Help: query-edge\t alias: qe

Usage: query-edge [-a | -n <node_name>]

\t -a\t\t show all edges(rising, according distance)
\t -n, --node\t show all edges adj-ed to the node

Examples:
query-edge -a

query-edge -n my_node

"""

HELP_ADD_EDGE = """Help: add-edge\t alias: ae, ie

Usage: add-edge <source_node> <target_node> <distance>

Note:
A new node will be created if insert node does not exist.

Example:
add-edge my_node1 my_node2 10

"""

HELP_DEL_EDGE = """Help: del-edge\t alias: de

Usage: del-edge [-a | [-e <source_node> <target_node>]]

\t -a\t\t will remove all edges from the graph(will leave nodes there)
\t -e, --edge\t will remove that edge

Example:
del-edge -a

del-edge -e my_node1 my_node2

"""

HELP_SET_EDGE_DIST = """Help: set-edgeDist\t alias: se, setedge

Usage: set-edgeDist <source_node> <target_node> <distance>

Example:
set-edgeDist my_node1 my_node2 10

"""

HELP_J_CONNECT = """Help: judge-connectivity\t alias: jc, j-connect

Usage: judge-connectivity [-a]

\t -a\t would additionally append edges to connect all components

Example:
judge-connectivity

judge-connectivity -a

"""

HELP_CONNECT_COMPONENT = """Help: connect-component\t alias: cc, c-comp

Example:
connect-component\t append edges to connent all components

"""

HELP_J_EULERIANPATH = """Help: judge-eulerianPath\t alias: je, j-euler

Usage: judge-eularpath [-c | -p]

\t -c\t judge existence of eularian-curcuit
\t -p\t judge existence of eularian-path

Example:
judge-eularpath -c

judge-eularpath -p

"""

HELP_G_S_PATH = """Help: get-shortestPath\t alias: gsp

Usage: get-shortestPath <source_node> <target_node>

Example:
get-shortestPath my_node1 my_node2

"""

HELP_G_MST = """Help: get-mst\t alias: gmst

Example:
get-mst\t will display the minimum spanning tree

"""

# HELP_F_APPROX = """Help: find-pathApproxTime\t alias: f-approx

# Usage: find-pathApproxTime <source_node> <target_node> <time>

# Example:
# find-pathApproxTime my_node1 my_node2 500

# """

HELP_F_TOUR = """Help: find-tour\t alias: f-tour

Usage: find-tour <node_type>

Example:
find-tour my_type

"""

functions = {
    "get-help", "?", "help", "tutorial", "get-alias", "alias", "load-graph",
    "load", "display", "dis", "show", "add-node", "an", "in", "del-node", "dn",
    "query-nodedata", "qn", "set-nodetime", "sn", "setnode", "query-edge",
    "qe", "add-edge", "ae", "ie", "del-edge", "de", "set-edgeDist", "se",
    "setedge", "judge-connectivity", "jc", "j-connect", "connect-component",
    "cc", "c-comp", "judge-eularpath", "je", "j-eular", "get-shortestPath",
    "gsp", "get-mst", "gmst", "find-tour", "f-tour"
}

help_func = {
    "get-help": HELP_DOC,
    "?": HELP_DOC,
    "help": HELP_DOC,
    "tutorial": TUTOR_DOC,
    "tutor": TUTOR_DOC,
    "get-alias": HELP_ALIAS,
    "alias": HELP_ALIAS,
    "load-graph": HELP_LOAD,
    "load": HELP_LOAD,
    "display": HELP_DIS,
    "dis": HELP_DIS,
    "show": HELP_DIS,
    "query-nodedata": HELP_QUERY_NODE,
    "qn": HELP_QUERY_NODE,
    "add-node": HELP_ADD_NODE,
    "an": HELP_ADD_NODE,
    "in": HELP_ADD_NODE,
    "del-node": HELP_DEL_NODE,
    "dn": HELP_DEL_NODE,
    "set-nodeTime": HELP_SET_NODE_TIME,
    "sn": HELP_SET_NODE_TIME,
    "setnode": HELP_SET_NODE_TIME,
    "query-edge": HELP_QUERY_EDGE,
    "qe": HELP_QUERY_EDGE,
    "add-edge": HELP_ADD_EDGE,
    "ae": HELP_ADD_EDGE,
    "ie": HELP_ADD_EDGE,
    "del-edge": HELP_DEL_EDGE,
    "de": HELP_DEL_EDGE,
    "set-edgeDist": HELP_SET_EDGE_DIST,
    "se": HELP_SET_EDGE_DIST,
    "setedge": HELP_SET_EDGE_DIST,
    "judge-connectivity": HELP_J_CONNECT,
    "jc": HELP_J_CONNECT,
    "j-connect": HELP_J_CONNECT,
    "connect-component": HELP_CONNECT_COMPONENT,
    "cc": HELP_CONNECT_COMPONENT,
    "c-comp": HELP_CONNECT_COMPONENT,
    "judge-eulerianpath": HELP_J_EULERIANPATH,
    "je": HELP_J_EULERIANPATH,
    "j-euler": HELP_J_EULERIANPATH,
    "get-shortestPath": HELP_G_S_PATH,
    "gsp": HELP_G_S_PATH,
    "get-mst": HELP_G_MST,
    "gmst": HELP_G_MST,
    # "find-pathApproxTime": HELP_F_APPROX,
    # "f-approx": HELP_F_APPROX,
    "find-tour": HELP_F_TOUR,
    "f-tour": HELP_F_TOUR
}
