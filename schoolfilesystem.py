import requests
#Libraries you may need:
# import csv, collections, dictionary , urlopen, etc 
import csv
import statistics
import pandas as pd
from bs4 import BeautifulSoup

#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        pass
    def process_file(self , file_path):        
        try:    
            with open('file_path', 'r') as file_path:
                read = file_path.read()
                print(f"File content:  {read}")
        except FileNotFoundError:
            print("File {file_path} not found")
        except Exception as e:
            print(f"Error: {e}")


    def transfer_data(self, file_path , criteria , Store_data):
        try: 
            source_data = pd.read_csv(file_path)
            # Add logic to filter and transfer data based on criteria
            filtered_data = source_data[source_data['Criteria'] == criteria]

            # Add logic to transfer data to destination file
            filtered_data.to_csv(Store_data , index = False)
            return filtered_data
        except FileNotFoundError:
            print(f"file {file_path} not found")
        except Exception as e :
            print(f"Error: {e}")
        
    def fetch_web_data(self,url):
        response = requests.get(url)
        try: 
            if response.status_code == 200:
                web_data = response.text  
                soup = BeautifulSoup(web_data, 'html.parser')
                text = soup.get_text(separator='\n', strip=True)

                print(f"Web Data: {text}")
                return text
            else:
                print(f"Error : {response.status_code}")
        except Exception as e :
            print(f"Error: {e}")    
    
    def analyze_content(file_path):
        if not file_path :
            
            return {"Error: Empty Data"}
        # calculate score 

        
    def generate_summary():
        pass

# Analyze content & display result area
# if __name__ == "__main__":
#     # Create an instance of the SchoolAssessmentSystem
#     school_system = SchoolAssessmentSystem()

#     # Example usage of the fetch_web_data method
#     url = "https://www.aupp.edu.kh"
#     # url = "https://stackoverflow.com/questions/73576241/how-to-transfer-data-from-file-to-file"
#     web_data = school_system.fetch_web_data(url)




