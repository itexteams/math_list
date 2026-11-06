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


def bt_dang7_p3_b3_c4_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                m=symbols('m')
                a=randint(-9,9)
                b=randint(-10,10)
                k=randint(1,5)
                c=randint(1,10)
                d=randint(-10,10)
                e=randint(-10,10)
                f=randint(-10,10)
                g=randint(1,9)
                while a==0 or b==0 or c==0 or e==0:
                    x=symbols('x')
                    m=symbols('m')
                    a=randint(-9,9)
                    b=randint(-10,10)
                    k=randint(1,5)
                    c=randint(1,10)
                    d=randint(-10,10)
                    e=randint(-10,10)
                    f=randint(-10,10)
                    g=randint(1,9)

                fx=a*x+m+b
                gx=c*x+g**2
                hx=e*x+f

                f0=m+b
                x0=Rational(c,2*g)
                kq=x0-b

                # Tạo phân số từ số thực
                #frac = frac(kq).limit_denominator()
                frac = Fraction(kq).limit_denominator()

                # Lấy tử số và mẫu số
                numerator = frac.numerator
                denominator = frac.denominator

                kq2=numerator+denominator

                kq1 = Decimal(float(kq)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)=\\heva{& %s &\\text{khi  } x\\le 0 \\\\ & \\dfrac{\\sqrt{%s}-%s}{x} & \\text{khi  } x>0}$$zz$'
                                ' Biết rằng $m=\\dfrac{a}{b}$ với $\\dfrac{a}{b}$ tối giản, $a, b$ là các số nguyên và $b>0$ thì hàm số liên tục tại $x=0$$zz$ Tổng $a+b$ bằng bao nhiêu?'


                                %(latex(fx),latex(gx),latex(g)))

                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} Tập xác định của hàm số $\\mathscr{D}=\\left[%s;+\\infty\\right)$ nên $0\\in\\mathscr{D}$$zz$\\\\ \n'
                        '\\hspace*{1cm} $f(0)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x\\to 0^- }{\\mathop{\\lim }}f(x)= \\underset{x\\to 0^- }{\\mathop{\\lim }}(%s)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x\\to 0^+ }{\\mathop{\\lim }}f(x)= \\underset{x\\to 0^+ }{\\mathop{\\lim }}\\dfrac{\\sqrt{%s}-%s}{x}=\\underset{x\\to 0^+ }{\\mathop{\\lim }}\\dfrac{\\left(\\sqrt{%s}-%s\\right)\\left(\\sqrt{%s}+%s\\right)}{x\\left(\\sqrt{%s}+%s\\right)}$\\\\ \n'
                        '\\hspace*{2.75cm} $=\\underset{x\\to 0^+ }{\\mathop{\\lim }}\\dfrac{%s}{\\left(\\sqrt{%s}+%s\\right)}=%s$\\\\ \n'
                        'Hàm số liên tục tại $x=0$ khi và chỉ khi\\\\ \n'
                        '\\hspace*{1cm}$\\underset{x\\to 0^+ }{\\mathop{\\lim }}f(x)= \\underset{x\\to 0^- }{\\mathop{\\lim }}f(x)=f(0)\\Leftrightarrow %s=%s\\Leftrightarrow m=%s$$zz$ \\\\ \n'
                        'Suy ra $a=%s, b=%s$, vậy $a+b=%s$$zz$'
                        %(latex(Rational(-g**2,c)),
                            latex(f0),
                        latex(fx),latex(f0),
                        latex(gx),latex(g),latex(gx),latex(g),latex(gx),latex(g),latex(gx),latex(g),
                        latex(c),latex(gx),latex(g),latex(x0),
                        latex(f0),latex(x0),latex(kq),
                        latex(numerator),latex(denominator),latex(kq2)
                        )
                        )


                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq2))
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                m=symbols('m')
                a=randint(-9,9)
                b=randint(-10,10)
                k=randint(1,5)
                c=randint(-10,-1)
                d=randint(-10,10)
                e=randint(-10,10)
                f=randint(-10,10)
                g=randint(1,9)
                while a==0 or b==0 or c==0 or e==0:
                    x=symbols('x')
                    m=symbols('m')
                    a=randint(-9,9)
                    b=randint(-10,10)
                    k=randint(1,5)
                    c=randint(-10,-1)
                    d=randint(-10,10)
                    e=randint(-10,10)
                    f=randint(-10,10)
                    g=randint(1,9)

                fx=a*x+m+b
                gx=c*x+g**2
                hx=e*x+f

                f0=m+b
                x0=Rational(c,2*g)
                kq=x0-b

                kq1 = Decimal(float(kq)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)=\\heva{& %s &\\text{khi  } x\\le 0 \\\\ & \\dfrac{\\sqrt{%s}-%s}{x} & \\text{khi  } x>0}$$zz$'
                                ' Giá trị của $m$ để hàm số liên tục tại $x=0$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$'


                                %(latex(fx),latex(gx),latex(g)))

                # Nội dung lời giải
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} Tập xác định của hàm số $\\mathscr{D}=\\left(-\\infty;%s\\right]$ nên $0\\in\\mathscr{D}$$zz$\\\\ \n'
                        '\\hspace*{1cm} $f(0)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x\\to 0^- }{\\mathop{\\lim }}f(x)= \\underset{x\\to 0^- }{\\mathop{\\lim }}(%s)=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x\\to 0^+ }{\\mathop{\\lim }}f(x)= \\underset{x\\to 0^+ }{\\mathop{\\lim }}\\dfrac{\\sqrt{%s}-%s}{x}=\\underset{x\\to 0^+ }{\\mathop{\\lim }}\\dfrac{\\left(\\sqrt{%s}-%s\\right)\\left(\\sqrt{%s}+%s\\right)}{x\\left(\\sqrt{%s}+%s\\right)}$\\\\ \n'
                        '\\hspace*{2.75cm} $=\\underset{x\\to 0^+ }{\\mathop{\\lim }}\\dfrac{%s}{\\left(\\sqrt{%s}+%s\\right)}=%s$\\\\ \n'
                        'Hàm số liên tục tại $x=0$ khi và chỉ khi\\\\ \n'
                        '\\hspace*{1cm}$\\underset{x\\to 0^+ }{\\mathop{\\lim }}f(x)= \\underset{x\\to 0^- }{\\mathop{\\lim }}f(x)=f(0)\\Leftrightarrow %s=%s\\Leftrightarrow m=%s\\approx%s$$zz$'
                        %(latex(Rational(-g**2,c)),
                            latex(f0),
                        latex(fx),latex(f0),
                        latex(gx),latex(g),latex(gx),latex(g),latex(gx),latex(g),latex(gx),latex(g),
                        latex(c),latex(gx),latex(g),latex(x0),
                        latex(f0),latex(x0),latex(kq),latex(kq1)
                        )
                        )


                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('.', ',').replace('$zz$', '.').replace(',0}', '}')
            return content      

