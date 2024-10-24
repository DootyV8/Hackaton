import numpy as np

def rotate_clockwise(mat):
    """Rotate the matrix clockwise by 90 degrees."""
    return np.rot90(mat, k=-1)

def rotate_counterclockwise(mat):
    """Rotate the matrix counterclockwise by 90 degrees."""
    return np.rot90(mat, k=1)

def move_row(mat, row, steps):
    """Move a row left or right by a specified number of steps (modulo for circular shift)."""
    row = row % mat.shape[0]
    mat[row, :] = np.roll(mat[row, :], steps)
    return mat

def move_column(mat, col, steps):
    """Move a column up or down by a specified number of steps (modulo for circular shift)."""
    col = col % mat.shape[1]
    mat[:, col] = np.roll(mat[:, col], steps)
    return mat

def replace_character(mat, old, new):
    """Replace all occurrences of a character in the matrix."""
    return np.where(mat == old, new, mat)

def mirror_row(mat, row):
    """Mirror a row horizontally."""
    row = row % mat.shape[0]
    mat[row, :] = mat[row, ::-1]
    return mat

def mirror_column(mat, col):
    """Mirror a column vertically."""
    col = col % mat.shape[1]
    mat[:, col] = mat[::-1, col]
    return mat

def clear_row(mat, row):
    """Clear a row by filling it with spaces."""
    row = row % mat.shape[0]
    mat[row, :] = ' '
    return mat

def clear_column(mat, col):
    """Clear a column by filling it with spaces."""
    col = col % mat.shape[1]
    mat[:, col] = ' '
    return mat

# Initial matrix from task.txt (simplified example)
matrix = np.array([
    list("  - HHH"),
    list("X,F)   "),
    list("  AABHB"),
    list("     H,"),
    list("XXHHAX "),
    list("FXH , A"),
    list("  )  *E"),
    list(",  C\"HH"),
    list(" FHHFH "),
    list("GHHFHF "),
    list(" ,   A "),
    list("H ),  )"),
    list(" A () ,"),
    list("H*   HH"),
    list("H XXXC "),
    list(")F   C)"),
    list(" \" AX  "),
    list("*X)X.  "),
    list(") FA  )"),
    list(")   X  "),
    list(" ( AXAX"),
    list("F   H-F"),
    list("  H.FAA"),
    list("BHHX  B"),
    list("G A*A ."),
    list("H\"HF  +"),
    list("H A A  "),
    list(" A* X+ "),
    list(")H ,AF "),
    list("B    F "),
    list(" HA FF "),
    list(")  X.+H"),
    list("F   FA)"),
    list("*H H+ H"),
    list("F FAD A"),
    list("  H  AB"),
    list("H F HHF"),
    list("H X HA "),
    list(" \"XA  H"),
    list(" FFH  ."),
    list("  X+  B"),
    list("H    H "),
    list("-FF XH "),
    list("  - .B "),
    list(" GH  HH"),
    list("XCFHH H"),
    list("H )  HB"),
    list("XH   DG"),
    list(" .-\" ( "),
    list("XX EX  "),
    list("  ) HHH"),
    list("HF DHXX"),
    list("HHBH, B"),
    list(" DG DH "),
    list("A HAF(+"),
    list("F-X. X)")
])

