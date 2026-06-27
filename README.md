# 🎨 Color Memory

Un juego de memoria visual inspirado en [Toon Tone](https://toontone.app/es/). Cada ronda te muestra un personaje animado y tenés que adivinar el color exacto de una parte de su cuerpo usando sliders de Matiz, Saturación y Brillo.

**[▶ Jugar ahora](https://devmayra.github.io/color-memory-game/)**

---

## Cómo se juega

1. Aparece un personaje animado y una pregunta: *¿De qué color es X de X?*
2. Ajustás los tres sliders (H / S / B) hasta que el color de la derecha te parezca correcto
3. Confirmás y el juego te muestra qué tan cerca estuviste
4. Son 5 rondas, al final te da un rango de **D** a **S**

## Puntaje

El sistema penaliza más equivocarse en el **Matiz** (el color base) que en Saturación o Brillo, igual que el juego original. La curva es exponencial: llegar a un 9 o 10 requiere estar muy cerca.

---

## Historia del proyecto

El prototipo fue hecho con **Python + tkinter** para definir la mecánica del juego: los sliders HSB, el algoritmo de scoring y el flujo de pantallas. Una vez que funcionó, lo porté a HTML/CSS/JS para poder jugarlo en el navegador sin instalar nada.

Se adjuntó el código original en la carpeta `/python`  también.

---

## Correrlo localmente

Solo abrís `index.html` en el navegador. No necesita servidor ni dependencias.

```bash
git clone https://github.com/devmayra/color-memory.git
cd color-memory
# abrís index.html con doble click o:
start index.html        # Windows
open index.html         # Mac
```
Para correr el prototipo Python:

```bash
cd python
pip install Pillow
python color_game.py
```
---

## Stack

- HTML + CSS + JavaScript puro (sin frameworks)
- Sin backend, sin dependencias externas
- Prototipo original: Python 3 + tkinter + Pillow

## Disclaimer

Este proyecto fue desarrollado con fines educativos y de aprendizaje. Los personajes utilizados pertenecen a sus respectivos dueños. Toon Tone es el juego original que inspiró este ejercicio.
