import pandas as pd
import requests
import os

def download_dataset():
    print("Descargando el dataset de seguros...")
    
    # URL del dataset
    url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
    
    try:
        # Descargar el dataset
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la descarga fue exitosa
        
        # Asegurarse de que la carpeta data existe
        if not os.path.exists('data'):
            os.makedirs('data')
        
        # Guardar el dataset en la carpeta data
        file_path = os.path.join('data', 'insurance.csv')
        with open(file_path, 'wb') as f:
            f.write(response.content)
            
        print("Dataset descargado exitosamente en la carpeta 'data'!")
        
        # Verificar que el dataset se cargó correctamente
        df = pd.read_csv(file_path)
        print(f"\nDataset cargado correctamente. Dimensiones: {df.shape}")
        print("\nPrimeras 5 filas del dataset:")
        print(df.head())
        
    except Exception as e:
        print(f"Error al descargar el dataset: {str(e)}")

if __name__ == "__main__":
    download_dataset() 