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


def bt_dang3_p1_b3_c2_hh10(self):
            # Khai báo biến
            a=randint(1,9)
            b=randint(1,9)
            while b<=a:
                a=randint(1,9)
                b=randint(1,9)
            c=randint(1,9)    
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho tam giác $ABC$ có trung tuyến $AM$. Gọi $I$ là điểm thuộc $AM$ sao cho $AI=%sAM$. Khẳng định nào sau đây đúng? \n'
                                %(latex(Rational(a,b))
                                ))
                # Các đáp án
                da_d = '\\True $\\overrightarrow{BI}=%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$' %(latex(Rational(b-a,b)),latex(Rational(a,2*b)))
                da_s1 = '$\\overrightarrow{BI}=%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$' %(latex(Rational(a,b)),latex(Rational(a,2*b)))
                da_s2 = '$\\overrightarrow{BI}=%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$' %(latex(Rational(b-a,b)),latex(Rational(a,b)))
                da_s3 = '$\\overrightarrow{BI}=%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$' %(latex(Rational(b-a,b)),latex(Rational(3*a,2*b)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        '\\immini{ \n'

                        'Ta có \\\\\n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+\\overrightarrow{AI}$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+%s\\overrightarrow{AM}$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+%s \\left( \\overrightarrow{AB}+\\overrightarrow{BM} \\right)$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+%s\\overrightarrow{AB}+%s\\overrightarrow{BM}$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+%s\\overrightarrow{AB}+%s \\cdot \\dfrac{1}{2}\\overrightarrow{BC}$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}-%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$ \\\\ \n'
                        '$\\overrightarrow{BI}=%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$.'
                        '}{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1] \n'
                            '\\clip(-0.5906537197496043,-0.5921150680303137) rectangle (6.3811864336352455,4.607934129080795); \n'
                            '\\draw (2.,4.)-- (0.,0.); \n'
                            '\\draw (2.,4.)-- (6.,0.); \n'
                            '\\draw (6.,0.)-- (0.,0.); \n'
                            '\\draw (2.,4.)-- (3.,0.); \n'
                            '\\draw (0.,0.)-- (%s,%s); \n'
                            '\\draw (1.531143386163028,4.550674576748805) node[anchor=north west] {$A$}; \n'
                            '\\draw (-0.46565064493016016,0.04176284285230242) node[anchor=north west] {$B$}; \n'
                            '\\draw (6.003763508038472,0.12079490254137053) node[anchor=north west] {$C$}; \n'
                            '\\draw (2.71099231217602,0.036923141297642965) node[anchor=north west] {$M$}; \n'
                            '\\draw (%s,%s) node[anchor=north west] {$I$}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(latex(Rational(a,b)),
                        latex(Rational(a,b)),
                        latex(Rational(a,b)),latex(Rational(a,b)),
                        latex(Rational(a,b)),latex(Rational(a,b)),
                        latex(Rational(a,b)),latex(Rational(a,2*b)),
                        latex(Rational(b-a,b)),latex(Rational(a,2*b)),

                        latex(2+a/b),latex(4-4*a/b),
                        latex(2+a/b+0.2),latex(4-4*a/b+0.2)
                            )
                        )
            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho tam giác $ABC$. Gọi $I$ là điểm thuộc $AC$ sao cho $AI=%sAC$. Biết $\\overrightarrow{BI}=x\\overrightarrow{BA}+y\\overrightarrow{BC}$, khi đó $x+%sy$ bằng \n'
                                %(latex(Rational(a,b)),latex(c)
                                ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(Rational(b-a+c*a,b)))
                da_s1 = '$%s$' %(latex(Rational(b-a+c*a+1,b)))
                da_s2 = '$%s$' %(latex(Rational(b-a+c*a-1,b)))
                da_s3 = '$%s$' %(latex(Rational(b-a+c*a+2,b)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        '\\immini{ \n'

                        'Ta có \\\\\n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+\\overrightarrow{AI}$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+%s\\overrightarrow{AC}$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+%s \\left( \\overrightarrow{AB}+\\overrightarrow{BC} \\right)$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}+%s\\overrightarrow{AB}+%s\\overrightarrow{BC}$ \\\\ \n'
                        '$\\overrightarrow{BI}=\\overrightarrow{BA}-%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$ \\\\ \n'
                        '$\\overrightarrow{BI}=%s\\overrightarrow{BA}+%s\\overrightarrow{BC}$. \\\\ \n'
                        '}{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1] \n'
                            '\\clip(-0.5801697495941384,-0.4872753664756542) rectangle (6.748125389076554,4.524062367837067); \n'
                            '\\draw (2.,4.)-- (0.,0.); \n'
                            '\\draw (2.,4.)-- (6.,0.); \n'
                            '\\draw (6.,0.)-- (0.,0.); \n'
                            '\\draw (1.531143386163028,4.550674576748805) node[anchor=north west] {$A$}; \n'
                            '\\draw (-0.56565064493016016,0.14176284285230242) node[anchor=north west] {$B$}; \n'
                            '\\draw (6.003763508038472,0.12079490254137053) node[anchor=north west] {$C$}; \n'
                            '\\draw (%s,%s) node[anchor=north west] {$I$}; \n'
                            '\\draw (0.,0.)-- (%s,%s); \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(latex(Rational(a,b)),
                        latex(Rational(a,b)),
                        latex(Rational(a,b)),latex(Rational(a,b)),
                        latex(Rational(a,b)),latex(Rational(a,b)),
                        latex(Rational(b-a,b)),latex(Rational(a,b)),

                        latex(2+4*a/b),latex(4-4*a/b+0.4),
                        latex(2+4*a/b),latex(4-4*a/b),
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

