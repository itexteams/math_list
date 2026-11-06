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


def bt_dang22_p4_b2_c1_hh10(self):
            # Khai báo biến
            lis1=[2,3,4,5,6,7,8,9]
            a=random.choice(lis1)
            b=random.choice(lis1)
            c=random.choice(lis1)
            while a+b-c<=0 or a+c-b<=0 or b+c-a<=0:
                a=random.choice(lis1)
                b=random.choice(lis1)
                c=random.choice(lis1)

            kq=Rational(c**2+b**2-a**2,2*c*b)
            kq_rad = math.acos(kq)
            kq_do=math.degrees(kq_rad)
            do=int(kq_do)
            phut=int((kq_do - do) * 60)
            giay=round((kq_do - do - phut / 60) * 3600,2)

            kq1=Rational(c**2+a**2-b**2,2*c*a)
            kq1_rad = math.acos(kq1)
            kq1_do=math.degrees(kq1_rad)
            do1=int(kq1_do)
            phut1=int((kq1_do - do1) * 60)
            giay1=round((kq1_do - do1 - phut1 / 60) * 3600,2)

            kq2=Rational(b**2+a**2-c**2,2*b*a)
            kq2_rad = math.acos(kq2)
            kq2_do=math.degrees(kq2_rad)
            do2=int(kq2_do)
            phut2=int((kq2_do - do2) * 60)
            giay2=round((kq2_do - do2 - phut2 / 60) * 3600,2)
            lis=['5','6','7']
            dang=random.choice(lis)

            if dang=='5':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $AB=%s, BC=%s, AC=%s$$zzz$ Tính chiều cao $h_a$ của tam giác.'''
                            %(latex(c),latex(a),latex(b)
                            ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(round(b*a*sin(kq2_rad)/a,1)))
                da_s1 = '$%s$' %(latex(round((1/2)*b*a*sin(kq2_rad)/a,1)))
                da_s2 = '$%s$' %(latex(round((1/3)*b*a*sin(kq2_rad)/a,1)))
                da_s3 = '$%s$' %(latex(round((1/4)*b*a*sin(kq2_rad)/a,1)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $ABC$, ta có\\\\ \n'
                        '$\\cos C = \\dfrac{AC^2+BC^2-AB^2}{2AC \\cdot BC} = \\dfrac{%s^2+%s^2-%s^2}{2 \\cdot %s \\cdot %s} = %s$$zzz$ \\\\ \n'
                        'Suy ra $\\widehat{C} \\approx %s^\\circ %s\'  %s\'\'  $$zzz$ \\\\ \n'
                        'Diện tích tam giác là $S=\\dfrac{1}{2} AC \\cdot BC \\sin C = \\dfrac{1}{2} \\cdot %s \\cdot %s \\sin \\left( %s^\\circ %s\'  %s\'\' \\right) \\approx %s$$zzz$ \\\\ \n'
                        'Ta có $S=\\dfrac{1}{2}a h_a =\\dfrac{1}{2}BC h_a \\Rightarrow h_a =\\dfrac{2S}{BC} =\\dfrac{2 \\cdot %s}{%s} \\approx %s$$zzz$'
                        %(latex(b),latex(a),latex(c),latex(b),latex(a),latex(kq2),
                        latex(do2),latex(phut2),latex(giay2),
                        latex(b), latex(a),latex(do2),latex(phut2),latex(giay2),latex(round((1/2)*b*a*sin(kq2_rad),1)),
                        latex(round((1/2)*b*a*sin(kq2_rad),1)),latex(a),latex(round(b*a*sin(kq2_rad)/a,1))
                        ))
            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $AB=%s, BC=%s, AC=%s$$zzz$ Tính chiều cao $h_b$ của tam giác.'''
                            %(latex(c),latex(a),latex(b)
                            ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(round(b*a*sin(kq2_rad)/b,1)))
                da_s1 = '$%s$' %(latex(round((1/2)*b*a*sin(kq2_rad)/b,1)))
                da_s2 = '$%s$' %(latex(round((1/3)*b*a*sin(kq2_rad)/b,1)))
                da_s3 = '$%s$' %(latex(round((1/4)*b*a*sin(kq2_rad)/b,1)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $ABC$, ta có\\\\ \n'
                        '$\\cos C = \\dfrac{AC^2+BC^2-AB^2}{2AC \\cdot BC} = \\dfrac{%s^2+%s^2-%s^2}{2 \\cdot %s \\cdot %s} = %s$$zzz$ \\\\ \n'
                        'Suy ra $\\widehat{C} \\approx %s^\\circ %s\'  %s\'\'  $$zzz$ \\\\ \n'
                        'Diện tích tam giác là $S=\\dfrac{1}{2} AC \\cdot BC \\sin C = \\dfrac{1}{2} \\cdot %s \\cdot %s \\sin \\left( %s^\\circ %s\'  %s\'\' \\right) \\approx %s$$zzz$ \\\\ \n'
                        'Ta có $S=\\dfrac{1}{2}b h_b =\\dfrac{1}{2}AC h_b \\Rightarrow h_b =\\dfrac{2S}{AC} =\\dfrac{2 \\cdot %s}{%s} \\approx %s$$zzz$'
                        %(latex(b),latex(a),latex(c),latex(b),latex(a),latex(kq2),
                        latex(do2),latex(phut2),latex(giay2),
                        latex(b), latex(a),latex(do2),latex(phut2),latex(giay2),latex(round((1/2)*b*a*sin(kq2_rad),1)),
                        latex(round((1/2)*b*a*sin(kq2_rad),1)),latex(b),latex(round(b*a*sin(kq2_rad)/b,1))
                        ))
            if dang=='7':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $AB=%s, BC=%s, AC=%s$$zzz$ Tính chiều cao $h_c$ của tam giác.'''
                            %(latex(c),latex(a),latex(b)
                            ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(round(b*a*sin(kq2_rad)/c,1)))
                da_s1 = '$%s$' %(latex(round((1/2)*b*a*sin(kq2_rad)/c,1)))
                da_s2 = '$%s$' %(latex(round((1/3)*b*a*sin(kq2_rad)/c,1)))
                da_s3 = '$%s$' %(latex(round((1/4)*b*a*sin(kq2_rad)/c,1)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $ABC$, ta có\\\\ \n'
                        '$\\cos C = \\dfrac{AC^2+BC^2-AB^2}{2AC \\cdot BC} = \\dfrac{%s^2+%s^2-%s^2}{2 \\cdot %s \\cdot %s} = %s$$zzz$ \\\\ \n'
                        'Suy ra $\\widehat{C} \\approx %s^\\circ %s\'  %s\'\'  $$zzz$ \\\\ \n'
                        'Diện tích tam giác là $S=\\dfrac{1}{2} AC \\cdot BC \\sin C = \\dfrac{1}{2} \\cdot %s \\cdot %s \\sin \\left( %s^\\circ %s\'  %s\'\' \\right) \\approx %s$$zzz$ \\\\ \n'
                        'Ta có $S=\\dfrac{1}{2}c h_c =\\dfrac{1}{2}AB h_c \\Rightarrow h_c =\\dfrac{2S}{AB} =\\dfrac{2 \\cdot %s}{%s} \\approx %s$$zzz$'
                        %(latex(b),latex(a),latex(c),latex(b),latex(a),latex(kq2),
                        latex(do2),latex(phut2),latex(giay2),
                        latex(b), latex(a),latex(do2),latex(phut2),latex(giay2),latex(round((1/2)*b*a*sin(kq2_rad),1)),
                        latex(round((1/2)*b*a*sin(kq2_rad),1)),latex(c),latex(round(b*a*sin(kq2_rad)/c,1))
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zzz$','.').replace('.00','').replace('\\frac','\\dfrac').replace('{,}0','')
            return content

