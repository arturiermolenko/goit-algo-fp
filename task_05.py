from collections import deque

import matplotlib.pyplot as plt

from task_04 import draw_tree, build_heap_tree


def generate_color(index, total_nodes):
    intensity = int(255 * (index / total_nodes))
    return "#{:02x}{:02x}ff".format(intensity, intensity)


def bfs_visualization(root):
    if root is None:
        return

    queue = deque([root])
    visited = set()
    position = 0
    total_nodes = count_nodes(root)

    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            node.color = generate_color(position, total_nodes)
            position += 1
            draw_tree(root)
            plt.pause(1)  # Pause to visualize each step

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def dfs_visualization(root):
    if root is None:
        return

    stack = [root]
    visited = set()
    position = 0
    total_nodes = count_nodes(root)

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            node.color = generate_color(position, total_nodes)
            position += 1
            draw_tree(root)
            plt.pause(1)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    heap_array = [0, 4, 1, 5, 10, 3]
    heap_root = build_heap_tree(heap_array)
    bfs_visualization(heap_root)

    heap_root = build_heap_tree(heap_array)
    dfs_visualization(heap_root)
