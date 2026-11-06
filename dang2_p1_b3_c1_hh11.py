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


def bt_dang2_p1_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$MN//(DBC)$',
                    '$NP//(ABD)$',
                    '$PQ//(ACD)$',
                    '$MQ//(ABC)$',
                    'Tứ giác $MNPQ$ là hình bình hành',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có $MN$ là đường trung bình của tam giác $ACD$ nên $MN//CD$ mà $CD\\subset (BCD)$.\\\\ \n'
                    'Vậy $MN//(BCD)$.'),

                    ('Ta có $NP$ là đường trung bình của tam giác $CAB$ nên $NP//AB$ mà $AB\\subset (ABD)$.\\\\ \n'
                            'Vậy $NP//(ABD)$.'),

                    ('Ta có $PQ$ là đường trung bình của tam giác $BCD$ nên $PQ//CD$ mà $CD\\subset (BCD)$.\\\\ \n'
                            'Vậy $PQ//(BCD)$.'),

                    ('Ta có $MQ$ là đường trung bình của tam giác $DAB$ nên $MQ//AB$ mà $AB\\subset (ABC)$.\\\\ \n'
                            'Vậy $MQ//(ABC)$.'),


                    ('Ta có $MN$ là đường trung bình của tam giác $ACD$ nên $\\heva {& MN//CD \\\\ & MN=\\dfrac{1}{2}CD}$.\\\\ \n'
                    'Ta có $PQ$ là đường trung bình của tam giác $BCD$ nên $\\heva {& PQ//CD \\\\ & PQ=\\dfrac{1}{2}CD}$.\\\\ \n'
                    'Vậy $MN//PQ$ và $MN=PQ$. Vậy $MNPQ$ là hình bình hành'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$MN//(ABC)$',
                    '$NP//(BCD)$',
                    '$PQ//(ABC)$',
                    '$MQ//(BCD)$',
                    '$MN//(ACD)$',
                    '$NP//(ABC)$',
                    '$PQ//(BCD)$',
                    '$MQ//(ABD)$',
                    'Tứ giác $ABCD$ là hình vuông',

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(0.7997145003756608,-2.748790383170552) rectangle (8.868835462058605,2.525439519158525);\n'
            '\\draw (2.,0.)-- (6.,2.);\n'
            '\\draw (6.,2.)-- (7.,0.);\n'
            '\\draw (7.,0.)-- (5.,-2.);\n'
            '\\draw (5.,-2.)-- (2.,0.);\n'
            '\\draw (4.,1.)-- (3.5,-1.);\n'
            '\\draw (5.,-2.)-- (6.,2.);\n'
            '\\draw (6.5,1.)-- (6.,-1.);\n'
            '\\draw (6.,-1.)-- (3.5,-1.);\n'
            '\\draw (4.,1.)-- (6.5,1.);\n'
            '\\draw (2.,0.)-- (3.75,0.);\n'
            '\\draw (6.25,0.)-- (7.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (3.75,0.)-- (6.25,0.);\n'
            '\\draw (1.4,0.3015477084898545) node[anchor=north west] {$A$};\n'
            '\\draw (6.9,0.18133734034560203) node[anchor=north west] {$B$};\n'
            '\\draw (5.8,2.5) node[anchor=north west] {$C$};\n'
            '\\draw (4.826761833208118,-1.892291510142753) node[anchor=north west] {$D$};\n'
            '\\draw (2.8,-0.9456348610067649) node[anchor=north west] {$M$};\n'
            '\\draw (3.774921111945909,1.789151014274979) node[anchor=north west] {$N$};\n'
            '\\draw (6.5,1.578782870022537) node[anchor=north west] {$P$};\n'
            '\\draw (5.9988129226145785,-0.8254244928625124) node[anchor=north west] {$Q$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hai tam giác $ABC$ và $ABD$ không cùng nằm trong một mặt phẳng, $M,N,P,Q$ lần lượt là trung điểm $AD,AC,BC,BD$. Khẳng định nào sau đây đúng? \n'
                                )
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

