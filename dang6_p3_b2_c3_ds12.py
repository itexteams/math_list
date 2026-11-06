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


def bt_dang6_p3_b2_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a1=randint(-9,-1)
                a=6*a1
                n=randint(1,2)
                f1=randint(-10,20)
                k=randint(-4,4)
                while a1==0 or k==0 or (a/(n+1))*k**(n+1)+f1-a/(n+1)>=999 or (a/(n+1))*k**(n+1)+f1-a/(n+1)<=-999:
                    x=symbols('x')
                    a1=randint(-9,-1)
                    a=6*a1
                    n=randint(1,2)
                    k=randint(-4,4)
                    f1=randint(-10,20)
                c=nsimplify(f1-a/(n+1))
                fk=nsimplify((a/(n+1))*k**(n+1)+c)
                kq=fk

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ lên tục trên $\\mathbb{R}$ thoả mãn $f(x)+xf\'(x)-%sx^{%s}=0$$zz$ Biết $f(1)=%s$$zz$ Hỏi giá trị $f(%s)$ bằng bao nhiêu?'
                                %(latex(a),latex(n),latex(f1),latex(k)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(x)+xf\'(x)-%sx^{%s}=0 \\Leftrightarrow f(x)+xf\'(x)=%sx^{%s}\\Leftrightarrow \\left[xf(x)\\right]\'=%sx^{%s}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle \\int{\\left[xf(x)\\right]\' \\text{d}x}=\\displaystyle \\int{\\left( %sx^{%s}\\right) \\text{d}x}\\Leftrightarrow xf(x)=%sx^{%s}+\\text{C}$$zz$\\\\ \n'
                        'Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(1)=%s\\Leftrightarrow 1\\cdot (%s)=%s\\cdot(1)^{%s}+\\text{C} \\Leftrightarrow \\text{C}=%s$$zz$\\\\ \n'
                        'Vậy $f(%s)=%s\\cdot(%s)^{%s}+%s=%s$$zz$'
                        %(latex(a),latex(n),latex(a),latex(n),latex(a),latex(n),
                            latex(a),latex(n),
                            latex(nsimplify(a/(n+1))),latex(n+1),
                            latex(f1),latex(f1),latex(nsimplify(a/(n+1))),latex(n+1),latex(f1),
                            latex(k),latex(nsimplify(a/(n+1))),latex(k),latex(n+1),latex(c),latex(kq)
                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='2':
                x=symbols('x')
                a1=randint(1,9)
                a=6*a1
                n=randint(1,2)
                f1=randint(-10,20)
                k=randint(-4,4)
                while a1==0 or k==0 or (a/(n+1))*k**(n+1)+f1-a/(n+1)>=999 or (a/(n+1))*k**(n+1)+f1-a/(n+1)<=-999:
                    x=symbols('x')
                    a1=randint(1,9)
                    a=6*a1
                    n=randint(1,2)
                    k=randint(-4,4)
                    f1=randint(-10,20)
                c=nsimplify(f1-a/(n+1))
                fk=nsimplify((a/(n+1))*k**(n+1)+c)
                kq=fk

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ lên tục trên $\\mathbb{R}$ thoả mãn $f(x)+xf\'(x)-%sx^{%s}=0$$zz$ Biết $f(1)=%s$$zz$ Hỏi giá trị $f(%s)$ bằng bao nhiêu?'
                                %(latex(a),latex(n),latex(f1),latex(k)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(x)+xf\'(x)-%sx^{%s}=0 \\Leftrightarrow f(x)+xf\'(x)=%sx^{%s}\\Leftrightarrow \\left[xf(x)\\right]\'=%sx^{%s}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle \\int{\\left[xf(x)\\right]\' \\text{d}x}=\\displaystyle \\int{ %sx^{%s} \\text{d}x}\\Leftrightarrow xf(x)=%sx^{%s}+\\text{C}$$zz$\\\\ \n'
                        'Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(1)=%s\\Leftrightarrow 1\\cdot (%s)=%s\\cdot(1)^{%s}+\\text{C} \\Leftrightarrow \\text{C}=%s$$zz$\\\\ \n'
                        'Vậy $f(%s)=%s\\cdot(%s)^{%s}+%s=%s$$zz$'
                        %(latex(a),latex(n),latex(a),latex(n),latex(a),latex(n),
                            latex(a),latex(n),
                            latex(nsimplify(a/(n+1))),latex(n+1),
                            latex(f1),latex(f1),latex(nsimplify(a/(n+1))),latex(n+1),latex(f1),
                            latex(k),latex(nsimplify(a/(n+1))),latex(k),latex(n+1),latex(c),latex(kq)
                            )
                        )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='3':
                x=symbols('x')
                a=randint(2,9)
                f0=randint(-10,20)
                k=randint(-2,5)
                c=f0-a
                kq1=a*(math.exp(k))+c
                while k==0 or kq1>=99 or f0==0 or kq1<=-10:
                    x=symbols('x')
                    a=randint(2,9)
                    f0=randint(-10,20)
                    k=randint(-2,5)
                    c=f0-a
                    kq1=a*(math.exp(k))+c
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ lên tục trên $\\mathbb{R}$ thoả mãn $f(x)+xf\'(x)-%se^{x}=0$$zz$ Biết $f(0)=%s$$zz$ Hỏi giá trị $f(%s)$ bằng bao nhiêu?(kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(f0),latex(k)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(x)+xf\'(x)-%se^{x}=0 \\Leftrightarrow f(x)+xf\'(x)=%se^{x}\\Leftrightarrow \\left[xf(x)\\right]\'=%se^{x}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle \\int{\\left[xf(x)\\right]\' \\text{d}x}=\\displaystyle \\int{%se^{x} \\text{d}x}\\Leftrightarrow xf(x)=%se^{x}+\\text{C}$$zz$\\\\ \n'
                        'Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(0)=%s\\Leftrightarrow 1\\cdot %s=%s\\cdot e^{0}+\\text{C} \\Leftrightarrow \\text{C}=%s$$zz$\\\\ \n'
                        'Vậy $f(%s)=%s\\cdot e^{%s}+%s=%s$.'
                        %(latex(a),latex(a),latex(a),
                            latex(a),latex(a),latex(f0),latex(f0),latex(a),latex(c),
                            latex(k),latex(a),latex(k),latex(c),latex(kq),

                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='4':
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                f0=randint(-10,20)
                k_1=randint(-6,6)
                k_2=randint(-6,6)
                k1=pi/k_1
                k2=pi/k_2
                f=-a*(cos(x))+b*(sin(x))
                f1=f.subs(x,k1)
                f2=f.subs(x,k2)
                kq1=f2-f1
                while k_1==0 or k_2==0 or a==0 or b==0 or kq1>=99 or f0==0 or kq1<=-10 or k_1==5 or k_1==-5 or k_2==5 or k_2==-5 or k_2>=k_1:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    f0=randint(-10,20)
                    k_1=randint(-6,6)
                    k_2=randint(-6,6)
                    k1=pi/k_1
                    k2=pi/k_2
                    f=-a*(cos(x))+b*(sin(x))
                    f1=f.subs(x,k1)
                    f2=f.subs(x,k2)
                    kq1=(f2-f1+k1*f0)/k2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ lên tục trên $\\mathbb{R}$ thoả mãn $f(x)+xf\'(x)-%s\\sin x -%s\\cos x=0$$zz$ Biết $f\\left(%s\\right)=%s$$zz$ Hỏi giá trị $f\\left(%s\\right)$ bằng bao nhiêu?(kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(b),latex(k1),latex(f0),latex(k2)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(x)+xf\'(x)-%s\\sin x -%s\\cos x=0 \\Leftrightarrow f(x)+xf\'(x)=%s\\sin x +%s\\cos x$\\\\ \n'
                        '\\hspace*{7.7cm}$\\Leftrightarrow \\left[xf(x)\\right]\'=%s\\sin x +%s\\cos x$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[xf(x)\\right]\' \\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s}\\left(%s\\sin x +%s\\cos x\\right)\\text{d}x$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow xf(x)\\bigg|_{%s}^{%s}=\\left(%s\\cos x+%s\\sin x\\right)\\bigg|_{%s}^{%s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow %s\\cdot f\\left(%s\\right)-%s\\cdot f\\left(%s\\right)=\\left[%s\\cos\\left(%s\\right)+%s\\sin \\left(%s\\right)\\right]-\\left[%s\\cos \\left(%s\\right)+%s\\sin \\left(%s\\right)\\right]$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow %s\\cdot f\\left(%s\\right)-%s\\cdot \\left(%s\\right)=%s$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow %s\\cdot f\\left(%s\\right)=%s+%s$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow f(%s)=%s$$zz$'
                        %(latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(k1),latex(k2),latex(k1),latex(k2),latex(a),latex(b),
                            latex(k1),latex(k2),latex(-a),latex(b),latex(k1),latex(k2),
                            latex(k2),latex(k2),latex(k1),latex(k1),latex(-a),latex(k2),latex(b),latex(k2),latex(-a),latex(k1),latex(b),latex(k1),
                            latex(k2),latex(k2),latex(k1),latex(f0),latex(nsimplify(f2-f1)),
                            latex(k2),latex(k2),latex(nsimplify(f2-f1)),latex(nsimplify(k1*f0)),
                            latex(k2),latex(kq)


                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='5':
                x=symbols('x')
                a=randint(2,9)
                b=randint(2,8)
                f0=randint(-10,20)
                k1=randint(1,3)
                k=randint(1,3)
                k2=k1+k
                f=(a*b**x)/ln(b)
                f1=f.subs(x,k1)
                f2=f.subs(x,k2)
                kq1=(f2-f1+k1*f0)/k2
                while a==b or kq1>=99 or f0==0 or kq1<=-10:
                    x=symbols('x')
                    a=randint(2,9)
                    b=randint(2,8)
                    f0=randint(-10,20)
                    k1=randint(1,3)
                    k=randint(1,3)
                    k2=k1+k
                    f=(a*b**x)/ln(b)
                    f1=f.subs(x,k1)
                    f2=f.subs(x,k2)
                    kq1=(f2-f1+k1*f0)/k2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ lên tục trên $\\mathbb{R}$ thoả mãn $f(x)+xf\'(x)-%s\\cdot %s^{x}=0$$zz$ Biết $f(%s)=%s$$zz$ Hỏi giá trị $f(%s)$ bằng bao nhiêu?(kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(b),latex(k1),latex(f0),latex(k2)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(x)+xf\'(x)-%s\\cdot %s^{x}=0 \\Leftrightarrow f(x)+xf\'(x)=%s\\cdot %s^{x}\\Leftrightarrow \\left[xf(x)\\right]\'=%s\\cdot %s^{x}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[xf(x)\\right]\' \\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} %s\\cdot %s^{x}\\text{d}x$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow xf(x)\\bigg|_{%s}^{%s}=\\dfrac{%s\\cdot %s^{x}}{\\ln %s}\\bigg|_{%s}^{%s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow %s\\cdot f(%s)-%s\\cdot f(%s)=\\dfrac{%s\\cdot %s^{%s}}{\\ln %s}-\\dfrac{%s\\cdot %s^{%s}}{\\ln %s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow f(%s)=%s$$zz$'
                        %(latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(k1),latex(k2),latex(k1),latex(k2),latex(a),latex(b),
                            latex(k1),latex(k2),latex(a),latex(b),latex(b),latex(k1),latex(k2),
                            latex(k2),latex(k2),latex(k1),latex(k1),latex(a),latex(b),latex(k2),latex(b),latex(a),latex(b),latex(k1),latex(b),
                            latex(k2),latex(kq)

                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='6':
                x=symbols('x')
                a=randint(2,9)
                f0=randint(-10,20)
                k1=randint(1,3)
                k=randint(1,3)
                k2=k1+k
                f=a*ln(x)
                f1=f.subs(x,k1)
                f2=f.subs(x,k2)
                kq1=(f2-f1+k1*f0)/k2
                while kq1>=99 or f0==0 or kq1<=-10:
                    x=symbols('x')
                    a=randint(2,9)
                    f0=randint(-10,20)
                    k1=randint(1,3)
                    k=randint(1,3)
                    k2=k1+k
                    f=a*ln(x)
                    f1=f.subs(x,k1)
                    f2=f.subs(x,k2)
                    kq1=(f2-f1+k1*f0)/k2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)$ lên tục trên $\\mathbb{R}$ thoả mãn $f(x)+xf\'(x)-\\dfrac{%s}{x}=0$$zz$ Biết $f(%s)=%s$$zz$ Hỏi giá trị $f(%s)$ bằng bao nhiêu?(kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(k1),latex(f0),latex(k2)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $f(x)+xf\'(x)-\\dfrac{%s}{x}=0 \\Leftrightarrow f(x)+xf\'(x)=\\dfrac{%s}{x}\\Leftrightarrow \\left[xf(x)\\right]\'=\\dfrac{%s}{x}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[xf(x)\\right]\' \\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} \\dfrac{%s}{x}\\text{d}x$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow xf(x)\\bigg|_{%s}^{%s}=%s\\ln \\abs{x}\\bigg|_{%s}^{%s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow %s\\cdot f(%s)-%s\\cdot f(%s)=%s\\ln\\abs{%s}-%s\\ln\\abs{%s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow f(%s)=%s$$zz$'
                        %(latex(a),latex(a),latex(a),
                            latex(k1),latex(k2),latex(k1),latex(k2),latex(a),
                            latex(k1),latex(k2),latex(a),latex(k1),latex(k2),
                            latex(k2),latex(k2),latex(k1),latex(k1),latex(a),latex(k2),latex(a),latex(k1),
                            latex(k2),latex(kq)

                            )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('-+', '-').replace('+1x', '+x').replace('-1x', '-x').replace('x^{1}', 'x').replace('\\limits_{\\dfrac', '\\limits_{\\tfrac').replace('\\bigg|_{\\dfrac', '\\bigg|_{\\tfrac').replace('}^{\\dfrac', '}^{\\tfrac').replace('\\limits_{- \\dfrac', '\\limits_{-\\tfrac').replace('\\bigg|_{- \\dfrac', '\\bigg|_{-\\tfrac').replace('^{- \\dfrac', '^{-\\tfrac').replace('1\\sin', '\\sin').replace('1\\cos', '\\cos').replace('-1\\sin', '-\\sin').replace('-1\\cos', '-\\cos').replace('=0+', '').replace('=0-', '-').replace('\\text{-', '\\text{$-$').replace('.', ',').replace('$zz$', '.')
            return content 

