'''
Templete1 :  File extend from HelperJSONBuilder to perform opertaions related to template 1
'''
import os

from ..ocr.helperJSONBuilder import HelperJSONBuilder

class Template1(HelperJSONBuilder):
    def __init__(self):
        self.imageTemplateName =  (os.path.splitext(os.path.basename(__file__))[0]).lower()
        super(Template1, self).__init__()

    '''
    Function : Create a dictonary object that can be directly saved into MongoDB
    '''
    def getStudentDetail(self, studentID):
        print "fn: getStudentDetail %s" % studentID
        try:
            selectedSequence = self.templateSequence[self.imageTemplateName]
            studentRecord = {'studentID': studentID}
            
            cropImagePath = os.path.join(self.tempDir, studentID, self.cropImageFolderName)
            
            for file_name in os.listdir(cropImagePath):
                cropImageFileName = os.path.join(cropImagePath, file_name)
                
                if file_name == selectedSequence['0']:
                    semester_1, major = self.getSemester(cropImageFileName)
                    studentRecord.update(major)

                elif (file_name == selectedSequence['1']): 
                    subjectByGrade = self.generateSubjectByGradeList(cropImageFileName)
                    studentRecord['Semester1']= semester_1
                    studentRecord['Semester1']['Subjects'] = subjectByGrade
        
            return studentRecord
        except Exception as ex:
            print "fn: getStudentDetail " + ex.message
            raise ex

# if __name__ == "__main__":
#     template = Template1()
#     print template.getStudentDetail('2345')
    # helperJSONBuilder.generateSubjectByGradeList("./images/test0_872.jpg")
