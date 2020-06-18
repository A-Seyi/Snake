# NX 11.0.2.7
# Journal created by ttvm4 on Thu Jan 16 13:52:36 2020 GMT Standard Time
#
import NXOpen
import new_part_bare
def main() : 
    new_part_bare.new_part()
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    # ----------------------------------------------
    #   Menu: File->Import->Part...
    # ----------------------------------------------
    
    partImporter1 = workPart.ImportManager.CreatePartImporter()
    
    partImporter1.FileName = "C:\\Users\\ttvm4\\OneDrive - Loughborough University\\4th YEAR\\Final Year Project\\geometry\\20CFD010 - REAR WING 003.prt"
    
    element1 = NXOpen.Matrix3x3()
    
    element1.Xx = 1.0
    element1.Xy = 0.0
    element1.Xz = 0.0
    element1.Yx = 0.0
    element1.Yy = 1.0
    element1.Yz = 0.0
    element1.Zx = 0.0
    element1.Zy = 0.0
    element1.Zz = 1.0
    This is just me typing rubbish!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    nXMatrix1 = workPart.NXMatrices.Create(element1)
    
    partImporter1.DestinationCoordinateSystem = nXMatrix1
    
    destinationPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    partImporter1.DestinationPoint = destinationPoint1
    
    nXObject1 = partImporter1.Commit()
    
    partImporter1.Destroy()
if __name__ == '__main__':
    main()


