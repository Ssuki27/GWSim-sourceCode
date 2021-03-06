# GWSim-sourceCode
Código fuente para el simulador GroundWave Simulator en Python

GroundWave Simulator ha sido desarrollado para la determinación y representación de intensidad de campo eléctrico recibido por onda de superficie para frecuencias entre 10 kHz y 30 MHz según la Rec. ITU-R P.368-9.

El simulador ha sido probado en entornos Windows 10 y Windows 10 Pro, y no se garantiza su funcionamiento fuera de éste.

El archivo principal del que se debe partir para su ejecución es GRMain.py, correspondiente a la primera ventana de bienvenida.

ventanaCalculos.py es la interfaz donde tienen lugar los cálculos tanto para terrenos homogéneos como para terrenos mixtos. Dentro de éste fichero se encuentran todas las posibles funciones a realizar. Su estructura base se ha realizado con el programa QtDesigner, que genera un archivo .ui (untitled.ui) y posteriormente convertido a .py con la opción pyuic5 (interfazCalculosStyle.py). Véase que se ha renombrado el archivo .py, interfazCalculosStyle.py y untitled.py son idénticos. Además, al generar el fichero .ui de QtDesigner y traducido a .py, se han incrustado algunas líneas de código adicionales, y se tendrá que hacer manualmente cada vez que se actualice la estructura con QtDesigner.

Para las ventanas emergentes o popUp's se utiliza popUpWarning.py, con estructura de QtDesigner: popUpWarning.ui.

info.py es otra ventana emergente de ayuda, al igual que freqWindow.py.

lectura2.py se encarga de la llamada a GRWAVE, lectura de sus datos de salida y posterior reconversión a estructuras de datos usando librería pandas.

mplwidget.py es la base para la representación de gráficas en ventanaCalculos.py, usando librería matplotlib.

Guia.txt ofrece una breve explicación del funcionamiento del simulador.
