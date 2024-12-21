"""
Model exported as python.
Name : 1.2 Umts
Group : 1.- Site_and_Cells
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class Umts(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        pass

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(6, model_feedback)
        results = {}
        outputs = {}

        # Ejecutar SQL y cargar desde PostgreSQL_site
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from site_and_cell_information."02_umts_sites"'
        }
        outputs['EjecutarSqlYCargarDesdePostgresql_site'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa sitio
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresql_site']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Site_and_Cell_Information\\sites.qml'
        }
        outputs['EstablecerElEstiloDeCapaSitio'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Ejecutar SQL y cargar desde PostgreSQL_cell_umts
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from site_and_cell_information."06_umts_cells"'
        }
        outputs['EjecutarSqlYCargarDesdePostgresql_cell_umts'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa celda
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresql_cell_umts']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Site_and_Cell_Information\\umts_cells.qml'
        }
        outputs['EstablecerElEstiloDeCapaCelda'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto sites umts
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaSitio']['OUTPUT'],
            'NAME': '1.2 Umts_sites'
        }
        outputs['CargarCapaEnElProyectoSitesUmts'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto cell umts
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaCelda']['OUTPUT'],
            'NAME': '1.2 Umts_cells'
        }
        outputs['CargarCapaEnElProyectoCellUmts'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '1.2 Umts'

    def displayName(self):
        return '1.2 Umts'

    def group(self):
        return '1.- Site_and_Cells'

    def groupId(self):
        return '1.- Site_and_Cells'

    def createInstance(self):
        return Umts()
