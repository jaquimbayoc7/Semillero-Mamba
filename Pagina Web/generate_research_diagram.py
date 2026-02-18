import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Crear figura con tamaño mayor
fig, ax = plt.subplots(figsize=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Colores CORHUILA
primary_green = '#1a7c5e'
secondary_green = '#2a9d7e'
accent_red = '#d32f2f'
light_bg = '#f8f9fa'

# Título
ax.text(5, 9.5, 'El Proceso de Investigación en el Semillero Mamba', 
        fontsize=26, fontweight='bold', ha='center', color=primary_green)
ax.text(5, 9.0, 'Paso a Paso hacia la Excelencia Académica', 
        fontsize=16, ha='center', color=secondary_green, style='italic')

# Definir pasos
steps = [
    {
        'num': '1',
        'title': 'Identificar\nProblema',
        'desc': 'Encontrar una problemática\nreal en desarrollo de software',
        'icon': '1️⃣',
        'x': 1,
        'y': 7.2
    },
    {
        'num': '2',
        'title': 'Investigación\nBibliográfica',
        'desc': 'Revisar literatura científica\ny trabajos previos relevantes',
        'icon': '2️⃣',
        'x': 3.2,
        'y': 7.2
    },
    {
        'num': '3',
        'title': 'Diseñar\nSolución',
        'desc': 'Proponer metodología y\napproach científico riguroso',
        'icon': '3️⃣',
        'x': 5.4,
        'y': 7.2
    },
    {
        'num': '4',
        'title': 'Implementar',
        'desc': 'Desarrollar con académicos\ny estándares profesionales',
        'icon': '4️⃣',
        'x': 7.6,
        'y': 7.2
    },
    {
        'num': '5',
        'title': 'Validar\nResultados',
        'desc': 'Realizar pruebas y\nevaluación exhaustiva',
        'icon': '5️⃣',
        'x': 9.2,
        'y': 7.2
    },
    {
        'num': '6',
        'title': 'Publicar y\nDifundir',
        'desc': 'Compartir en conferencias\ny revistas académicas',
        'icon': '6️⃣',
        'x': 5.4,
        'y': 3
    }
]

# Dibujar cajas para cada paso
for i, step in enumerate(steps):
    x, y = step['x'], step['y']
    
    # Si es el último paso, hacer la caja más grande y centrada
    if i == 5:
        box_width = 2.8
    else:
        box_width = 2.2
    
    box_height = 2.0
    
    # Crear caja redondeada
    fancy_box = FancyBboxPatch(
        (x - box_width/2, y - box_height/2),
        box_width, box_height,
        boxstyle="round,pad=0.15",
        linewidth=3,
        edgecolor=secondary_green,
        facecolor='white',
        zorder=2
    )
    ax.add_patch(fancy_box)
    
    # Número del paso (círculo)
    circle = plt.Circle((x, y + box_height/2 - 0.35), 0.35, 
                        color=accent_red, zorder=3)
    ax.add_patch(circle)
    ax.text(x, y + box_height/2 - 0.35, step['num'], 
            fontsize=14, fontweight='bold', ha='center', va='center', 
            color='white', zorder=4)
    
    # Icono
    ax.text(x, y + 0.45, step['icon'], fontsize=32, ha='center', va='center', zorder=3)
    
    # Título
    ax.text(x, y - 0.10, step['title'], fontsize=12, fontweight='bold', 
            ha='center', va='center', color=primary_green, zorder=3)
    
    # Descripción
    ax.text(x, y - 0.75, step['desc'], fontsize=9, ha='center', va='center', 
            color='#555', style='italic', zorder=3)

# Dibujar flechas entre pasos
arrows = [
    ((1.8, 7), (2.1, 7)),  # 1 -> 2
    ((3.8, 7), (4.1, 7)),  # 2 -> 3
    ((5.8, 7), (6.1, 7)),  # 3 -> 4
    ((7.8, 7), (8.1, 7)),  # 4 -> 5
    ((9, 6.2), (8.5, 4.2)),  # 5 -> 6
    ((4, 2.2), (1.6, 6.2)),  # 6 -> 1 (feedback loop)
]

for start, end in arrows:
    if start == (4, 2.2):  # Flecha de feedback curva
        arrow = FancyArrowPatch(start, end,
                              arrowstyle='->,head_width=0.3,head_length=0.3',
                              color=secondary_green, linewidth=2,
                              connectionstyle="arc3,rad=0.5", zorder=1)
    else:
        arrow = FancyArrowPatch(start, end,
                              arrowstyle='->,head_width=0.2,head_length=0.2',
                              color=secondary_green, linewidth=2, zorder=1)
    ax.add_patch(arrow)

# Área de feedback
ax.text(5.4, 1.3, '↩️ Iteración Continua', fontsize=12, 
        ha='center', color=secondary_green, fontweight='bold', style='italic')

# Información adicional en bottom
info_box = FancyBboxPatch(
    (0.3, -0.25), 9.4, 1.2,
    boxstyle="round,pad=0.1",
    linewidth=1,
    edgecolor=light_bg,
    facecolor=light_bg,
    zorder=0
)
ax.add_patch(info_box)

info_text = '💡 En el Semillero Mamba cada paso es revisado por coordinadores expertos y refinado basado en feedback académico riguroso'
ax.text(5, 0.35, info_text, fontsize=11, ha='center', va='center', 
        color='#555', style='italic', weight='bold')

# Guardar figura con mejor resolución
plt.tight_layout(pad=0.5)
plt.savefig('research-process-diagram.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.3)
print("✅ Imagen generada: research-process-diagram.png (300 DPI)")

plt.close()

# Crear una segunda imagen más simple
fig, ax = plt.subplots(figsize=(16, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Título
ax.text(5, 9.6, 'Ciclo de Investigación Científica', 
        fontsize=24, fontweight='bold', ha='center', color=primary_green)
ax.text(5, 9.1, 'Proceso Riguroso y Sistemático', 
        fontsize=16, ha='center', color=secondary_green, style='italic')

# Crear un ciclo circular
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
radius = 3.2
center_x, center_y = 5, 5.2

cycle_steps = [
    {'label': 'Pregunta de\nInvestigación', 'icon': '❓', 'color': primary_green},
    {'label': 'Revisión de\nLiteratura', 'icon': '📖', 'color': secondary_green},
    {'label': 'Hipótesis y\nDiseño', 'icon': '📋', 'color': accent_red},
    {'label': 'Ejecución del\nProyecto', 'icon': '⚙️', 'color': primary_green},
    {'label': 'Análisis de\nResultados', 'icon': '📊', 'color': secondary_green},
    {'label': 'Conclusiones\ny Publicación', 'icon': '📝', 'color': accent_red},
]

for i, (angle, step) in enumerate(zip(angles, cycle_steps)):
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    
    # Crear círculo para cada paso
    circle = plt.Circle((x, y), 0.85, 
                       color=step['color'], alpha=0.15, zorder=1)
    ax.add_patch(circle)
    
    circle_border = plt.Circle((x, y), 0.85, 
                              color=step['color'], alpha=1, 
                              fill=False, linewidth=3, zorder=2)
    ax.add_patch(circle_border)
    
    # Icono más grande
    ax.text(x, y + 0.15, step['icon'], fontsize=32, ha='center', va='center', zorder=3)
    
    # Etiqueta con mejor posición
    ax.text(x, y - 1.5, step['label'], fontsize=11, ha='center', va='top', 
            fontweight='bold', color=step['color'], zorder=3)

# Dibujar flechas circulares
for i in range(len(cycle_steps)):
    start_angle = angles[i]
    end_angle = angles[(i + 1) % len(cycle_steps)]
    
    start_x = center_x + radius * np.cos(start_angle)
    start_y = center_y + radius * np.sin(start_angle)
    end_x = center_x + radius * np.cos(end_angle)
    end_y = center_y + radius * np.sin(end_angle)
    
    arrow = FancyArrowPatch(
        (start_x * 0.80 + center_x * 0.20, start_y * 0.80 + center_y * 0.20),
        (end_x * 0.80 + center_x * 0.20, end_y * 0.80 + center_y * 0.20),
        arrowstyle='->,head_width=0.35,head_length=0.35',
        color=secondary_green, linewidth=3.5, zorder=1,
        connectionstyle="arc3,rad=0.35"
    )
    ax.add_patch(arrow)

# Centro con texto
center_circle = plt.Circle((center_x, center_y), 1.3, 
                          color=light_bg, zorder=2, edgecolor=primary_green, linewidth=3)
ax.add_patch(center_circle)

ax.text(center_x, center_y + 0.25, 'Investigación', fontsize=14, fontweight='bold',
        ha='center', va='center', color=primary_green, zorder=3)
ax.text(center_x, center_y - 0.35, 'Rigurosa', fontsize=14, fontweight='bold',
        ha='center', va='center', color=primary_green, zorder=3)

# Info bottom
info_text = 'Este ciclo se repite iterativamente hasta alcanzar conclusiones robustas y publicables'
ax.text(5, 0.4, info_text, fontsize=12, ha='center', color='#666', style='italic', weight='bold',
        bbox=dict(boxstyle='round', facecolor=light_bg, alpha=0.9, pad=0.6, linewidth=1.5, edgecolor=secondary_green))

plt.tight_layout(pad=0.5)
plt.savefig('research-cycle.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.3)
print("✅ Imagen generada: research-cycle.png (300 DPI)")

print("\n✨ Ambas imágenes han sido generadas exitosamente!")
print("   - research-process-diagram.png")
print("   - research-cycle.png")
