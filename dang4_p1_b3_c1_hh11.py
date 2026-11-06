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


def bt_dang4_p1_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$GM//(BCD)$',
                    '$GP//(ABC)$',
                    '$GN//(ACD)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có $AM=2MB \\Rightarrow \\dfrac{AM}{AB}=\\dfrac{2}{3}$.\\\\ \n'
                    'Mặt khác gọi $S$ là trung điểm $BD$, $G$ là trọng tâm tam giác $ABD$ nên $\\dfrac{AG}{AS}=\\dfrac{2}{3}$.\\\\ \n'
                    'Trong tam giác $ABP$ có $\\dfrac{AM}{AB}=\\dfrac{AG}{AS}=\\dfrac{2}{3}\\Rightarrow GM//SB$ mà $SB\\subset (BCD)$.\\\\ \n'
                    'Vậy $GM//(BCD)$.'),

                    ('Ta có $PA=\\dfrac{1}{2}PD \\Rightarrow \\dfrac{DP}{DA}=\\dfrac{2}{3}$.\\\\ \n'
                            'Mặt khác gọi $Q$ là trung điểm $AB$, $G$ là trọng tâm tam giác $ABD$ nên $\\dfrac{DG}{AQ}=\\dfrac{2}{3}$.\\\\ \n'
                            'Trong tam giác $DAQ$ có $\\dfrac{DP}{DA}=\\dfrac{DG}{DQ}=\\dfrac{2}{3}\\Rightarrow GP//QA$ mà $QA\\subset (ABC)$.\\\\ \n'
                            'Vậy $GP//(ABC)$.'),

                    ('Ta có $BD=3DN \\Rightarrow \\dfrac{BN}{BD}=\\dfrac{2}{3}$.\\\\ \n'
                            'Mặt khác gọi $R$ là trung điểm $AD$, $G$ là trọng tâm tam giác $ABD$ nên $\\dfrac{BG}{BR}=\\dfrac{2}{3}$.\\\\ \n'
                            'Trong tam giác $BDR$ có $\\dfrac{BN}{BD}=\\dfrac{BG}{BR}=\\dfrac{2}{3}\\Rightarrow GN//DR$ mà $DR\\subset (ACD)$.\\\\ \n'
                            'Vậy $GN//(ACD)$.'),


                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$GM//(ABC)$',
                    '$GM//(ACD)$',
                    '$GN//(BCD)$',
                    '$GN//(ABC)$',
                    '$GP//(BCD)$',
                    '$GP//(ACD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.2037689475746367,-2.7002490312917398) rectangle (6.181180597653652,2.7057271063917194);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.);\n'
            '\\draw (5.,0.)-- (2.,-2.);\n'
            '\\draw (2.,-2.)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (2.,2.);\n'
            '\\draw (2.,2.)-- (5.,0.);\n'
            '\\draw (2.,2.)-- (2.,-2.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (3.5,-1.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,-1.)-- (5.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.3333333333333335,-0.6666666666666666)-- (3.,-1.3333333333333333);\n'
            '\\draw (5.071024783665086,0.4) node[anchor=north west] {$A$};\n'
            '\\draw (1.6279328388309817,-2) node[anchor=north west] {$B$};\n'
            '\\draw (-0.6,0.3727909755461789) node[anchor=north west] {$D$};\n'
            '\\draw (1.8692710592632786,2.7057271063917194) node[anchor=north west] {$C$};\n'
            '\\draw (1.9,-0.04552860653646973) node[anchor=north west] {$G$};\n'
            '\\draw (2.9955160879473315,-1.1395952058295507) node[anchor=north west] {$M$};\n'
            '\\draw (3.1,0.6) node[anchor=north west] {$P$};\n'
            '\\draw (-0.15,-0.31904525635973996) node[anchor=north west] {$N$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.3333333333333335,-0.6666666666666666)-- (3.3333333333333335,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.6666666666666666,-0.6666666666666666)-- (2.3333333333333335,-0.6666666666666666);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,-2.)-- (2.5,0.);\n'
            '\\draw (0.4,-0.7695432678333616) node[anchor=north west] {$S$};\n'
            '\\draw (3.5747278169848444,-0.6890971943559292) node[anchor=north west] {$Q$};\n'
            '\\draw (2.335858285432386,0.6) node[anchor=north west] {$R$};\n'
            '\\end{tikzpicture};\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $G$ là trọng tâm của tam giác $ABD$, $M$ thuộc cạnh $AB$ sao cho $AM=2MB$, $N$ thuộc cạnh $BD$ sao cho $BD=3DN$, $P$ thuộc cạnh $AD$ sao cho $PA=\\dfrac{1}{2}PD$ Khẳng định nào sau đây đúng? \n'
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

