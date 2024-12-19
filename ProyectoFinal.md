El presente proyecto intenta analizar las nuevas reformas a la constitución que van dirigidas hacia el poder judicial y a los organismos autónomos, e intentar descubrir cómo afectan a dichas partes y al pueblo mexicano en general. Este análisis va desde la recolección de la información en diferentes medios, el tratamiento de la misma para manejarla en un formato óptimo para su manejo, y lo más importante es la creación o implementación de herramientas para facilitar el análisis.

En este caso se usó el modelo de Llama 3.2, con las herramientas de Ollama, que es una herramienta para ejecutar localmente grandes modelos de redes neuronales, en conjunto con AnythingLLM que permite gestionar grandes volúmenes de documentos, realizar análisis complejos y generar informes detallados, todo desde una interfaz fácil de usar.

Se generó un corpus donde se introdujo toda la información relacionada con la reforma al Poder Judicial, tomada de varias fuentes oficiales, noticias y videos, este corpus se le paso al modelo a través de AnythingLLM y posteriormente se hicieron las preguntas. 

Preguntas de la reforma al poder judicial

¿El diagnóstico de la ley al poder judicial es conocido y qué estudios  
expertos se tuvieron en cuenta?

La reforma no parece haber sido precedida por un diagnóstico detallado ni un debate nacional amplio. Según algunas fuentes y citas adjuntas en las noticias que se consultaron, parece de un acto que el presidente hizo desde el sentimiento de poder, y que incluso podría tacharse de revanchismo, pero las fuentes oficiales (del gobierno) mencionan que la causa de esta reforma es la corrupción, dado que el 49% de los Jueces y Magistrados tienen al menos un familiar, el caso que más familiares tiene cuenta con un número de 26\.

Hasta este punto, parece que es conveniente la reforma dado que liberará vacantes para las personas que realmente lo merecen.

Modelo: 

“Según lo que he encontrado, el diagnóstico de la ley sobre el poder judicial se basa en varios estudios y expertos. Algunos de los estudios mencionados son:

\* Un estudio realizado en Estados Unidos, donde se elige a jueces locales, demostró que en determinadas circunstancias, la elección de personas juzgadoras puede resultar contraproducente para la legitimidad judicial.

\* Una serie de estudios realizados en Estados Unidos confirman que el público está particularmente desinformado en el caso de elecciones judiciales.

Además, se menciona a expertos como Amaya Navarro y Tayler, Tom R., cuyas opiniones sobre la socialización judicial y la creación de popularidad en los tribunales se han considerado en el diagnóstico.“

¿Por qué la reforma no incluyó a las fiscalías y a la defensoría, limitándose solo al Poder Judicial?

Con base en las fuentes consultadas, la reforma parece centrarse exclusivamente en cambiar la estructura del Poder Judicial para supuestamente mejorar la impartición de justicia y reducir la percepción de corrupción y nepotismo​.

Modelo:

“Lamentablemente, no tengo información específica sobre por qué la reforma se limitó solo al Poder Judicial y no incluyó a las Fiscalías y la Defensoría. El texto proporcionado solo menciona los problemas asociados con los cambios para garantizar una justicia pronta y expedita, sin ofrecer explicaciones sobre la selección de prioridades o el proceso de toma de decisiones que llevó a la reforma.”

¿Qué medidas concretas se implementarán para evitar la captación del crimen organizado y la violencia en el contexto electoral?

De acuerdo con las fuentes consultadas no se mencionan medidas específicas en la reforma para abordar este problema en el contexto electoral. Al contrario, se señala que el proceso de elección popular podría exponer a los jueces a la violencia política y al crimen organizado​, como sucede en las elecciones a cargos políticos.  
Lamentablemente y fuera del tema, el crimen organizado es un caso muy arraigado en el país y no depende completamente del gobierno, también de la cultura y de la gente en general, debe de ser un problema prioritario, pero realmente es un problema enorme muy difícil de remediar.

Modelo:  
“Lo siento, pero no tengo información específica sobre las medidas concretas que se implementarán para evitar la captación del crimen organizado y la violencia en el contexto electoral. El texto proporcionado solo menciona los problemas asociados con la elección de personas juzgadoras y su posible vulnerabilidad ante la violencia política o del crimen organizado, sin ofrecer soluciones o propuestas concretas para abordar este tema.”

¿Cómo garantizar que juristas probos y honestos se animen a competir públicamente frente a los riesgos de la violencia?

La reforma no presenta un esquema claro para proteger a los candidatos durante el proceso electoral al igual que con los candidatos a puestos políticos, lo cual podría poner en riesgo la integridad de los candidatos al puesto jurídico. Además, la exposición pública podría generar vulnerabilidades frente a actores externos, exactamente igual que con las elecciones políticas, que justo se acaban de vivir las más violentas de la historia de México al parecer​. Esto puede ser un gran golpe para todas las partes y una desincentivación para los candidatos.

