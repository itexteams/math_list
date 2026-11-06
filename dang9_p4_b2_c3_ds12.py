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


def bt_dang9_p4_b2_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a2=randint(2,9)
                a=a2**2
                f0=randint(1,20)
                k1=randint(1,5)
                k=randint(1,3)
                k2=k1+k
                f=(a2)*(math.e)**(x/2)
                f1=f.subs(x,k1)
                f2=f.subs(x,k2)
                kq1=(f2-f1+sqrt(f0))**2
                while  kq1>=99 or f0==0 or kq1<=-10:
                    x=symbols('x')
                    a2=randint(2,9)
                    a=a2**2
                    f0=randint(1,20)
                    k1=randint(1,5)
                    k=randint(1,3)
                    k2=k1+k
                    f=(a2)*(math.e)**(x/2)
                    f1=f.subs(x,k1)
                    f2=f.subs(x,k2)
                    kq1=(f2-f1+sqrt(f0))**2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ thoả mãn $\\left[f\'(x)\\right]^2=%se^{x}f(x),\\forall x \\in \\mathbb{R}$ và $f(%s)=%s$$zz$ Biết hàm số $f(x)$ đồng biến và có đạo hàm $f\'(x)$ liên tục trên $\\mathbb{R}$$zz$ Tính $f(%s)$ (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(k1),latex(f0),latex(k2)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\left[f\'(x)\\right]^2=%se^{x}f(x) \\Leftrightarrow f\'(x)=%se^{\\tfrac{x}{2}}\\sqrt{f(x)}\\Leftrightarrow \\dfrac{f\'(x)}{2\\sqrt{f(x)}}=%se^{\\tfrac{x}{2}}\\Leftrightarrow \\left[\\sqrt{f(x)}\\right]\'=%se^{\\tfrac{x}{2}}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[\\sqrt{f(x)}\\right]\' \\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} %se^{\\tfrac{x}{2}}\\text{d}x$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow \\sqrt{f(x)}\\bigg|_{%s}^{%s}=%se^{\\tfrac{x}{2}}\\bigg|_{%s}^{%s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow \\sqrt{f(%s)}-\\sqrt{f(%s)} =%se^{\\tfrac{%s}{2}}-%se^{\\tfrac{%s}{2}}$$zz$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow f(%s)=%s$$zz$'
                        %(latex(a),latex(a2),latex(nsimplify(a2/2)),latex(nsimplify(a2/2)),
                            latex(k1),latex(k2),latex(k1),latex(k2),latex(nsimplify(a2/2)),
                            latex(k1),latex(k2),latex(a2), latex(k1),latex(k2),

                            latex(k2),latex(k1),latex(a2),latex(k2),latex(a2),latex(k1),
                            latex(k2),latex(kq)

                            )
                        )

                #Đáp án

            if dang=='2':
                x=symbols('x')
                n1=randint(1,4)
                n=n1*2
                a2=randint(2,9)
                a=a2**2
                f0=randint(1,20)
                k1=randint(1,5)
                k=randint(1,3)
                k2=k1+k
                f=(a2/(n1+1))*x**(n1+1)
                f1=f.subs(x,k1)
                f2=f.subs(x,k2)
                kq1=(f2-f1+sqrt(f0))**2
                while  kq1>=99 or f0==0 or kq1<=-10:
                    x=symbols('x')
                    n1=randint(1,4)
                    n=n1*2
                    a2=randint(2,9)
                    a=a2**2
                    f0=randint(1,20)
                    k1=randint(1,5)
                    k=randint(1,3)
                    k2=k1+k
                    f=(a2/(n1+1))*x**(n1+1)
                    f1=f.subs(x,k1)
                    f2=f.subs(x,k2)
                    kq1=(f2-f1+sqrt(f0))**2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ thoả mãn $\\left[f\'(x)\\right]^2=%sx^{%s}f(x),\\forall x \\in \\mathbb{R}$ và $f(%s)=%s$$zz$ Biết hàm số $f(x)$ đồng biến và có đạo hàm $f\'(x)$ liên tục trên $\\mathbb{R}$$zz$ Tính $f(%s)$ (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(n),latex(k1),latex(f0),latex(k2)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\left[f\'(x)\\right]^2=%sx^{%s}f(x) \\Leftrightarrow f\'(x)=%sx^{%s}\\sqrt{f(x)}\\Leftrightarrow \\dfrac{f\'(x)}{2\\sqrt{f(x)}}=%sx^{%s}\\Leftrightarrow \\left[\\sqrt{f(x)}\\right]\'=%sx^{%s}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[\\sqrt{f(x)}\\right]\' \\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} %sx^{%s}\\text{d}x$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow \\sqrt{f(x)}\\bigg|_{%s}^{%s}=%sx^{%s}\\bigg|_{%s}^{%s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow \\sqrt{f(%s)}-\\sqrt{f(%s)} =%s\\cdot %s^{%s}-%s\\cdot %s^{%s}$$zz$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow f(%s)=%s$$zz$'
                        %(latex(a),latex(n),latex(a2),latex(n1),latex(nsimplify(a2)),latex(n1),latex(a2),latex(n1),
                            latex(k1),latex(k2),latex(k1),latex(k2),latex(a2),latex(n1),
                            latex(k1),latex(k2),latex(nsimplify(a2/(n1+1))),latex(n1+1),latex(k1),latex(k2),
                            latex(k2),latex(k1),latex(nsimplify(a2/(n1+1))),latex(k2),latex(n1+1),latex(nsimplify(a2/(n1+1))),latex(k1),latex(n1+1),
                            latex(k2),latex(kq)

                            )
                        )

                #Đáp án

            if dang=='3':
                x=symbols('x')
                a=randint(2,9)
                b=randint(1,9)
                f0=randint(1,20)
                k1=randint(1,5)
                k=randint(1,3)
                k2=k1+k
                f=(1/(3*a))*(a*x+b)**(3/2)
                f1=f.subs(x,k1)
                f2=f.subs(x,k2)
                kq1=(f2-f1+sqrt(f0))**2
                while a==b or kq1>=99 or f0==0 or kq1<=-10:
                    x=symbols('x')
                    a=randint(2,9)
                    b=randint(1,9)
                    f0=randint(1,20)
                    k1=randint(1,5)
                    k=randint(1,3)
                    k2=k1+k
                    f=(1/(3*a))*(a*x+b)**(3/2)
                    f1=f.subs(x,k1)
                    f2=f.subs(x,k2)
                    kq1=(f2-f1+sqrt(f0))**2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ thoả mãn $\\left[f\'(x)\\right]^2=(%sx+%s)f(x),\\forall x \\in \\mathbb{R}$ và $f(%s)=%s$$zz$ Biết hàm số $f(x)$ đồng biến và có đạo hàm $f\'(x)$ liên tục trên $\\mathbb{R}$$zz$ Tính $f(%s)$ (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(b),latex(k1),latex(f0),latex(k2)))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\left[f\'(x)\\right]^2=(%sx+%s)f(x) \\Leftrightarrow f\'(x)=\\sqrt{%sx+%s}\\sqrt{f(x)}$\\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow \\dfrac{f\'(x)}{2\\sqrt{f(x)}}=\\dfrac{\\sqrt{%sx+%s}}{2}\\Leftrightarrow \\left[\\sqrt{f(x)}\\right]\'=\\dfrac{\\sqrt{%sx+%s}}{2}$$zz$\\\\ \n'
                        'Suy ra\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[\\sqrt{f(x)}\\right]\' \\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} \\dfrac{\\sqrt{%sx+%s}}{2}\\text{d}x$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow \\sqrt{f(x)}\\bigg|_{%s}^{%s}=\\dfrac{1}{%s}\\left(%sx+%s\\right)^{\\dfrac{3}{2}}\\bigg|_{%s}^{%s}$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow \\sqrt{f(%s)}-\\sqrt{f(%s)} =\\dfrac{1}{%s}\\left(%s\\cdot %s+%s\\right)^{\\tfrac{3}{2}}-\\dfrac{1}{%s}\\left(%s\\cdot %s+%s\\right)^{\\tfrac{3}{2}}$$zz$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow f(%s)=%s$$zz$'
                        %(latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(k1),latex(k2),latex(k1),latex(k2),latex(a),latex(b),
                            latex(k1),latex(k2),latex(3*a),latex(a),latex(b),latex(k1),latex(k2),
                            latex(k2),latex(k1),latex(3*a),latex(a),latex(k2),latex(b),latex(3*a),latex(a),latex(k1),latex(b),
                            latex(k2),latex(kq)

                            )
                        )

                #Đáp án

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('-+', '-').replace('+1x', '+x').replace('.', ',').replace('$zz$', '.').replace('\\text{-', '\\text{$-$').replace('1e', 'e').replace('x^{1}', 'x').replace('=1x', '=x').replace('1\\cdot', '')
            return content 

