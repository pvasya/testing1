import math

EPS = 1e-8

def eq4_to_ABC(a, b):
    """Converts x/a + y/b = 1 to Ax + By + C = 0."""
    if a == 0 or b == 0:
        raise ValueError(' "a = 0 or b = 0"; "Set non-zero integer values for a and b in Line 1." ')
    A = b
    B = a
    C = -a * b
    return float(A), float(B), float(C)

def eq6_to_ABC(x0, y0, an, bn):
    """Converts an(x - x0) + bn(y - y0) = 0 to Ax + By + C = 0."""
    if an == 0 and bn == 0:
        raise ValueError(' "Zero normal vector"; "Set at least one coordinate of the normal vector (an, bn) to a non-zero value." ')
    A = an
    B = bn
    C = -(an * x0 + bn * y0)
    return float(A), float(B), float(C)

def approx_eq(x, y, eps=EPS):
    """Checks if two values are equal within epsilon."""
    return abs(x - y) <= eps

def intersect_two_lines(A1, B1, C1, A2, B2, C2, eps=EPS):
    """Calculates intersection type and points for two lines."""
    D = A1 * B2 - A2 * B1
    if abs(D) > eps:
        x = (B1 * C2 - B2 * C1) / D
        y = (C1 * A2 - C2 * A1) / D
        return ('point', (x, y))
    
    # D approx 0: parallel or coincident
    if approx_eq(A1 * C2, A2 * C1, eps) and approx_eq(B1 * C2, B2 * C1, eps):
        return ('coincident', None)
    return ('parallel', None)

def unique_points(points, eps=EPS):
    """Filters unique points from a list based on epsilon."""
    unique = []
    for p in points:
        found = False
        for q in unique:
            if approx_eq(p[0], q[0], eps) and approx_eq(p[1], q[1], eps):
                found = True
                break
        if not found:
            unique.append(p)
    return unique

def validate_params(params, N=48):
    """Validates input ranges and types."""
    MIN = -100 - N
    MAX = 100 + N
    
    for key, val in params.items():
        if not isinstance(val, int):
            raise ValueError(f' "Non-integer value for {key}"; "Ensure all inputs are integers." ')
        if val < MIN or val > MAX:
            raise ValueError(f' "Value {key}={val} outside of range"; "Set value between {MIN} and {MAX}." ')

def analyze_three_lines(params, N=48):
    """Main analysis function for three lines."""
    validate_params(params, N)
    
    A1, B1, C1 = eq4_to_ABC(params['a'], params['b'])
    A2, B2, C2 = eq6_to_ABC(params['x01'], params['y01'], params['a1'], params['b1'])
    A3, B3, C3 = eq6_to_ABC(params['x02'], params['y02'], params['a2'], params['b2'])
    
    pairs = [
        (A1, B1, C1, A2, B2, C2),
        (A1, B1, C1, A3, B3, C3),
        (A2, B2, C2, A3, B3, C3)
    ]
    
    results = []
    intersection_points = []
    coinc_count = 0
    
    for p in pairs:
        cls, pt = intersect_two_lines(*p)
        results.append(cls)
        if cls == 'point':
            intersection_points.append(pt)
        if cls == 'coincident':
            coinc_count += 1
            
    unique_pts = unique_points(intersection_points)
    m = len(unique_pts)
    
    unique_pts.sort(key=lambda p: (round(p[0], 8), round(p[1], 8)))
    
    if coinc_count == 3:
        return {'case': 'coincident', 'points': []}
    if m == 0:
        return {'case': 'no_intersection', 'points': []}
    if m == 1:
        return {'case': 'one_point', 'points': unique_pts}
    if m == 2:
        return {'case': 'two_points', 'points': unique_pts}
    if m == 3:
        return {'case': 'three_points', 'points': unique_pts}
    
    return {'case': 'unknown', 'points': unique_pts}
