from db.resources import resources

class ReportService:
    @staticmethod
    def report():
        for key, value in resources.items() :
            print (key, value)
            