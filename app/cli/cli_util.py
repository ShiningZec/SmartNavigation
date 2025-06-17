__author__ = 'ShiningZec'

from .cli_doc import HELP_DOC, TUTOR_DOC, HELP_EXIT, help_func
from core.graph_util import GraphManager, read_graph

import shlex
from typing import List


class Cli:

    def __init__(self, node_file, edge_file):
        self.graph = None
        self.nodepath = node_file
        self.edgepath = edge_file

    def execute_command(self, command: str) -> List[str | None]:
        # 这里可以使用 shlex 解析命令

        tokens = shlex.split(command)
        if not tokens:
            return ["""\n""", None, None]

        func = tokens[0].lower()
        for _ in range(3):
            tokens.append(None)

        if func in {"display", "show", "dis"}:
            return self.showit(tokens[1:])
        elif func in {"help", "get-help", "?"}:
            return [self.helpit(tokens[1:]), None, None]
        elif func == "exit":
            return [HELP_EXIT, None, None]
        elif func in {"gsp", "get-shortestpath"}:
            return self.gsp(tokens[1:])
        elif func in {"get-mst", "gmst"}:
            return self.gmst(tokens[1:])
        elif func in {"find-tour", "f-tour"}:
            return self.ftour(tokens[1:])
        else:
            return [self._subfunc(tokens), None, None]

    def _subfunc(self, args: List[str]) -> str:
        func = args[0]

        if func is None:
            return """\n"""
        elif func in {"tutor", "tutorial"}:
            return TUTOR_DOC
        elif func in {"display", "show", "dis"}:
            raise Exception("Error: No Recurssion Use of Display.")
        elif func in {"get-help", "?", "help"}:
            return self.helpit(args[1:])
        elif func in {"get-alias", "alias"}:
            return self.alias(args[1:])
        elif func == "load":
            return self.load(args[1:])
        elif func in {"query-node", "qn"}:
            return self.querynode(args[1:])
        elif func in {"add-node", "an", "in"}:
            return self.addnode(args[1:])
        elif func in {"del-node", "dn"}:
            return self.delnode(args[1:])
        elif func in {"set-nodetime", "sn", "setnode"}:
            return self.setnode(args[1:])
        elif func in {"query-edge", "qe"}:
            return self.queryedge(args[1:])
        elif func in {"add-edge", "ae", "ie"}:
            return self.addedge(args[1:])
        elif func in {"del-edge", "de"}:
            return self.deledge(args[1:])
        elif func in {"set-edgedist", "se", "setedge"}:
            return self.setedge(args[1:])
        elif func in {"judge-connectivity", "jc", "j-connect"}:
            return self.jconnect(args[1:])
        elif func in {"connect-component", "cc", "c-comp"}:
            return self.ccomp(args[1:])
        elif func in {"judge-eulerianpath", "je", "j-eulerian"}:
            return self.jeuler(args[1:])
        elif func in {"get-shortestpath", "gsp"}:
            raise Exception("Error: Donot call gsp after dis")
        elif func in {"get-mst", "gmst"}:
            raise Exception("Error: Donot call gmst after dis")
        # elif func in {"find-pathapproxtime", "f-approx"}:
        #     return self.fapprox(args[1:])
        elif func in {"find-tour", "f-tour"}:
            raise Exception("Error: Donot call f-tour after dis")
        else:
            return f"Unknown function: {func}"

    def showit(self, args: List[str]) -> List[str]:
        if not args:
            return [help_func['show'], None, None]
        try:
            for _ in range(3):
                args.append(None)
            if args[0] is None:
                return ["""\n""", None, None]
            if args[0] == "cli":
                return [self._subfunc(args[1:]), None, None]
            elif args[0] == "main":
                return [None, self._subfunc(args[1:]), None]
            elif args[0] == "sub":
                return [None, None, self._subfunc(args[1:])]
            else:
                return ["""Error: Bad Output Position""", None, None]
        except Exception:
            return ["""Error: Bad Command""", None, None]

    def helpit(self, args: List[str]) -> List[str]:
        if not args:
            return HELP_DOC
        elif args[0] is None:
            return HELP_DOC
        else:
            return help_func.get(args[0].lower(),
                                 """Error: No such function""")

    def alias(self, args: List[str]) -> str:
        func = args[0]

        if func is None:
            raise Exception("Error: Bad Input")
        elif func in {"tutor", "tutorial"}:
            return """Alias: tutorial: tutor"""
        elif func in {"display", "show", "dis"}:
            return """Alias: display: dis, show"""
        elif func in {"get-help", "?", "help"}:
            return """Alias: get-help: ?, help"""
        elif func in {"get-alias", "alias"}:
            return """Alias: get-alias: alias"""
        elif func in {"query-node", "qn"}:
            return """Alias: query-node: qn"""
        elif func in {"add-node", "an", "in"}:
            return """Alias: add-node: an, in"""
        elif func in {"del-node", "dn"}:
            return """Alias: del-node: dn"""
        elif func in {"set-nodetime", "sn", "setnode"}:
            return """Alias: set-nodeTime: sn, setnode"""
        elif func in {"query-edge", "qe"}:
            return """Alias: query-edge: qn"""
        elif func in {"add-edge", "ae", "ie"}:
            return """Alias: add-edge: ae, ie"""
        elif func in {"del-edge", "de"}:
            return """Alias: del-edge: de"""
        elif func in {"set-edgedist", "se", "setedge"}:
            return """Alias: set-edgeDist: se, setedge"""
        elif func in {"judge-connectivity", "jc", "j-connect"}:
            return """Alias: judge-connectivity: jc, j-connect"""
        elif func in {"connect-component", "cc", "c-comp"}:
            return """Alias: connect-component: cc, c-comp"""
        elif func in {"judge-eulerianpath", "je", "j-eulerian"}:
            return """Alias: judge-eulerianpath: je, j-eulerian"""
        elif func in {"get-shortestpath", "gsp"}:
            return """Alias: get-shortestPath: gsp"""
        elif func in {"get-mst", "gmst"}:
            return """Alias: get-mst: gmst"""
        # elif func in {"find-pathapproxtime", "f-approx"}:
        #     return """Alias: find-pathApproxTime: f-approx"""
        elif func in {"find-tour", "f-tour"}:
            return """Alias: find-tour: f-tour"""
        else:
            return f"Alias: No such alias or no such function: {func}"

    def load(self, args: List[str]) -> str:
        if not args:
            self.graph = GraphManager()
            return """Loaded successfully a void graph"""
        elif args[0] is None:
            self.graph = GraphManager()
            return """Loaded successfully a void graph"""
        elif args[0].lower() == "-d":
            self.graph = read_graph(self.nodepath, self.edgepath)
        else:
            node_file = self.nodepath
            edge_file = self.edgepath
            try:
                for i in range(len(args)):
                    if args[i].lower() in {"-n", "--nodes"}:
                        if args[i + 1] is not None:
                            node_file = args[i + 1]
                    elif args[i].lower() in {"-e", "--edges"}:
                        if args[i + 1] is not None:
                            edge_file = args[i + 1]
            except Exception:
                return """Failed to load files"""
            self.graph = read_graph(node_file, edge_file)
            return f"Loaded successfully with file {node_file} and {edge_file}"

        return """Loaded successfully with default files"""

    def querynode(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded"""

        if args is None:
            rst = self.graph.get_node(None)
        elif args[0] is None:
            rst = self.graph.get_node(None)
        elif args[0].lower() == '-a':
            rst = self.graph.get_node(None)
        elif len(args) < 2:
            return """Error: Missing Arguments"""
        elif args[0].lower() in {'-n', "--name"}:
            rst = self.graph.get_node(args[1])
        elif args[0].lower() in {'-t', "--type"}:
            rst = self.graph.get_nodes_by_node_type(args[1])
        else:
            return "Error: Bad Arguments"

        if len(rst) == 0:
            return """No nodes"""
        else:
            return "\n".join(rst)

    def addnode(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """Error: No arguments."""
        elif len(args) < 3:
            return """Error: Missing Arguments"""
        else:
            try:
                self.graph.add_node(args[0].strip(), args[1].strip(),
                                    int(args[2]))
            except Exception:
                return """Error: Failed to add the node"""
            return f"Added node {args[0]} Successfully"

    def delnode(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """Error: No arguments."""
        elif args[0] is None:
            return """Error: No arguments."""
        elif args[0].lower() == '-a':
            self.graph.remove_all_nodes(None)
            return """Removed all nodes successfully"""
        else:
            self.graph.remove_node(args[0].strip())

        return f"Removed node {args[0]} successfully"

    def setnode(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """Error: No arguments."""
        elif len(args) < 2:
            return """Error: Missing Arguments"""
        else:
            try:
                self.graph.set_time_for_node(args[0], int(args[1]))
            except Exception:
                return """Failed to set node time"""

        return """Set node time successfully"""

    def queryedge(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded"""

        if not args:
            rst = self.graph.get_all_edges()
        elif args[0] is None:
            rst = self.graph.get_all_edges()
        elif args[0].lower() == '-a':
            rst = self.graph.get_all_edges()
        elif len(args) < 2:
            return """Error: Missing Arguments"""
        elif args[0].lower() in {'-n', "--name"}:
            rst = self.graph.get_edges_from_source(args[1])
        else:
            return """Error: Bad Option"""

        if len(rst) == 0:
            return """No edges"""
        else:
            return "\n".join(rst)

    def addedge(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """Error: No arguments."""
        elif len(args) < 3:
            return """Error: Missing Arguments"""
        else:
            try:
                self.graph.add_edge(args[0].strip(), args[1].strip(),
                                    int(args[2].strip()))
            except Exception:
                return """Error: Failed to add the edge"""
        return f"Added edge from {args[0]} to {args[1]} Successfully"

    def deledge(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """Error: No arguments."""
        elif args[0].lower() == '-a':
            self.graph.remove_all_edges(None)
            return """Removed edge(s) successfully"""
        elif len(args) < 2:
            return """Error: Missing Arguments"""
        else:
            self.graph.remove_edge(args[0].strip(), args[1].strip())
            return f"Removed edge from {args[0]} to {args[1]} successfully"

    def setedge(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """Error: No arguments."""
        elif len(args) < 3:
            return """Error: Missing Arguments"""
        else:
            try:
                self.graph.set_dist_for_edge(args[0], args[1], int(args[2]))
            except Exception:
                return """Failed to set edge dist"""

        return """Set edge dist successfully"""

    def jconnect(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """True""" if self.graph.is_connected() else """False"""
        elif args[0] is None:
            return """True""" if self.graph.is_connected() else """False"""
        else:
            if self.graph.is_connected():
                return """The graph is already connected"""
            else:
                self.graph.connect_components()
                return """Edges have been appended to connect the graph"""

    def ccomp(self, args: List[str]) -> str:
        if self.graph is None:
            return """Error: Graph not loaded."""

        if self.graph.is_connected():
            return """The graph is already connected"""
        else:
            self.graph.connect_components()
            return """Edges have been appended to connect the graph"""

    def jeuler(self, args: List[str]) -> str:
        graph = self.graph
        if graph is None:
            return """Error: Graph not loaded."""

        if not args:
            return """Has eulerian curcuit""" if graph.has_eulerian_circuit(
            ) else """No eulerian curcuits"""
        elif args[0] is None:
            return """Has eulerian curcuit""" if graph.has_eulerian_circuit(
            ) else """No eulerian curcuits"""
        elif args[0] == '-c':
            return """Has eulerian curcuit""" if graph.has_eulerian_circuit(
            ) else """No eulerian curcuits"""
        elif args[0] == '-p':
            return """Has eulerian path""" if graph.has_eulerian_path(
            ) else """No eulerian path"""
        else:
            return """Error: Bad Option"""

    def gsp(self, args: List[str]) -> List[str]:
        if self.graph is None:
            return ["""Error: Graph not loaded.""", None, None]

        if not args:
            return ["""Error: No Arguments""", None, None]
        elif len(args) < 2:
            return ["""Error: Missing Arguments""", None, None]
        else:
            r1, r2 = self.graph.find_shortest_path(args[0], args[1])
            return ["Distance: " + str(r2), "\n-> ".join(r1), None]

    def gmst(self, args: List[str]) -> List[str]:
        if self.graph is None:
            return ["""Error: Graph not loaded.""", None, None]

        self.graph.toggle_use_time_weight()
        mst = self.graph.minimum_spanning_tree()
        self.graph.toggle_use_time_weight()

        power = 0
        nodes = []
        edges = []
        for node, data in mst.nodes(data=True):
            node_type = data.get('node_type', '<no_type>')
            time = data.get('time', 0)
            try:
                time = int(time)
            except ValueError:
                time = 0
            nodes.append((node, node_type, time))
            for target in mst[node]:
                dist = mst[node][target]['distance']
                power += dist
                edges.append((node, target, dist))

        rstnodes = [
            f"{n[0]} [{n[1]}]: {n[2]}"
            for n in sorted(nodes, key=(lambda x: x[2]))
        ]
        rstedges = [str(power // 2)]
        rstedges.extend(f"{e[0]} -> {e[1]}: {e[2]}"
                        for e in sorted(edges, key=(lambda x: x[2])))
        return [
            """Generated mst successfully""", "\n".join(rstnodes),
            "\n".join(rstedges)
        ]

    # def fapprox(self, args: List[str]) -> str:
    #     if self.graph is None:
    #         return """Error: Graph not loaded"""

    #     if not args:
    #         return """Error: No Arguments"""
    #     elif len(args) < 3:
    #         return """Error: Missing Arguments"""
    #     else:
    #         self.graph.toggle_use_time_weight()
    #         rst = self.graph.find_path_approx_time(args[0].strip(),
    #                                                args[1].strip(),
    #                                                int(args[2].strip()))
    #         self.graph.toggle_use_time_weight()
    #         return "\n-> ".join(rst)

    def ftour(self, args: List[str]) -> str:
        if self.graph is None:
            return ["""Error: Graph not loaded""", None, None]

        if not args:
            return ["""Error: No Arguments""", None, None]
        elif args[0] is None:
            return ["""Error: No Arguments""", None, None]
        elif not self.graph.is_connected():
            return ["""Error: graph not connected.""", None, None]
        else:
            rst1, rst2 = self.graph.find_path_covering_type(args[0].strip())
            result1 = ["Brief: "]
            result1.extend(str(node) for node in rst1)
            result2 = ["Detail: "]
            result2.extend(str(node) for node in rst2)

            return [
                """Find route successfully""", "\n-> ".join(result1),
                "\n-> ".join(result2)
            ]
