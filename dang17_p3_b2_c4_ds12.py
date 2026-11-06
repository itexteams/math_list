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


def bt_dang17_p3_b2_c4_ds12(self):
            # Khai báo biến
            a=randint(8,40)
            kb=a*10
            b=randint(3,20)
            bb=b*10
            n=kb+bb
            d=randint(88,98)
            d1=d/100
            dd=randint(2,8)
            d2=dd/100
            while a==b or a<=b+3 or d==90:
                a=randint(8,40)
                kb=a*10
                b=randint(3,20)
                bb=b*10
                n=kb+bb
                d=randint(88,98)
                d1=d/100
                dd=randint(2,8)
                d2=dd/100
            p12=nsimplify(kb/n)
            p11=1-p12
            p21=round(d1,2)
            p22=1-p21
            q21=round(d2,2)
            q22=1-q21
            pb=p11*p21+p12*q21
            number = Decimal(float(pb))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            # Nội dung câu hỏi
            noidungcauhoi = ('Giả sử trong một nhóm $%s$ người có $%s$ người không nhiễm bệnh và $%s$ người nhiễm bệnh$zz$ '
                            'Để phát hiện ra người nhiễm bệnh, người ta tiến hành xét nghiệm tất cả mọi người của nhóm đó$zz$ Biết rằng đối với người nhiễm bệnh, '
                            'xác suất xét nghiệm có kết quả dương tính là $%s$; còn đối với người không nhiễm bệnh, xác suất có kết quả xét nghiệm dương tính là $%s$$zz$ '
                            'Chọn ngẫu nhiên một người từ nhóm $%s$ người trên$zz$ Tính xác suất để chọn được người có kết quả dương tính (kết quả làm tròn đến hàng phần trăm)$zz$'
                            %(latex(n),latex(kb),latex(bb),latex(d1),latex(d2),latex(n)
                            )
                            )
            # Nội dung lời giải
            loigiai = ('Xét các biến cố:\\\\ \n'
                        '\\hspace*{1cm} $A$: "Chọn được người có kết quả dương tính"\\\\ \n'
                    '\\hspace*{1cm} $B$: "Chọn được người nhiễm bệnh";\\\\ \n'
                    '\\hspace*{1cm} $\\overline{B}$: "Chọn được người không nhiễm bệnh"$zz$\\\\ \n'
                        'Ta có sơ đồ cây\\\\ \n'
                        '\\begin{center}'
                        '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                        '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                        '\\node (A) at (0,0){Chọn 1 người};\n'
                        '\\def \\gocA{30}\n'
                        '\\def \\kcA{4}\n'
                        '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$B$};\n'
                        '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$\\overline{B}$};\n'
                        '\\def \\gocB{15}\n'
                        '\\def \\kcB{4}\n'
                        '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\end{scope}\n'
                        '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                            '\\draw (A)--(B1) node[above]{$\\mathrm{P}(B)=$\\fbox{$%s$}};\n'
                            '\\draw (A)--(B2) node[below]{$\\mathrm{P}(\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(A|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{A}|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(A|\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{A}|\\overline{B})=$\\fbox{$%s$}};\n'
                        '\\end{scope}\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Xác suất để chọn được người có kết quả dương tính bằng\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(A)=\\mathrm{P}(B)\\cdot\\mathrm{P}(A|B)+\\mathrm{P}(\\overline{B})\\cdot\\mathrm{P}(A|\\overline{B})=%s\\cdot %s+%s\\cdot %s\\approx%s$$zz$\\\\ \n'
                        %(latex(p11),latex(p12),latex(p21),latex(p22),latex(q21),latex(q22),
                        latex(p11),latex(p21),latex(p12),latex(q21),latex(kq))
                        )


            #Đáp án
            dapan='  \\shortans[0]{$%s$}   \n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content 

