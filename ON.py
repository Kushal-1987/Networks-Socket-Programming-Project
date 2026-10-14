import sys
import socket

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


def main():
    
    adj_mat = read_config(sys.argv[1])
    socketfd = socket.socket(socket.PF_INET, socket.SOCK_STREAM)

    if socketfd.bind(("",5000))==-1:
        print("ON binding failed")

    socketfd.listen()

    l = []
    for _ in range(len(adj_mat)):
        l.append(socketfd.accept())

if __name__ == "__main__":
    main()
