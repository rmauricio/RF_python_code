"""
Model exported as python.
Name : 4.1 Gsm simulation
Group : 4.- Rf simulation
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class GsmSimulation(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(6, model_feedback)
        results = {}
        outputs = {}

        # Ejecutar SQL y cargar desde PostgreSQL bs
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geom',
            'ID_FIELD': 'id',
            'SQL': 'select * from drivetest_and_simulations.simulation_gsm_best_server'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlBs'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa bs
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlBs']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Drivetest_and_Simulation\\generic_best_server.qml'
        }
        outputs['EstablecerElEstiloDeCapaBs'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL level
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geom',
            'ID_FIELD': 'id',
            'SQL': 'select * from drivetest_and_simulations.simulation_gsm_rxlev'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlLevel'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa level
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlLevel']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Drivetest_and_Simulation\\simulation_gsm_rxlev.qml'
        }
        outputs['EstablecerElEstiloDeCapaLevel'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto bs
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaBs']['OUTPUT'],
            'NAME': '4.1 Gsm Best server'
        }
        outputs['CargarCapaEnElProyectoBs'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto level
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaLevel']['OUTPUT'],
            'NAME': '4.1 Gsm RxLevel'
        }
        outputs['CargarCapaEnElProyectoLevel'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '4.1 Gsm simulation'

    def displayName(self):
        return '4.1 Gsm simulation'

    def group(self):
        return '4.- Rf simulation'

    def groupId(self):
        return '4.- Rf simulation'

    def createInstance(self):
        return GsmSimulation()
