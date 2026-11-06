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


def bt_dang11_p3_b1_c1_hh10(self):
            #Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                ta=randint(-10,10)
                a=randint(2,9)
                b=randint(-6,6)
                c=randint(2,9)
                d=randint(-6,6)
                t=a*ta+b
                m=c*ta+d
                while a*b*c*d==0 or m==0 or ta==0 or t%m==0 or abs(a)==abs(b) or abs(c)==abs(d) or gcd(a,b)==gcd(b,c):
                    ta=randint(-10,10)
                    a=randint(2,9)
                    b=randint(-6,6)
                    c=randint(2,9)
                    d=randint(-6,6)
                    t=a*ta+b
                    m=c*ta+d
                kq1=t/m
                # Tạo phân số từ số thực
                frac = Fraction(kq1).limit_denominator()

                # Lấy tử số và mẫu số
                numerator = frac.numerator
                denominator = frac.denominator

                kq=numerator+denominator



                # Nội dung câu hỏi
                noidungcauhoi = ('Cho góc $\\alpha \\left(0^\\circ < \\alpha <180^\\circ\\right)$ thoả mãn $\\tan \\alpha =%s$. Giá trị của biểu thức \\\\ $P=\\dfrac{%s\\sin \\alpha+%s\\cos \\alpha}{%s\\sin \\alpha+%s\\cos \\alpha}=\\dfrac{m}{n}$'
                                 'với $m,n \\in \\mathbb{Z},n>0$ và $\\dfrac{m}{n}$ là phân số tối giản. Khi đó $m+n$ bằng bao nhiêu? '
                                 %(latex(ta),latex(a),latex(b),latex(c),latex(d)
                              ))
                # Nội dung lời giải
                loigiai = ('Vì $\\tan \\alpha  = %s$ nên $\\cos \\alpha \\ne 0 $, chia cả tử và mẫu cho $\\cos \\alpha$ ta có \\\\ \n'
                         '$$P=\\dfrac{%s\\sin \\alpha +%s\\cos \\alpha}{%s\\sin \\alpha +%s\\cos \\alpha} =\\dfrac{%s\\dfrac{\\sin \\alpha}{\\cos \\alpha} +%s\\dfrac{\\cos \\alpha}{\\cos \\alpha}}{%s\\dfrac{\\sin \\alpha}{\\cos \\alpha} +%s\\dfrac{\\cos \\alpha}{\\cos \\alpha}} =\\dfrac{%s\\tan \\alpha +%s}{%s\\tan \\alpha +%s} =\\dfrac{%s\\cdot (%s) +%s}{%s\\cdot (%s) +%s}=%s.$$ \\\\ \n'
                         'Vậy $m+n=%s+%s=%s$.'
                         %(latex(ta), latex(a),latex(b),latex(c),latex(d), latex(a),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(d),
                           latex(a),latex(ta),latex(b),latex(c),latex(ta),latex(d),
                           latex(nsimplify(kq1)),latex(numerator),latex(denominator),latex(kq)
                             ))


                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('1\\sin','\\sin').replace('1\\cos','\\cos').replace('1\\tan','\\tan').replace('-1\\sin','-\\sin').replace('-1\\cos','-\\cos').replace('-1\\tan','-\\tan').replace('-1\\cdot','-').replace('1\\cdot','').replace('1\\dfrac','\\dfrac').replace('-1\\dfrac','-\\dfrac')
            return content  

