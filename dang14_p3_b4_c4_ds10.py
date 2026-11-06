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


def bt_dang14_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':


                a = randint(1, 9) # Nghiệm x = a
                m = randint(2, 8) # Hệ số m
                n = a**4 + m*(a**2)

                # Các thành phần của phương trình để hiển thị
                # Phương trình: (x^2 - 2ax) + sqrt(m*x^2 - 2*m*a*x + n) = 0
                b1 = -2*a
                b2 = m
                c2 = -2*m*a
                d2 = n

                # Nghiệm đúng
                kq = a

                # Các đáp án trắc nghiệm
                du = ['$x = %s$'%(latex(kq))]
                da = random.choice(du)

                s = ['$x = %s$'%(latex(kq + 1)),
                     '$x = %s$'%(latex(kq + 2)),
                     '$x = %s$'%(latex(kq - 1)),
                     '$x = %s$'%(latex(kq + 3)),
                     '$x = %s$'%(latex(kq - 2)),
                     '$x = %s$'%(latex(kq + 4))]

                # Lấy ngẫu nhiên 3 đáp án sai không trùng đáp án đúng
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                # Hiển thị phương trình dưới dạng x^2 + b1*x + sqrt(b2*x^2 + c2*x + d2) = 0
                noidungcauhoi = ('''Phương trình sau: $x^2 %s x + \\sqrt{%s x^2 %s x + %s} = 0$ có nghiệm bằng bao nhiêu?'''
                                 %(('- ' + str(abs(b1)) if b1 < 0 else '+ ' + str(b1)),
                                   latex(b2),
                                   ('- ' + str(abs(c2)) if c2 < 0 else '+ ' + str(c2)),
                                   latex(d2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                t_val = a**2
                loigiai = ('''Đặt $t = \\sqrt{%s x^2 %s x + %s}$ ($t \\ge 0$). \\\\
                             Khi đó $t^2 = %s(x^2 %s x) + %s \\Rightarrow x^2 %s x = \\frac{t^2 - %s}{%s}$. \\\\
                             Thay vào phương trình ta được: \\\\
                             $\\frac{t^2 - %s}{%s} + t = 0 \\Leftrightarrow t^2 + %s t - %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & t = %s \\text{ (nhận)} \\\\ & t = %s \\text{ (loại)} \\end{aligned} \\right.$ \\\\
                             Với $t = %s$ thì $\\frac{%s^2 - %s}{%s} = x^2 %s x \\Leftrightarrow x^2 %s x + %s = 0 \\Leftrightarrow (x - %s)^2 = 0 \\Leftrightarrow x = %s$. \\\\
                             Vậy phương trình có nghiệm $x = %s$.'''
                           %(latex(b2), ('- ' + str(abs(c2)) if c2 < 0 else '+ ' + str(c2)), latex(d2),
                             latex(b2), ('- ' + str(abs(b1)) if b1 < 0 else '+ ' + str(b1)), latex(d2),
                             ('- ' + str(abs(b1)) if b1 < 0 else '+ ' + str(b1)), latex(d2), latex(b2),
                             latex(d2), latex(b2), latex(b2), latex(d2),
                             latex(t_val), latex(-(t_val + b2)),
                             latex(t_val), latex(t_val), latex(d2), latex(b2),
                             ('- ' + str(abs(b1)) if b1 < 0 else '+ ' + str(b1)),
                             ('- ' + str(abs(b1)) if b1 < 0 else '+ ' + str(b1)),
                             latex(a**2), latex(a), latex(a), latex(a)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(a))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

