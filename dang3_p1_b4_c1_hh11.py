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


def bt_dang3_p1_b4_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                hinhve=('''\\begin{center} \n'''
                    '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'''
            '''\\clip(-0.722104677671335,0.29778093237477865) rectangle (7.422555527460984,5.7397287824407615);\n'''
            '''\\draw (1.,1.)-- (5.,1.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (1.,1.)-- (3.,2.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (3.,2.)-- (5.,1.);\n'''
            '''\\draw (1.,1.)-- (2.,4.);\n'''
            '''\\draw (2.,4.)-- (6.,4.);\n'''
            '''\\draw (6.,4.)-- (5.,1.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (3.,2.)-- (4.,5.);\n'''
            '''\\draw (4.,5.)-- (2.,4.);\n'''
            '''\\draw (4.,5.)-- (6.,4.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (1.5,2.5)-- (3.5,3.5);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (3.5,3.5)-- (5.5,2.5);\n'''
            '''\\draw (5.5,2.5)-- (1.5,2.5);\n'''
            '''\\draw (1.3779758684950703,4.534465164640913) node[anchor=north west] {$A$};\n'''
            '''\\draw (3.78850310409477,5.684944072540769) node[anchor=north west] {$B$};\n'''
            '''\\draw (6.089460919894483,4.461418884774256) node[anchor=north west] {$C$};\n'''
            '''\\draw (0.3188048104285354,1.5578292600746204) node[anchor=north west] {$A'$};\n'''
            '''\\draw (2.4554084965282694,2.5) node[anchor=north west] {$B'$};\n'''
            '''\\draw (5.139859281627935,1.3569519904413123) node[anchor=north west] {$C'$};\n'''
            '''\\draw (0.9214366193284603,2.9457085775411125) node[anchor=north west] {$D$};\n'''
            '''\\draw (3.03977873546153,4) node[anchor=north west] {$E$};\n'''
            '''\\draw (5.614660100761209,2.7448313079078046) node[anchor=north west] {$F$};\n'''
            '''\\end{tikzpicture}\n'''
            '''\\end{center}\n''')
                #NHập đáp án đúng vào đây
                du = ['''$(AEF)//(DB'C')$''',
                      '''$(CDE)//(FA'B')$''',
                      '''$(BDF)//(EA'C')$''',
                      '''$(ABF)//(DEC')$''',
                      '''$(BCD)//(EFA')$''',
                      '''$(ACE)//(DFB')$''',
                      ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('''Ta có hai tứ giác $B'C'FE; B'DAE$ là hình bình hành nên\\\\ \n'''
                             '''$B'C'//EF\\subset (AEF)\\Rightarrow B'C'//(AEF)$.\\\\ \n'''
                             '''$B'D//EA\\subset (AEF)\\Rightarrow B'D//(AEF)$.\\\\ \n'''
                             '''Vậy $(AEF)//(DB'C')$.'''
                             ),
                      ('''Ta có hai tứ giác $CDA'F; CEB'F$ là hình bình hành nên\\\\ \n'''
                             '''$CD//A'F'\\subset (FA'B')\\Rightarrow CD//(FA'B')$.\\\\ \n'''
                             '''$CE//B'F\\subset (FA'B')\\Rightarrow CE//(FA'B')$.\\\\ \n'''
                             '''Vậy $(CDE)//(FA'B')$.'''
                             ),

                      ('''Ta có hai tứ giác $BDA'E; BFC'E$ là hình bình hành nên\\\\ \n'''
                             '''$BD//A'E\\subset (EA'C')\\Rightarrow BD//(EA'C')$.\\\\ \n'''
                             '''$BF//C'E\\subset (EA'C')\\Rightarrow BF//(EA'C')$.\\\\ \n'''
                             '''Vậy $(BDF)//(EA'C')$.'''
                             ),

                      ('''Ta có hai tứ giác $AFC'D; BFC'E$ là hình bình hành nên\\\\ \n'''
                             '''$AF//C'D\\subset (DEC')\\Rightarrow AF//(DEC')$.\\\\ \n'''
                             '''$BF//C'E\\subset (DEC')\\Rightarrow BF//(DEC')$.\\\\ \n'''
                             '''Vậy $(ABF)//(DEC')$.'''
                             ),

                      ('''Ta có hai tứ giác $CDA'F; BDA'E$ là hình bình hành nên\\\\ \n'''
                             '''$CD//A'F\\subset (EFA')\\Rightarrow CD//(EFA')$.\\\\ \n'''
                             '''$BD//A'E\\subset (EFA')\\Rightarrow BD//(EFA')$.\\\\ \n'''
                             '''Vậy $(BCD)//(EFA')$.'''
                             ),

                      ('''Ta có hai tứ giác $CEB'F; AEB'D$ là hình bình hành nên\\\\ \n'''
                             '''$CE//B'F\\subset (DFB')\\Rightarrow CE//(DFB')$.\\\\ \n'''
                             '''$AE//B'D\\subset (DFB')\\Rightarrow AE//(DFB')$.\\\\ \n'''
                             '''Vậy $(ACE)//(DFB')$.'''
                             ),
                      ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['''$(AEF)//(A'B'C')$''',
                      '''$(BDF)//(A'B'C')$''',
                     '''$(AEF)//(BCD)$''',
                     '''$(ABF)//(DEC)$''',
                     '''$(ACE)//(DFB)$''',
                     '''$(ABC)//(EA'B')$''',
                     '''$(A'B'C')//(ACE)$''',
                     '''$(A'B'C')//(BCD)$''',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hình lăng trụ $ABC.A'B'C'$. Lấy các điểm $D,E,F$ lần lượt là trung điểm của $AA',BB',CC'$. Mệnh đề nào sau đây đúng?'''
                                 %(
                                 ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(hinhve)+''+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

