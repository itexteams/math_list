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


def bt_dang1_p4_b3_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='1':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                S=(12,15,18)
                d=random.choice(S)
                c=(2*a-b)/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\cos \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Gọi $t_1;t_2$ lần lượt là hai thời điểm trong ngày khi chiều cao của mực nước biển là $%s$ m$zz$ Tính $t_1+t_2$$zz$ \n'
                                %(latex(a),latex(b),latex(d),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Do chiều cao của mực nước là $%s$ m nên\\\\ \n'
                            '$%s+%s{\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=%s \\Leftrightarrow {\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=-\\dfrac{1}{2}\\Leftrightarrow {\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=\\cos\\dfrac{2\\pi}{3}$\\\\ \n'
                            '$\\Leftrightarrow\\hoac{& \\dfrac{\\pi}{%s} t=\\dfrac {2\\pi} {3} + k2\\pi \\\\& \\dfrac{\\pi}{%s} t=\\dfrac {-2\\pi} {3} + k2\\pi} \\Leftrightarrow \\hoac{& t=%s + %sk \\\\& t=-%s + %sk}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $t=%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_1=%s \\hspace*{0$zz$2cm}(k=0)$$zz$\\\\ \n'
                            '\\hspace*{0$zz$7cm}$t=-%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_2=%s \\hspace*{0$zz$2cm}(k=1)$$zz$\\\\ \n'
                            'Vậy $t_1 + t_2 = %s+%s=%s$$zz$'
                            %(latex(c),latex(a),latex(b),latex(d),latex(c),latex(d),
                            latex(d),latex(d),latex(d),latex(2*d/3),latex(2*d),latex(2*d/3),latex(2*d),
                            latex(2*d/3),latex(2*d),latex(2*d/3),
                            latex(2*d/3),latex(2*d),latex(4*d/3),
                            latex(2*d/3),latex(4*d/3),latex(2*d))
            )


            if dang=='2':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                S=(10,12,14,16)
                d=random.choice(S)
                c=a

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\cos \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Gọi $t_1;t_2$ lần lượt là hai thời điểm trong ngày khi chiều cao của mực nước biển là $%s$ m$zz$ Tính $t_1+t_2$$zz$\n'
                                %(latex(a),latex(b),latex(d),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Do chiều cao của mực nước là $%s$ m nên\\\\ \n'
                            '$%s+%s{\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=%s \\Leftrightarrow {\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=0\\Leftrightarrow {\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=\\cos\\dfrac{\\pi}{2}$\\\\ \n'
                            '$\\Leftrightarrow\\hoac{& \\dfrac{\\pi}{%s} t=\\dfrac {\\pi} {2} + k2\\pi \\\\& \\dfrac{\\pi}{%s} t=\\dfrac {-\\pi} {2} + k2\\pi} \\Leftrightarrow \\hoac{& t=%s + %sk \\\\& t=-%s + %sk}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $t=%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_1=%s \\hspace*{0$zz$2cm}(k=0)$$zz$\\\\ \n'
                            '\\hspace*{0$zz$7cm}$t=-%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_2=%s \\hspace*{0$zz$2cm}(k=1)$$zz$\\\\ \n'
                            'Vậy $t_1 + t_2 = %s+%s=%s$$zz$'
                            %(latex(c),
                            latex(a),latex(b),latex(d),latex(c),latex(d),latex(d),
                            latex(d),latex(d),latex(d/2),latex(2*d),latex(d/2),latex(2*d),
                            latex(d/2),latex(2*d),latex(d/2),
                            latex(d/2),latex(2*d),latex(3*d/2),
                            latex(d/2),latex(3*d/2),latex(2*d))
            )


            if dang=='3':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                d=12
                c=(2*a+b)/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\cos \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Gọi $t_1;t_2$ lần lượt là hai thời điểm trong ngày khi chiều cao của mực nước biển là $%s$ m$zz$ Tính $t_1+t_2$$zz$\n'
                                %(latex(a),latex(b),latex(d),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Do chiều cao của mực nước là $%s$ m nên\\\\ \n'
                            '$%s+%s{\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=%s \\Leftrightarrow {\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=\\dfrac{1}{2}\\Leftrightarrow {\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=\\cos\\dfrac{\\pi}{3}$\\\\ \n'
                            '$\\Leftrightarrow\\hoac{& \\dfrac{\\pi}{%s} t=\\dfrac {\\pi} {3} + k2\\pi \\\\& \\dfrac{\\pi}{%s} t=\\dfrac {-\\pi} {3} + k2\\pi} \\Leftrightarrow \\hoac{& t=%s + %sk \\\\& t=-%s + %sk}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $t=%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_1=%s \\hspace*{0$zz$2cm}(k=0)$$zz$\\\\ \n'
                            '\\hspace*{0$zz$7cm}$t=-%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_2=%s \\hspace*{0$zz$2cm}(k=1)$$zz$\\\\ \n'
                            'Vậy $t_1 + t_2 = %s+%s=%s$$zz$'
                            %(latex(c),latex(a),latex(b),latex(d),latex(c),latex(d),
                            latex(d),latex(d),latex(d),latex(2*d/3),latex(2*d),latex(2*d/3),latex(2*d),
                            latex(d/3),latex(2*d),latex(d/3),
                            latex(d/3),latex(2*d),latex(5*d/3),
                            latex(d/3),latex(5*d/3),latex(2*d))
            )



            if dang=='4':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                S=(12,18,24)
                d=random.choice(S)
                c=(2*a+b)/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\sin \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Gọi $t_1;t_2$ lần lượt là hai thời điểm trong ngày khi chiều cao của mực nước biển là $%s$ m$zz$ Tính $t_1+t_2$$zz$\n'
                                %(latex(a),latex(b),latex(d),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Do chiều cao của mực nước là $%s$ m nên\\\\ \n'
                            '$%s+%s{\\sin \\left(\\dfrac{\\pi}{%s} t\\right)}=%s \\Leftrightarrow {\\sin \\left(\\dfrac{\\pi}{%s} t\\right)}=\\dfrac{1}{2}\\Leftrightarrow '
                            '{\\sin\\left(\\dfrac{\\pi}{%s} t\\right)}=\\sin\\dfrac{\\pi}{6}$\\\\ \n'
                            '$\\Leftrightarrow\\hoac{& \\dfrac{\\pi}{%s} t=\\dfrac {\\pi} {6} + k2\\pi \\\\& \\dfrac{\\pi}{%s} t=\\dfrac {5\\pi} {6} + k2\\pi} '
                            '\\Leftrightarrow \\hoac{& t=%s + %sk \\\\& t=%s + %sk}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $t=%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_1=%s \\hspace*{0$zz$2cm}(k=0)$$zz$\\\\ \n'
                            '\\hspace*{0$zz$7cm}$t=%s+%sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z}), (0\\le t \\le 24)\\Rightarrow t_2=%s \\hspace*{0$zz$2cm}(k=0)$$zz$\\\\ \n'
                            'Vậy $t_1 + t_2 = %s+%s=%s$$zz$'
                            %(latex(c),
                            latex(a),latex(b),latex(d),latex(c),latex(d),
                            latex(d),
                            latex(d),latex(d),
                            latex(d/6),latex(2*d),
                            latex(5*d/6),latex(2*d),
                            latex(d/6),latex(2*d),latex(d/6),
                            latex(5*d/6),latex(2*d),latex(5*d/6),
                            latex(d/6),latex(5*d/6),latex(d))
            )


            if dang=='5':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                S=(6,8)
                d=random.choice(S)
                c=(2*a+b)/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\sin \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Gọi $t_1;t_2$ lần lượt là hai thời điểm trong ngày khi chiều cao của mực nước biển là cao nhất$zz$ Tính $t_1+t_2$$zz$ \n'
                                %(latex(a),latex(b),latex(d))
                                )

                # Nội dung lời giải
                loigiai = ('Để chiều cao của mực nước là cao nhất thì $h(t)$ đạt giá trị lớn nhất khi đó\\\\ \n'
                            '${\\sin \\left(\\dfrac{\\pi}{%s} t\\right)}=1\\Leftrightarrow {\\sin\\left(\\dfrac{\\pi}{%s} t\\right)}=\\sin\\dfrac{\\pi}{2}$\\\\ \n'
                            '$\\hspace*{2$zz$4cm}\\Leftrightarrow\\dfrac{\\pi}{%s} t=\\dfrac {\\pi} {2} + k2\\pi \\\\ \n'
                            '\\hspace*{2$zz$3cm}\\Leftrightarrow t=%s + %sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $ k\\in \\mathbb {Z}, 0\\le t \\le 24\\\\ \n'
                            '\\hspace*{0$zz$2cm}\\Rightarrow t_1=%s \\hspace*{0$zz$2cm}(k=0);\\hspace*{0$zz$2cm}t_2=%s \\hspace*{0$zz$2cm}(k=1)$$zz$\\\\ \n'
                            'Vậy $t_1 + t_2 = %s+%s=%s$$zz$'
                            %(
                            latex(d),
                            latex(d),
                            latex(d),
                            latex(d/2),latex(2*d),
                            latex(d/2),latex(5*d/2),
                            latex(d/2),latex(5*d/2),latex(3*d))
            )



            if dang=='6':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                S=(10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48)
                d=random.choice(S)
                c=(2*a+b)/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\sin \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Tìm thời điểm trong ngày chiều cao của mực nước biển cao nhất$zz$\n'
                                %(latex(a),latex(b),latex(d))
                                )

                # Nội dung lời giải
                loigiai = ('Để chiều cao của mực nước là cao nhất thì $h(t)$ đạt giá trị lớn nhất khi đó\\\\ \n'
                            '${\\sin \\left(\\dfrac{\\pi}{%s} t\\right)}=1\\Leftrightarrow {\\sin\\left(\\dfrac{\\pi}{%s} t\\right)}=\\sin\\dfrac{\\pi}{2}$\\\\ \n'
                            '$\\hspace*{2$zz$4cm}\\Leftrightarrow\\dfrac{\\pi}{%s} t=\\dfrac {\\pi} {2} + k2\\pi \\\\ \n'
                            '\\hspace*{2$zz$3cm}\\Leftrightarrow t=%s + %sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $ k\\in \\mathbb {Z},\\hspace*{0$zz$2cm} 0\\le t \\le 24\\\\ \n'
                            '\\hspace*{0$zz$2cm}\\Rightarrow t=%s \\hspace*{0$zz$2cm}(k=0)$$zz$\\\\ \n'
                            'Vậy $t=%s$ giờ$zz$'
                            %(
                            latex(d),
                            latex(d),
                            latex(d),
                            latex(d/2),latex(2*d),
                            latex(d/2),latex(d/2))
            )



            if dang=='7':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                S=(8,10,12,14,16)
                d=random.choice(S)
                c=(2*a+b)/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\sin \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Tìm thời điểm trong ngày chiều cao của mực nước biển thấp nhất$zz$\n'
                                %(latex(a),latex(b),latex(d))
                                )

                # Nội dung lời giải
                loigiai = ('Để chiều cao của mực nước là cao nhất thì $h(t)$ đạt giá trị nhỏ nhất khi đó\\\\ \n'
                            '${\\sin \\left(\\dfrac{\\pi}{%s} t\\right)}=-1\\Leftrightarrow {\\sin\\left(\\dfrac{\\pi}{%s} t\\right)}=\\sin\\left(-\\dfrac {\\pi} {2}\\right)$\\\\ \n'
                            '$\\hspace*{2$zz$4cm}\\Leftrightarrow\\dfrac{\\pi}{%s} t=-\\dfrac {\\pi} {2} + k2\\pi \\\\ \n'
                            '\\hspace*{2$zz$3cm}\\Leftrightarrow t=-%s + %sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $ k\\in \\mathbb {Z},\\hspace*{0$zz$2cm} 0\\le t \\le 24\\\\ \n'
                            '\\hspace*{0$zz$2cm}\\Rightarrow t=%s \\hspace*{0$zz$2cm}(k=1)$$zz$\\\\ \n'
                            'Vậy $t=%s$ giờ$zz$'
                            %(
                            latex(d),
                            latex(d),
                            latex(d),
                            latex(d/2),latex(2*d),
                            latex(3*d/2),latex(3*d/2))
            )


            if dang=='8':
                t=symbols('t')
                a=randint(7,20)
                b=randint(2,9)
                d=randint(9,23)
                c=(2*a+b)/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Biết chiều cao của mực nước biển $h(m)$ theo thời gian $t(h) (0\\le t \\le 24)$ được cho bởi công thức ${h=%s+%s\\cos \\left(\\frac{\\pi}{%s} t\\right)}$$zz$ '
                                ' Tìm thời điểm trong ngày chiều cao của mực nước biển thấp nhất$zz$\n'
                                %(latex(a),latex(b),latex(d))
                                )

                # Nội dung lời giải
                loigiai = ('Để chiều cao của mực nước là cao nhất thì $h(t)$ đạt giá trị nhỏ nhất khi đó\\\\ \n'
                            '${\\cos \\left(\\dfrac{\\pi}{%s} t\\right)}=-1\\Leftrightarrow {\\cos\\left(\\dfrac{\\pi}{%s} t\\right)}=\\cos\\pi$\\\\ \n'
                            '$\\hspace*{2$zz$6cm}\\Leftrightarrow\\dfrac{\\pi}{%s} t=\\pi + k2\\pi \\\\ \n'
                            '\\hspace*{2$zz$5cm}\\Leftrightarrow t=%s + %sk \\hspace*{0$zz$2cm}( k\\in \\mathbb {Z})$$zz$\\\\ \n'
                            'Với $ k\\in \\mathbb {Z},\\hspace*{0$zz$2cm} 0\\le t \\le 24\\\\ \n'
                            '\\hspace*{0$zz$2cm}\\Rightarrow t=%s \\hspace*{0$zz$2cm}(k=0)$$zz$\\\\ \n'
                            'Vậy $t=%s$ giờ$zz$'
                            %(
                            latex(d),
                            latex(d),
                            latex(d),
                            latex(d),latex(2*d),
                            latex(d),latex(d))
            )



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace(',0', '')
            return content

