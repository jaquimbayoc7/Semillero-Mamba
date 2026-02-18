from PIL import Image, ImageDraw, ImageFont
import math

# Crear imagen 1: Proceso de Investigación
width, height = 1920, 1440
img1 = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img1, 'RGBA')

# Colores CORHUILA
primary_green = '#1a7c5e'
secondary_green = '#2a9d7e'
accent_red = '#d32f2f'
light_gray = '#f5f5f5'

# Intentar cargar fuentes
try:
    title_font = ImageFont.truetype("arial.ttf", 80)
    subtitle_font = ImageFont.truetype("arial.ttf", 48)
    step_title_font = ImageFont.truetype("arial.ttf", 40)
    step_desc_font = ImageFont.truetype("arial.ttf", 28)
    info_font = ImageFont.truetype("arial.ttf", 32)
except:
    from PIL import ImageFont
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    step_title_font = ImageFont.load_default()
    step_desc_font = ImageFont.load_default()
    info_font = ImageFont.load_default()

# Dibujar fondo sutil
for y in range(height):
    opacity = int(20 * (1 - y / height))

# Título
draw.text((width//2, 80), "El Proceso de Investigacion en el Semillero Mamba", 
          font=title_font, fill=primary_green, anchor="mm")
draw.text((width//2, 160), "Pasos hacia la Excelencia Academica", 
          font=subtitle_font, fill=secondary_green, anchor="mm")

# Definir posiciones de pasos (horizontal)
steps_data = [
    {"num": "1", "title": "Identificar\nProblema", "desc": "Encontrar problematica\nreal en software"},
    {"num": "2", "title": "Investigacion\nBibliografica", "desc": "Revisar literatura\ncientifica"},
    {"num": "3", "title": "Disenar\nSolucion", "desc": "Proponer metodologia\ncientifica"},
    {"num": "4", "title": "Implementar", "desc": "Desarrollar con\nestandares academicos"},
    {"num": "5", "title": "Validar\nResultados", "desc": "Pruebas exhaustivas\ny evaluacion"},
    {"num": "6", "title": "Publicar y\nDifundir", "desc": "Conferencias y\nrevistas academicas"},
]

# Primera fila (5 pasos)
y_pos_1 = 350
x_positions_1 = [150 + i * 330 for i in range(5)]

for i, step in enumerate(steps_data[:5]):
    x = x_positions_1[i]
    
    # Caja redondeada
    box_width = 280
    box_height = 200
    draw.rectangle(
        [(x - box_width//2, y_pos_1 - box_height//2), 
         (x + box_width//2, y_pos_1 + box_height//2)],
        outline=secondary_green, width=4, fill=(255, 255, 255)
    )
    
    # Numero en circulo rojo
    circle_radius = 35
    draw.ellipse(
        [(x - circle_radius, y_pos_1 - box_height//2 - circle_radius),
         (x + circle_radius, y_pos_1 - box_height//2 + circle_radius)],
        fill=accent_red
    )
    draw.text((x, y_pos_1 - box_height//2), step['num'],
              font=step_title_font, fill='white', anchor="mm")
    
    # Titulo
    draw.text((x, y_pos_1 - 20), step['title'],
              font=step_title_font, fill=primary_green, anchor="mm")
    
    # Descripcion
    draw.text((x, y_pos_1 + 60), step['desc'],
              font=step_desc_font, fill='#666666', anchor="mm")
    
    # Flecha horizontal (excepto ultimo)
    if i < 4:
        arrow_x = x + box_width//2 + 20
        arrow_end_x = x_positions_1[i+1] - box_width//2 - 20
        draw.line([(arrow_x, y_pos_1), (arrow_end_x, y_pos_1)], 
                  fill=secondary_green, width=3)
        # Punta de flecha
        draw.polygon([(arrow_end_x, y_pos_1), 
                      (arrow_end_x - 20, y_pos_1 - 15),
                      (arrow_end_x - 20, y_pos_1 + 15)],
                     fill=secondary_green)

# Segundo paso (paso 6 en el centro abajo)
y_pos_2 = 750
x_pos_2 = width // 2
step_6 = steps_data[5]

# Caja para paso 6
box_width = 320
box_height = 220
draw.rectangle(
    [(x_pos_2 - box_width//2, y_pos_2 - box_height//2), 
     (x_pos_2 + box_width//2, y_pos_2 + box_height//2)],
    outline=secondary_green, width=4, fill=(255, 255, 255)
)

# Numero en circulo
circle_radius = 35
draw.ellipse(
    [(x_pos_2 - circle_radius, y_pos_2 - box_height//2 - circle_radius),
     (x_pos_2 + circle_radius, y_pos_2 - box_height//2 + circle_radius)],
    fill=accent_red
)
draw.text((x_pos_2, y_pos_2 - box_height//2), step_6['num'],
          font=step_title_font, fill='white', anchor="mm")

# Titulo paso 6
draw.text((x_pos_2, y_pos_2 - 20), step_6['title'],
          font=step_title_font, fill=primary_green, anchor="mm")

# Descripcion paso 6
draw.text((x_pos_2, y_pos_2 + 70), step_6['desc'],
          font=step_desc_font, fill='#666666', anchor="mm")

# Flechas de retroalimentacion (desde paso 5 hacia paso 1)
draw.text((width//2, 950), "Iteracion Continua",
          font=info_font, fill=secondary_green, anchor="mm")

# Informacion inferior
info_box_y = 1100
draw.rectangle([(100, info_box_y), (width-100, info_box_y + 280)],
               outline=secondary_green, width=3, fill=(245, 250, 248))

info_text = "En el Semillero Mamba cada paso es revisado por coordinadores expertos\ny refinado continuamente basado en feedback academico riguroso"
draw.text((width//2, info_box_y + 140), info_text,
          font=info_font, fill='#333333', anchor="mm")

# Guardar
img1.save('research-process-diagram.png', 'PNG', quality=95)
print("Imagen 1 generada: research-process-diagram.png")

# ============================================
# Crear imagen 2: Ciclo de Investigacion
# ============================================
img2 = Image.new('RGB', (1800, 1900), color='white')
draw2 = ImageDraw.Draw(img2, 'RGBA')

# Titulo
draw2.text((900, 50), "Ciclo de Investigacion Cientifica",
           font=title_font, fill=primary_green, anchor="mm")
draw2.text((900, 130), "Proceso Riguroso y Sistematico",
           font=subtitle_font, fill=secondary_green, anchor="mm")

# Datos del ciclo
cycle_steps = [
    "Pregunta de\nInvestigacion",
    "Revision de\nLiteratura",
    "Hipotesis y\nDiseño",
    "Ejecucion del\nProyecto",
    "Analisis de\nResultados",
    "Conclusiones y\nPublicacion",
]

# Posiciones en circulo
center_x, center_y = 900, 1000
radius = 420

# Colores alternos para pasos
colors = [primary_green, secondary_green, accent_red] * 2

for i, title in enumerate(cycle_steps):
    angle = (i * 360 / len(cycle_steps)) - 90
    rads = math.radians(angle)
    
    x = center_x + radius * math.cos(rads)
    y = center_y + radius * math.sin(rads)
    
    color = colors[i]
    
    # Circulo principal para cada paso (ampliado)
    circle_r = 100
    draw2.ellipse([(x - circle_r, y - circle_r),
                   (x + circle_r, y + circle_r)],
                  outline=color, width=5, fill=(255, 255, 255))
    
    # Numero en circulo rojo (arriba del circulo principal)
    num_circle_r = 32
    num_y = y - circle_r - 50
    draw2.ellipse([(x - num_circle_r, num_y - num_circle_r),
                   (x + num_circle_r, num_y + num_circle_r)],
                  fill=accent_red)
    draw2.text((x, num_y), str(i+1),
               font=step_title_font, fill='white', anchor="mm")
    
    # Etiqueta FUERA del circulo, posicionada según el ángulo
    # Para el paso 1, aumentar distancia hacía arriba
    if i == 0:  # Paso 1 - mover más hacia arriba
        text_distance = circle_r + 120
    else:
        text_distance = circle_r + 90
    text_x = x + text_distance * math.cos(rads)
    text_y = y + text_distance * math.sin(rads)
    draw2.text((text_x, text_y), title,
               font=step_title_font, fill=color, anchor="mm")
    
    # Flecha al siguiente paso
    next_i = (i + 1) % len(cycle_steps)
    next_angle = (next_i * 360 / len(cycle_steps)) - 90
    next_rads = math.radians(next_angle)
    
    next_x = center_x + radius * math.cos(next_rads)
    next_y = center_y + radius * math.sin(next_rads)
    
    # Ajustar para que la flecha salga del circulo
    from_x = x + (circle_r + 15) * math.cos(rads)
    from_y = y + (circle_r + 15) * math.sin(rads)
    to_x = next_x - (circle_r + 15) * math.cos(next_rads)
    to_y = next_y - (circle_r + 15) * math.sin(next_rads)
    
    draw2.line([(from_x, from_y), (to_x, to_y)],
               fill=secondary_green, width=5)

# Centro circulo (ampliado)
center_r = 140
draw2.ellipse([(center_x - center_r, center_y - center_r),
               (center_x + center_r, center_y + center_r)],
              outline=primary_green, width=4, fill=(245, 250, 248))
draw2.text((center_x, center_y - 30), "Investigacion",
           font=step_title_font, fill=primary_green, anchor="mm")
draw2.text((center_x, center_y + 30), "Rigurosa",
           font=step_title_font, fill=primary_green, anchor="mm")

# Info box
info_y = 1650
draw2.rectangle([(80, info_y), (1720, info_y + 200)],
                outline=secondary_green, width=3, fill=(245, 250, 248))
info_text2 = "Este ciclo se repite iterativamente hasta alcanzar conclusiones robustas y publicables"
draw2.text((900, info_y + 100), info_text2,
           font=info_font, fill='#333333', anchor="mm")

# Guardar
img2.save('research-cycle.png', 'PNG', quality=95)
print("Imagen 2 generada: research-cycle.png")

print("\n✨ Ambas imagenes han sido generadas con PIL/Pillow!")
print("   - Maxima calidad y nitidez")
print("   - Sin distorsiones")
print("   - Colores vibrantes CORHUILA")
