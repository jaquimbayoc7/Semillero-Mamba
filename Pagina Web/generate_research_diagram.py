import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Crear figura
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Colores CORHUILA
primary_green = '#1a7c5e'
secondary_green = '#2a9d7e'
accent_red = '#d32f2f'
light_bg = '#f8f9fa'

# Título
ax.text(5, 9.3, 'El Proceso de Investigación en el Semillero Mamba', 
        fontsize=20, fontweight='bold', ha='center', color=primary_green)
ax.text(5, 8.9, 'Paso a Paso', 
        fontsize=14, ha='center', color=secondary_green, style='italic')

# Definir pasos
steps = [
    {
        'num': '1',
        'title': 'Identificar\nProblema',
        'desc': 'Encontrar una problemática\nreal en software',
        'icon': '🔍',
        'x': 1,
        'y': 7
    },
    {
        'num': '2',
        'title': 'Investigación\nBibliográfica',
        'desc': 'Revisar literatura científica\ny trabajos previos',
        'icon': '📚',
        'x': 3,
        'y': 7
    },
    {
        'num': '3',
        'title': 'Diseñar\nSolución',
        'desc': 'Proponer metodología y\napproach científico',
        'icon': '✏️',
        'x': 5,
        'y': 7
    },
    {
        'num': '4',
        'title': 'Implementar',
        'desc': 'Desarrollar la solución\ncon rigor académico',
        'icon': '💻',
        'x': 7,
        'y': 7
    },
    {
        'num': '5',
        'title': 'Validar\nResultados',
        'desc': 'Realizar pruebas y\nevaluación exhaustiva',
        'icon': '✅',
        'x': 9,
        'y': 7
    },
    {
        'num': '6',
        'title': 'Publicar y\nDifundir',
        'desc': 'Compartir en conferencias\ny revistas académicas',
        'icon': '📢',
        'x': 5,
        'y': 3
    }
]

# Dibujar cajas para cada paso
for i, step in enumerate(steps):
    x, y = step['x'], step['y']
    
    # Si es el último paso, hacer la caja más grande y centrada
    if i == 5:
        box_width = 2.2
    else:
        box_width = 1.8
    
    box_height = 1.6
    
    # Crear caja redondeada
    fancy_box = FancyBboxPatch(
        (x - box_width/2, y - box_height/2),
        box_width, box_height,
        boxstyle="round,pad=0.1",
        linewidth=2,
        edgecolor=secondary_green,
        facecolor='white',
        zorder=2
    )
    ax.add_patch(fancy_box)
    
    # Número del paso (círculo)
    circle = plt.Circle((x, y + box_height/2 - 0.25), 0.28, 
                        color=accent_red, zorder=3)
    ax.add_patch(circle)
    ax.text(x, y + box_height/2 - 0.25, step['num'], 
            fontsize=12, fontweight='bold', ha='center', va='center', 
            color='white', zorder=4)
    
    # Icono
    ax.text(x, y + 0.4, step['icon'], fontsize=28, ha='center', va='center', zorder=3)
    
    # Título
    ax.text(x, y - 0.15, step['title'], fontsize=9, fontweight='bold', 
            ha='center', va='center', color=primary_green, zorder=3)
    
    # Descripción
    ax.text(x, y - 0.65, step['desc'], fontsize=7, ha='center', va='center', 
            color='#666', style='italic', zorder=3)

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
ax.text(3.5, 1.3, '🔄 Iteración Continua', fontsize=10, 
        ha='center', color=secondary_green, fontweight='bold', style='italic')

# Información adicional en bottom
info_box = FancyBboxPatch(
    (0.5, 0.05), 9, 0.8,
    boxstyle="round,pad=0.08",
    linewidth=1,
    edgecolor=light_bg,
    facecolor=light_bg,
    zorder=0
)
ax.add_patch(info_box)

info_text = '💡 En el Semillero Mamba cada paso es revisado por coordinadores expertos y refinado basado en feedback académico'
ax.text(5, 0.45, info_text, fontsize=9, ha='center', va='center', 
        color='#666', style='italic')

# Guardar figura
plt.tight_layout()
plt.savefig('research-process-diagram.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✅ Imagen generada: research-process-diagram.png")

plt.close()

# Crear una segunda imagen más simple
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Título
ax.text(5, 9.5, 'Ciclo de Investigación Científica', 
        fontsize=18, fontweight='bold', ha='center', color=primary_green)

# Crear un ciclo circular
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
radius = 3
center_x, center_y = 5, 5

cycle_steps = [
    {'label': 'Pregunta\nde Investigación', 'icon': '❓', 'color': primary_green},
    {'label': 'Revisión de\nLiteratura', 'icon': '📖', 'color': secondary_green},
    {'label': 'Hipótesis y\nDiseño', 'icon': '📋', 'color': accent_red},
    {'label': 'Ejecución del\nProyecto', 'icon': '⚙️', 'color': primary_green},
    {'label': 'Análisis de\nResultados', 'icon': '📊', 'color': secondary_green},
    {'label': 'Conclusiones y\nPublicación', 'icon': '📝', 'color': accent_red},
]

for i, (angle, step) in enumerate(zip(angles, cycle_steps)):
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    
    # Crear círculo para cada paso
    circle = plt.Circle((x, y), 0.7, 
                       color=step['color'], alpha=0.2, zorder=1)
    ax.add_patch(circle)
    
    circle_border = plt.Circle((x, y), 0.7, 
                              color=step['color'], alpha=1, 
                              fill=False, linewidth=2, zorder=2)
    ax.add_patch(circle_border)
    
    # Icono
    ax.text(x, y + 0.15, step['icon'], fontsize=24, ha='center', va='center', zorder=3)
    
    # Etiqueta
    ax.text(x, y - 1.2, step['label'], fontsize=9, ha='center', va='top', 
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
        (start_x * 0.85 + center_x * 0.15, start_y * 0.85 + center_y * 0.15),
        (end_x * 0.85 + center_x * 0.15, end_y * 0.85 + center_y * 0.15),
        arrowstyle='->,head_width=0.25,head_length=0.25',
        color=secondary_green, linewidth=2.5, zorder=1,
        connectionstyle="arc3,rad=0.3"
    )
    ax.add_patch(arrow)

# Centro con texto
center_circle = plt.Circle((center_x, center_y), 1.2, 
                          color=light_bg, zorder=2, edgecolor=primary_green, linewidth=2)
ax.add_patch(center_circle)

ax.text(center_x, center_y + 0.2, 'Investigación', fontsize=12, fontweight='bold',
        ha='center', va='center', color=primary_green, zorder=3)
ax.text(center_x, center_y - 0.3, 'Rigurosa', fontsize=12, fontweight='bold',
        ha='center', va='center', color=primary_green, zorder=3)

# Info bottom
ax.text(5, 0.5, 'Este ciclo se repite iterativamente hasta alcanzar conclusiones robustas y publicables', 
        fontsize=10, ha='center', color='#666', style='italic',
        bbox=dict(boxstyle='round', facecolor=light_bg, alpha=0.8, pad=0.5))

plt.tight_layout()
plt.savefig('research-cycle.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✅ Imagen generada: research-cycle.png")

print("\n✨ Ambas imágenes han sido generadas exitosamente!")
print("   - research-process-diagram.png")
print("   - research-cycle.png")
