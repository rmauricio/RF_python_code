"""
Model exported as python.
Name : 5.2 Umts kpis
Group : 5.- Last_week_KPIs
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class UmtsKpis(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(15, model_feedback)
        results = {}
        outputs = {}

        # Ejecutar SQL y cargar desde PostgreSQL data int
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_umts_data_int_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlDataInt'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL voice acc
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_umts_voice_acc_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlVoiceAcc'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL data acc
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_umts_data_acc_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlDataAcc'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa voice acc
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlVoiceAcc']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaVoiceAcc'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL voice ret
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_umts_voice_ret_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlVoiceRet'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL data ret
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_umts_data_ret_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlDataRet'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa voice ret
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlVoiceRet']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaVoiceRet'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa data int
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlDataInt']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaDataInt'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa data acc
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlDataAcc']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaDataAcc'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(9)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto voice acc
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaVoiceAcc']['OUTPUT'],
            'NAME': '5.2 Umts Voice accessibility'
        }
        outputs['CargarCapaEnElProyectoVoiceAcc'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(10)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto voice ret
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaVoiceRet']['OUTPUT'],
            'NAME': '5.2 Umts Voice retainability '
        }
        outputs['CargarCapaEnElProyectoVoiceRet'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(11)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa data ret
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlDataRet']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaDataRet'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(12)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto data ret
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaDataRet']['OUTPUT'],
            'NAME': '5.2 Umts Data retainability '
        }
        outputs['CargarCapaEnElProyectoDataRet'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(13)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto data int
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaDataInt']['OUTPUT'],
            'NAME': '5.2 Umts Data Integrity '
        }
        outputs['CargarCapaEnElProyectoDataInt'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(14)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto dat acc
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaDataAcc']['OUTPUT'],
            'NAME': '5.2 Umts Data accessibility'
        }
        outputs['CargarCapaEnElProyectoDatAcc'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '5.2 Umts kpis'

    def displayName(self):
        return '5.2 Umts kpis'

    def group(self):
        return '5.- Last_week_KPIs'

    def groupId(self):
        return '5.- Last_week_KPIs'

    def createInstance(self):
        return UmtsKpis()
