from graphviz import Digraph


def jk(q: bool, j: bool, k: bool) -> bool:
    if j and k:
        return not q
    if j:
        return True
    if k:
        return False
    return q


def get_next(q: tuple[bool]) -> tuple[bool]:
    q3, q2, q1, q0 = q
    j0 = True
    k0 = True
    j1 = (not q0) or ((not q3) and (not q2))
    k1 = not q0
    j2 = (not q1) and (not q0)
    k2 = (not q1) and (not q0)
    j3 = (not q2) and (not q1)
    k3 = ((not q1) and (not q0)) or (q3 and q2)
    return (jk(q3, j3, k3), jk(q2, j2, k2), jk(q1, j1, k1), jk(q0, j0, k0))


def from_str(s: str) -> tuple[bool]:
    return tuple(map(bool, map(int, list(s))))


def to_str(q: tuple[bool]) -> str:
    return ''.join(map(str, map(int, q)))


if __name__ == '__main__':
    g = Digraph()
    for i in range(1 << 4):
        q = bin(i)[2:].zfill(4)
        g.edge(q, to_str(get_next(from_str(q))))
    g.render(format='png', view=True, engine='circo')
