import tkinter as tk

class PaintApp:
    def __init__(root):
        root.root = tk.Tk()
        root.root.title("Paint -BY ANJALI")
        root.root.iconbitmap("images/paint.ico")

        root.canvas = tk.Canvas(root.root, bg="white", width=600, height=400)
        root.canvas.pack()

        root.draw_mode = False
        root.start_x = None
        root.start_y = None
        root.brush_color = "black"
        root.brush_size = 2

        root.canvas.bind("<Button-1>", root.start_draw)
        root.canvas.bind("<B1-Motion>", root.draw)
        root.canvas.bind("<ButtonRelease-1>", root.stop_draw)

        root.color_palette = tk.Frame(root.root)
        root.color_palette.pack(pady=10)

        colors = ["black", "red", "green", "blue", "yellow", "orange", "purple"]
        for color in colors:
            button = tk.Button(root.color_palette, bg=color, width=2, command=lambda c=color: root.change_color(c))
            button.pack(side="left", padx=5)

        root.size_scale = tk.Scale(root.root, from_=1, to=10, orient="horizontal", label="Brush Size", command=root.change_size)
        root.size_scale.pack()

        clear_button = tk.Button(root.root, text="Clear Canvas", command=root.clear_canvas)
        clear_button.pack()

    def start_draw(root, event):
        root.draw_mode = True
        root.start_x = event.x
        root.start_y = event.y

    def draw(root, event):
        if root.draw_mode:
            x, y = event.x, event.y
            root.canvas.create_line(root.start_x, root.start_y, x, y, width=root.brush_size, fill=root.brush_color)
            root.start_x = x
            root.start_y = y

    def stop_draw(root, event):
        root.draw_mode = False

    def change_color(root, color):
        root.brush_color = color

    def change_size(root, size):
        root.brush_size = int(size)

    def clear_canvas(root):
        root.canvas.delete("all")

app = PaintApp()
app.root.mainloop()
