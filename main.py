import tkinter as tk
from tkinter import messagebox, filedialog
import geometry_calc as gc

class GeometryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometry Analysis Tool")
        self.root.geometry("600x500")
        self.N = 48
        self.min_val = -100 - self.N
        self.max_val = 100 + self.N

        self.setup_ui()

    def setup_ui(self):
        header_frame = tk.Frame(self.root, pady=10)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text=f"Range: [{self.min_val}; {self.max_val}] (N={self.N})", font=("Arial", 10, "bold")).pack()

        group1 = tk.LabelFrame(self.root, text="Line 1: x/a + y/b = 1", padx=10, pady=10)
        group1.pack(fill="x", padx=10, pady=5)
        
        tk.Label(group1, text="a (non-zero):").grid(row=0, column=0, sticky="w")
        self.ent_a = tk.Entry(group1)
        self.ent_a.grid(row=0, column=1, padx=5)

        tk.Label(group1, text="b (non-zero):").grid(row=1, column=0, sticky="w")
        self.ent_b = tk.Entry(group1)
        self.ent_b.grid(row=1, column=1, padx=5)

        group2 = tk.LabelFrame(self.root, text="Line 2: a1(x - x01) + b1(y - y01) = 0", padx=10, pady=10)
        group2.pack(fill="x", padx=10, pady=5)

        tk.Label(group2, text="x01 (point X):").grid(row=0, column=0, sticky="w")
        self.ent_x01 = tk.Entry(group2)
        self.ent_x01.grid(row=0, column=1, padx=5)

        tk.Label(group2, text="y01 (point Y):").grid(row=1, column=0, sticky="w")
        self.ent_y01 = tk.Entry(group2)
        self.ent_y01.grid(row=1, column=1, padx=5)

        tk.Label(group2, text="a1 (normal X):").grid(row=2, column=0, sticky="w")
        self.ent_a1 = tk.Entry(group2)
        self.ent_a1.grid(row=2, column=1, padx=5)

        tk.Label(group2, text="b1 (normal Y):").grid(row=3, column=0, sticky="w")
        self.ent_b1 = tk.Entry(group2)
        self.ent_b1.grid(row=3, column=1, padx=5)

        group3 = tk.LabelFrame(self.root, text="Line 3: a2(x - x02) + b2(y - y02) = 0", padx=10, pady=10)
        group3.pack(fill="x", padx=10, pady=5)

        tk.Label(group3, text="x02 (point X):").grid(row=0, column=0, sticky="w")
        self.ent_x02 = tk.Entry(group3)
        self.ent_x02.grid(row=0, column=1, padx=5)

        tk.Label(group3, text="y02 (point Y):").grid(row=1, column=0, sticky="w")
        self.ent_y02 = tk.Entry(group3)
        self.ent_y02.grid(row=1, column=1, padx=5)

        tk.Label(group3, text="a2 (normal X):").grid(row=2, column=0, sticky="w")
        self.ent_a2 = tk.Entry(group3)
        self.ent_a2.grid(row=2, column=1, padx=5)

        tk.Label(group3, text="b2 (normal Y):").grid(row=3, column=0, sticky="w")
        self.ent_b2 = tk.Entry(group3)
        self.ent_b2.grid(row=3, column=1, padx=5)

        btn_frame = tk.Frame(self.root, pady=10)
        btn_frame.pack()
        
        tk.Button(btn_frame, text="Calculate", command=self.calculate, width=15, bg="lightblue").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear, width=15).pack(side="left", padx=5)

    def get_params(self):
        try:
            return {
                'a': int(self.ent_a.get()),
                'b': int(self.ent_b.get()),
                'x01': int(self.ent_x01.get()),
                'y01': int(self.ent_y01.get()),
                'a1': int(self.ent_a1.get()),
                'b1': int(self.ent_b1.get()),
                'x02': int(self.ent_x02.get()),
                'y02': int(self.ent_y02.get()),
                'a2': int(self.ent_a2.get()),
                'b2': int(self.ent_b2.get())
            }
        except ValueError:
            raise ValueError(' "Invalid input format"; "Please ensure all fields are filled with integers." ')

    def calculate(self):
        try:
            params = self.get_params()
            res = gc.analyze_three_lines(params, self.N)
            message = self.format_result(res)
            
            messagebox.showinfo(title="Result", message=message)
            
        except ValueError as e:
            messagebox.showerror(title="Error", message=str(e))
        except Exception as e:
            messagebox.showerror(title="Unexpected Error", message=f"An error occurred: {str(e)}")

    def format_result(self, res):
        case = res['case']
        pts = res['points']
        
        if case == 'coincident':
            return "Прямі співпадають"
        if case == 'no_intersection':
            return "Прямі не перетинаються"
        
        formatted_pts = []
        for p in pts:
            formatted_pts.append(f"({p[0]:.6f}, {p[1]:.6f})")
            
        if case == 'one_point':
            p = pts[0]
            return f"Єдина точка перетину прямих (x0, y0), x0= {p[0]:.6f}, y0= {p[1]:.6f}"
        if case == 'two_points':
            return f"Дві точки перетину прямих (x1, y1) = {formatted_pts[0]}, (x2, y2) = {formatted_pts[1]}"
        if case == 'three_points':
            p1, p2, p3 = pts
            return (f"Три точки перетину прямих x1= {p1[0]:.6f}, y1= {p1[1]:.6f}, x2= {p2[0]:.6f}, y2= {p2[1]:.6f}, x3= {p3[0]:.6f}, y3= {p3[1]:.6f}")
            
        return f"Unknown result: {case}"

    def clear(self):
        for entry in [self.ent_a, self.ent_b, self.ent_x01, self.ent_y01, self.ent_a1, self.ent_b1, self.ent_x02, self.ent_y02, self.ent_a2, self.ent_b2]:
            entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryApp(root)
    root.mainloop()
