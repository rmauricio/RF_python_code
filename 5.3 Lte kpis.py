"""
Model exported as python.
Name : 5.3 Lte kpis
Group : 5.- Last_week_KPIs
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class LteKpis(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(12, model_feedback)
        results = {}
        outputs = {}

        # Ejecutar SQL y cargar desde PostgreSQL data int
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_lte_data_int_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlDataInt'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL data p95_prb
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select *\nfrom geo_kpis_report.weekly_cell_lte_capacity_p95_prb_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlDataP95_prb'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL data acc
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_lte_data_acc_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlDataAcc'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa data p95_prb
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlDataP95_prb']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\capacity_p95_prb.qml'
        }
        outputs['EstablecerElEstiloDeCapaDataP95_prb'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL data ret
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from geo_kpis_report.weekly_cell_lte_data_ret_offenders'
        }
        outputs['EjecutarSqlYCargarDesdePostgresqlDataRet'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa data int
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlDataInt']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaDataInt'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa data acc
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlDataAcc']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaDataAcc'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto data p95_prb
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaDataP95_prb']['OUTPUT'],
            'NAME': '5.3 Lte Data capacity p95_prb'
        }
        outputs['CargarCapaEnElProyectoDataP95_prb'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa data ret
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresqlDataRet']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Geo_Kpis_Report\\traffic_light.qml'
        }
        outputs['EstablecerElEstiloDeCapaDataRet'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(9)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto data ret
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaDataRet']['OUTPUT'],
            'NAME': '5.3 Lte Data retainability '
        }
        outputs['CargarCapaEnElProyectoDataRet'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(10)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto data int
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaDataInt']['OUTPUT'],
            'NAME': '5.3 Lte Data Integrity '
        }
        outputs['CargarCapaEnElProyectoDataInt'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(11)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto dat acc
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaDataAcc']['OUTPUT'],
            'NAME': '5.3 Lte Data accessibility'
        }
        outputs['CargarCapaEnElProyectoDatAcc'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '5.3 Lte kpis'

    def displayName(self):
        return '5.3 Lte kpis'

    def group(self):
        return '5.- Last_week_KPIs'

    def groupId(self):
        return '5.- Last_week_KPIs'

    def createInstance(self):
        return LteKpis()
