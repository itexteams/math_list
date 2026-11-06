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


def bt_dang12_p1_b3_c2_hh10(self):
            # Khai báo biến
            a=randint(2,10)
            b=randint(2,10)

            kq1=Rational(2*a**2+a*b,2*a*b+2*b**2)
            kq2=Rational(8*a**2+4*a*b,6*a*b+6*b**2)
            kq3=Rational(4*a**2+4*a*b,6*a*b+6*b**2)
            kq4=Rational(8*a**2+4*a*b,3*a*b+6*b**2)

            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho tam giác $ABC$ có trọng tâm $G$. Gọi $H$ là chân đường cao hạ từ $A$ thỏa mãn $\\overrightarrow{BH}=%s\\overrightarrow{HC}$. Điểm $M$ di động trên $BC$ sao cho $\\overrightarrow{BM}=x\\overrightarrow{BC}$. Giá trị của $x$ để độ dài vectơ $\\overrightarrow{MA}+\\overrightarrow{GC}$ đạt giá trị nhỏ nhất là  \n'
                                %(latex(Rational(a,b))
                                ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(kq2))
                da_s1 = '$%s$' %(latex(kq1))
                da_s2 = '$%s$' %(latex(kq3))
                da_s3 = '$%s$' %(latex(kq4))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]   \n'
                                '\\clip(-0.4584469584762757,-0.605325032090909) rectangle (6.369173603941442,4.460600841999274); \n'
                                '\\draw (2.,4.)-- (0.,0.); \n'
                                '\\draw (0.,0.)-- (6.,0.); \n'
                                '\\draw (6.,0.)-- (2.,4.); \n'
                                '\\draw (2.,4.)-- (3.,0.); \n'
                                '\\draw (0.,0.)-- (4.,2.); \n'
                                '\\draw (2.6666666666666665,1.3333333333333333)-- (6.,0.); \n'
                                '\\draw (2.,4.)-- (5.333333333333333,2.6666666666666665); \n'
                                '\\draw (5.333333333333333,2.6666666666666665)-- (6.,0.); \n'
                                '\\draw (5.333333333333333,2.6666666666666665)-- (4.,2.); \n'
                                '\\draw (2.,4.)-- (2.,0.); \n'
                                '\\draw (4.,2.)-- (4.,0.); \n'
                                '\\draw (5.333333333333333,2.6666666666666665)-- (5.333333333333333,0.); \n'
                                '\\draw (2.,4.)-- (3.550264017329468,0.); \n'
                                '\\draw (3.550264017329468,0.)-- (5.333333333333333,2.6666666666666665); \n'
                                '\\draw (1.6427140458941405,4.584738391305744) node[anchor=north west] {$A$}; \n'
                                '\\draw (-0.4645762511483652,0.07743702415086273) node[anchor=north west] {$B$}; \n'
                                '\\draw (5.874152962355491,0.08586618533903276) node[anchor=north west] {$C$}; \n'
                                '\\draw (1.6595723682704803,0.010003734645502554) node[anchor=north west] {$H$}; \n'
                                '\\draw (2.056892878372512,1.7452610051504868) node[anchor=north west] {$G$}; \n'
                                '\\draw (5.3913909061137195,3.0023559564458604) node[anchor=north west] {$E$}; \n'
                                '\\draw (5.031236843538489,-0.03214207129534756) node[anchor=north west] {$F$}; \n'
                                '\\draw (3.699429375807626,2.629172995650299) node[anchor=north west] {$P$}; \n'
                                '\\draw (3.6910002146194556,0.010003734645502554) node[anchor=north west] {$Q$}; \n'
                                '\\draw (3.2021088657055945,0.0268620570218426) node[anchor=north west] {$M$}; \n'
                                '\\draw (2.671071710850883,0.010003734645502554) node[anchor=north west] {$I$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'
                        'Dựng hình bình hành $AGCE$. Ta có $\\overrightarrow{MA}+\\overrightarrow{GC}=\\overrightarrow{MA}+\\overrightarrow{AE}=\\overrightarrow{ME}$. \\\\ \n'
                        'Dựng $EF\\bot BC$ tại $F$ khi đó $\\left| \\overrightarrow{MA}+\\overrightarrow{GC} \\right| =\\left| \\overrightarrow{ME} \\right|=ME \\ge EF$. \\\\ \n'
                        'Do đó $\\left| \\overrightarrow{MA}+\\overrightarrow{GC} \\right|$ nhỏ nhất khi $M\\equiv F$.\\\\ \n'
                        'Gọi $P$ là trung điểm của $AC$, Dựng $PQ\\bot BC$ tại $Q$, ta có $BP=\\dfrac{3}{4}BE $. \\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\bigtriangleup BPQ \\sim \\bigtriangleup BEF \\Rightarrow \\dfrac{BQ}{BF}=\\dfrac{BP}{BE}=\\dfrac{3}{4} \\Rightarrow \\overrightarrow{BF} =\\dfrac{4}{3} \\overrightarrow{BQ}$. \\\\ \n'
                        'Mặt khác \\\\ \n'
                        '$\\overrightarrow{BH} =%s \\overrightarrow{HC} \\Rightarrow PQ$ là đường trung bình của $\\bigtriangleup AHC \\Rightarrow \\overrightarrow{HQ} =\\dfrac{1}{2} \\overrightarrow{HC}$. \\\\ \n'
                        '$\\overrightarrow{BQ}=\\overrightarrow{BH}+\\overrightarrow{HQ}=%s \\overrightarrow{HC}+\\dfrac{1}{2} \\overrightarrow{HC}=%s \\overrightarrow{HC}=%s \\cdot %s \\overrightarrow{BC}=%s \\overrightarrow{BC} \\\\ \n'
                        '\\Rightarrow \\overrightarrow{BF}=\\dfrac{4}{3} \\overrightarrow{BQ}=\\dfrac{4}{3} \\cdot %s \\overrightarrow{BC}=%s \\overrightarrow{BC} $ \\\\ \n'
                        'Vậy $x=%s$.'
                        %(latex(Rational(a,b)),latex(Rational(a,b)),latex(Rational(2*a+b,2*b)),latex(Rational(2*a+b,2*b)),latex(Rational(a,a+b)),latex(kq1),latex(kq1),latex(kq2),
                        latex(kq2)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-')
            return content

