"""
Model exported as python.
Name : 2.3 Bolivia localities
Group : 2.- Geo_Data_Information
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class BoliviaLocalities(QgsProcessingAlgorithm):

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
            'GEOMETRY_FIELD': 'geom',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_data_information.localidades_bolivia_registro_new_sites'
        }
        outputs['EjecutarSqlYCargarDesdePostgresql'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresql']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Data_Information\\localidades_bolivia_registro_new_sites.qml'
        }
        outputs['EstablecerElEstiloDeCapa'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapa']['OUTPUT'],
            'NAME': '2.3 Bolivia localities'
        }
        outputs['CargarCapaEnElProyecto'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '2.3 Bolivia localities'

    def displayName(self):
        return '2.3 Bolivia localities'

    def group(self):
        return '2.- Geo_Data_Information'

    def groupId(self):
        return '2.- Geo_Data_Information'

    def createInstance(self):
        return BoliviaLocalities()
