from tqdm.auto import tqdm
from Person import Person
from Eye import Eye
from EyeImage import EyeImage
from IOP import IOP
from Refractive_Defect import Refractive_Defect
import pandas as pd

class Database:

    def __init__(self, 
                 od_Spreadsheet_filePath, 
                 os_Spreadsheet_filePath, 
                 odfundusImages, 
                 osfundusImages, 
                 odimagesWithContours, 
                 osimagesWithContours):
        pd.set_option('display.max_colwidth', 500)
        df_od = pd.read_excel(od_Spreadsheet_filePath, header=2)
        df_od.columns=[ 'id'\
                        , 'age'\
                        , 'gender'\
                        , 'od_eye_diagnosis'\
                        , 'od_eye_refractive_defect_dioptre_1'\
                        , 'od_eye_refractive_defect_dioptre_2'\
                        , 'od_eye_refractive_defect_astigmatism'\
                        , 'od_eye_phakic_Pseudophakic'\
                        , 'od_eye_iop_pneumatic'\
                        , 'od_eye_iop_perkins'\
                        , 'od_eye_pachymetry'\
                        , 'od_eye_axialLength'\
                        , 'od_eye_vf_md']
        df_od['id'] = df_od['id'].str[-3:]

        df_os = pd.read_excel(os_Spreadsheet_filePath, header=2)
        df_os.columns=['id'\
                        , 'age'\
                        , 'gender'\
                        , 'os_eye_diagnosis'\
                        , 'os_eye_refractive_defect_dioptre_1'\
                        , 'os_eye_refractive_defect_dioptre_2'\
                        , 'os_eye_refractive_defect_astigmatism'\
                        , 'os_eye_phakic_Pseudophakic'\
                        , 'os_eye_iop_pneumatic'\
                        , 'os_eye_iop_perkins'\
                        , 'os_eye_pachymetry'\
                        , 'os_eye_axialLength'\
                        , 'os_eye_vf_md']
        df_os['id'] = df_os['id'].str[-3:]

        df_os=df_os.drop(columns=['age', 'gender'])

        df = pd.merge(df_od, df_os, on='id', how='inner')
        df['id'] = df['id'].astype(int)

        df_osfundusImages = pd.DataFrame(data=osfundusImages, columns=['id'\
                                                                        , 'os_eye_fundus_image_fileName'\
                                                                        , 'os_eye_fundus_image_format'\
                                                                        , 'os_eye_fundus_image_width'\
                                                                        , 'os_eye_fundus_image_height'\
                                                                        , 'os_eye_fundus_image_path'])
        df_odfundusImages = pd.DataFrame(data=odfundusImages, columns=['id'\
                                                                        , 'od_eye_fundus_image_fileName'\
                                                                        , 'od_eye_fundus_image_format'\
                                                                        , 'od_eye_fundus_image_width'\
                                                                        , 'od_eye_fundus_image_height'\
                                                                        , 'od_eye_fundus_image_path'])

        df_fundusImages = pd.merge(df_osfundusImages, df_odfundusImages, on = 'id', how='inner')

        df_osimagesWithContours = pd.DataFrame(data=osimagesWithContours, columns=['id'\
                                                                        , 'os_eye_image_with_contour_fileName'\
                                                                        , 'os_eye_image_with_contour_format'\
                                                                        , 'os_eye_image_with_contour_width'\
                                                                        , 'os_eye_image_with_contour_height'\
                                                                        , 'os_eye_image_with_contour_path'])
        df_odimagesWithContours = pd.DataFrame(data=odimagesWithContours, columns=['id'\
                                                                        , 'od_eye_image_with_contour_fileName'\
                                                                        , 'od_eye_image_with_contour_format'\
                                                                        , 'od_eye_image_with_contour_width'\
                                                                        , 'od_eye_image_with_contour_height'\
                                                                        , 'od_eye_image_with_contour_path'])

        df_odimagesWithContours = pd.merge(df_osimagesWithContours, df_odimagesWithContours, on = 'id', how='inner')

        df_images = pd.merge(df_fundusImages, df_odimagesWithContours, on = 'id', how='inner')

        self._datasource = pd.merge(df, df_images)
        self._datasource['os_eye_fundus_image_fileName'] = self._datasource['os_eye_fundus_image_fileName'].astype('string')
        self._datasource['os_eye_fundus_image_path'] = self._datasource['os_eye_fundus_image_path'].astype('string')
        self._datasource['od_eye_fundus_image_fileName'] = self._datasource['od_eye_fundus_image_fileName'].astype('string')
        self._datasource['od_eye_fundus_image_path'] = self._datasource['od_eye_fundus_image_path'].astype('string')
        self._datasource['os_eye_image_with_contour_fileName'] = self._datasource['os_eye_image_with_contour_fileName'].astype('string')
        self._datasource['os_eye_image_with_contour_path'] = self._datasource['os_eye_image_with_contour_path'].astype('string')
        self._datasource['od_eye_image_with_contour_fileName'] = self._datasource['od_eye_image_with_contour_fileName'].astype('string')
        self._datasource['od_eye_image_with_contour_path'] = self._datasource['od_eye_image_with_contour_path'].astype('string')

        self._datasource.set_index('id')

    def insert(self, person: Person) -> int:
        id = int(self._datasource['id'].max()) + 1
        item = {
            'id' : id\
            , 'age': person.age\
            , 'gender': person.gender\
           , 'od_eye_diagnosis': person.odEye.diagnosis\
            , 'od_eye_refractive_defect_dioptre_1': person.odEye.refractiveDefect.dioptre1\
            , 'od_eye_refractive_defect_dioptre_2': person.odEye.refractiveDefect.dioptre2\
            , 'od_eye_refractive_defect_astigmatism': person.odEye.refractiveDefect.astigmatism\
            , 'od_eye_phakic_Pseudophakic': person.odEye.phakic_Pseudophakic\
            , 'od_eye_iop_pneumatic': person.odEye.iop.pneumatic\
            , 'od_eye_iop_perkins': person.odEye.iop.perkins\
            , 'od_eye_pachymetry': person.odEye.pachymetry\
            , 'od_eye_axialLength': person.odEye.axialLength\
            , 'od_eye_vf_md': person.odEye.vf_md\
            , 'os_eye_diagnosis': person.osEye.diagnosis\
            , 'os_eye_refractive_defect_dioptre_1': person.osEye.refractiveDefect.dioptre1\
            , 'os_eye_refractive_defect_dioptre_2': person.osEye.refractiveDefect.dioptre2\
            , 'os_eye_refractive_defect_astigmatism': person.osEye.refractiveDefect.astigmatism\
            , 'os_eye_phakic_Pseudophakic': person.osEye.phakic_Pseudophakic\
            , 'os_eye_iop_pneumatic': person.osEye.iop.pneumatic\
            , 'os_eye_iop_perkins': person.osEye.iop.perkins\
            , 'os_eye_pachymetry': person.osEye.pachymetry\
            , 'os_eye_axialLength': person.osEye.axialLength\
            , 'os_eye_vf_md': person.osEye.vf_md\
            , 'os_eye_fundus_image_fileName': person.osEye.fundusImage.fileName\
            , 'os_eye_fundus_image_format': person.osEye.fundusImage.format\
            , 'os_eye_fundus_image_width': person.osEye.fundusImage.width\
            , 'os_eye_fundus_image_height': person.osEye.fundusImage.height\
            , 'os_eye_fundus_image_path': person.osEye.fundusImage.path\
            , 'od_eye_fundus_image_fileName': person.odEye.fundusImage.fileName\
            , 'od_eye_fundus_image_format': person.odEye.fundusImage.format\
            , 'od_eye_fundus_image_width': person.odEye.fundusImage.width\
            , 'od_eye_fundus_image_height': person.odEye.fundusImage.height\
            , 'od_eye_fundus_image_path': person.odEye.fundusImage.path\
            , 'os_eye_image_with_contour_fileName': person.osEye.imageWithContour.fileName\
            , 'os_eye_image_with_contour_format': person.osEye.imageWithContour.format\
            , 'os_eye_image_with_contour_width': person.osEye.imageWithContour.width\
            , 'os_eye_image_with_contour_height': person.osEye.imageWithContour.height\
            , 'os_eye_image_with_contour_path': person.osEye.imageWithContour.path\
            , 'od_eye_image_with_contour_fileName': person.odEye.imageWithContour.fileName\
            , 'od_eye_image_with_contour_format': person.odEye.imageWithContour.format\
            , 'od_eye_image_with_contour_width': person.odEye.imageWithContour.width\
            , 'od_eye_image_with_contour_height': person.odEye.imageWithContour.height\
            , 'od_eye_image_with_contour_path': person.odEye.imageWithContour.path\
        }
        self._datasource = self._datasource.append(item, ignore_index=True)
        return id

    def select(self, top=None) -> pd.DataFrame:
        if (top is None):
            return self._datasource
        else:
            return self._datasource.head(top)

    def delete(self, index: str):
        self._datasource = self._datasource.drop(index)
        return self

    def get(self, index) -> Person:

        for i, samble in tqdm(self._datasource.iterrows()):
          if self._datasource.at[i, 'id'] == index:
            od_eye = Eye(self._datasource.at[i,'od_eye_diagnosis']\
                      , Refractive_Defect(self._datasource.at[i,'od_eye_refractive_defect_dioptre_1']\
                                          , self._datasource.at[i,'od_eye_refractive_defect_dioptre_2']\
                                          , self._datasource.at[i,'od_eye_refractive_defect_astigmatism'])\
                      , self._datasource.at[i,'od_eye_phakic_Pseudophakic']\
                      , IOP( self._datasource.at[i,'od_eye_iop_pneumatic']\
                              , self._datasource.at[i,'od_eye_iop_perkins'])
                      , self._datasource.at[i,'od_eye_pachymetry']\
                      , self._datasource.at[i,'od_eye_axialLength']\
                      , self._datasource.at[i,'od_eye_vf_md']
                      , EyeImage(self._datasource.at[i,'id']\
                                          , self._datasource.at[i,'od_eye_fundus_image_fileName']\
                                          , self._datasource.at[i,'od_eye_fundus_image_format']\
                                          , self._datasource.at[i,'od_eye_fundus_image_width']\
                                          , self._datasource.at[i,'od_eye_fundus_image_height']\
                                          , self._datasource.at[i,'od_eye_fundus_image_path'])\
                      , EyeImage(self._datasource.at[i,'id']\
                                          , self._datasource.at[i,'od_eye_image_with_contour_fileName']\
                                          , self._datasource.at[i,'od_eye_image_with_contour_format']\
                                          , self._datasource.at[i,'od_eye_image_with_contour_width']\
                                          , self._datasource.at[i,'od_eye_image_with_contour_height']\
                                          , self._datasource.at[i,'od_eye_image_with_contour_path']))
            os_eye = Eye(self._datasource.at[i,'os_eye_diagnosis']\
                      , Refractive_Defect(self._datasource.at[i,'os_eye_refractive_defect_dioptre_1']\
                                          , self._datasource.at[i,'os_eye_refractive_defect_dioptre_2']\
                                          , self._datasource.at[i,'os_eye_refractive_defect_astigmatism'])\
                      , self._datasource.at[i,'os_eye_phakic_Pseudophakic']\
                      , IOP( self._datasource.at[i,'os_eye_iop_pneumatic']\
                            , self._datasource.at[i,'os_eye_iop_perkins'])\
                      , self._datasource.at[i,'os_eye_pachymetry']\
                      , self._datasource.at[i,'os_eye_axialLength']\
                      , self._datasource.at[i,'os_eye_vf_md']\
                      , EyeImage(self._datasource.at[i,'id']\
                                          , self._datasource.at[i,'os_eye_fundus_image_fileName']\
                                          , self._datasource.at[i,'os_eye_fundus_image_format']\
                                          , self._datasource.at[i,'os_eye_fundus_image_width']\
                                          , self._datasource.at[i,'os_eye_fundus_image_height']\
                                          , self._datasource.at[i,'os_eye_fundus_image_path'])\
                      , EyeImage(self._datasource.at[i,'id']\
                                          , self._datasource.at[i,'os_eye_image_with_contour_fileName']\
                                          , self._datasource.at[i,'os_eye_image_with_contour_format']\
                                          , self._datasource.at[i,'os_eye_image_with_contour_width']\
                                          , self._datasource.at[i,'os_eye_image_with_contour_height']\
                                          , self._datasource.at[i,'os_eye_image_with_contour_path']))
            return Person(self._datasource.at[i,'id'], self._datasource.at[i,'age'], self._datasource.at[i,'gender'], od_eye, os_eye )
        return None


