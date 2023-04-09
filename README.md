# Challenge-Machine-Learning-Engineer
Desafío para el puesto ML Engineer en Latam Airlines

Comentarios sobre el Notebook Actual.

La solución no compila, a continuación se presentan los errores y soluciones:
- TypeError: barplot() takes from 0 to 1 positional arguments but 2 were given. La solución es poner explícitamente cuáles
son los valores de x e y en los argumentos de la función.

- En esta llamada a la función calcular_tasa: tasas_destinos = calcular_tasa(df, 'SIGLADES'), aparece el siguiente error: 'Series' object has no attribute 'iteritems'. Usar el siguiente comando para la iteración: for name, total in total_values.items():.

- labels_ = labels -> labels_ = label

- Según lo que veo la Regresión Logística obtuvo un puntaje de 0.82 de acuerdo al accuracy, sin embargo, el f1-score en la clase 1 fue de 0.06. Al ejecutar el modelo XGBoost los resultados fueron análogos, igual a 0.82.

- Me da curiosidad que al incorporar los features más importantes los resultados no sean mejores. 

- Mi principal preocupación está en la métrica que se está utilizando, creo que es importante tomar en cuenta el desbalance (balanced accuracy). Por otro lado, el problema pide ver la probabilidad de que el vuelo se atrase, por lo que ese feature debiese ser considerado, que no sea sólo clasificación binaria.

- Respecto a la técnica de upsampling empleada, creo que modificó la distribución de los datos, ya que fue aplicada a todo el dataframe y no sólo al conjunto de entrenamiento, esto puede traer errores en los resultados del modelo. 

- Creo que la conclusión final, no es del todo acertada, el basar la decisión en el accuracy, cuando el f1 de la clase minoritaria subió.

- Falta incorporar nuevos features.




1. Escoger el modelo que a tu criterio tenga un mejor performance, argumentando la decisión.

En este caso, con el código entregado no podría tomar una decisión 100% segura. Pero sí me inclinaría más por la última parte del código en donde se emplearon técnicas de balanceo y de optimización de hiperparámetros, es decir, al XGBoost. Como mencioné, independiente que haya bajado el accuracy general, aumento el f1-score en la clase minoritaria. Sin embargo, como la implementación tiene errores en cuanto a la forma en que se agregaron nuevos datos, se proponen mejoras y nuevos experimentos.

2. Implementar mejoras sobre el modelo escogiendo la o las técnicas que prefieras.

La respuesta a esta pregunta se encuentra en la siguiente parte del notebook.



3. Exponer el modelo seleccionado como API REST para ser expuesto.
4. Hacer pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto
debes utilizar esta herramienta y presentar las métricas obtenidas.
5. ¿Cómo podrías mejorar el performance de las pruebas anteriores?