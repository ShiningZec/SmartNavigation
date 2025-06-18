__author__ = 'ShiningZec'

import csv  # for csv handling
import itertools  # for faster itering
import random  # for random distance generation
from typing import Any, Dict, List, Optional, Tuple

import networkx as nx  # core util


class GraphManager:

    def __init__(
            self,
            nodes: Optional[List[Tuple[
                Any, Any, int]]] = None,  # (node, node_type, time)
            edges: Optional[List[Tuple[Any, Any,
                                       int]]] = None,  # (u, v, distance)
            ratio: int = 1,
            use_time_weight: bool = False):
        """
        初始化图对象，并添加节点和边。
        节点必须是 (node, node_type, time) 三元组。
        边必须是 (u, v, distance) 三元组。
        """
        self.graph = nx.Graph()
        self.ratio = ratio
        self.use_time_weight = use_time_weight

        # handle nodes
        if nodes is not None:
            for node_info in nodes:
                if len(node_info) != 3:
                    raise ValueError(
                        "A node must contain attr: (node, node_type, time)")
                else:
                    node, node_type, time = node_info
                self.graph.add_node(node, node_type=node_type, time=time)

        # handle edges
        if edges is not None:
            for edge in edges:
                if len(edge) != 3:
                    raise ValueError(
                        "An edge must contain attr: (u, v, distance)")
                u, v, distance = edge
                self.graph.add_edge(u, v, distance=distance)

    def add_node(self, node: Any, node_type: Any, time: int):
        if node is not None and node_type is not None and time is not None:
            self.graph.add_node(node, node_type=node_type, time=time)

    def add_nodes(self, nodes: Optional[List[Tuple[Any, Any, int]]]):
        if nodes is not None:
            for node_info in nodes:
                node, node_type1, time1 = node_info
                self.graph.add_node(node, node_type=node_type1, time=time1)

    def get_node(self, name: str | None = None) -> List[str]:
        """
        通过子串匹配返回所有与 name 匹配的节点，以及它们的 node_type 和 time 属性。

        Args:
            name (str | None): 需要匹配的子串。

        Returns:
            List[Tuple[node, node_type, time]]
        """
        if name is None:
            result = []
            for node, data in self.graph.nodes(data=True):
                node_type = data.get('node_type', '<no_type>')
                time = data.get('time', 0)
                result.append(f"{node} [{node_type}]: {time}")
            return result

        result = []
        for node, data in self.graph.nodes(data=True):
            if name in str(node):
                node_type = data.get('node_type', None)
                time = data.get('time', 0)
                result.append(f"{node} [{node_type}]: {time}")
        return result

    def get_nodes_by_node_type(self, node_type_in: Any) -> List[str]:
        result = []
        for node, data in self.graph.nodes(data=True):
            node_type = data.get('node_type', None)
            time = data.get('time', 0)
            if node_type_in in node_type:
                result.append(f"{node} [{node_type}]: {time}")
        return result

    def set_time_for_node(self, node: Any, time: int):
        if node in self.graph:
            self.graph[node]['time'] = time
        else:
            raise KeyError("No nodes with such name.")

    def set_dist_for_edge(self, source: Any, target: Any, dist: int):
        self.graph[source][target]['distance'] = dist

    def add_edge(self, source: Any, target: Any, distance: int):
        self.graph.add_edge(source, target, distance=int(distance))

    def add_edges(self, edges: Optional[List[Tuple[Any, Any, int]]]):
        if edges is not None:
            for edge in edges:
                source, target, distance = edge
                self.graph.add_edge(source, target, distance=int(distance))

    def get_all_edges(self) -> List[str]:
        rst = []
        edges = []
        for source in self.graph:
            for target in self.graph[source]:
                distance = self.graph[source][target]['distance']
                edges.append((source, target, distance))
        rst = [
            f"{e[0]} -> {e[1]}: {e[2]}"
            for e in sorted(edges, key=(lambda x: x[2]))
        ]
        return rst

    def get_edges_from_source(self, source: Any) -> List[str]:
        rst = []
        edges = []
        for target in self.graph[source]:
            distance = self.graph[source][target]['distance']
            edges.append((source, target, distance))
        rst = [
            f"{e[0]} -> {e[1]}: {e[2]}"
            for e in sorted(edges, key=(lambda x: x[2]))
        ]
        return rst

    def get_edge_data(self, source: Any, target: Any) -> int | None:
        return self.graph.get_edge_data(source, target, None)

    def remove_edge(self, source: Any, target: Any):
        self.graph.remove_edge(source, target)

    def remove_all_edges(self):
        self.graph.clear_edges()

    def remove_node(self, node: Any):
        self.graph.remove_node(node)

    def remove_all_nodes(self):
        self.graph.clear()

    def __str__(self):
        return self.graph.__str__()

    def __len__(self):
        return self.graph.__len__()

    def __repr__(self):
        return self.graph.__repr__()

    def __getitem__(self, key: Any):
        return self.graph.__getitem__(key)

    def set_ratio(self, new_ratio: int):
        self.ratio = new_ratio

    def get_ratio(self) -> int:
        return self.ratio

    def toggle_use_time_weight(self, flag: bool | None = None):
        """_summary_
        Toggle whether or not to calc time as weight.

        Args:
            flag (bool | None, optional): _description_ Set to or Change it.
            Defaults to None.
        """
        if flag is None:
            self.use_time_weight = not self.use_time_weight
        else:
            self.use_time_weight = flag

    def is_connected(self) -> bool:
        """
        判断全图连通性。
        """
        return nx.is_connected(self.graph)

    def connect_components(self):
        """
        如果图不连通，为每个连通分量之间添加一条随机正整数边。
        """
        if self.is_connected():
            return
        components = list(nx.connected_components(self.graph))
        for i in range(len(components) - 1):
            u = random.choice(list(components[i]))
            v = random.choice(list(components[i + 1]))
            random_distance = random.randint(1, 10)
            self.graph.add_edge(u, v, distance=random_distance)

    def has_eulerian_path(self) -> bool:
        if not nx.is_connected(self.graph):
            return False
        odd_degree_nodes = [
            node for node, degree in self.graph.degree() if degree % 2 == 1
        ]

        return len(odd_degree_nodes) <= 2

    def has_eulerian_circuit(self) -> bool:
        if not nx.is_connected(self.graph):
            return False
        for _, degree in self.graph.degree():
            if degree % 2 != 0:
                return False
        return True

    def _effective_distance(self, u: Any, v: Any) -> int:
        """
        计算在是否使用 time 权重时的边的有效距离。
        只有到达顶点 v 采用 time 权重作为距离。
        """
        edge_distance = self.graph[u][v]['distance']
        if self.use_time_weight:
            node_v_time = self.graph.nodes[v].get('time', 0)
            extra_time = node_v_time * self.ratio
            return edge_distance + extra_time
        return edge_distance

    def dijkstra(self, entrance: Any) -> Dict[Any, int]:
        """
        计算从 entrance 出发的最短距离。
        """

        def custom_weight(u, v, attrs):
            base_distance = attrs['distance']
            if self.use_time_weight:
                node_v_time = self.graph.nodes[v].get('time', 0)
                extra_time = node_v_time * self.ratio
                return base_distance + extra_time
            return base_distance

        lengths = nx.single_source_dijkstra_path_length(self.graph,
                                                        source=entrance,
                                                        weight=custom_weight)
        return {node: int(dist) for node, dist in lengths.items()}

    def minimum_spanning_tree(self) -> nx.Graph:
        """
        计算最小生成树，返回一个承载最小生成树的图。
        """
        if not self.is_connected():
            raise Exception('Not a connected graph.')

        mst = nx.minimum_spanning_tree(self.graph, weight='distance')
        return mst

    def find_shortest_path(self, start: Any,
                           end: Any) -> Tuple[List[Any], int]:
        """
        计算从 start 到 end 的最短路径及其总权值。

        :return:
            (path: List[Any], total_length: int)
        """
        try:
            path = nx.shortest_path(self.graph,
                                    source=start,
                                    target=end,
                                    weight='distance')
            total_length = self._calculate_path_length(path)
            return path, total_length
        except nx.NetworkXNoPath:
            print(f"Warning: No path between {start} and {end}.")
            return [], -1

    def find_path_approx_time(self, start: str, end: str,
                              target_time: int) -> List[Any]:
        """
        给定起点和终点，找到一条总时间（边距离+节点时间）最接近 target_time 的路径。
        这里使用 DFS+剪枝（只选取简单路径）做启发式搜索。
        """
        best_path = []
        best_diff = 1_152_921_504_606_846_976

        def dfs(node, path, visited, current_time):
            nonlocal best_path, best_diff

            if node == end:
                diff = abs(current_time - target_time)
                if diff < best_diff:
                    best_diff = diff
                    best_path = [str(node1) for node1 in path]
                return

            for neighbor in self.graph.neighbors(node):
                if neighbor in visited:
                    continue
                edge_data = self.graph.get_edge_data(node, neighbor)
                distance = edge_data.get('distance', 0)

                node_time = self.graph.nodes[neighbor].get(
                    'time', 0) * self.ratio if self.use_time_weight else 0
                next_time = current_time + distance + node_time

                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, path, visited, next_time)
                path.pop()
                visited.remove(neighbor)

        node_time_start = self.graph.nodes[start].get(
            'time', 0) * self.ratio if self.use_time_weight else 0
        dfs(start, [start], set([start]), node_time_start)

        return best_path

    def find_path_with_all_type(self, start: str, node_type: str) -> list:
        """
        从 start 出发，经过所有目标类型的节点（只经过一次），的最短路径。
        """
        # 目标节点集合
        type_nodes = [
            n for n, d in self.graph.nodes(data=True)
            if d.get('node_type') == node_type
        ]
        if start not in type_nodes:
            type_nodes.insert(0, start)
        else:
            type_nodes = [start] + [n for n in type_nodes if n != start]

        # 计算目标节点之间的最短路径长度（Dijkstra）
        pairwise_distances = {}
        pairwise_paths = {}
        for u, v in itertools.combinations(type_nodes, 2):
            try:
                path = nx.shortest_path(self.graph,
                                        source=u,
                                        target=v,
                                        weight=self._get_weight_key())
                length = self._calculate_path_length(path)
                pairwise_distances[(u, v)] = length
                pairwise_distances[(v, u)] = length
                pairwise_paths[(u, v)] = path
                pairwise_paths[(v, u)] = list(reversed(path))
            except nx.NetworkXNoPath:
                continue  # 如果无法到达，跳过

        # 穷举
        best_length = 1_152_921_504_606_846_976
        best_order = []

        permutations = itertools.permutations(type_nodes[1:])  # start点固定
        for perm in permutations:
            route = [start] + list(perm)
            total_length = 0
            for i in range(len(route) - 1):
                u, v = route[i], route[i + 1]
                dist = pairwise_distances.get((u, v),
                                              1_152_921_504_606_846_976)
                total_length += dist
            if total_length < best_length:
                best_length = total_length
                best_order = route

        # connect path
        full_path = []
        for i in range(len(best_order) - 1):
            u, v = best_order[i], best_order[i + 1]
            sub_path = pairwise_paths.get((u, v))
            if sub_path:
                if full_path and full_path[-1] == sub_path[0]:
                    full_path.extend(str(node1) for node1 in sub_path[1:])
                else:
                    full_path.extend(str(node2) for node2 in sub_path)
            else:
                assert False, 'This should not happen'  # This won't happen

        return full_path

    def _calculate_path_length(self, path: List[Any]) -> int:
        total_length = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            edge_data = self.graph.get_edge_data(u, v)
            distance = edge_data.get('distance', 0)
            u_time = self.graph.nodes[u].get(
                'time', 0) * self.ratio if self.use_time_weight else 0
            v_time = self.graph.nodes[v].get(
                'time', 0) * self.ratio if self.use_time_weight else 0
            total_length += distance + (u_time + v_time) // 2
        return total_length

    def _get_weight_key(self):
        # 方便切换 time/ratio 权重
        return lambda u, v, d: d.get('distance', 0) + ((
            (self.graph.nodes[u].get('time', 0) + self.graph.nodes[v].get(
                'time', 0)) * self.ratio // 2) if self.use_time_weight else 0)

    def find_path_covering_type(self, node_type: str) -> Tuple[List[Any]]:
        """
        找到一条路径，覆盖所有 node_type == 指定类型的节点。
        忽略节点 time，仅考虑边 distance。
        返回该路径的节点顺序。
        """
        import itertools

        # Step 1: 获取目标节点
        target_nodes = [
            node for node, data in self.graph.nodes(data=True)
            if data.get('node_type') == node_type
        ]
        if not target_nodes:
            return []

        # Step 2: 构造最短路径完全图（目标节点之间）
        complete_graph = nx.Graph()
        shortest_paths = dict()
        weight_key = self._get_weight_key()

        for u, v in itertools.combinations(target_nodes, 2):
            try:
                length, path = nx.single_source_dijkstra(self.graph,
                                                         u,
                                                         v,
                                                         weight=weight_key)
                complete_graph.add_edge(u, v, weight=length)
                shortest_paths[(u, v)] = path
                shortest_paths[(v, u)] = path[::-1]  # 用于反向还原
            except nx.NetworkXNoPath:
                continue

        # Step 3: 对完全图构造MST
        mst = nx.minimum_spanning_tree(complete_graph)

        # Step 4: 把MST边转换为原图路径
        final_path = []
        visited = set()

        def dfs(u):
            nonlocal final_path, visited

            visited.add(u)
            final_path.append(u)
            for v in mst.neighbors(u):
                if v not in visited:
                    path_uv = shortest_paths[(u, v)]
                    final_path.extend(path_uv[1:len(path_uv) - 1])  # 避免重复 u, v
                    dfs(v)

        start_node = target_nodes[0]
        dfs(start_node)

        return [node for node in final_path if node in mst], final_path


def read_graph(node_csv: str, edge_csv: str) -> GraphManager:
    """
    从 CSV 文件中读取节点和边信息，并生成 GraphManager。

    :param node_csv: 节点 CSV 文件路径，每行格式: nodename, nodetype, time
    :param edge_csv: 边 CSV 文件路径，每行格式: start, end, distance
    :return: GraphManager 对象
    """
    nodes: List[Tuple[str, int]] = []
    with open(node_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                name = row[0].strip()
                name_type = row[1].strip()
                time = int(row[2].strip())
                nodes.append((name, name_type, time))
            except Exception:
                ...

    edges: List[Tuple[str, str, int]] = []
    with open(edge_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                u = row[0].strip()
                v = row[1].strip()
                distance = (int)(row[2].strip())
                edges.append((u, v, distance))
            except Exception:
                ...

    return GraphManager(nodes=nodes, edges=edges)