Modelo:   
“Según el texto proporcionado, Arro22 menciona que una parte central de una educación orientada al desarrollo de virtudes debe consistir en la interacción entre personas y el estudio de casos decididos por jueces ejemplares. También se menciona la importancia de la socialización judicial para adquirir las virtudes judiciales.

En cuanto a garantizar que juristas probos y honestos se animen a competir públicamente frente a los riesgos de la violencia, el texto no ofrece soluciones específicas. Sin embargo, se sugiere que la formación y educación en virtudes judiciales, así como la socialización judicial, pueden ser fundamentales para crear un cuerpo de jueces y juristas comprometidos con la justicia y la integridad.”

¿Cómo se conforman los comités de postulación?  
La reforma plantea procesos de elección popular para jueces, los comités de evaluación estarán integrados con paridad de género por cinco personas de prestigio con al menos cinco años en la actividad jurídica. Deben contar con nacionalidad mexicana, un título de licenciatura en Derecho con antigüedad mínima de cinco años, y no haber sido condenados por algún delito. Además de no haber tenido cargos de dirección en partidos políticos los últimos 3 años.

Modelo:

“Según el texto proporcionado, los comités de evaluación estarán integrados por cinco personas con paridad de género, que deben tener nacionalidad mexicana, título de licenciatura en Derecho con al menos cinco años de antigüedad, y no haber sido condenados por ningún delito. Además, no pueden haber desempeñado ni haber desempeñado cargo de dirección nacional o estatal en algún partido político en los últimos tres años anteriores a la designación.”

¿Cómo asegurar la carrera judicial?

La eliminación inmediata de jueces actuales y la instauración de un sistema electoral plantea riesgos para la continuidad de la carrera judicial, lo que puede impactar negativamente la profesionalización y la calidad de la justicia​.

Modelo:

“No se menciona explícitamente cómo asegurar la carrera judicial en el texto proporcionado. Sin embargo, se menciona que los jueces y juezas solo pueden ser destituidos por faltas de disciplina graves o incompetencia, y que todo proceso disciplinario debe resolverse de acuerdo con las normas de comportamiento judicial establecidas en procedimientos justos que aseguren la objetividad e imparcialidad.”

¿Cómo compatibilizar la incorporación de medidas para preservar la identidad de los jueces (conocidos como "jueces sin rostro") con los estándares internacionales?

La figura de los "jueces sin rostro", incluida en la reforma, ya ha sido declarada contraria a la Convención Americana de Derechos Humanos por la Corte Interamericana, lo que supone un desafío de compatibilidad con los estándares internacionales​.

Modelo: 

“No se menciona específicamente cómo compatibilizar la incorporación de medidas para preservar la identidad de los jueces (“jueces sin rostro”) con los estándares internacionales en el texto proporcionado. Sin embargo, se puede inferir que es posible hacerlo al establecer protocolos y procedimientos claros para garantizar la privacidad y seguridad de los jueces, mientras se mantiene la transparencia y rendición de cuentas necesarias.”

¿Cómo impactará el costo económico de esta reforma en la promoción y el acceso a la justicia?

Los costos económicos de la reforma son significativos, especialmente por la elección popular y el reemplazo masivo de jueces. Esto podría agravar el acceso a la justicia debido a la interrupción de casos en curso y la necesidad de reestructurar completamente el sistema judicial​.

Modelo:

“Según el texto proporcionado, el costo económico de la reforma es uno de los problemas asociados con ella, ya que implicaría el pago de indemnizaciones a miles de personas que administran justicia y que serán removidas de sus puestos. Esto podría tener un impacto negativo en la promoción y el acceso a la justicia, ya que podría limitar los recursos disponibles para el sistema judicial y comprometer la eficiencia y efectividad de los procedimientos judiciales.”

Preguntas para la ley de desaparición de los organismos autónomos.

¿Es constitucional esta ley, considerando que algunos organismos autónomos están establecidos en la Constitución?

No parece ser constitucional eliminar organismos autónomos establecidos directamente en la Constitución, ya que su creación responde a funciones esenciales que requieren independencia de los poderes del Estado. La propuesta enfrenta cuestionamientos por contravenir principios de autonomía establecidos en la Carta Magna y compromisos internacionales que exigen órganos independientes para garantizar derechos fundamentales​

Modelo:

“No se menciona explícitamente si es constitucional la ley en el texto proporcionado. Sin embargo, se indica que los órganos constitucionales autónomos son aquellos cuya creación se contempla directamente en la Constitución, lo que sugiere que cualquier cambio o reforma a estos organismos podría estar sujeta a requisitos especiales y análisis constitucional.”

