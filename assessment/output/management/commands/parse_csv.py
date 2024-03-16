import xlrd
import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from output.models import Data, MetadataCountries

class Command(BaseCommand):
    help = 'Load data from xls'

    def handle(self, *args, **options):
        # Drop the data from the table so that if we rerun the file, we don't repeat values
        Data.objects.all().delete()
        MetadataCountries.objects.all().delete()
        print("Tables dropped successfully")

        # Open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        file_path = os.path.join(base_dir, 'output', 'output_data', 'test_API_EG.ELC.RNEW.ZS_DS2_en_excel_v2_6299116.xls')

        try:
            workbook = xlrd.open_workbook(file_path)

            # Process Data sheet
            sheet_data = workbook.sheet_by_index(0)
            for row_index in range(1, sheet_data.nrows):  # Skip the header row
                row = sheet_data.row_values(row_index)
                data = Data.objects.create(
                    countryName=row[0],
                    year1=float(row[3]),
                    year2=float(row[8]),
                    year3=float(row[13]),
                    year4=float(row[18]),
                    year5=float(row[23]),
                    year6=float(row[28]),
                )

            # Process Metadata sheet
            sheet_metadata = workbook.sheet_by_index(1)
            for row_index in range(1, sheet_metadata.nrows):  # Skip the header row
                row = sheet_metadata.row_values(row_index)
                if row[4]:  # Check if tableName is not empty
                    metadataCountries = MetadataCountries.objects.create(
                        region=row[1],
                        incomeGroup=row[2],  # Consider changing the type if needed
                        specialNotes=row[3],  # Consider changing the type if needed
                        tableName=row[4],  # Consider changing the type if needed
                    )
                

            self.stdout.write(self.style.SUCCESS("Data parsed successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
