import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang8_p1_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(2,7)

                du = ['$-%sa^2$'%(latex(2*a*a)),
                    ]
                da= random.choice(du)
                s = ['$%sa^2$'%(latex(2*a*a)),
                    '$-%sa^2$'%(latex(2*a)),
                    '$%sa^2$'%(latex(3*a*a)),
                    '$-%sa$'%(latex(2*a*a)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hình lập phương $ABCD.A\'B\'C\'D\'$ cạnh bằng $%sa$. Tích vô hướng $\\vec{AC}\\cdot\\vec{C\'A\'}$ bằng'
                            '}{'
                            '\\scalebox{0.6}{ '  
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.8492177589851994,-1.1656236786469323) rectangle (7.319915433403805,6.2085835095137405); \n'
                                '\\draw (0.,0.)-- (4.,0.); \n'
                                '\\draw (4.,0.)-- (6.,2.); \n'
                                '\\draw [dashed](6.,2.)-- (2.,2.); \n'
                                '\\draw [dashed] (2.,2.)-- (0.,0.); \n'
                                '\\draw  (0.,0.)-- (0.,3.); \n'
                                '\\draw  (0.,3.)-- (2.,5.); \n'
                                '\\draw[dashed] (2.,5.)-- (2.,2.); \n'
                                '\\draw  (2.,5.)-- (6.,5.); \n'
                                '\\draw  (6.,5.)-- (6.,2.); \n'
                                '\\draw  (6.,5.)-- (4.,3.); \n'
                                '\\draw  (4.,3.)-- (4.,0.); \n'
                                '\\draw  (4.,3.)-- (0.,3.); \n'
                                '\\draw (-0.409471458773783,0) node[anchor=north west] {$A$}; \n'
                                '\\draw (3.8695983086680767,0.1197885835095153) node[anchor=north west] {$B$}; \n'
                                '\\draw (6.135983086680762,2.3692600422832983) node[anchor=north west] {$C$}; \n'
                                '\\draw (1.4002536997885846,2.504566596194503) node[anchor=north west] {$D$}; \n'
                                '\\draw (-0.6124312896405906,3.553192389006342) node[anchor=north west] {$A\'$}; \n'
                                '\\draw (4.106384778012686,3.2994926004228327) node[anchor=north west] {$B\'$}; \n'
                                '\\draw (6.119069767441861,5.718097251585622) node[anchor=north west] {$C\'$}; \n'
                                '\\draw (1.4509936575052864,5.7688372093023235) node[anchor=north west] {$D\'$}; \n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(a)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Vì $AC,C\'A\'$ là các đường chéo của hình vuông cạnh có độ dài cạnh bằng $%sa$ nên ta có '
                        '$\\abs{\\vec{AC}}=%sa\\sqrt{2},\\abs{\\vec{C\'A\'}}=%sa\\sqrt{2}$.\\\\ \n'
                        '$\\vec{AC}$ và $\\vec{C\'A\'}$ ngược hướng nên $(\\vec{AC},\\vec{C\'A\'})=180^{\\circ}$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '$$\\vec{AC}\\cdot\\vec{C\'A\'}=\\abs{\\vec{AC}}\\cdot\\abs{\\vec{C\'A\'}}\\cdot\\cos (\\vec{AC},\\vec{C\'A\'})=%sa\\sqrt{2}\\cdot %sa\\sqrt{2}\\cdot\\cos 180^{\\circ}=-%sa^2.$$'
                        %(latex(a),latex(a),latex(a),
                            latex(a),latex(a),latex(2*a*a)


                            )

                        )
            if dang=='2':
                # Khai báo biến
                a=randint(2,7)

                du = ['$-%sa^2$'%(latex(2*a*a)),
                    ]
                da= random.choice(du)
                s = ['$%sa^2$'%(latex(2*a*a)),
                    '$-%sa^2$'%(latex(2*a)),
                    '$%sa^2$'%(latex(3*a*a)),
                    '$-%sa$'%(latex(2*a*a)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hình lập phương $ABCD.A\'B\'C\'D\'$ cạnh bằng $%sa$. Tích vô hướng $\\vec{BD}\\cdot\\vec{D\'B\'}$ bằng'
                            '}{'
                            '\\scalebox{0.6}{ '  
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.8492177589851994,-1.1656236786469323) rectangle (7.319915433403805,6.2085835095137405); \n'
                                '\\draw (0.,0.)-- (4.,0.); \n'
                                '\\draw (4.,0.)-- (6.,2.); \n'
                                '\\draw [dashed](6.,2.)-- (2.,2.); \n'
                                '\\draw [dashed] (2.,2.)-- (0.,0.); \n'
                                '\\draw  (0.,0.)-- (0.,3.); \n'
                                '\\draw  (0.,3.)-- (2.,5.); \n'
                                '\\draw[dashed] (2.,5.)-- (2.,2.); \n'
                                '\\draw  (2.,5.)-- (6.,5.); \n'
                                '\\draw  (6.,5.)-- (6.,2.); \n'
                                '\\draw  (6.,5.)-- (4.,3.); \n'
                                '\\draw  (4.,3.)-- (4.,0.); \n'
                                '\\draw  (4.,3.)-- (0.,3.); \n'
                                '\\draw (-0.409471458773783,0) node[anchor=north west] {$A$}; \n'
                                '\\draw (3.8695983086680767,0.1197885835095153) node[anchor=north west] {$B$}; \n'
                                '\\draw (6.135983086680762,2.3692600422832983) node[anchor=north west] {$C$}; \n'
                                '\\draw (1.4002536997885846,2.504566596194503) node[anchor=north west] {$D$}; \n'
                                '\\draw (-0.6124312896405906,3.553192389006342) node[anchor=north west] {$A\'$}; \n'
                                '\\draw (4.106384778012686,3.2994926004228327) node[anchor=north west] {$B\'$}; \n'
                                '\\draw (6.119069767441861,5.718097251585622) node[anchor=north west] {$C\'$}; \n'
                                '\\draw (1.4509936575052864,5.7688372093023235) node[anchor=north west] {$D\'$}; \n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(a)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Vì $BD,D\'B\'$ là các đường chéo của hình vuông cạnh có độ dài cạnh bằng $%sa$ nên ta có '
                        '$\\abs{\\vec{BD}}=%sa\\sqrt{2},\\abs{\\vec{D\'B\'}}=%sa\\sqrt{2}$.\\\\ \n'
                        '$\\vec{BD}$ và $\\vec{D\'B\'}$ ngược hướng nên $(\\vec{BD},\\vec{D\'B\'})=180^{\\circ}$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '$$\\vec{BD}\\cdot\\vec{D\'B\'}=\\abs{\\vec{BD}}\\cdot\\abs{\\vec{D\'B\'}}\\cdot\\cos (\\vec{BD},\\vec{D\'B\'})=%sa\\sqrt{2}\\cdot %sa\\sqrt{2}\\cdot\\cos 180^{\\circ}=-%sa^2.$$'
                        %(latex(a),latex(a),latex(a),
                            latex(a),latex(a),latex(2*a*a)


                            )

                        )

            if dang=='3':
                # Khai báo biến
                a=randint(2,7)

                du = ['$-%sa^2$'%(latex(2*a*a)),
                    ]
                da= random.choice(du)
                s = ['$%sa^2$'%(latex(2*a*a)),
                    '$-%sa^2$'%(latex(2*a)),
                    '$%sa^2$'%(latex(3*a*a)),
                    '$-%sa$'%(latex(2*a*a)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hình lập phương $ABCD.A\'B\'C\'D\'$ cạnh bằng $%sa$. Tích vô hướng $\\vec{AB\'}\\cdot\\vec{C\'D}$ bằng'
                            '}{'
                            '\\scalebox{0.6}{ '  
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.8492177589851994,-1.1656236786469323) rectangle (7.319915433403805,6.2085835095137405); \n'
                                '\\draw (0.,0.)-- (4.,0.); \n'
                                '\\draw (4.,0.)-- (6.,2.); \n'
                                '\\draw [dashed](6.,2.)-- (2.,2.); \n'
                                '\\draw [dashed] (2.,2.)-- (0.,0.); \n'
                                '\\draw  (0.,0.)-- (0.,3.); \n'
                                '\\draw  (0.,3.)-- (2.,5.); \n'
                                '\\draw[dashed] (2.,5.)-- (2.,2.); \n'
                                '\\draw  (2.,5.)-- (6.,5.); \n'
                                '\\draw  (6.,5.)-- (6.,2.); \n'
                                '\\draw  (6.,5.)-- (4.,3.); \n'
                                '\\draw  (4.,3.)-- (4.,0.); \n'
                                '\\draw  (4.,3.)-- (0.,3.); \n'
                                '\\draw (-0.409471458773783,0) node[anchor=north west] {$A$}; \n'
                                '\\draw (3.8695983086680767,0.1197885835095153) node[anchor=north west] {$B$}; \n'
                                '\\draw (6.135983086680762,2.3692600422832983) node[anchor=north west] {$C$}; \n'
                                '\\draw (1.4002536997885846,2.504566596194503) node[anchor=north west] {$D$}; \n'
                                '\\draw (-0.6124312896405906,3.553192389006342) node[anchor=north west] {$A\'$}; \n'
                                '\\draw (4.106384778012686,3.2994926004228327) node[anchor=north west] {$B\'$}; \n'
                                '\\draw (6.119069767441861,5.718097251585622) node[anchor=north west] {$C\'$}; \n'
                                '\\draw (1.4509936575052864,5.7688372093023235) node[anchor=north west] {$D\'$}; \n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(a)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Vì $AB\',C\'D$ là các đường chéo của hình vuông cạnh có độ dài cạnh bằng $%sa$ nên ta có '
                        '$\\abs{\\vec{AB\'}}=%sa\\sqrt{2},\\abs{\\vec{C\'D}}=%sa\\sqrt{2}$.\\\\ \n'
                        '$\\vec{AB\'}$ và $\\vec{C\'D}$ ngược hướng nên $(\\vec{AB\'},\\vec{C\'D})=180^{\\circ}$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '$$\\vec{AB\'}\\cdot\\vec{C\'D}=\\abs{\\vec{AB\'}}\\cdot\\abs{\\vec{C\'D}}\\cdot\\cos (\\vec{AB\'},\\vec{C\'D})=%sa\\sqrt{2}\\cdot %sa\\sqrt{2}\\cdot\\cos 180^{\\circ}=-%sa^2.$$'
                        %(latex(a),latex(a),latex(a),
                            latex(a),latex(a),latex(2*a*a)


                            )

                        )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

