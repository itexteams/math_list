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


def bt_dang6_p1_b4_c2_hh10(self):
            # Khai báo biến
            x1=randint(-9,9)
            y1=randint(-9,9)
            x2=randint(-9,9)
            y2=randint(-9,9)

            i=randint(-3,3)
            if i==0:
                i=randint(-3,3)

            lis0=['A','B','C','D','M','N','E','H']
            d1=random.choice(lis0)
            lis0.remove(d1)
            d2=random.choice(lis0)

            ab=sqrt((x2-x1)**2+(y2-y1)**2)
            ab1=sqrt((x2-x1-1)**2+(y2-y1+1)**2)
            ab2=sqrt((x2-x1+1)**2+(y2-y1+2)**2)
            ab3=sqrt((x2-x1-3)**2+(y2-y1+3)**2)

            lisdang=['1','2','3']
            dang=random.choice(lisdang)

            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho hai điểm $%s(%s;%s)$ và $%s(%s;%s)$. Tọa độ vectơ $\\overrightarrow{%s%s}$ là  \n'
                                %(str(d1),latex(x1),latex(y1),str(d2),latex(x2),latex(y2),str(d1),str(d2)
                                ))
                # Các đáp án
                da_d = '\\True $(%s;%s)$' %(latex(x2-x1),latex(y2-y1))
                da_s1 = '$(%s;%s)$' %(latex(x2-x1+i),latex(y2-y1))
                da_s2 = '$(%s;%s)$' %(latex(x2-x1),latex(y2-y1-i))
                da_s3 = '$(%s;%s)$' %(latex(x2-x1-i),latex(y2-y1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n '
                        '$\\overrightarrow{%s%s}=(x_%s-x_%s; y_%s-y_%s)=(%s-%s;%s-%s)=(%s;%s)$. '
                        %(str(d1),str(d2),str(d2),str(d1),str(d2),str(d1),latex(x2),latex(x1),latex(y2),latex(y1),latex(x2-x1),latex(y2-y1)
                        ))
            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho hai điểm $%s(%s;%s)$ và $%s(%s;%s)$. Tọa độ trung điểm đoạn thẳng $%s%s$ là  \n'
                                %(str(d1),latex(x1),latex(y1),str(d2),latex(x2),latex(y2),str(d1),str(d2)
                                ))
                # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$' %(latex(Rational(x1+x2,2)),latex(Rational(y1+y2,2)))
                da_s1 = '$\\left( %s;%s \\right)$' %(latex(Rational(x1+x2+1,2)),latex(Rational(y1+y2,2)))
                da_s2 = '$\\left( %s;%s \\right)$' %(latex(Rational(x1+x2,2)),latex(Rational(y1+y2-1,2)))
                da_s3 = '$\\left( %s;%s \\right)$' %(latex(Rational(x1+x2-1,2)),latex(Rational(y1+y2,2)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Gọi $I$ là trung điểm đoạn thẳng $%s%s$, ta có \\\\ \n '
                        '$x_I=\\dfrac{x_%s +x_%s}{2}=\\dfrac{%s +%s}{2}=%s$. \\\\ \n'
                        '$y_I=\\dfrac{y_%s +y_%s}{2}=\\dfrac{%s +%s}{2}=%s$. '
                        %(str(d1),str(d2),str(d1),str(d2),latex(x1),latex(x2),latex(Rational(x1+x2,2)),
                        str(d1),str(d2),latex(y1),latex(y2),latex(Rational(y1+y2,2)),
                        ))
            if dang=='3':
                #Nội ung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho hai điểm $%s(%s;%s)$ và $%s(%s;%s)$. Độ dài đoạn thẳng $%s%s$ là  \n'
                                %(str(d1),latex(x1),latex(y1),str(d2),latex(x2),latex(y2),str(d1),str(d2)
                                ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(ab))
                da_s1 = '$%s$' %(latex(ab1))
                da_s2 = '$%s$' %(latex(ab2))
                da_s3 = '$%s$' %(latex(ab3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n '
                        '$\\overrightarrow{%s%s}=(x_%s-x_%s; y_%s-y_%s)=(%s-%s;%s-%s)=(%s;%s)$. \\\\ \n'
                        'Độ dài đoạn thẳng $%s%s$ là $\\sqrt{%s+%s} =%s$. '
                        %(str(d1),str(d2),str(d2),str(d1),str(d2),str(d1),latex(x2),latex(x1),latex(y2),latex(y1),latex(x2-x1),latex(y2-y1),
                        str(d1),str(d2),latex((x2-x1)**2),latex((y2-y1)**2),latex(ab)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('--', '+')
            return content

