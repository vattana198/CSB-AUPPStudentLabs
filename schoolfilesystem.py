#Libraries you may need:
import unittest
import csv
import statistics
import pandas
import pandas as pd
from bs4 import BeautifulSoup
import requests
import pandas as pd
# from pandas import *
import os

#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = pandas.DataFrame()
   
    def process_file(self, file_path):        
        try:    
            with open(file_path, 'r') as file:
                read = file.read()
                return f"File content: {read}"
        except FileNotFoundError:
            print(f"File {file_path} not found")
        except Exception as e:
            print(f"Error: {e}")       

    def transfer_data(self, old_file_path , new_file_path):
            try: 
                with open(new_file_path , 'a') as file:
                    file.write(self.process_file(old_file_path))
            except FileNotFoundError:
                print(f"file {old_file_path} not found")
            except Exception as e :
                print(f"Error: {e}")

    def fetch_web_data(self, url):
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an HTTPError for bad requests

                if response.status_code == 200:
                    web_data = response.text

                    # Use BeautifulSoup to parse the HTML
                    soup = BeautifulSoup(web_data, 'html.parser')

                    # Extract text from all non-script and non-style elements
                    text_content = soup.get_text(separator='\n', strip=True)
                    return text_content
                else:
                    print(f"Error: {response.status_code}")

            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

    def analyze_content(file_path):
        
        try:
            df = pd.read_csv(file_path)

            df.columns = df.columns.str.strip() 
            print(f"File content:\n{df}")

            score_columns = ['Math', 'English', 'Science']
            for column in score_columns:
                if column not in df.columns:
                    print(f"Column {column} not found in the DataFrame.")
                    return 
                
            # Find the name of the student with the highest score in each subject
            top_scorers = {}
            for subject in score_columns:
                top_scorer_row = df[df[subject] == df[subject].max()]
                top_scorer_name = top_scorer_row.iloc[0]['Name']
                top_scorers[subject] = top_scorer_name

            # Print the top scorers in each subject
            print("\nTop Scorers in Each Subject:")
            for subject, top_scorer in top_scorers.items():
                print(f"{subject}: {top_scorer}")
            
            df['Score'] = df[score_columns].mean(axis=1)


            analysis_result = {
                "Total Students": len(df),
                "Class Average": round(df['Score'].mean(),2),
                "Minimum Score": round(df['Score'].min(),2),
                "Maximum Score": round(df['Score'].max(),2),
            }
            print("\n Analysis Results:")
            for key ,value in analysis_result.items():
                print(f"{key}: {value}")
        except FileNotFoundError:
            print(f"File {file_path} not Found")
        except Exception as e :
            print(f"Error: {e}")

        


    def generate_summary(file_path):
        try:
            def calculate_gpa(score):
                if 93 <= score <= 100:
                    return 4.00
                elif 90 <= score < 93:
                    return 3.67
                elif 87 <= score < 90:
                    return 3.33
                elif 83 <= score < 87:
                    return 3.00
                elif 80 <= score < 83:
                    return 2.67
                elif 77 <= score < 80:
                    return 2.33
                elif 73 <= score < 77:
                    return 2.00
                elif 70 <= score < 73:
                    return 1.67
                elif 67 <= score < 70:
                    return 1.33
                elif 63 <= score < 67:
                    return 1.00
                elif 60 <= score < 63:
                    return 0.67
                else:
                    return 0.00

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Remove trailing spaces from column names
            df.columns = df.columns.str.strip() 
            print(f"File content:\n{df}")

            # Check if there are columns with scores in the DataFrame
            score_columns = ['Math', 'English', 'Science']
            for column in score_columns:
                if column not in df.columns:
                    print(f"Column {column} not found in the DataFrame.")
                    return

            # Find the top scorer in each subject
            top_scorers = {subject: df[df[subject] == df[subject].max()].iloc[0]['Name'] for subject in score_columns}

            # Print the top scorers in each subject
            print("\nTop Scorers in Each Subject:")
            for subject, top_scorer in top_scorers.items():
                print(f"{subject}: {top_scorer}")

            # Continue with the analysis results
            df['Score'] = df[score_columns].mean(axis=1)

            # Calculate GPA for each student
            df['GPA'] = df['Score'].apply(calculate_gpa)

            # Generate analysis results
            analysis_result = {
                "Total Students": len(df),
                "Class Average Score": round(df['Score'].mean(), 2),
                "Class Average GPA": round(df['GPA'].mean(), 2),
                "Minimum Score": round(df['Score'].min(), 2),
                "Maximum Score": round(df['Score'].max(), 2),
            }

            # Print analysis results
            print("\nAnalysis Results:")
            for key, value in analysis_result.items():
                print(f"{key}: {value}")

            # Generate and return the summary report
            summary = f"\nSchool Assessment Summary Report:\n\n"
            summary += f"Total Students: {analysis_result['Total Students']} \n"
            summary += f"Class Average Score: {analysis_result['Class Average Score']: .2f} \n"
            summary += f"Class Average GPA: {analysis_result['Class Average GPA']: .2f} \n"

            

        except FileNotFoundError:
            return f"File {file_path} not found"
        except Exception as e:
            return f"Error: {e}"




# Create an instance of  class
school_system = SchoolAssessmentSystem()

school_system.process_file("temp_source.csv")
school_system.transfer_data("analysis.csv", "temp_file.csv")

print(school_system.process_file("studentinformation.csv"))
print(school_system)


file_path = "studentinformation.csv"  

# Call the analyze_content function
school_system.analyze_content(file_path)


if __name__ == "__main__":
    SchoolAssessmentSystem.analyze_content("studentinformation.csv")


if __name__ == "__main__":
    SchoolAssessmentSystem.generate_summary("studentinformation.csv")

