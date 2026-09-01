class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total = len(litter)

        if total == 0:
            return 0

        full_mask = (1 << total) - 1

        q = deque()
        q.append((start[0], start[1], energy, full_mask, 0))

        visited = set()
        visited.add((start[0], start[1], energy, full_mask))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == 0:
                return moves

            if e == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = e - 1

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                new_mask = mask

                if classroom[nr][nc] == 'L':
                    index = litter[(nr, nc)]
                    new_mask = mask & ~(1 << index)

                state = (nr, nc, new_energy, new_mask)

                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, new_energy, new_mask, moves + 1))

        return -1
        