def get_artistic_photograph_count(N, C, X, Y):
    count = 0
    B = [0] * (N + 1)
    P = [0] * (N + 1)
    
    for i in range(1, N + 1):
        curr = C[i - 1]
        P[i] = P[i - 1] + (1 if curr == 'P' else 0)
        B[i] = B[i - 1] + (1 if curr == 'B' else 0)
    
    for i in range(N):
        if C[i] == 'A':
            x_start = i + X if i + X <= N else N
            y_end = i + Y + 1 if i + Y + 1 <= N else N
            x_end = i - X + 1 if i - X + 1 >= 0 else 0
            y_start = i - Y if i - Y >= 0 else 0
            
            count += (P[y_end] - P[x_start]) * (B[x_end] - B[y_start])
            count += (B[y_end] - B[x_start]) * (P[x_end] - P[y_start])
    
    return count