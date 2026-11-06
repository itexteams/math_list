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


def bt_dang3_p1_b2_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$IJ$ song song $MN$',
                    '$IJ$ song song $CD$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Xét $\\Delta AMN$ có $\\dfrac{AI}{AM}=\\dfrac{AJ}{AN}=\\dfrac{2}{3} \\Rightarrow IJ//MN$.\\\\ \n'
                    ),

                    ('Ta có $MN//CD$ \\hspace*{1cm} $(1)$.\\\\ \n'
                            'Xét $\\Delta AMN$ có $\\dfrac{AI}{AM}=\\dfrac{AJ}{AN}=\\dfrac{2}{3} \\Rightarrow IJ//MN$ \\hspace*{1cm} $(2)$.\\\\ \n'
                            'Từ $(1)$ và $(2)$ ta có $IJ//MN//CD$.'),


                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$IJ$ cắt $AB$',
                    '$IJ$ chéo $CD$',
                    '$IJ$ cắt $BC$',
                    '$IJ$ song song $BD$',
                    '$MN$ cắt $AB$',
                    '$MN$ chéo $CD$',
                    '$MN$ cắt $AC$',
                    '$MN$ chéo $IJ$',
                    '$IJ$ song song $AD$',
                    '$MN$ song song $AC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.1115710565452597,-1.5135594171366384) rectangle (5.3022309523852575,3.563441286163126);\n'
            '\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (4.,0.);\n'
            '\\draw (0.,0.)-- (1.,-1.);\n'
            '\\draw (1.,-1.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (2.,3.);\n'
            '\\draw (2.,3.)-- (0.,0.);\n'
            '\\draw (2.,3.)-- (1.,-1.);\n'
            '\\draw [dash pattern=on 1pt off 1pt] (2.,0.)-- (2.,3.);\n'
            '\\draw (0.5,-0.5)-- (2.,3.);\n'
            '\\draw [dash pattern=on 1pt off 1pt] (1.,0.6666666666666666)-- (2.,1.);\n'
            '\\draw [dash pattern=on 1pt off 1pt] (0.5,-0.5)-- (2.,0.);\n'
            '\\draw (1.8180147834540454,3.6061051576194263) node[anchor=north west] {$A$};\n'
            '\\draw (-0.8,0.24988060305711723) node[anchor=north west] {$B$};\n'
            '\\draw (0.5,-0.9304865072338644) node[anchor=north west] {$C$};\n'
            '\\draw (4.0791999706379745,0.3636509269405853) node[anchor=north west] {$D$};\n'
            '\\draw (2.15932575510445,0.6480767366492556) node[anchor=north west] {$N$};\n'
            '\\draw (-0.45,-0.2763071449039228) node[anchor=north west] {$M$};\n'
            '\\draw (0.5665412207358956,0.9609451273287929) node[anchor=north west] {$I$};\n'
            '\\draw (2.0313341407355483,1.5013541657752665) node[anchor=north west] {$J$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $I,J$ lần lượt là trọng tâm các tam giác $ABC$ và $ABD$. $M,N$ lần lượt là trung điểm $BC$ và $BD$. '
                                'Chọn khẳng định đúng trong các khẳng định sau. \n'
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

