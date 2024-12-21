"""
Model exported as python.
Name : 7.3 Phycellid cell
Group : 7.- Optimization LTE Nokia parameters
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class PhycellidCell(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Ejecutar SQL y cargar desde PostgreSQL
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select *\nfrom site_and_cell_information."07_lte_fdd_cells"v'
        }
        outputs['EjecutarSqlYCargarDesdePostgresql'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresql']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_optimization\\LTE phycellid.qml'
        }
        outputs['EstablecerElEstiloDeCapa'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapa']['OUTPUT'],
            'NAME': '7.3 Phycellid cell'
        }
        outputs['CargarCapaEnElProyecto'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '7.3 Phycellid cell'

    def displayName(self):
        return '7.3 Phycellid cell'

    def group(self):
        return '7.- Optimization LTE Nokia parameters'

    def groupId(self):
        return '7.- Optimization LTE Nokia parameters'

    def createInstance(self):
        return PhycellidCell()
