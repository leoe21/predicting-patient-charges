import pandas as pd
from pycaret.regression import *
import os

# Crear directorio para el modelo si no existe
if not os.path.exists('models'):
    os.makedirs('models')

# Cargar el dataset
print("Cargando el dataset...")
data = pd.read_csv(os.path.join('data', 'insurance.csv'))

# Configurar el entorno de PyCaret
print("Configurando el entorno de PyCaret...")
setup(data, 
      target='charges',
      session_id=123,
      normalize=True,
      polynomial_features=True,
      bin_numeric_features=['age', 'bmi'])

# Entrenar el modelo de regresión lineal
print("Entrenando el modelo...")
lr = create_model('lr')

# Evaluar el modelo
print("Evaluando el modelo...")
print("\nMétricas del modelo:")
print(lr)

# Guardar el modelo
print("\nGuardando el modelo...")
save_model(lr, 'models/insurance_model')

print("\n¡Modelo entrenado y guardado exitosamente!") 