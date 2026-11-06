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


def bt_dang14_p1_b2_c1_hh10(self):
            # Khai báo biến
            lis0=[30,45,60,90,120,135,150]
            goc=random.choice(lis0)
            goc_rad=goc * pi / 180

            lis1=[2,3,4,5,6,7,8,9]
            c1=random.choice(lis1)
            c2=random.choice(lis1)
            kq11=c1**2+c2**2-2*c1*c2*cos(goc_rad)
            kq1=round(math.sqrt(kq11), 2)
            #dang 4
            kq44=round((c1**2+kq1**2-c2**2)/(2*c1*kq1), 2)
            kq444 = math.acos(kq44)
            kq4=math.degrees(kq444)
            do=int(kq4)
            phut=int((kq4 - do) * 60)
            giay=round((kq4 - do - phut / 60) * 3600,2)
            lis=['6','8','9']
            dang=random.choice(lis)

            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $\\widehat{A} = %s^\\circ$ và $AB=%s, AC=%s$$zzz$ Bán kính đường tròn nội tiếp tam giác là \n'''
                            %(latex(goc),latex(c1),latex(c2)
                            ))
                # Các đáp án
                da_d = '\\True $r \\approx %s$' %(latex(round(2*0.5*c1*c2*sin(goc_rad)/(c1+c2+kq1),1)))
                da_s1 = '$r \\approx %s$' %(latex(round(0.5*c1*c2*sin(goc_rad)/(c1+c2+kq1),1)))
                da_s2 = '$r \\approx %s$' %(latex(round(0.5*0.5*c1*c2*sin(goc_rad)/(c1+c2+kq1),1)))
                da_s3 = '$r \\approx %s$' %(latex(round(3*0.5*c1*c2*sin(goc_rad)/(c1+c2+kq1),1)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $ABC$, ta có \\\\ \n'
                        '$BC^2 = AB^2 + AC^2 -2 AB \\cdot AC \\cdot \\cos A$ \\\\ \n'
                        '$BC^2 = %s^2 + %s^2 -2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ = %s$$zzz$\\\\ \n'
                        'Suy $BC = \\sqrt{%s} \\approx %s$$zzz$\\\\ \n'
                        'Diện tích tam giác là \\\\ \n'
                        '$S=\\dfrac{1}{2}AB \\cdot AC \\sin A =\\dfrac{1}{2} \\cdot %s \\cdot %s \\sin %s^\\circ \\approx  %s$$zzz$\\\\ \n'
                        'Ta có \\\\ \n'
                        '$S=pr= \\dfrac{AB+AC+BC}{2}r \\Rightarrow r=\\dfrac{2S}{AB+AC+BC} =\\dfrac{2 \\cdot %s}{%s+%s+%s} \\approx %s$$zzz$\\\\ \n'
                        %(latex(c1),latex(c2),latex(c1),latex(c2),latex(goc),latex(kq11),
                        latex(kq11), latex(kq1),
                        latex(c1),latex(c2),latex(goc), latex(round(0.5*c1*c2*sin(goc_rad),1)),
                        latex(round(0.5*c1*c2*sin(goc_rad),1)),latex(c1),latex(c2),latex(kq1),latex(round(2*0.5*c1*c2*sin(goc_rad)/(c1+c2+kq1),1))
                        ))


            if dang=='8':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $\\widehat{A} = %s^\\circ$ và $AB=%s, AC=%s$$zzz$ Bán kính đường tròn ngoại tiếp tam giác là \n'''
                            %(latex(goc),latex(c1),latex(c2)
                            ))
                # Các đáp án
                da_d = '\\True $R \\approx %s$' %(latex(round(c1*c2*kq1/(4*0.5*c1*c2*sin(goc_rad)),1)))
                da_s1 = '$R \\approx %s$' %(latex(round(c1*c2*kq1/(0.5*c1*c2*sin(goc_rad)),1)))
                da_s2 = '$R \\approx %s$' %(latex(round(c1*c2*kq1/(3*0.5*c1*c2*sin(goc_rad)),1)))
                da_s3 = '$R \\approx %s$' %(latex(round(c1*c2*kq1/(2*0.5*c1*c2*sin(goc_rad)),1)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $ABC$, ta có \\\\ \n'
                        '$BC^2 = AB^2 + AC^2 -2 AB \\cdot AC \\cdot \\cos A$ \\\\ \n'
                        '$BC^2 = %s^2 + %s^2 -2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ = %s$$zzz$\\\\ \n'
                        'Suy $BC = \\sqrt{%s} \\approx %s$$zzz$\\\\ \n'
                        'Diện tích tam giác là \\\\ \n'
                        '$S=\\dfrac{1}{2}AB \\cdot AC \\sin A =\\dfrac{1}{2} \\cdot %s \\cdot %s \\sin %s^\\circ \\approx  %s$$zzz$\\\\ \n'
                        'Ta có \\\\ \n'
                        '$S=\\dfrac{abc}{4R} = \\dfrac{AB \\cdot AC \\cdot BC}{4R} \\Rightarrow R=\\dfrac{AB \\cdot AC \\cdot BC}{4S} =\\dfrac{%s \\cdot %s \\cdot %s}{4 \\cdot %s} \\approx %s$$zzz$\\\\ \n'
                        %(latex(c1),latex(c2),latex(c1),latex(c2),latex(goc),latex(kq11),
                        latex(kq11), latex(kq1),
                        latex(c1),latex(c2),latex(goc), latex(round(0.5*c1*c2*sin(goc_rad),1)),
                        latex(c1),latex(c2),latex(kq1),latex(round(0.5*c1*c2*sin(goc_rad),1)),latex(round(c1*c2*kq1/(4*0.5*c1*c2*sin(goc_rad)),1))
                        ))
            if dang=='9':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $\\widehat{A} = %s^\\circ$ và $AB=%s, AC=%s$$zzz$ Đường cao $h_a$ tam giác là \n'''
                            %(latex(goc),latex(c1),latex(c2)
                            ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(round(2*0.5*c1*c2*sin(goc_rad)/kq1,1)))
                da_s1 = '$%s$' %(latex(round(0.5*c1*c2*sin(goc_rad)/kq1,1)))
                da_s2 = '$%s$' %(latex(round(3*0.5*c1*c2*sin(goc_rad)/kq1,1)))
                da_s3 = '$%s$' %(latex(round(4*0.5*c1*c2*sin(goc_rad)/kq1,1)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $ABC$, ta có \\\\ \n'
                        '$BC^2 = AB^2 + AC^2 -2 AB \\cdot AC \\cdot \\cos A$ \\\\ \n'
                        '$BC^2 = %s^2 + %s^2 -2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ = %s$$zzz$\\\\ \n'
                        'Suy $BC = \\sqrt{%s} \\approx %s$$zzz$\\\\ \n'
                        'Diện tích tam giác là \\\\ \n'
                        '$S=\\dfrac{1}{2}AB \\cdot AC \\sin A =\\dfrac{1}{2} \\cdot %s \\cdot %s \\sin %s^\\circ \\approx  %s$$zzz$\\\\ \n'
                        'Ta có \\\\ \n'
                        '$S=\\dfrac{1}{2}a h_a = \\dfrac{1}{2}BC h_a \\Rightarrow h_a=\\dfrac{2S}{BC} =\\dfrac{2 \\cdot %s}{%s} \\approx %s$$zzz$\\\\ \n'
                        %(latex(c1),latex(c2),latex(c1),latex(c2),latex(goc),latex(kq11),
                        latex(kq11), latex(kq1),
                        latex(c1),latex(c2),latex(goc), latex(round(0.5*c1*c2*sin(goc_rad),1)),
                        latex(round(0.5*c1*c2*sin(goc_rad),1)),latex(kq1),latex(round(2*0.5*c1*c2*sin(goc_rad)/kq1,1))
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zzz$','.').replace('.00','')
            return content

