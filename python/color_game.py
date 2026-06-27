import tkinter as tk
from tkinter import font as tkfont
import colorsys
import random
from PIL import Image, ImageTk
import math

# ─── DATOS DEL JUEGO ────────────────────────────────────────────────────────
CHALLENGES = [
    {
        "name": "Tinkerbell",
        "part": "vestido",
        "image": "assets/campanita.png",
        "h": 129, "s": 47, "b": 46,
    },
    {
        "name": "SpongeBob",
        "part": "cuerpo",
        "image": "assets/bobesponja.png",
        "h": 59, "s": 76, "b": 100,
    },
    {
        "name": "Bart Simpson",
        "part": "short",
        "image": "assets/bartsimpson.png",
        "h": 196, "s": 100, "b": 87,
    },
    {
        "name": "Garfield",
        "part": "pelaje",
        "image": "assets/garfield.png",
        "h": 38, "s": 91, "b": 100,
    },
    {
        "name": "Kirby",
        "part": "zapato",
        "image": "assets/kirby.png",
        "h": 344, "s": 100, "b": 72,
    },
    {
        "name": "Sonic",
        "part": "pelaje",
        "image": "assets/sonic.png",
        "h": 227, "s": 86, "b": 98,
    },
    {
        "name": "Marceline",
        "part": "bajo (centro)",
        "image": "assets/marceline.png",
        "h": 358, "s": 98, "b": 58,
    },
    {
        "name": "Mordecai",
        "part": "plumaje",
        "image": "assets/mordecai.png",
        "h": 221, "s": 35, "b":83,
    },
    {
        "name": "Rigby",
        "part": "pecho",
        "image": "assets/rigby.png",
        "h": 31, "s": 18, "b": 75,
    },
    {
        "name": "Gumball",
        "part": "pelaje",
        "image": "assets/gumball.png",
        "h": 198, "s": 77, "b": 100,
    },
    {
        "name": "Pink Panther",
        "part": "ojo",
        "image": "assets/panterarosa.png",
        "h": 56, "s": 100, "b": 100,
    },
    {
        "name": "Remy",
        "part": "pelaje",
        "image": "assets/remy.png",
        "h": 180, "s": 12, "b": 41,
    },
    {
        "name": "Hinata",
        "part": "pelo",
        "image": "assets/hinata.png",
        "h": 23, "s": 71, "b": 100,
    },
    {
        "name": "Tendou",
        "part": "número de camiseta",
        "image": "assets/tendou.png",
        "h": 327, "s": 43, "b": 59,
    },
    {   "name": "Kitty",
        "part": "moño",
        "image": "assets/kitty.png",
        "h": 344, "s": 92, "b": 91,
    },
    {
        "name": "Kuromi",
        "part": "gorro",
        "image": "assets/kuromi.png",
        "h": 40, "s": 3, "b": 36,
    },
    {
        "name": "Melody",
        "part": "gorro",
        "image": "assets/mymelody.png",
        "h": 348, "s": 45, "b": 95,
    },
    {
        "name": "Purple Guy",
        "part": "cuerpo",
        "image": "assets/hombremorado.png",
        "h": 269, "s": 50, "b": 58,
    },
    {
        "name": "Mangle",
        "part": "pecho",
        "image": "assets/mangle.png",
        "h": 352, "s": 55, "b": 100,
    },
    {
        "name": "Cupcake",
        "part": "fuego",
        "image": "assets/cupcake.png",
        "h": 42, "s": 100, "b": 100,
    },
]

TOTAL_ROUNDS = 5

# ─── UTILIDADES DE COLOR ─────────────────────────────────────────────────────
def hsb_to_hex(h, s, b):
    r, g, bl = colorsys.hsv_to_rgb(h / 360, s / 100, b / 100)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(bl*255):02x}"

def score_colors(h1, s1, b1, h2, s2, b2):
    dh = min(abs(h1 - h2), 360 - abs(h1 - h2)) / 180
    ds = abs(s1 - s2) / 100
    db = abs(b1 - b2) / 100
    dist = math.sqrt((dh * 0.6)**2 + (ds * 0.25)**2 + (db * 0.15)**2)
    max_dist = math.sqrt(0.6**2 + 0.25**2 + 0.15**2)
    raw = 1 - dist / max_dist
    score = 10 * (raw ** 1.8)
    return round(score, 2)

