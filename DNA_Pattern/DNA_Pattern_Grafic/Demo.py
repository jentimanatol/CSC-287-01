import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class DNAPatternVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DNA Pattern Visualizer")
        self.geometry("800x600")
        
        self.create_widgets()
        
    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10)
        
        ttk.Label(frame, text="DNA Sequence:").grid(row=0, column=0, padx=5, pady=5)
        self.dna_input = ttk.Entry(frame, width=50)
        self.dna_input.grid(row=0, column=1, padx=5, pady=5)
        self.dna_input.insert(0, "ACGTACGTACGTACG")
        
        ttk.Label(frame, text="Pattern Length (k):").grid(row=1, column=0, padx=5, pady=5)
        self.k_input = ttk.Entry(frame, width=10)
        self.k_input.grid(row=1, column=1, padx=5, pady=5)
        self.k_input.insert(0, "3")
        
        ttk.Label(frame, text="Threshold:").grid(row=2, column=0, padx=5, pady=5)
        self.threshold_input = ttk.Entry(frame, width=10)
        self.threshold_input.grid(row=2, column=1, padx=5, pady=5)
        self.threshold_input.insert(0, "2")
        
        visualize_button = ttk.Button(frame, text="Visualize Patterns", command=self.visualize_patterns)
        visualize_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.result_area = ScrolledText(self, wrap=tk.WORD, height=10, width=60)
        self.result_area.pack(pady=10)
        
    def visualize_patterns(self):
        dna_sequence = self.dna_input.get()
        k = int(self.k_input.get())
        threshold = int(self.threshold_input.get())
        
        pattern_map = self.count_patterns(dna_sequence, k)
        self.result_area.delete('1.0', tk.END)
        
        for pattern, count in pattern_map.items():
            if count >= threshold:
                self.result_area.insert(tk.END, f"Pattern DNA {pattern} : {count} times\n")
        
        self.draw_dna_helix(dna_sequence)
        
    def count_patterns(self, dna_sequence, k):
        pattern_map = {}
        for i in range(len(dna_sequence) - k + 1):
            pattern = dna_sequence[i:i+k]
            if pattern in pattern_map:
                pattern_map[pattern] += 1
            else:
                pattern_map[pattern] = 1
        return pattern_map
    
    def draw_dna_helix(self, dna_sequence):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_axis_off()

        colors = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'orange'}
        radius = 1
        helix_height = 2
        base_pair_spacing = 0.5

        for i, base in enumerate(dna_sequence):
            x = radius * (i % 2)
            y = -i * base_pair_spacing
            ax.add_patch(patches.Circle((x, y), radius=0.3, color=colors[base]))
            ax.text(x, y, base, fontsize=12, ha='center', va='center', color='white')
            if i < len(dna_sequence) - 1:
                next_x = radius * ((i + 1) % 2)
                next_y = -(i + 1) * base_pair_spacing
                ax.plot([x, next_x], [y, next_y], color='black')

        plt.show()

if __name__ == "__main__":
    app = DNAPatternVisualizer()
    app.mainloop()
