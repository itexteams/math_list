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


def bt_dang1_p1_b1_c1_hh10(self):
            # Khai báo biến
            def to_latex(expr_str: str) -> str:
                """
                Nhận vào chuỗi biểu thức (Python hoặc LaTeX),
                trả về mã LaTeX tương đương (chuẩn để hiển thị đẹp).
                """
                expr_str = expr_str.strip()

                # Nếu chuỗi có ký hiệu LaTeX, dùng parse_latex
                if "\\" in expr_str:
                    expr_str = expr_str.replace("$", "")
                    expr = parse_latex(expr_str)
                else:
                    expr = sympify(expr_str)

                # Xuất lại dưới dạng LaTeX
                return latex(expr)

            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                gg=['30','60','45','120','150','135']
                g=int(random.choice(gg))
                kq=nsimplify(sin(math.radians(g)))

                d = [
                    '$%s$'%(latex(kq))
                     ]
                da= random.choice(d)
                s = ['1','-1','sqrt(2)/2','1/2','sqrt(3)/3','sqrt(3)/2','sqrt(3)','-sqrt(2)/2','-1/2','-sqrt(3)/3','-sqrt(3)/2','-sqrt(3)']
                rm='%s'%(kq)
                s.remove(rm)
                das11 = random.choice(s)
                das1='$%s$'%(to_latex(das11))
                s.remove(das11)
                das22 = random.choice(s)
                das2 = '$%s$'%(to_latex(das22))
                s.remove(das22)
                das33 = random.choice(s)
                das3 ='$%s$'%(to_latex(das33))
                # Câu hỏi
                noidungcauhoi = ('Giá trị $\\sin %s^{\\circ}$ bằng \\\\ \n'
                                %(latex(g))
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
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\sin %s^{\\circ}=%s$.'

                         %(latex(g),latex(kq)
                           ))
            if dang=='2':
                gg=['30','60','45','120','150','135']
                g=int(random.choice(gg))
                kq=nsimplify(cos(math.radians(g)))

                d = [
                    '$%s$'%(latex(kq))
                     ]
                da= random.choice(d)
                s = ['1','-1','sqrt(2)/2','1/2','sqrt(3)/3','sqrt(3)/2','sqrt(3)','-sqrt(2)/2','-1/2','-sqrt(3)/3','-sqrt(3)/2','-sqrt(3)']
                rm='%s'%(kq)
                s.remove(rm)
                das11 = random.choice(s)
                das1='$%s$'%(to_latex(das11))
                s.remove(das11)
                das22 = random.choice(s)
                das2 = '$%s$'%(to_latex(das22))
                s.remove(das22)
                das33 = random.choice(s)
                das3 ='$%s$'%(to_latex(das33))
                # Câu hỏi
                noidungcauhoi = ('Giá trị $\\cos %s^{\\circ}$ bằng \\\\ \n'
                                %(latex(g))
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
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\cos %s^{\\circ}=%s$.'

                         %(latex(g),latex(kq)
                           ))
            if dang=='3':
                gg=['30','60','45','120','150','135']
                g=int(random.choice(gg))
                kq=nsimplify(tan(math.radians(g)))

                d = [
                    '$%s$'%(latex(kq))
                     ]
                da= random.choice(d)
                s = ['1','-1','sqrt(2)/2','1/2','sqrt(3)/3','sqrt(3)/2','sqrt(3)','-sqrt(2)/2','-1/2','-sqrt(3)/3','-sqrt(3)/2','-sqrt(3)']
                rm='%s'%(kq)
                s.remove(rm)
                das11 = random.choice(s)
                das1='$%s$'%(to_latex(das11))
                s.remove(das11)
                das22 = random.choice(s)
                das2 = '$%s$'%(to_latex(das22))
                s.remove(das22)
                das33 = random.choice(s)
                das3 ='$%s$'%(to_latex(das33))
                # Câu hỏi
                noidungcauhoi = ('Giá trị $\\tan %s^{\\circ}$ bằng \\\\ \n'
                                %(latex(g))
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
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\tan %s^{\\circ}=%s$.'

                         %(latex(g),latex(kq)
                           ))
            if dang=='4':
                gg=['30','60','45','120','150','135']
                g=int(random.choice(gg))
                kq=nsimplify(cot(math.radians(g)))

                d = [
                    '$%s$'%(latex(kq))
                     ]
                da= random.choice(d)
                s = ['1','-1','sqrt(2)/2','1/2','sqrt(3)/3','sqrt(3)/2','sqrt(3)','-sqrt(2)/2','-1/2','-sqrt(3)/3','-sqrt(3)/2','-sqrt(3)']
                rm='%s'%(kq)
                s.remove(rm)
                das11 = random.choice(s)
                das1='$%s$'%(to_latex(das11))
                s.remove(das11)
                das22 = random.choice(s)
                das2 = '$%s$'%(to_latex(das22))
                s.remove(das22)
                das33 = random.choice(s)
                das3 ='$%s$'%(to_latex(das33))
                # Câu hỏi
                noidungcauhoi = ('Giá trị $\\cot %s^{\\circ}$ bằng \\\\ \n'
                                %(latex(g))
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
                loigiai=('Sử dụng máy tính cầm tay ta tính được $\\cot %s^{\\circ}=%s$.'

                         %(latex(g),latex(kq)
                           ))
            # Xuất câu trắc nghiệm
            content = (
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\n').replace('\\frac', '\\dfrac')
            return content

