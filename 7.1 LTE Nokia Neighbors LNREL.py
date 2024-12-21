"""
Model exported as python.
Name : 7.1 LTE Nokia Neighbors LNREL
Group : 7.- Optimization LTE Nokia parameters
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class LteNokiaNeighborsLnrel(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Ejecutar SQL y cargar desde PostgreSQL lnrel
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': "SELECT * FROM cm_nokia_lte.lte_nokia_source_neighbors_lnrel('20251')"
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlLnrel'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa lnrel
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlLnrel']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_optimization\\LTE Nokia Neighbors lnrel.qml'
        }
        outputs['EstablecerElEstiloDeCapaLnrel'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto lnrel
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaLnrel']['OUTPUT'],
            'NAME': '7.1 LTE Nokia Neighbors lnrel'
        }
        outputs['CargarCapaEnElProyectoLnrel'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '7.1 LTE Nokia Neighbors LNREL'

    def displayName(self):
        return '7.1 LTE Nokia Neighbors LNREL'

    def group(self):
        return '7.- Optimization LTE Nokia parameters'

    def groupId(self):
        return '7.- Optimization LTE Nokia parameters'

    def createInstance(self):
        return LteNokiaNeighborsLnrel()