# Apply transformations step by step (this is a small subset, add all commands)
matrix = rotate_clockwise(matrix)
matrix = move_column(matrix, 27 % matrix.shape[1], 3081622)
matrix = move_column(matrix, 21 % matrix.shape[1], -6275953)
matrix = move_column(matrix, 22 % matrix.shape[1], -161226)
matrix = move_row(matrix, 4, 1084723)
matrix = move_column(matrix, 7 % matrix.shape[1], 9558215)
matrix = replace_character(matrix, 'X', '/')
matrix = move_row(matrix, 3, 4054298)
matrix = move_column(matrix, 7 % matrix.shape[1], 7919146)
matrix = replace_character(matrix, 'Q', '_')
matrix = move_column(matrix, 16 % matrix.shape[1], 4548320)
matrix = move_column(matrix, 7 % matrix.shape[1], -5420259)
matrix = move_column(matrix, 14 % matrix.shape[1], 652146)
matrix = mirror_row(matrix, 6)
matrix = mirror_row(matrix, 5)
matrix = replace_character(matrix, 'W', '|')
matrix = mirror_row(matrix, 3)
matrix = move_column(matrix, 1 % matrix.shape[1], -4476643)
matrix = move_row(matrix, 6, -6332715)
matrix = move_column(matrix, 18 % matrix.shape[1], 8047735)
matrix = move_row(matrix, 5, 291770)
matrix = move_row(matrix, 3, 4395856)
matrix = move_column(matrix, 51 % matrix.shape[1], 9657638)
matrix = move_column(matrix, 38 % matrix.shape[1], 1209216)
matrix = move_row(matrix, 4, 1770486)
matrix = move_column(matrix, 54 % matrix.shape[1], -4831015)
matrix = rotate_counterclockwise(matrix)
matrix = mirror_column(matrix, 1)
matrix = move_column(matrix, 0, 2361304)
matrix = move_row(matrix, 32, 8110895)
matrix = rotate_clockwise(matrix)
matrix = move_column(matrix, 23 % matrix.shape[1], 1389525)
matrix = move_column(matrix, 26 % matrix.shape[1], -2070680)
matrix = replace_character(matrix, 'H', '_')
matrix[:, 28] = ' '
matrix = move_column(matrix, 18 % matrix.shape[1], -9369767)
matrix = move_row(matrix, 3, 4396407)
matrix = mirror_column(matrix, 33)
matrix = replace_character(matrix, 'H', '|')
matrix = move_row(matrix, 5, 1262846)
matrix = move_column(matrix, 42 % matrix.shape[1], 8692770)
matrix = mirror_column(matrix, 32)
matrix = move_column(matrix, 44 % matrix.shape[1], 1940085)
matrix = rotate_counterclockwise(matrix)
matrix = mirror_column(matrix, 1)
matrix = rotate_clockwise(matrix)
matrix = move_row(matrix, 6, 458219)
matrix = move_row(matrix, 0, -7931458)
matrix = move_column(matrix, 36 % matrix.shape[1], 8518421)
matrix = rotate_counterclockwise(matrix)
matrix = mirror_row(matrix, 8)
matrix = move_row(matrix, 5, 7108847)
matrix = replace_character(matrix, 'C', '>')
matrix = move_column(matrix, 5 % matrix.shape[1], 2509153)
matrix = move_column(matrix, 4 % matrix.shape[1], -7665938)
matrix = move_row(matrix, 9, -7266971)
matrix = move_column(matrix, 4 % matrix.shape[1], 5097266)
matrix = mirror_column(matrix, 2)
matrix = move_column(matrix, 1 % matrix.shape[1], -7042062)
matrix = move_column(matrix, 5 % matrix.shape[1], 9105863)
matrix = mirror_column(matrix, 4)
matrix = mirror_row(matrix, 13)
matrix = mirror_row(matrix, 41)
matrix = mirror_row(matrix, 41)
matrix = move_column(matrix, 5 % matrix.shape[1], -6075944)
matrix = mirror_column(matrix, 0)
matrix = move_column(matrix, 5 % matrix.shape[1], 9797903)
matrix = move_column(matrix, 2 % matrix.shape[1], -5551206)
matrix = move_row(matrix, 14, -9896355)
matrix = mirror_row(matrix, 12)
matrix = move_column(matrix, 0, 2678859)
matrix = move_column(matrix, 3 % matrix.shape[1], -6892073)
matrix = replace_character(matrix, 'A', 'C')
matrix = move_column(matrix, 5 % matrix.shape[1], -8421732)
matrix = move_column(matrix, 5 % matrix.shape[1], -5874801)
matrix = mirror_row(matrix, 18)
matrix = move_column(matrix, 1 % matrix.shape[1], -1508373)
matrix = move_column(matrix, 6 % matrix.shape[1], -2555832)
matrix = move_column(matrix, 3 % matrix.shape[1], -2629476)
matrix = move_column(matrix, 3 % matrix.shape[1], -9027568)
matrix = move_column(matrix, 1 % matrix.shape[1], -7269228)
matrix = move_column(matrix, 4 % matrix.shape[1], -2644826)
matrix = rotate_clockwise(matrix)
matrix = move_row(matrix, 5, 7159564)
matrix = replace_character(matrix, 'H', '\\')
matrix = rotate_counterclockwise(matrix)
matrix = move_column(matrix, 1 % matrix.shape[1], 2589504)
matrix = move_column(matrix, 0, 1723480)
matrix = move_column(matrix, 2 % matrix.shape[1], -2256561)
matrix = mirror_column(matrix, 5)
matrix = mirror_row(matrix, 39)
matrix = mirror_column(matrix, 6)
matrix = move_row(matrix, 3, -632264)
matrix = move_row(matrix, 36, 6287492)
matrix = rotate_clockwise(matrix)
matrix = rotate_clockwise(matrix)
matrix = move_column(matrix, 3 % matrix.shape[1], 924317)
matrix = move_column(matrix, 5 % matrix.shape[1], 6308150)
matrix = mirror_column(matrix, 0)
matrix = move_row(matrix, 45, -372701)
matrix = replace_character(matrix, 'H', 'U')
matrix = rotate_clockwise(matrix)
matrix = replace_character(matrix, 'E', 'A')
matrix = move_row(matrix, 3, 7298359)
matrix = move_column(matrix, 0, 5575906)
matrix = rotate_counterclockwise(matrix)
matrix = rotate_counterclockwise(matrix)
matrix = replace_character(matrix, 'H', 'u')
matrix = rotate_counterclockwise(matrix)
matrix = move_column(matrix, 4 % matrix.shape[1], -1682555)
matrix = mirror_column(matrix, 4)
matrix = move_row(matrix, 52, 9571309)
matrix = mirror_column(matrix, 5)
matrix = move_row(matrix, 16, 7156160)
matrix = mirror_row(matrix, 50)
matrix = rotate_counterclockwise(matrix)
matrix = rotate_clockwise(matrix)
matrix[55, :] = ' '
matrix = move_row(matrix, 0, 928237)
matrix = mirror_row(matrix, 10)
matrix = move_column(matrix, 3 % matrix.shape[1], 8437633)
matrix = move_column(matrix, 5 % matrix.shape[1], -5835078)
matrix = move_column(matrix, 0, -7265728)
matrix = move_row(matrix, 35, 1011947)
matrix = move_row(matrix, 25, 5539144)
matrix = move_column(matrix, 1 % matrix.shape[1], -1534228)
matrix = move_row(matrix, 8, 600754)
matrix = move_column(matrix, 0, -2843732)
matrix = mirror_column(matrix, 0)
matrix = replace_character(matrix, 'G', 'U')
matrix = move_row(matrix, 42, 9378683)
matrix[32, :] = ' '
matrix = move_row(matrix, 28, 7218964)
matrix = move_column(matrix, 3 % matrix.shape[1], 6835329)
matrix = move_column(matrix, 2 % matrix.shape[1], 7832880)
matrix = move_column(matrix, 5 % matrix.shape[1], 9512585)
matrix = move_column(matrix, 6 % matrix.shape[1], 1951013)
matrix = replace_character(matrix, 'A', '<')
matrix = move_column(matrix, 3 % matrix.shape[1], -7325642)
matrix = move_column(matrix, 6 % matrix.shape[1], 9859014)
matrix = replace_character(matrix, 'H', '|')
matrix = move_column(matrix, 1 % matrix.shape[1], -6919673)
matrix = move_column(matrix, 4 % matrix.shape[1], 720572)
matrix[7, :] = ' '
matrix = mirror_row(matrix, 29)
matrix = move_row(matrix, 36, 4389213)
matrix = move_column(matrix, 3 % matrix.shape[1], -6743048)
matrix = move_row(matrix, 42, -8035040)
matrix = move_column(matrix, 1 % matrix.shape[1], -9945607)
matrix = replace_character(matrix, 'E', 'G')
matrix = move_row(matrix, 34, -1977661)
matrix = mirror_column(matrix, 0)
matrix = mirror_column(matrix, 1)
matrix = replace_character(matrix, 'G', 'H')
matrix = move_column(matrix, 0, -6281352)
matrix = rotate_counterclockwise(matrix)
matrix = mirror_column(matrix, 27)
matrix = move_column(matrix, 45 % matrix.shape[1], 3431830)
matrix = move_row(matrix, 5, -1392238)
matrix = move_row(matrix, 3, 6528341)
matrix = move_column(matrix, 38 % matrix.shape[1], -4556704)
matrix = move_column(matrix, 2 % matrix.shape[1], -1217036)
matrix = replace_character(matrix, 'D', 'u')
matrix = move_row(matrix, 5, 6147689)
matrix = mirror_row(matrix, 2)
matrix = rotate_counterclockwise(matrix)
matrix = rotate_counterclockwise(matrix)
matrix = move_row(matrix, 4, 875911)
matrix = move_row(matrix, 2, -7281879)
matrix = rotate_counterclockwise(matrix)
matrix = rotate_clockwise(matrix)
matrix = move_row(matrix, 0, -4761095)
matrix = replace_character(matrix, 'E', '\\')
matrix = move_column(matrix, 25 % matrix.shape[1], 3710264)
matrix = mirror_row(matrix, 3)
matrix = replace_character(matrix, 'G', '\\')
matrix = move_row(matrix, 1, -9618448)
matrix = move_row(matrix, 4, 4686438)
matrix = replace_character(matrix, 'E', 'H')
matrix[:, 42] = ' '
matrix = replace_character(matrix, 'C', '|')
matrix = replace_character(matrix, 'F', '\\')
matrix = mirror_row(matrix, 4)
matrix = replace_character(matrix, 'G', 'A')
matrix = move_column(matrix, 3 % matrix.shape[1], 4943735)
matrix = move_column(matrix, 15 % matrix.shape[1], -6640132)
matrix = replace_character(matrix, 'B', '(')
matrix[:, 43] = ' '
matrix = move_row(matrix, 4, -834554)
matrix = move_column(matrix, 42 % matrix.shape[1], 8539877)
matrix = move_row(matrix, 6, -7997173)
matrix = mirror_row(matrix, 6)
matrix = move_column(matrix, 39 % matrix.shape[1], 847196)
matrix = move_column(matrix, 5 % matrix.shape[1], 5829437)
matrix = move_row(matrix, 4, 6859660)
matrix = rotate_clockwise(matrix)
matrix[22, :] = ' '
matrix = move_column(matrix, 1 % matrix.shape[1], 1980150)
matrix = rotate_counterclockwise(matrix)
matrix[:, 11] = ' '
# Final result
print("\n".join("".join(row) for row in matrix))