¿Cómo afectaría la eliminación de estos organismos a la transparencia y rendición de cuentas del gobierno?

La desaparición de organismos como el INAI limitaría significativamente el acceso a la información pública y la protección de datos personales. Esto aumentaría los riesgos de opacidad, dificultando la supervisión ciudadana y la investigación de casos de corrupción. También centralizará funciones en el Ejecutivo, generando conflictos de interés al depender de la autorregulación gubernamental​

Modelo:

“Según el texto, la eliminación de estos organismos autónomos podría comprometer la transparencia y rendición de cuentas del gobierno. Esto se debe a que estos organismos desempeñan un papel importante en la protección de los derechos humanos y garantizar que el gobierno actúe de manera justa e imparcial. Su eliminación podría permitir que el gobierno controle o manipule información y procedimientos judiciales, lo que comprometería la transparencia y rendición de cuentas necesarias.”

¿Qué funciones críticas podrían perder independencia y control al pasar al poder ejecutivo u otras instituciones?

Funciones como la regulación de mercados, la supervisión de políticas sociales, y la protección de derechos de acceso a la información y competencia económica perderían independencia. Por ejemplo, la transferencia de la COFECE y el INAI al Ejecutivo debilitaría su capacidad para actuar con imparcialidad y proteger derechos ciudadanos frente a intereses gubernamentales o privados​.

Modelo:

“Según el texto, las funciones críticas que podrían perder independencia y control al pasar al poder ejecutivo o otras instituciones son aquellas que involucran la toma de decisiones sobre justicia social, políticas sociales y económicas. Esto incluye la capacidad de los organismos autónomos para investigar y sancionar violaciones de derechos humanos, así como su independencia en la formulación e implementación de políticas públicas que afectan a las comunidades marginadas.”

¿Existen alternativas para mejorar la eficiencia de los organismos autónomos sin eliminarlos?

Sí, se podrían implementar medidas para optimizar recursos y evitar duplicidad de funciones sin eliminar los organismos. Esto incluiría reforzar la colaboración entre instituciones, racionalizar presupuestos y mejorar los mecanismos de rendición de cuentas, en lugar de desmantelar estructuras clave para la democracia y la transparencia​.

Modelo:

“No se menciona explícitamente en el texto que existan alternativas para mejorar la eficiencia de los organismos autónomos sin eliminarlos. Sin embargo, se sugiere que la propuesta original ignora cómo la mayor autonomía de estos organismos protege el interés público frente a la intervención política del Poder Ejecutivo u otros poderes del Estado o fácticos, lo que podría implicar que algunas reformas y mecanismos para mejorar su eficiencia podrían ser diseñados en lugar de eliminarlos.”

¿Qué sectores de la sociedad civil y grupos de interés se verían afectados por la desaparición de estos organismos?

Diversos sectores serían impactados, incluyendo periodistas, organizaciones de derechos humanos, académicos y consumidores. La desaparición de organismos como el INAI y la COFECE afectaría la capacidad de supervisar actividades gubernamentales, proteger datos personales y garantizar mercados justos y competitivos. Esto también podría impactar negativamente la inversión extranjera y los derechos de los ciudadanos en general​.

Modelo:

“Según el texto, los sectores de la sociedad civil y grupos de interés que podrían verse afectados por la desaparición de estos organismos incluyen a las comunidades marginadas, personas que administran justicia y sus familias, así como otros ciudadanos que dependen del trabajo de estas instituciones para proteger sus derechos humanos. También se menciona que miles de personas podrían ser afectadas por el pago de indemnizaciones debido a la remoción de personas juzgadoras.”

Conclusiones:

Las reformas a la ley parecen no haber estado bien planeadas, desde mi punto de vista la del poder judicial tenía otras intenciones pero después del análisis comprendo que no es tan buena como parece, por reducir el nepotismo en un poder puede afectar bastantes sectores como el económico o la seguridad, exponiendo a los candidatos y a los ciudadanos a vivir actos de violencia como suele suceder en períodos electorales, independientemente del partido político que se apoye, que ahora eso tiene mucho peso en la política, debemos de reconocer las cosas que nos ayudan a avanzar y las que nos hacen retroceder, se justifica que el PRI hizo lo mismo, pero el propósito de mejorar es hacerlo diferente, debía de ser una reforma más elaborada y estudiada, dado que se contrapone incluso con estándares internacionales

En cuanto a la de organismos autónomos, me parece que es cierto que atenta contra la misma constitución , contra los derechos de los ciudadanos y supone algunos riesgos al involucrar poderes del estado en funciones autónomas, pudiendo desembocar en más corrupción y conflictos de interés.

