"""
Model exported as python.
Name : 1.3 Lte
Group : 1.- Site_and_Cells
With QGIS : 33601
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
import processing


class Lte(QgsProcessingAlgorithm):

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
            'SQL': 'select * from site_and_cell_information."03_lte_fdd_sites"'
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

        # Ejecutar SQL y cargar desde PostgreSQL_cell_lte
        alg_params = {
            'DATABASE': 'optinet_db',
            'GEOMETRY_FIELD': 'geometry',
            'ID_FIELD': 'id',
            'SQL': 'select * from site_and_cell_information."07_lte_fdd_cells"'
        }
        outputs['EjecutarSqlYCargarDesdePostgresql_cell_lte'] = processing.run('qgis:postgisexecuteandloadsql', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Establecer el estilo de capa celda
        alg_params = {
            'INPUT': outputs['EjecutarSqlYCargarDesdePostgresql_cell_lte']['OUTPUT'],
            'STYLE': 'C:\\Users\\macabrera\\Documents\\QGIS exports\\Optinet_QGIS_layers\\Table_Site_and_Cell_Information\\lte_cells.qml'
        }
        outputs['EstablecerElEstiloDeCapaCelda'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto sites lte
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaSitio']['OUTPUT'],
            'NAME': '1.3 Lte_sites'
        }
        outputs['CargarCapaEnElProyectoSitesLte'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Cargar capa en el proyecto cell lte
        alg_params = {
            'INPUT': outputs['EstablecerElEstiloDeCapaCelda']['OUTPUT'],
            'NAME': '1.3 Lte_cells'
        }
        outputs['CargarCapaEnElProyectoCellLte'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return '1.3 Lte'

    def displayName(self):
        return '1.3 Lte'

    def group(self):
        return '1.- Site_and_Cells'

    def groupId(self):
        return '1.- Site_and_Cells'

    def createInstance(self):
        return Lte()
