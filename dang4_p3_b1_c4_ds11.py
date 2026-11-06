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


def bt_dang4_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                n=symbols('n')
                a=randint(-5,5)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)

                while a==0 or c==0 or b==0 or d==0:
                    n=symbols('n')
                    a=randint(-5,5)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)


                un=a*n+b
                u1=a*1+b
                u2=a*2+b
                u3=a*3+b
                mau=c*n**2+d
                sn=n*(u1+un)/2
                sn1=a*n**2+(u1+b)*n
                bt=sn1/(mau*2)
                tu1=(a+(u1+b)/n)
                mau1=(2*c)+(2*d)/n**2
                x0=Rational(a,(2*c))
                while x0>=100 or x0<=-9.9:
                    n=symbols('n')
                    a=randint(-5,5)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                    while a==0 or c==0 or b==0 or d==0:
                        n=symbols('n')
                        a=randint(-5,5)
                        b=randint(-9,9)
                        c=randint(-9,9)
                        d=randint(-9,9)


                    un=a*n+b
                    u1=a*1+b
                    u2=a*2+b
                    u3=a*3+b
                    mau=c*n**2+d
                    sn=n*(u1+un)/2
                    sn1=a*n**2+(u1+b)*n
                    bt=sn1/(mau*2)
                    tu1=(a+(u1+b)/n)
                    mau1=(2*c)+(2*d)/n**2
                    x0=Rational(a,(2*c))


                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi =('Cho dãy số $(u_n)$ với $u_n=\\dfrac{%s+%s+%s+\\cdots+(%s)}{%s}$$zz$ Khi đó $\\underset{n\\to +\\infty }{\\mathop{\\lim }}{u}_{n}$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục)'
                                %(latex(u1),latex(u2),latex(u3),latex(un),latex(mau),))

                # Nội dung lời giải
                loigiai = ('Đặt $S_n=%s+%s+%s+\\cdots+(%s)$ các số hạng lập thành một cấp số cộng với số hạng đầu $a_1=%s$ và $a_n=%s$$zz$\\\\ \n'
                        '\\hspace*{1cm} $S_n=\\dfrac{n(a_1+a_n)}{2}=\\dfrac{n(%s+%s)}{2}=%s=\\dfrac{%s}{2}$$zz$ \\\\ \n'
                        'Khi đó $u_n=\\dfrac{S_n}{%s}=\\dfrac{%s}{2(%s)}=%s$$zz$ \\\\ \n'
                        'Vậy $\\underset{n\\to +\\infty }{\\mathop{\\lim }}{u}_{n}=\\underset{n\\to +\\infty }{\\mathop{\\lim }}%s=\\underset{n\\to +\\infty }{\\mathop{\\lim }}\\dfrac{%s}{%s}=%s\\approx %s$$zz$'

                        %(latex(u1),latex(u2),latex(u3),latex(un),latex(u1),latex(un),
                        latex(u1),latex(un),latex(sn),latex(sn1),
                        latex(mau),latex(sn1),latex(mau),latex(bt),
                        latex(bt),latex(tu1),latex(mau1),latex(x0),latex(kq),)
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                n=symbols('n')
                a=randint(-5,5)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)

                while a==0 or c==0 or b==0 or d==0:
                    n=symbols('n')
                    a=randint(-5,5)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)


                un=a*n+b
                u1=a*1+b
                u2=a*2+b
                u3=a*3+b
                mau=c*n**2+d
                sn=n*(u1+un)/2
                sn1=a*n**2+(u1+b)*n
                bt=sn1/(mau*2)
                tu1=(a+(u1+b)/n)
                mau1=(2*c)+(2*d)/n**2
                x0=Rational(a,(2*c))


                # Tạo phân số từ số thực
                frac = Fraction(x0).limit_denominator()

                # Lấy tử số và mẫu số
                c1 = frac.numerator
                d1 = frac.denominator

                kq=c1+d1

                # Nội dung câu hỏi
                noidungcauhoi =('Cho dãy số $(u_n)$ với $u_n=\\dfrac{%s+%s+%s+\\cdots+(%s)}{%s}$$zz$ Biết $\\underset{n\\to +\\infty }{\\mathop{\\lim }}{u}_{n}=\\dfrac{m}{n}$ với $m\\in \\mathbb{Z}$; $n\\in \\mathbb{N}$ và $\\dfrac{m}{n}$ là là phân số tối giản$zz$ $m+n$ bằng bao nhiêu?'
                                %(latex(u1),latex(u2),latex(u3),latex(un),latex(mau),))

                # Nội dung lời giải
                loigiai = ('Đặt $S_n=%s+%s+%s+\\cdots+(%s)$ các số hạng lập thành một cấp số cộng với số hạng đầu $a_1=%s$ và $a_n=%s$$zz$\\\\ \n'
                        '\\hspace*{1cm} $S_n=\\dfrac{n(a_1+a_n)}{2}=\\dfrac{n(%s+%s)}{2}=%s=\\dfrac{%s}{2}$$zz$ \\\\ \n'
                        'Khi đó $u_n=\\dfrac{S_n}{%s}=\\dfrac{%s}{2(%s)}=%s$$zz$ \\\\ \n'
                        'Suy ra $\\underset{n\\to +\\infty }{\\mathop{\\lim }}{u}_{n}=\\underset{n\\to +\\infty }{\\mathop{\\lim }}%s=\\underset{n\\to +\\infty }{\\mathop{\\lim }}\\dfrac{%s}{%s}=%s \\Rightarrow m=%s;n=%s$$zz$\\\\ \n'
                        'Vậy $m+n=%s+%s=%s$$zz$'

                        %(latex(u1),latex(u2),latex(u3),latex(un),latex(u1),latex(un),
                        latex(u1),latex(un),latex(sn),latex(sn1),
                        latex(mau),latex(sn1),latex(mau),latex(bt),
                        latex(bt),latex(tu1),latex(mau1),latex(x0),latex(c1),latex(d1),
                        latex(c1),latex(d1),latex(kq))

                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content    