# ─── APLICACIÓN PRINCIPAL ────────────────────────────────────────────────────
class ColorGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎨 Color Memory")
        self.geometry("820x720")
        self.resizable(False, False)
        self.configure(bg="#0f0f1a")
        self._setup_fonts()
        self._new_game()

    def _setup_fonts(self):
        self.font_title  = tkfont.Font(family="Helvetica", size=22, weight="bold")
        self.font_sub    = tkfont.Font(family="Helvetica", size=13)
        self.font_label  = tkfont.Font(family="Helvetica", size=11, weight="bold")
        self.font_value  = tkfont.Font(family="Courier",   size=12, weight="bold")
        self.font_score  = tkfont.Font(family="Helvetica", size=36, weight="bold")
        self.font_btn    = tkfont.Font(family="Helvetica", size=13, weight="bold")
        self.font_small  = tkfont.Font(family="Helvetica", size=10)

    def _new_game(self):
        self.round_num  = 0
        self.scores     = []
        self.challenges = random.sample(CHALLENGES, TOTAL_ROUNDS)
        self._clear()
        self._show_round()

    def _clear(self):
        for w in self.winfo_children():
            w.destroy()

    # ── PANTALLA DE RONDA ────────────────────────────────────────────────────
    def _show_round(self):
        self._clear()
        ch = self.challenges[self.round_num]

        self.h_var = tk.IntVar(value=180)
        self.s_var = tk.IntVar(value=50)
        self.b_var = tk.IntVar(value=50)

        # Encabezado
        hdr = tk.Frame(self, bg="#0f0f1a")
        hdr.pack(fill="x", padx=30, pady=(24, 0))
        tk.Label(hdr, text=f"Ronda {self.round_num+1} / {TOTAL_ROUNDS}",
                 bg="#0f0f1a", fg="#8888aa", font=self.font_sub).pack(side="left")
        score_text = "  ·  ".join(f"{s:.1f}" for s in self.scores) if self.scores else "—"
        tk.Label(hdr, text=f"Anteriores: {score_text}",
                 bg="#0f0f1a", fg="#555577", font=self.font_small).pack(side="right")

        # Título
        tk.Label(self, text=f"¿De qué color es el {ch['part']} de {ch['name']}?",
                 bg="#0f0f1a", fg="#ffffff", font=self.font_title).pack(pady=(12, 2))
        tk.Label(self, text=f"«{ch['name']}»",
                 bg="#0f0f1a", fg="#9988ff", font=self.font_sub).pack(pady=(0, 16))

        # Zona de colores
        color_frame = tk.Frame(self, bg="#0f0f1a")
        color_frame.pack(pady=4)

        # Izquierdo — imagen del personaje
        left = tk.Frame(color_frame, bg="#1a1a2e", bd=0)
        left.pack(side="left", padx=16)
        tk.Label(left, text="PERSONAJE",
                 bg="#1a1a2e", fg="#555577", font=self.font_small).pack(pady=(8,4), padx=20)
        self.hidden_canvas = tk.Canvas(left, width=180, height=180,
                                       bg="#1a1a2e", highlightthickness=0)
        self.hidden_canvas.pack(padx=16, pady=4)
        
        try:
            img = Image.open(ch["image"]).convert("RGBA")
            fondo = Image.new("RGBA", img.size, (26, 26, 46))
            fondo.paste(img, mask=img.split()[3])
            img = fondo.convert("RGB").resize((160, 160))
            photo = ImageTk.PhotoImage(img)
            self.hidden_canvas.create_image(10, 10, anchor="nw", image=photo)
            self.hidden_canvas._photo = photo
        except Exception:
            self.hidden_canvas.create_text(90, 90, text="IMG\nFALTANTE", fill="#555577")
            
        tk.Label(left, text=f"adiviná el {ch['part']}",
                 bg="#1a1a2e", fg="#333355", font=self.font_small).pack(pady=(4,8), padx=20)

        # Derecho — tu selección
        right = tk.Frame(color_frame, bg="#1a1a2e", bd=0)
        right.pack(side="left", padx=16)
        tk.Label(right, text="TU SELECCIÓN",
                 bg="#1a1a2e", fg="#555577", font=self.font_small).pack(pady=(8,4), padx=20)
        self.preview_canvas = tk.Canvas(right, width=180, height=180,
                                        bg="#1a1a2e", highlightthickness=0)
        self.preview_canvas.pack(padx=16, pady=4)
        self.hex_label = tk.Label(right, text="#808080",
                                  bg="#1a1a2e", fg="#888899", font=self.font_value)
        self.hex_label.pack(pady=(4,8))

        # Sliders HSB Personalizados
        sliders_frame = tk.Frame(self, bg="#0f0f1a")
        sliders_frame.pack(pady=12, fill="x", padx=60)
        self._make_slider(sliders_frame, "Matiz (H)",      self.h_var, 0, 360, "#ff6666", "hue")
        self._make_slider(sliders_frame, "Saturación (S)", self.s_var, 0, 100, "#66aaff", "sat")
        self._make_slider(sliders_frame, "Brillo (B)",     self.b_var, 0, 100, "#ffee66", "bri")

        # Botón confirmar
        tk.Button(self, text="✓  Confirmar color",
                  bg="#7755ff", fg="white",
                  font=self.font_btn, bd=0, padx=24, pady=10,
                  activebackground="#9977ff", activeforeground="white",
                  cursor="hand2", command=self._submit).pack(pady=18)

        self._update_preview()

    def _make_slider(self, parent, label, var, from_, to, accent, gradient_type=None):
        row = tk.Frame(parent, bg="#0f0f1a")
        row.pack(fill="x", pady=8)

        tk.Label(row, text=label, bg="#0f0f1a", fg="#aaaacc",
                 font=self.font_label, width=18, anchor="w").pack(side="left")

        center_frame = tk.Frame(row, bg="#0f0f1a")
        center_frame.pack(side="left", padx=8)

        # El canvas ahora contiene tanto el fondo de color como el cuadradito interactivo
        bar = tk.Canvas(center_frame, height=26, width=380, bg="#0f0f1a", highlightthickness=0, cursor="hand2")
        bar.pack()
        
        setattr(self, f"canvas_{gradient_type}", bar)
        setattr(self, f"var_{gradient_type}", var)

        val_label = tk.Label(row, text=str(var.get()), bg="#0f0f1a",
                                  fg=accent, font=self.font_value, width=4)
        val_label.pack(side="left", padx=(8, 0))
        setattr(self, f"val_label_{gradient_type}", val_label)

        # Manejador del arrastre del mouse simulando un Scale
        def update_from_mouse(event):
            w = 380
            thumb_w = 16
            start_x = thumb_w / 2
            end_x = w - start_x
            playable_w = end_x - start_x
            
            cx = max(start_x, min(event.x, end_x))
            pct = (cx - start_x) / playable_w
            val = int(from_ + pct * (to - from_))
            var.set(val)

        bar.bind("<Button-1>", update_from_mouse)
        bar.bind("<B1-Motion>", update_from_mouse)

        def on_var_change(*args):
            val_label.config(text=str(var.get()))
            self._update_preview()

        var.trace_add("write", on_var_change)

    def _draw_gradient(self, canvas, gradient_type, var):
        canvas.delete("all")
        w = 380
        thumb_w = 16
        start_x = thumb_w / 2
        end_x = w - start_x
        playable_w = end_x - start_x
        
        try:
            current_h = self.h_var.get() / 360
            current_s = self.s_var.get() / 100
            current_b = self.b_var.get() / 100
        except (AttributeError, tk.TclError):
            return

        # 1. Dibujar la franja del gradiente en el medio (de y=9 a y=17)
        for i in range(w):
            if i <= start_x:
                val_pct = 0.0
            elif i >= end_x:
                val_pct = 1.0
            else:
                val_pct = (i - start_x) / playable_w

            if gradient_type == "hue":
                r, g, bl = colorsys.hsv_to_rgb(val_pct, 1.0, 1.0)
            elif gradient_type == "sat":
                r, g, bl = colorsys.hsv_to_rgb(current_h, val_pct, max(0.2, current_b))
            elif gradient_type == "bri":
                r, g, bl = colorsys.hsv_to_rgb(current_h, current_s, val_pct)

            color = f"#{int(r*255):02x}{int(g*255):02x}{int(bl*255):02x}"
            canvas.create_line(i, 9, i, 17, fill=color)

        # 2. Calcular el color exacto que le corresponde al tirador en su posición actual
        max_val = 360 if gradient_type == "hue" else 100
        current_val_pct = var.get() / max_val
        
        if gradient_type == "hue":
            r, g, bl = colorsys.hsv_to_rgb(current_val_pct, 1.0, 1.0)
        elif gradient_type == "sat":
            r, g, bl = colorsys.hsv_to_rgb(current_h, current_val_pct, max(0.2, current_b))
        elif gradient_type == "bri":
            r, g, bl = colorsys.hsv_to_rgb(current_h, current_s, current_val_pct)
        
        exact_color = f"#{int(r*255):02x}{int(g*255):02x}{int(bl*255):02x}"

        # 3. Dibujar el cuadradito selector con su respectivo color dinámico de relleno
        pos = start_x + (current_val_pct * playable_w)
        # Dibujamos el cuadrado de 16x22 píxeles con un borde blanco nítido
        canvas.create_rectangle(pos - 8, 2, pos + 8, 24, fill=exact_color, outline="#ffffff", width=2)

        # 4. Sincronizar el color del texto de la derecha para mejorar el diseño
        val_label = getattr(self, f"val_label_{gradient_type}", None)
        if val_label:
            text_r, text_g, text_bl = colorsys.hsv_to_rgb(
                current_val_pct if gradient_type == "hue" else current_h,
                current_val_pct if gradient_type == "sat" else current_s,
                max(0.6, current_val_pct if gradient_type == "bri" else current_b)
            )
            text_color = f"#{int(text_r*255):02x}{int(text_g*255):02x}{int(text_bl*255):02x}"
            val_label.config(fg=text_color)

    def _update_preview(self):
        h, s, b = self.h_var.get(), self.s_var.get(), self.b_var.get()
        hex_c = hsb_to_hex(h, s, b)
        self.preview_canvas.delete("all")
        self.preview_canvas.create_rectangle(10, 10, 170, 170,
                                             fill=hex_c, outline="#ffffff", width=1)
        self.hex_label.config(text=hex_c.upper(), fg="#888899")

        for g_type in ["hue", "sat", "bri"]:
            canvas = getattr(self, f"canvas_{g_type}", None)
            var = getattr(self, f"var_{g_type}", None)
            if canvas and var:
                self._draw_gradient(canvas, g_type, var)

    # ── ENVÍO Y RESULTADO ────────────────────────────────────────────────────
    def _submit(self):
        ch = self.challenges[self.round_num]
        h_g, s_g, b_g = self.h_var.get(), self.s_var.get(), self.b_var.get()
        h_r, s_r, b_r = ch["h"], ch["s"], ch["b"]
        pts = score_colors(h_g, s_g, b_g, h_r, s_r, b_r)
        self.scores.append(pts)
        self._show_result(ch, h_g, s_g, b_g, pts)

    def _show_result(self, ch, h_g, s_g, b_g, pts):
        self._clear()
        h_r, s_r, b_r = ch["h"], ch["s"], ch["b"]
        hex_real  = hsb_to_hex(h_r, s_r, b_r)
        hex_guess = hsb_to_hex(h_g, s_g, b_g)

        if pts >= 8:   score_color, emoji = "#44dd88", "🎯"
        elif pts >= 5: score_color, emoji = "#ffcc44", "👀"
        else:          score_color, emoji = "#ff6655", "😅"

        tk.Label(self, text=f"{emoji}  Puntuación de la ronda",
                 bg="#0f0f1a", fg="#aaaacc", font=self.font_sub).pack(pady=(28, 4))
        tk.Label(self, text=f"{pts:.2f} / 10",
                 bg="#0f0f1a", fg=score_color, font=self.font_score).pack(pady=(0, 20))

        comp = tk.Frame(self, bg="#0f0f1a")
        comp.pack(pady=4)
        for title, hx, h, s, b in [
            ("TU COLOR", hex_guess, h_g, s_g, b_g),
            ("COLOR REAL", hex_real, h_r, s_r, b_r),
        ]:
            box = tk.Frame(comp, bg="#1a1a2e")
            box.pack(side="left", padx=20)
            tk.Label(box, text=title, bg="#1a1a2e", fg="#555577",
                     font=self.font_small).pack(pady=(8,4), padx=20)
            c = tk.Canvas(box, width=160, height=160, bg="#1a1a2e", highlightthickness=0)
            c.pack(padx=16)
            c.create_rectangle(8, 8, 152, 152, fill=hx, outline="#ffffff")
            tk.Label(box, text=hx.upper(), bg="#1a1a2e", fg="#777799",
                     font=self.font_value).pack(pady=(4,2))
            tk.Label(box, text=f"H{h}  S{s}  B{b}",
                     bg="#1a1a2e", fg="#555577", font=self.font_small).pack(pady=(0,8))

        tk.Label(self, text=f"«{ch['name']}»",
                 bg="#0f0f1a", fg="#7766cc", font=self.font_sub).pack(pady=(16, 4))
        prog_text = "  ·  ".join(f"{s:.1f}" for s in self.scores)
        tk.Label(self, text=f"Rondas: {prog_text}",
                 bg="#0f0f1a", fg="#444466", font=self.font_small).pack(pady=4)

        if self.round_num + 1 < TOTAL_ROUNDS:
            btn_text = f"Siguiente ronda →  ({self.round_num+2}/{TOTAL_ROUNDS})"
            cmd = self._next_round
        else:
            btn_text = "Ver resultado final 🏆"
            cmd = self._show_final

        tk.Button(self, text=btn_text,
                  bg="#7755ff", fg="white", font=self.font_btn,
                  bd=0, padx=24, pady=10,
                  activebackground="#9977ff", activeforeground="white",
                  cursor="hand2", command=cmd).pack(pady=20)

    def _next_round(self):
        self.round_num += 1
        self._show_round()

    # ── PANTALLA FINAL ───────────────────────────────────────────────────────
    def _show_final(self):
        self._clear()
        avg = sum(self.scores) / len(self.scores)

        if avg >= 8.5:  rank, color, msg = "S", "#ffd700", "¡Memoria de color perfecta!"
        elif avg >= 7:  rank, color, msg = "A", "#44dd88", "¡Excelente!"
        elif avg >= 5:  rank, color, msg = "B", "#66aaff", "Buen ojo"
        elif avg >= 3:  rank, color, msg = "C", "#ffcc44", "Sigue practicando"
        else:           rank, color, msg = "D", "#ff6655", "¡La práctica hace al maestro!"

        tk.Label(self, text="🎨  Resultado Final",
                 bg="#0f0f1a", fg="#aaaacc", font=self.font_title).pack(pady=(32, 4))
        tk.Label(self, text=f"Rango  {rank}",
                 bg="#0f0f1a", fg=color,
                 font=tkfont.Font(family="Helvetica", size=52, weight="bold")).pack(pady=4)
        tk.Label(self, text=f"Promedio: {avg:.2f} / 10   —   {msg}",
                 bg="#0f0f1a", fg=color, font=self.font_sub).pack(pady=(0, 20))

        detail = tk.Frame(self, bg="#0f0f1a")
        detail.pack(pady=4)
        for i, (ch, sc) in enumerate(zip(self.challenges, self.scores)):
            clr = "#44dd88" if sc >= 8 else "#ffcc44" if sc >= 5 else "#ff6655"
            bar_w = int(sc / 10 * 200)
            row = tk.Frame(detail, bg="#0f0f1a")
            row.pack(fill="x", pady=2, padx=30)
            tk.Label(row, text=f"R{i+1}", bg="#0f0f1a", fg="#555577",
                     font=self.font_small, width=3).pack(side="left")
            tk.Label(row, text=ch["name"], bg="#0f0f1a", fg="#888899",
                     font=self.font_small, width=22, anchor="w").pack(side="left")
            bar_bg = tk.Frame(row, bg="#1a1a2e", height=10, width=200)
            bar_bg.pack(side="left", padx=6)
            bar_bg.pack_propagate(False)
            tk.Frame(bar_bg, bg=clr, height=10, width=bar_w).place(x=0, y=0)
            tk.Label(row, text=f"{sc:.2f}", bg="#0f0f1a", fg=clr,
                     font=self.font_value, width=5).pack(side="left")

        btns = tk.Frame(self, bg="#0f0f1a")
        btns.pack(pady=24)
        tk.Button(btns, text="🔄  Jugar de nuevo",
                  bg="#7755ff", fg="white", font=self.font_btn,
                  bd=0, padx=20, pady=9,
                  activebackground="#9977ff", cursor="hand2",
                  command=self._new_game).pack(side="left", padx=8)
        tk.Button(btns, text="✕  Salir",
                  bg="#2a2a3e", fg="#aaaacc", font=self.font_btn,
                  bd=0, padx=20, pady=9,
                  activebackground="#3a3a5e", cursor="hand2",
                  command=self.destroy).pack(side="left", padx=8)


# ─── ENTRY POINT ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = ColorGame()
    app.mainloop()