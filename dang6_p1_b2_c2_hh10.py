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


def bt_dang6_p1_b2_c2_hh10(self):
            # Khai báo biến
            a=randint(2,10)
            b=randint(2,10)
            lis0=[30,45,60,90, 120,135,150]
            goc=random.choice(lis0)
            goc_rad=goc*pi/180

            ab=sqrt(a**2+b**2-2*a*b*cos(goc_rad))
            oi=sqrt((2*(a**2+b**2)-ab**2)/4)
            oc=2*oi

            kq=oc+ab
            kq1=sqrt(a**2+b**2-2*a*b*cos(goc_rad))+2*sqrt((2*(a**2+b**2)-ab**2)/2)
            kq2=sqrt(a**2+b**2-2*a*b*cos(goc_rad))+2*sqrt((2*(a**2+b**2)-ab**2)/1)
            kq3=sqrt(a**2+b**2-2*a*b*cos(goc_rad))+sqrt((2*(a**2+b**2)-ab**2)/2)
            # Câu hỏi
            noidungcauhoi=('''Cho hai vectơ $\\vec{a}$ và $\\vec{b}$ tạo với nhau một góc $%s^\\circ$, biết $\\left| \\vec{a} \\right|=%s$ và $\\left| \\vec{b} \\right|=%s$. Tổng $\\left| \\vec{a} +\\vec{b} \\right|+\\left| \\vec{a} -\\vec{b} \\right|$ bằng \n'''
                        %(latex(goc),latex(a),latex(b)
                        ))
            # Các đáp án
            da_d = '\\True $%s$' %(latex(kq))
            da_s1 = '$%s$' %(latex(kq1))
            da_s2 = '$%s$' %(latex(kq2))
            da_s3 = '$%s$' %(latex(kq3))    
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=(
                    '\\begin{center} \n'    
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1.5] \n'
                        '\\clip(-4.484917496691633,-0.9922131489393506) rectangle (3.6582881314316507,3.8790754553038442); \n'
                        '\\draw [->] (-4.066781135812386,1.359803881006398) -- (-2.7705584170867312,3.4400322763806304); \n'
                        '\\draw [->] (-3.0737072787241866,1.7674868328636613) -- (-1.0666527465038125,1.3911641080723414); \n'
                        '\\draw [->] (-0.32446070594315163,-0.14548701815888113) -- (0.9717620127825031,1.9347413772153508); \n'
                        '\\draw [->] (-0.32446070594315163,-0.14548701815888113) -- (1.682593826277222,-0.5218097429502009); \n'
                        '\\draw [->] (-0.32446070594315163,-0.14548701815888113) -- (2.9788165450028767,1.5584186524240309); \n'
                        '\\draw (0.9717620127825031,1.934741377215351)-- (2.9788165450028767,1.5584186524240309); \n'
                        '\\draw (2.9788165450028767,1.5584186524240309)-- (1.6825938262772222,-0.5218097429502009); \n'
                        '\\draw (-1,0) node[anchor=north west] {$O$}; \n'
                        '\\draw (0.7,2.5) node[anchor=north west] {$A$}; \n'
                        '\\draw (1.682593826277221,-0.39636883468642764) node[anchor=north west] {$B$}; \n'
                        '\\draw (3.08335063522269,1.8824743321054531) node[anchor=north west] {$C$}; \n'
                        '\\draw (-4,3) node[anchor=north west] {$\\vec{a}$}; \n'
                        '\\draw (-2,2.2) node[anchor=north west] {$\\vec{b}$}; \n'
                        '\\draw (0.9717620127825031,1.934741377215351)-- (1.6825938262772222,-0.5218097429502009); \n'
                        '\\draw (1.4317120097496745,0.858040247951305) node[anchor=north west] {$I$}; \n'
                    '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                    'Dựng $\\overrightarrow{OA}=\\vec{a}; \\overrightarrow{OB}=\\vec{b}$. \\\\ \n'
                    'Dựng hình bình hành $OACB$ suy ra $\\vec{a}+\\vec{b}=\\overrightarrow{OC}$ và $\\vec{a}-\\vec{b}=\\overrightarrow{BA}$\\\\ \n'
                    'Xét tam giác $OAB$ ta có\\\\ \n'
                    'Áp dụng định lí cosin:\\\\ \n'
                    '$AB=\\sqrt{OA^2+OB^2-2OA \\cdot OB \\cos %s^\\circ}=\\sqrt{%s^2+%s^2-2 \\cdot %s \\cdot %s \\cos %s^\\circ}=%s$. \\\\ \n'
                    'Áp dụng công thức độ dài đường trung tuyến:\\\\ \n'
                    '$OI=\\sqrt{\\dfrac{2(OA^2+OB^2)-AB^2}{4}}=\\sqrt{\\dfrac{2(%s^2+%s^2)-(%s)^2}{4}}=%s \\Rightarrow OC=2OI=%s$.\\\\ \n'
                    'Vậy $\\left| \\vec{a} +\\vec{b} \\right|+\\left| \\vec{a} -\\vec{b} \\right| = \\left| \\overrightarrow{OC} \\right|+\\left| \\overrightarrow{BA} \\right|=%s+%s=%s$.'


                    %(latex(goc),latex(a),latex(b),latex(a),latex(b),latex(goc),latex(ab),
                    latex(a),latex(b),latex(ab),latex(oi),latex(oc),latex(oc),latex(ab),latex(kq)

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

