class Germany:
    def __init__(self, lst):
        self.lst = lst

    def h(self, n):
        H = {
            'Ulm':0,
            'Bassel':204,
            'Bayreuth':207,
            'Bern':247,
            'Frankfurt':215,
            'Innbruck':163,
            'Karlsruhe':137,
            'Landeck':143,
            'Linz':318,
            'Munchen':120,
            'Mannheim':164,
            'Memmingen':47,
            'Nurnberg':132,
            'Passau':257,
            'Rosenheim':168,
            'Stuttgart':75,
            'Salzburg':236,
            'Wurzburg':153,
            'Zurich':157
        }
        return H[n]

    def get_neighbour(self, v):
        return self.lst[v]

    def a_star(self, start, stop):
        open_lst = set([start])
        close_lst = set([])
        p = {}
        p[start] = 0
        path = {}
        path[start] = start

        while len(open_lst) > 0:
            n = None

            for v in open_lst:
                if n is None or p[v] + self.h(v) < p[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist')
                return None

            if n == stop:
                r_path = []

                while path[n] != n:
                    r_path.append(n)
                    n = path[n]

                r_path.append(start)
                r_path.reverse()

                print('Path found: {}'.format(r_path))
                return r_path

            for (m, weight) in self.get_neighbour(n):
                if m not in open_lst and m not in close_lst:
                    open_lst.add(m)
                    path[m] = n
                    p[m] = p[n] + weight
                else:
                    if p[m] > p[n] + weight:
                        p[m] = p[n] + weight
                        path[m] = n
                        if m in close_lst:
                            close_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)
            close_lst.add(n)

        print('Path does not exist')
        return None