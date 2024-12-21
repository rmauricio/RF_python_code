from qgis.core import QgsProject, QgsCategorizedSymbolRenderer, QgsRendererCategory
from PyQt5.QtGui import QColor

# Nombres de las capas y campos comunes
nombre_capa_puntos = "PCI_2131099650_LTEINCERPAZ"
nombre_capa_poligonos = "tb_ep_lte_fdd_carrier1"
campo_comun_puntos = "PCI"
campo_comun_poligonos = "phycellid"

# Obtener las capas por nombre
layer1 = QgsProject.instance().mapLayersByName(nombre_capa_puntos)[0]
layer2 = QgsProject.instance().mapLayersByName(nombre_capa_poligonos)[0]

# Obtener índices de campo
index_puntos = layer1.fields().lookupField(campo_comun_puntos)
index_poligonos = layer2.fields().lookupField(campo_comun_poligonos)

# Unir todas las características de ambas capas
features = []
features.extend(layer1.getFeatures())
features.extend(layer2.getFeatures())

# Obtener valores únicos en el campo común
values = set()
for feature in features:
    if feature.geometry():
        if feature.fields().indexFromName(campo_comun_puntos) != -1:
            values.add(feature[campo_comun_puntos])
        elif feature.fields().indexFromName(campo_comun_poligonos) != -1:
            values.add(feature[campo_comun_poligonos])

# Crear un diccionario para asignar colores a los valores
color_dict = {}
for value in values:
    color_dict[value] = "#{:06x}".format(hash(str(value)) & 0xFFFFFF)  # Asignar color basado en el valor

# Asignar el renderizador a la capa de puntos
renderer_puntos = QgsCategorizedSymbolRenderer(campo_comun_puntos, [])
for value, color in color_dict.items():
    symbol = QgsSymbol.defaultSymbol(layer1.geometryType())
    symbol.setColor(QColor(color))
    symbol_layer = symbol.symbolLayer(0)
    symbol_layer.setStrokeColor(QColor('#00000000'))  # Hacer transparente el contorno
    category = QgsRendererCategory(value, symbol, str(value))
    renderer_puntos.addCategory(category)
layer1.setRenderer(renderer_puntos)

# Asignar el renderizador a la capa de polígonos
renderer_poligonos = QgsCategorizedSymbolRenderer(campo_comun_poligonos, [])
for value, color in color_dict.items():
    symbol = QgsSymbol.defaultSymbol(layer2.geometryType())
    symbol.setColor(QColor(color))
    category = QgsRendererCategory(value, symbol, str(value))
    renderer_poligonos.addCategory(category)
layer2.setRenderer(renderer_poligonos)

# Refrescar las capas en QGIS
layer1.triggerRepaint()
layer2.triggerRepaint()
