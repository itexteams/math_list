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


def bt_dang8_p3_b2_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a1=randint(1,3)
                k=randint(1,3)
                b1=a1+k
                a=randint(2,9)
                n=randint(1,5)
                f3=randint(2,50)
                f0=nsimplify(1/f3)
                f=(-a*x**(n+1))/(n+1)
                f1=f.subs(x,a1)
                f2=f.subs(x,b1)
                kq1=1/(f2-f1+1/f0)
                while f0==0 or (f2-f1+1/f0)==0 or kq1<=0.1:
                    x=symbols('x')
                    a1=randint(1,3)
                    k=randint(1,3)
                    b1=a1+k
                    a=randint(2,9)
                    n=randint(1,5)
                    f3=randint(2,50)
                    f0=nsimplify(1/f3)
                    f=(-a*x**(n+1))/(n+1)
                    f1=f.subs(x,a1)
                    f2=f.subs(x,b1)
                    kq1=1/(f2-f1+1/f0)
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ thoả mãn $f(%s)=%s$ và $f\'(x)=%sx^{%s}\\left[f(x)\\right]^{2}$ với mọi $x \\in \\mathbb{R}$$zz$ Hỏi giá trị $f(%s)$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a1),latex(f0),latex(a),latex(n),latex(b1)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm}$f\'(x)=%sx^{%s}\\left[f(x)\\right]^{2} \\Leftrightarrow \\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=%sx^{%s} \\Leftrightarrow -\\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=-%sx^{%s} \\Leftrightarrow \\left[\\dfrac{1}{f(x)}\\right]\' =-%sx^{%s}$$zz$\\\\ \n'  
                        'Suy ra \n'
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle\\int\\limits_{%s}^{%s}\\left[\\dfrac{1}{f(x)}\\right]\'\\text{d}x=-%s\\displaystyle\\int\\limits_{%s}^{%s} x^{%s}\\text{d}x'
                        '\\Leftrightarrow \\dfrac{1}{f(x)}\\bigg|_{%s}^{%s}=-%sx^{%s}\\bigg|_{%s}^{%s}'
                        '&\\Leftrightarrow& \\dfrac{1}{f(%s)}-\\dfrac{1}{f(%s)}=-%s\\cdot %s^{%s}+%s\\cdot %s^{%s}\\\\ \n'
                        '&\\Leftrightarrow& f(%s)\\approx %s$zz$\n'
                        '\\end{eqnarray*}\n'
                        'Vậy $f(%s)\\approx %s$$zz$'
                        %(latex(a),latex(n),latex(a),latex(n),latex(a),latex(n),latex(a),latex(n),
                            latex(a1),latex(b1),latex(a),latex(a1),latex(b1),latex(n),
                            latex(a1),latex(b1),latex(nsimplify(a/(n+1))),latex(n+1),latex(a1),latex(b1),
                            latex(b1),latex(a1),latex(nsimplify(a/(n+1))),latex(b1),latex(n+1),latex(nsimplify(a/(n+1))),latex(a1),latex(n+1),
                            latex(b1),latex(kq),latex(b1),latex(kq)

                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='2':
                x=symbols('x')
                a1=randint(1,3)
                k=randint(1,3)
                b1=a1+k
                a=randint(2,9)
                f3=randint(2,50)
                f0=nsimplify(1/f3)
                f=-a*(math.e)**x
                f1=f.subs(x,a1)
                f2=f.subs(x,b1)
                kq1=1/(f2-f1+1/f0)
                while f0==0 or (f2-f1+1/f0)==0 or kq1<=0.1:
                    x=symbols('x')
                    a1=randint(1,3)
                    k=randint(1,3)
                    b1=a1+k
                    a=randint(2,9)
                    f3=randint(2,50)
                    f0=nsimplify(1/f3)
                    f=-a*(math.e)**x
                    f1=f.subs(x,a1)
                    f2=f.subs(x,b1)
                    kq1=1/(f2-f1+1/f0)
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ thoả mãn $f(%s)=%s$ và $f\'(x)=%se^{x}\\left[f(x)\\right]^{2}$ với mọi $x \\in \\mathbb{R}$$zz$ Hỏi giá trị $f(%s)$ bằng bao nhiêu?(kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a1),latex(f0),latex(a),latex(b1)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm}$f\'(x)=%se^{x}\\left[f(x)\\right]^{2} \\Leftrightarrow \\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=%se^{x} \\Leftrightarrow -\\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=-%se^{x} \\Leftrightarrow \\left[\\dfrac{1}{f(x)}\\right]\' =-%se^{x}$$zz$\\\\ \n'  
                        'Suy ra \n'
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle\\int\\limits_{%s}^{%s}\\left[\\dfrac{1}{f(x)}\\right]\'\\text{d}x=-%s\\displaystyle\\int\\limits_{%s}^{%s} e^{x}\\text{d}x'
                        '\\Leftrightarrow \\dfrac{1}{f(x)}\\bigg|_{%s}^{%s}=-%se^{x}\\bigg|_{%s}^{%s}'
                        '&\\Leftrightarrow& \\dfrac{1}{f(%s)}-\\dfrac{1}{f(%s)}=-%s\\cdot e^{%s}+%s\\cdot e^{%s}\\\\ \n'
                        '&\\Leftrightarrow& f(%s)\\approx %s$zz$\n'
                        '\\end{eqnarray*}\n'
                        'Vậy $f(%s)\\approx %s$$zz$'
                        %(latex(a),latex(a),latex(a),latex(a),
                            latex(a1),latex(b1),latex(a),latex(a1),latex(b1),
                            latex(a1),latex(b1),latex(a),latex(a1),latex(b1),
                            latex(b1),latex(a1),latex(a),latex(b1),latex(a),latex(a1),
                            latex(b1),latex(kq),latex(b1),latex(kq)

                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='3':
                x=symbols('x')
                a2=randint(1,6)
                a1=pi/a2
                k=randint(1,3)
                b2=randint(1,6)
                b1=pi/b2
                a=randint(2,9)
                f3=randint(2,50)
                f0=nsimplify(1/f3)
                f=a*cos(x)
                f1=f.subs(x,a1)
                f2=f.subs(x,b1)
                kq1=1/(f2-f1+1/f0)
                while a2==5 or b2==5 or a2<=b2 or f0==0 or (f2-f1+1/f0)==0 or kq1<=0.1:
                    x=symbols('x')
                    a2=randint(1,6)
                    a1=pi/a2
                    k=randint(1,3)
                    b2=randint(1,6)
                    b1=pi/b2
                    a=randint(2,9)
                    f3=randint(2,50)
                    f0=nsimplify(1/f3)
                    f=a*cos(x)
                    f1=f.subs(x,a1)
                    f2=f.subs(x,b1)
                    kq1=1/(f2-f1+1/f0)
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ thoả mãn $f\\left(%s\\right)=%s$ và $f\'(x)=%s\\sin x\\left[f(x)\\right]^{2}$ với mọi $x \\in \\mathbb{R}$$zz$ Hỏi giá trị $f\\left(%s\\right)$ bằng bao nhiêu?(kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a1),latex(f0),latex(a),latex(b1)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm}$f\'(x)=%s\\sin x\\left[f(x)\\right]^{2} \\Leftrightarrow \\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=%s\\sin x \\Leftrightarrow -\\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=-%s\\sin x \\Leftrightarrow \\left[\\dfrac{1}{f(x)}\\right]\' =-%s\\sin x $$zz$\\\\ \n'  
                        'Suy ra \n'
                        '\\begin{eqnarray*}\n'
                        '&&\\displaystyle\\int\\limits_{%s}^{%s}\\left[\\dfrac{1}{f(x)}\\right]\'\\text{d}x=-%s\\displaystyle\\int\\limits_{%s}^{%s} \\sin x\\text{d}x '
                        '\\Leftrightarrow \\dfrac{1}{f(x)}\\bigg|_{%s}^{%s}=%s\\cos x\\bigg|_{%s}^{%s}\\\\ \n'
                        '&\\Leftrightarrow& \\dfrac{1}{f(%s)}-\\dfrac{1}{f(%s)}=%s\\cdot \\cos \\left(%s\\right)-%s\\cdot \\cos \\left(%s\\right)\\\\ \n'
                        '&\\Leftrightarrow& f\\left(%s\\right)\\approx %s$zz$\n'
                        '\\end{eqnarray*}\n'
                        'Vậy $\\left(%s\\right)\\approx %s$$zz$'
                        %(latex(a),latex(a),latex(a),latex(a),
                            latex(a1),latex(b1),latex(a),latex(a1),latex(b1),
                            latex(a1),latex(b1),latex(a),latex(a1),latex(b1),
                            latex(b1),latex(a1),latex(a),latex(b1),latex(a),latex(a1),
                            latex(b1),latex(kq),latex(b1),latex(kq)

                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='4':
                x=symbols('x')
                a2=randint(1,6)
                a1=pi/a2
                k=randint(1,3)
                b2=randint(1,6)
                b1=pi/b2
                a=randint(2,9)
                f3=randint(2,50)
                f0=nsimplify(1/f3)
                f=-a*sin(x)
                f1=f.subs(x,a1)
                f2=f.subs(x,b1)
                kq1=1/(f2-f1+1/f0)
                while a2==5 or b2==5 or a2<=b2 or f0==0 or (f2-f1+1/f0)==0 or kq1<=0.1:
                    x=symbols('x')
                    a2=randint(1,6)
                    a1=pi/a2
                    k=randint(1,3)
                    b2=randint(1,6)
                    b1=pi/b2
                    a=randint(2,9)
                    f3=randint(2,50)
                    f0=nsimplify(1/f3)
                    f=-a*sin(x)
                    f1=f.subs(x,a1)
                    f2=f.subs(x,b1)
                    kq1=1/(f2-f1+1/f0)
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ thoả mãn $f\\left(%s\\right)=%s$ và $f\'(x)=%s\\cos x\\left[f(x)\\right]^{2}$ với mọi $x \\in \\mathbb{R}$$zz$ Hỏi giá trị $f\\left(%s\\right)$ bằng bao nhiêu?(kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a1),latex(f0),latex(a),latex(b1)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm}$f\'(x)=%s\\cos x\\left[f(x)\\right]^{2} \\Leftrightarrow \\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=%s\\cos x \\Leftrightarrow -\\dfrac{f\'(x)}{\\left[f(x)\\right]^{2}}=-%s\\cos x \\Leftrightarrow \\left[\\dfrac{1}{f(x)}\\right]\' =-%s\\cos x $$zz$\\\\ \n'  
                        'Suy ra \n'
                        '\\begin{eqnarray*}\n'
                        '&&\\displaystyle\\int\\limits_{%s}^{%s}\\left[\\dfrac{1}{f(x)}\\right]\'\\text{d}x=-%s\\displaystyle\\int\\limits_{%s}^{%s} \\cos x\\text{d}x '
                        '\\Leftrightarrow \\dfrac{1}{f(x)}\\bigg|_{%s}^{%s}=-%s\\sin x\\bigg|_{%s}^{%s}\\\\ \n'
                        '&\\Leftrightarrow& \\dfrac{1}{f(%s)}-\\dfrac{1}{f(%s)}=-%s\\cdot \\sin \\left(%s\\right)+%s\\cdot \\sin \\left(%s\\right)\\\\ \n'
                        '&\\Leftrightarrow& f\\left(%s\\right)\\approx %s$zz$\n'
                        '\\end{eqnarray*}\n'
                        'Vậy $\\left(%s\\right)\\approx %s$$zz$'
                        %(latex(a),latex(a),latex(a),latex(a),
                            latex(a1),latex(b1),latex(a),latex(a1),latex(b1),
                            latex(a1),latex(b1),latex(a),latex(a1),latex(b1),
                            latex(b1),latex(a1),latex(a),latex(b1),latex(a),latex(a1),
                            latex(b1),latex(kq),latex(b1),latex(kq)

                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('-+', '-').replace('+1x', '+x').replace('-1x', '-x').replace('x^{1}', 'x').replace('\\text{-', '\\text{$-$').replace('.', ',').replace('$zz$', '.').replace('=1\\cdot', '=').replace('-1\\cdot', '-').replace('+1\\cdot', '+').replace('\\limits_{\\dfrac', '\\limits_{\\tfrac').replace('\\bigg|_{\\dfrac', '\\bigg|_{\\tfrac').replace('}^{\\dfrac', '}^{\\tfrac')
            return content 

