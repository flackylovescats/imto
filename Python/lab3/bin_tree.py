def gen_bin_tree(height=4, root=3):
    """
    A function that recursively generates a binary tree structure as nested dictionaries.

    Parameters
    ----------
    height : int
        The desired depth of the binary tree
    root : int
        Number for the root node

    Returns
    -------
    The binary tree represented as nested dictionaries.
    """
    tree = {"root": root}
    if height > 1:
        tree["left"] = gen_bin_tree(height - 1, root + 2)
        tree["right"] = gen_bin_tree(height - 1, root * 3)
    return tree

if __name__ == "__main__":
    print(gen_bin_tree())