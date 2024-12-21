"""
Model exported as python.
Name : 5.1 Gsm kpis
Group : 5.- Last_week_KPIs
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class GsmKpis(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(6, model_feedback)
        results = {}
        outputs = {}

        # Ejecutar SQL y cargar desde PostgreSQL voice acc
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_gsm_voice_acc_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlVoiceAcc'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa voice acc
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlVoiceAcc']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaVoiceAcc'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL voice ret
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_gsm_voice_ret_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlVoiceRet'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa voice ret
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlVoiceRet']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaVoiceRet'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto voice acc
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaVoiceAcc']['OUTPUT'],
            'NAME': '5.1 Gsm Voice accessibility'
        }
        outputs['CargarCapaEnElProyectoVoiceAcc'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto voice ret
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaVoiceRet']['OUTPUT'],
            'NAME': '5.1 Gsm Voice retainability '
        }
        outputs['CargarCapaEnElProyectoVoiceRet'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '5.1 Gsm kpis'

    def displayName(self):
        return '5.1 Gsm kpis'

    def group(self):
        return '5.- Last_week_KPIs'

    def groupId(self):
        return '5.- Last_week_KPIs'

    def createInstance(self):
        return GsmKpis()
