import nltk
import nest_asyncio #type: ignore
nest_asyncio.apply()

text = """REFORMA AL PODER JUDICIAL 10 DE SEPTIEMBRE DE 2024 INTEGRACIÓN DE LA SUPREMA CORTESe ha dicho que la reforma busca que el Ejecutivo tenga el control de la Suprema Corte,pero… ¿cómo se eligen hoy a las Ministras y Ministros?
        1.                     2.             3.           4.                5.                           Senado elige
                           candidatura
                           por mayoría                   APRUEBA
                           calificada ⅔                                  Presidente
                              partes                     RECHAZA          designa  Presidente                  APRUEBA
   propone                                Presidente    Senado elige
     terna                    RECHAZA     propone       por mayoría
                                          nueva terna   calificada ⅔
                                                        partes
Requisitos:
• Abogado
• 35 años
• 10 años de experiencia
           INTEGRACIÓN DE LA SUPREMA CORTEDe mantener este sistema, la Presidenta electa podrá designar a4 Ministros que sustituirán los nombramientos de Felipe Calderón:   •   Luis María Aguilar Morales (diciembre 2024)   •   Jorge Mario Pardo Rebolledo (febrero 2026)   •   Alfredo Gutiérrez Ortiz Mena (noviembre 2027)   •   Alberto Pérez Dayán (noviembre 2027).Para diciembre de este año, habrán 4 Ministros que podránevitar la invalidación de leyes generales.A mitad del sexenio, la Corte tendrá una mayoría de 7 Ministros.            LA JUSTICIA AL SERVICIO DE LA POLÍTICA                    Actos de injerencia en el reciente proceso electoral:1. En diciembre de 2023, la ministra Piña convocó a una cena privada en casa del ministroGonzález Alcántara al dirigente del PRI, Alejandro Moreno, al coordinador de campaña de XóchitlGálvez, Santiago Creel, y a los magistrados electorales de la Sala Superior del Tribunal Electoral.2.   En julio de 2024, un juez de Distrito ordenó al Tribunal Electoral designar dos magistraturasvacantes para calificar la elección presidencial, lo cual fue rechazado por la Sala Superior al serexcesiva y violatoria del artículo 99 constitucional.3.   En agosto de 2024, la ministra Piña admitió un recurso del dirigente delPAN, Marko Cortés, para que la Corte interpretara y definiera los criteriospara la asignación de diputaciones plurinominales en el Congreso.       PROCESOS VICIADOS EN SELECCIÓN                 DE JUECES1. Venta de exámenes. Se han documentado casosde corrupción al más alto nivel de la Escuela
Judicial, donde se vendieron los exámenes de
oposición para jueces en 186 mil pesos.2. Los concursos de oposición son impugnados
con frecuencia ante la inequidad, influyentismo o
falta de criterios objetivos, que permiten que
personas cercanas a jueces y magistrados resulten
vencedoras.
                                      NEPOTISMO    En diciembre de 2022, el Consejo de la Judicatura Federal reveló que:•   La mitad del personal 49% equivalente a (24 mil 546 personas) tiene al menos un familiar
    en el Poder Judicial.•   El 85.4% \de los magistrados y el 67% \de los jueces cuentan con familia al interior del PJF•   Los El 23.7% del personal del PJF tiene más de 4 familiares trabajando en la institución•   La persona que acumula más familiares en el PJF tiene 26
    parientes trabajando, e incluyen a un magistrado, 13
    secretarios, 2 actuarios y 10 oficiales.•   Esta información se obtiene del registro voluntario que realizan
    los trabajadores; por lo que se estima que la presencia de
    familiares políticos (cuñados, nueras, suegros, yernos) no
    registrados es mucho mayor.
                                            DISCIPLINA
De 2004 al 2023, se presentaron 38 mil quejas contra funcionarios del Poder Judicial.De estas quejas, se desecharon el 86% sin siquiera iniciar una investigación.De las quejas que sí se investigaron, el Consejo de la Judicatura sancionó a 472 jueces y
magistrados Apercibimientos y amonestaciones:   292   (0.7% del total) Suspensiones:     102                     (0.27% del total) Destituciones:    41                      (0.11% del total) Inhabilitación:   23                      (0.06% del total) Sanción económica: 14                     (0.04% del total)De enero de 2023 a la fecha, el poder Ejecutivo han
presentado 72 denuncias contra jueces y
magistrados ante el Consejo de la Judicatura Federal.
Ninguna ha resultado en sanción.
                                    REMUNERACIONES
     Artículo 127, fracción II de la Constitución:
   “Ningún servidor público podrá recibir remuneración… por el desempeño de su función, empleo, cargo o
   comisión, mayor a la establecida para el Presidente de la República en el presupuesto correspondiente.”Aunque esta reforma data de 2009, el Poder Judicial se ha resistido a cumplir con esta regla:1. Que los Ministros designados antes de 2009 ya tienen un derecho adquirido.2. Que los Ministros designados después de 2009 tendrán diferencias salariales discriminatorias.3. Que hay ambigüedad en los conceptos que comprenden la remuneración del Presidente/a.
                             PRESIDENTE                   MINISTROS
      SALARIO                  $129,432                    $286,423
  PRESTACIONES                  $32,106                    $174,360
       TOTAL                   $161,538                   $460,783Además de salarios y prestaciones, los Ministros reciben beneficios
adicionales que suman en total más de 700 mil pesos mensuales.
 (alimentos, camionetas, gasolina, telefonía, entre otros privilegios)"""
tokens = nltk.word_tokenize(text)
text2 = nltk.Text(tokens)
text2