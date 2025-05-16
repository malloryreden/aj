# Basado en el rango vocal proporcionado (E2 a D4), vamos a visualizar el rango y verificar que se mantenga dentro del uso efectivo para MAIKA.
import matplotlib.pyplot as plt
import numpy as np

# Notas desde E2 a D4
notes = [
    "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2",
    "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3",
    "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4"
]

# Convert note names to MIDI numbers (E2 = 40, D4 = 62)
note_midi = list(range(40, 63))
frequencies = [440 * 2 ** ((n - 69) / 12) for n in note_midi]

# Plotting the vocal range
plt.figure(figsize=(12, 2))
plt.barh(["MAIKA Vocal Range (E2–D4)"], [note_midi[-1] - note_midi[0]], left=note_midi[0], color="skyblue")
plt.yticks([])
plt.xticks(note_midi, notes, rotation=45)
plt.title("Rango Vocal de MAIKA (E2 a D4)")
plt.grid(axis="x")
plt.tight_layout()
plt.show()
