import sys

def read_config(file):
    #file = sys.argv[1]
    adj = []
    with open(file,"r") as f:
    
        for line in f:
            line = line.strip()

            if line == "" or line[0]=="#":
                continue

            
            adj.append(list(map(int,line.split())))

    n = len(adj)+1

    adj_mat = [[0]*n for _ in range(n)]

    for i in range(n-1):
        for j in range(i + 1, n):
            adj_mat[i][j] = adj[i][j - i - 1]
            adj_mat[j][i] = adj_mat[i][j]

    return adj_mat

adj = read_config(sys.argv[1])

