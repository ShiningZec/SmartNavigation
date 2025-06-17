__author__ = 'ShiningZec'

from app import ui

import json
import os

DEFAULT_PATH_NODES = 'data/ECNU-nodes.csv'
DEFAULT_PATH_EDGES = 'data/ECNU-edges.csv'


def main():
    config_file = 'config.json'
    if not os.path.exists(config_file):
        print(f"Config file {config_file} does not exist, exit.")
        return

    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    use_custom_file = config.get('use_custom_files', False)
    if use_custom_file:
        nodepath = config['custom_file_path'].get('node_file',
                                                  DEFAULT_PATH_NODES)
        edgepath = config['custom_file_path'].get('edge_file',
                                                  DEFAULT_PATH_EDGES)
    else:
        nodepath = DEFAULT_PATH_NODES
        edgepath = DEFAULT_PATH_EDGES

    app = ui.SmartNavigationApp(nodepath, edgepath)
    app.mainloop()


if __name__ == "__main__":
    main()
