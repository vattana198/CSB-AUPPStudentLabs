
import pandas as pd

class SchoolAssessmentSystem:
    def __init__(self):
        self.data = pd.DataFrame()

    def import_and_process_files(self, file_paths):
        for file_path in file_paths:
            # Detect file format and read data
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            elif file_path.endswith('.txt'):
                data = pd.read_csv(file_path, delimiter='\t')
            else:
                print(f"Unsupported file format for {file_path}")
                continue

            # Extract relevant data
            # Assume the columns 'StudentName', 'StudentID', 'Subject', 'Score' are present
            relevant_columns = ['StudentName', 'StudentID', 'Subject', 'Score']
            data = data[relevant_columns]

            # Concatenate data
            self.data = pd.concat([self.data, data])

    def transform_data(self):
        # Perform data transformations (e.g., converting scores to percentages)
        # Handle missing or inconsistent data gracefully
        # For simplicity, let's assume there are no missing values

        self.data['Percentage'] = (self.data['Score'] / max(self.data['Score'])) * 100

    def content_analysis(self):
        # Identify commonalities and discrepancies in the assessment data
        common_data = self.data.groupby(['StudentID', 'Subject']).count().reset_index()
        discrepancies = common_data[common_data.duplicated(subset=['StudentID', 'Subject'], keep=False)]

        if not discrepancies.empty:
            print("Discrepancies found:")
            print(discrepancies)
        else:
            print("No discrepancies found.")

    def data_transfer(self, source_file, destination_file):
        # Transfer specific data between files
        # For simplicity, let's assume data transfer is a copy operation
        source_data = pd.read_csv(source_file)
        self.data = pd.concat([self.data, source_data])

        # Save the updated data to the destination file
        self.data.to_csv(destination_file, index=False)

    def summarization(self):
        # Generate summary reports
        class_summary = self.data.groupby('Subject')['Percentage'].mean()
        individual_summary = self.data.groupby('StudentID')['Percentage'].mean()

        print("\nClass Summary:")
        print(class_summary)

        print("\nIndividual Summary:")
        print(individual_summary)

    def run(self):
        file_paths = ['file1.csv', 'file2.xlsx', 'file3.txt']
        
        # Feature 1: File Import and Processing
        self.import_and_process_files(file_paths)

        # Feature 2: Data Transformation
        self.transform_data()

        # Feature 3: Content Analysis
        self.content_analysis()

        # Feature 4: Data Transfer
        self.data_transfer('source_file.csv', 'destination_file.csv')

        # Feature 5: Summarization
        self.summarization()

if __name__ == "__main__":
    assessment_system = SchoolAssessmentSystem()
    assessment_system.run()
