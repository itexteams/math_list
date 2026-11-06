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


def bt_dang5_p3_b2_c1_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                def round_SA(a): 
                    # Kiểm tra nếu a là số nguyên
                    if a == int(a):
                        return "", int(a)

                    # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                    str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                    integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                    # Xác định cách làm tròn
                    if len(integer_part) > 2:
                        number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                        cirle = "(làm tròn kết quả đến hàng đơn vị)"
                    elif len(integer_part) == 2 and len(decimal_part) > 1:
                        number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        cirle = "(làm tròn kết quả đến hàng phần chục)"
                    elif len(decimal_part) <= 2:
                        number = str_a  # Không cần làm tròn thêm
                        cirle = ""
                    else:
                        number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        cirle = "(làm tròn kết quả đến hàng phần trăm)"

                    # Chuyển dấu chấm thành dấu phẩy (nếu có)
                    return cirle, str(number).replace('.', ',')
                a=randint(4,20)
                b=randint(3,25)
                lis1=['30','45','60']
                g=random.choice(lis1)
                lis2=['A','B','C']
                d1=random.choice(lis2)
                if g=='30':
                    si=0.5
                if g=='60':
                    si=sqrt(3)/2
                if g=='45':
                    si=sqrt(2)/2
                if d1=='A':
                    d2='B'
                    d3='C'
                if d1=='B':
                    d2='A'
                    d3='C'
                if d1=='C':
                    d2='A'
                    d3='B'
                s=0.5*a*b*si
                p1=str(d1)+str(d2)
                p2=str(d1)+str(d3)
                kq=round_SA(s)[1]

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác $ABC$ có $\\widehat{%s}=%s^\\circ$ và $%s=%s,%s=%s$$zz$ Hỏi diện tích của tam giác $ABC$ bằng bao nhiêu? %s'
                                 %(d1,latex(g),p1,latex(a),p2,latex(b),round_SA(s)[0]
                              ))
                # Nội dung lời giải
                loigiai = ('Diện tích của tam giác $ABC$ là\\\\ \n'
                           '\\hspace*{1cm}$S_{ABC}=\\dfrac{1}{2}\\cdot %s\\cdot %s=\\dfrac{1}{2}\\cdot %s\\cdot %s\\cdot \\sin %s^\\circ =%s$zz$$'
                         %(p1,p2,latex(a),latex(b),latex(g),latex(kq)
                             ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('$zz$','.')
            return content 

