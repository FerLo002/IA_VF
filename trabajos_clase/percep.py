import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Generar datos artificiales
# np.random.seed(0)
# X = np.random.rand(1000, 2)  # 1000 puntos con 2 características cada uno
# y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Etiqueta 1 si la suma de las características > 1, de lo contrario 0

datos_modelo=[(0.5,0.8,1),(0.6,0.9,1),(0.7,0.6,0),(0.4,0.5,0),(0.3,0.9,1),(0.8,0.4,0)]

 # Separar datos
x1 = [x for x, y, z in datos_modelo]
x2 = [y for x, y, z in datos_modelo]
target0 = [z for x, y, z in datos_modelo]

# Definir características (X) y etiquetas (y)
X = np.array(list(zip(x1, x2)))  # Convertir a numpy array
y = np.array(target0)  # Convertir a numpy array
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de red neuronal multicapa
model = Sequential([
    # Dense(1, input_dim=2, activation='relu'),  # Capa oculta con 4 neuronas y activación ReLU
    Dense(1, input_dim=2, activation='sigmoid')            # Capa de salida con 1 neurona y activación sigmoide
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nPrecisión en el conjunto de prueba: {accuracy:.2f}")

# Probar con un nuevo dato
nuevo_dato = np.array([[0.8, 0.3]])  # Ejemplo con características específicas
prediccion = model.predict(nuevo_dato)
print(f"Predicción para {nuevo_dato}: {prediccion[0][0]:.2f}")