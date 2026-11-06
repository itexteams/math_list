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


def bt_dang6_p1_b5_c2_hh10(self):
            # Khai báo biến
            a=randint(1,20)
            i=randint(-3,3)
            if i==0:
                i=randint(-3,3)

            lisdang=['1','2','3']
            dang=random.choice(lisdang)

            if dang=='3':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho tam giác đều $ABC$ có tâm $O$ cạnh $%s$, $M$ là trung điểm của $BC$. Tích $\\overrightarrow{OM} \\cdot \\overrightarrow{AC}$ bằng   \n'
                                %(latex(a)
                                ))
                # Các đáp án
                da_d = '\\True $%s$'%(latex(Rational(a**2,4)))
                da_s1 = '$%s$'%(latex(-Rational(a**2,4)+i))
                da_s2 = '$%s$'%(latex(-Rational(a**2,4)-i))
                da_s3 = '$%s$'%(latex(-Rational(a**2,4)+2*i))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('\\immini{ \n'
                        'Độ dài trung tuyến $AM=%s$.\\\\ \n'
                        '$OA=OB=OC=%s$, $OM=%s$. \\\\ \n'
                        'Góc giữa hai vectơ $\\overrightarrow{OM}$ và $\\overrightarrow{AC}$ là $30^\\circ$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\overrightarrow{OM} \\cdot \\overrightarrow{AC} = \\left| \\overrightarrow{OM} \\right| \\cdot \\left| \\overrightarrow{AC} \\right| \\cdot \\cos 30^\\circ$ \\\\ \n'
                        '\\hspace*{1.6cm} $=OM \\cdot AC \\cdot \\cos 30^\\circ$ \\\\ \n'
                        '\\hspace*{1.6cm} $=%s \\cdot %s \\cdot \\cos 30^\\circ = %s$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {A};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {B};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {C};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {M};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(latex(a*sqrt(3)/2),latex(a*sqrt(3)/3),latex(a*sqrt(3)/6),
                        latex(a*sqrt(3)/6),latex(a),
                        latex(Rational(a**2,4))
                        ))

            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho tam giác đều $ABC$ có tâm $O$ cạnh $%s$, $M$ là trung điểm của $BC$. Tích $\\overrightarrow{OA} \\cdot \\overrightarrow{OC}$ bằng   \n'
                                %(latex(a)
                                ))
                # Các đáp án
                da_d = '\\True $%s$'%(latex(-Rational(a**2,6)))
                da_s1 = '$%s$'%(latex(-Rational(a**2,6)+i))
                da_s2 = '$%s$'%(latex(-Rational(a**2,6)-i))
                da_s3 = '$%s$'%(latex(-Rational(a**2,6)+2*i))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('\\immini{ \n'
                        'Độ dài trung tuyến $AM=%s$.\\\\ \n'
                        '$OA=OB=OC=%s$. \\\\ \n'
                        'Góc giữa hai vectơ $\\overrightarrow{OA}$ và $\\overrightarrow{OC}$ là $120^\\circ$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\overrightarrow{OA} \\cdot \\overrightarrow{OC} = \\left| \\overrightarrow{OA} \\right| \\cdot \\left| \\overrightarrow{OC} \\right| \\cdot \\cos 120^\\circ$ \\\\ \n'
                        '\\hspace*{1.6cm} $=OA \\cdot OC \\cdot \\cos 120^\\circ$ \\\\ \n'
                        '\\hspace*{1.6cm} $=%s \\cdot %s \\cdot \\cos 120^\\circ = %s$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {A};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {B};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {C};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {M};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(latex(a*sqrt(3)/2),latex(a*sqrt(3)/3),
                        latex(a*sqrt(3)/3),latex(a*sqrt(3)/3),
                        latex(-Rational(a**2,6))
                        ))

            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho tam giác đều $ABC$ có tâm $O$ cạnh $%s$, $M$ là trung điểm của $BC$. Tích $\\overrightarrow{CA} \\cdot \\overrightarrow{CB}$ bằng   \n'
                                %(latex(a)
                                ))
                # Các đáp án
                da_d = '\\True $%s$'%(latex(Rational(a**2,2)))
                da_s1 = '$%s$'%(latex(Rational(a**2,2)+i))
                da_s2 = '$%s$'%(latex(Rational(a**2,2)-i))
                da_s3 = '$%s$'%(latex(Rational(a**2,2)+2*i))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('\\immini{ \n'
                        'Độ dài trung tuyến $AM=%s$.\\\\ \n'
                        '$OA=OB=OC=%s$. \\\\ \n'
                        'Góc giữa hai vectơ $\\overrightarrow{CA}$ và $\\overrightarrow{CB}$ là $60^\\circ$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\overrightarrow{CA} \\cdot \\overrightarrow{CB} = \\left| \\overrightarrow{CA} \\right| \\cdot \\left| \\overrightarrow{CB} \\right| \\cdot \\cos 60^\\circ$ \\\\ \n'
                        '\\hspace*{1.6cm} $=CA \\cdot CB \\cdot \\cos 60^\\circ$ \\\\ \n'
                        '\\hspace*{1.6cm} $=%s \\cdot %s \\cdot \\cos 60^\\circ = %s$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-3.5082521596683605,-2.324972514432068) rectangle (3.9337747347675935,3.9179238006678525);  \n'
                            '\\draw (0.,3.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (-2.598076211353316,-1.5)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (2.598076211353316,-1.5)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (0.,-1.5);  \n'
                            '\\draw (0.,0.)-- (-2.598076211353316,-1.5);  \n'
                            '\\draw (0.,0.)-- (2.598076211353316,-1.5);  \n'
                            '\\draw (0,3.53) node[anchor=north] {A};  \n'
                            '\\draw (-2.8,-1.5) node[anchor=north west] {B};  \n'
                            '\\draw (2.6,-1.5) node[anchor=north west] {C};  \n'
                            '\\draw (0,0.5) node[anchor=north west] {O};  \n'
                            '\\draw (-0.03448213087018273,-1.632690942856631) node[anchor=north] {M};  \n'
                        '\\end{tikzpicture}  \n'
                        '} \n'

                        %(latex(a*sqrt(3)/2),latex(a*sqrt(3)/3),
                        latex(a),latex(a),
                        latex(Rational(a**2,2))
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

