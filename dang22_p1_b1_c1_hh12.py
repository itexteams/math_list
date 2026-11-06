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


def bt_dang22_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1', '2'] # Add a new problem type
            dang=random.choice(lisdang)

            if dang=='1':
                # (Original problem code remains here)
                r1=92
                v1=80
                t=10
                g=t*v1*360
                g1=Rational(g,180)
                kq1=r1*g1
                kq2=kq1*pi/100000
                kq3 = Decimal(float(kq2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq=str(kq3).replace('.',',')
                kq4=round(kq2,1)
                du = ['$%s$'%(kq),
                ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq4+1)).replace('.',','),
                '$%s$'%(latex(kq4+2)).replace('.',','),
                '$%s$'%(latex(kq4+3)).replace('.',','),
                '$%s$'%(latex(kq4-1)).replace('.',','),
                '$%s$'%(latex(kq4-2)).replace('.',','),
                '$%s$'%(latex(kq4-3)).replace('.',','),
                ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                noidungcauhoi = ('''Một máy kéo nông nghiệp với bánh xe sau có đường kính là $%s$cm. Xe chuyển động với vận tốc không đổi trên một đường thẳng, biết rằng vận tốc của bánh xe sau là $%s$ vòng/phút. Quãng đường (đơn vị: km) đi được của máy kéo trong $%s$ phút là'''
                %(latex(2*r1),latex(v1),latex(t)))
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                loigiai=('''Bán kính của bánh sau là $\\frac{%s}{2}=%s$cm. \\\\
                Góc mà bánh xe sau quay được trong $%s$ phút là \\\\
                $%s \\cdot %s \\cdot 360^\\circ=%s^\\circ=%s^\\circ \\cdot \\frac{\\pi}{180}=%s\\pi$.\\\\
                Quãng dường đi được của máy kéo sau $%s$ phút là \\\\
                $%s \\cdot %s\\pi=%s\\pi \\text{(cm)} \\approx %s$ km.'''
                %(latex(2*r1),latex(r1),
                latex(t),latex(t),latex(v1),latex(g),latex(g),latex(g1),
                latex(t),latex(r1),latex(g1),latex(kq1),latex(kq)
                ))

            if dang=='2':
                # New problem: Dot product in a pyramid
                a_val = random.randint(2, 10)
                a = symbols('a')

                # Calculate symbolic result
                MS = a * sqrt(3)/2
                CB = a
                cos_SMO = sqrt(3)/3
                result_sym = MS * CB * cos_SMO

                # Substitute random value for 'a'
                result_val = result_sym.subs(a, a_val)

                # Correct answer
                kq = latex(result_val)
                du = ['$%s$'%(kq),]
                da= random.choice(du)

                # Incorrect answers
                s_inc = [result_val + 1, result_val + 2, result_val - 1, result_val - 2, result_val+2, result_val-3]
                s_latex = [latex(i) for i in s_inc]
                s = ['$%s$'%(i) for i in s_latex]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có tất cả các cạnh bên và cạnh đáy đều bằng $%s$ và $ABCD$ là hình vuông. Gọi $M$ là trung điểm của $CD$. Giá trị của $\\vec{MS} \\cdot \\vec{CB}$ bằng'''
                %(latex(a_val)))

                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                loigiai=('''Ta có $|\\vec{MS}|=\\frac{%s\\sqrt{3}}{2}$, $|\\vec{CB}|=%s$.\\\\
                Góc giữa $\\vec{MS}$ và $\\vec{CB}$ bằng góc $\\widehat{SMO}$. Ta có $\\cos\\widehat{SMO} = \\frac{OM}{SM} = \\frac{%s/2}{\\frac{%s\\sqrt{3}}{2}} = \\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}$.\\\\
                Vậy $\\vec{MS} \\cdot \\vec{CB} = |\\vec{MS}| \\cdot |\\vec{CB}| \\cdot \\cos\\widehat{SMO} = \\frac{%s\\sqrt{3}}{2} \\cdot %s \\cdot \\frac{\\sqrt{3}}{3} = \\frac{%s}{2} \\cdot \\frac{3}{3} = \\frac{%s}{2}$.\\\\
                Kết quả là $%s$.'''
                %(latex(a_val), latex(a_val),
                latex(a_val), latex(a_val),
                latex(a_val), latex(a_val), latex(a_val**2), latex(a_val**2),
                latex(result_val)))

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

