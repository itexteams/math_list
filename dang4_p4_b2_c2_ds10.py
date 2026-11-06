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


def bt_dang4_p4_b2_c2_ds10(self):
            # Khai báo biến
            x = symbols('x')
            y = symbols('y')
            #Điểm A
            lis_xa=[1,1.5,2]
            xa=random.choice(lis_xa)
            lis_ya=[2,2.5,3,3.5,4]
            ya=random.choice(lis_ya)
            #Điểm D
            xd=xa+0.5
            yd=ya-1
            #Điểm C
            lis_xc=[1.5,2,2.5,3]
            d_xc=random.choice(lis_xc)
            xc=xa+d_xc
            yc=ya-1.5
            #Điểm B
            xb=xc
            yb=ya

            lis2=[10,15,20,25,30]
            i=random.choice(lis2)
            k=random.choice(lis2)
            #while i<=k:
                #i=random.choice(lis2)
                #k=random.choice(lis2)
            #Rút gọn các BPT
            lis3=[100,200,300]
            m=random.choice(lis3)
            n=random.choice(lis3)

            bpt1=2*x+y>=ya+2*xa
            pt11=2*x*m+y*m>=ya*m+2*xa*m
            pt111=2*x*m+y*m
            pt1=Eq(2*x+y,ya+2*xa)
            bpt2=(yd-yc)*x+(xc-xd)*y>=yc*(xc-xd)-xc*(yc-yd)
            pt22=n*(yd-yc)*x+n*(xc-xd)*y>=n*yc*(xc-xd)-n*xc*(yc-yd)
            pt222=n*(yd-yc)*x+n*(xc-xd)*y
            pt2=Eq((yd-yc)*x+(xc-xd)*y,yc*(xc-xd)-xc*(yc-yd))

            a=ya*m+2*xa*m
            b=n*yc*(xc-xd)-n*xc*(yc-yd)
            c=2*m
            d=n*(yd-yc)
            e=m
            f=n*(xc-xd)
            #Tiền
            tien=i*x+k*y
            tien_a=i*xa+k*ya
            tien_b=i*xb+k*yb
            tien_c=i*xc+k*yc
            tien_d=i*xd+k*yd
            #Tìm GTNN
            tien_min=min(tien_a,tien_b,tien_c,tien_d)
            # Khởi tạo biến để lưu trữ giá trị x và y tương ứng với tien_min
            x_tien_min = None
            y_tien_min = None
            # Tìm x và y tương ứng với tien_min
            if tien_min == tien_a:
                x_tien_min = xa
                y_tien_min = ya
            elif tien_min == tien_b:
                x_tien_min = xb
                y_tien_min = yb
            elif tien_min == tien_c:
                x_tien_min = xc
                y_tien_min = yc
            elif tien_min == tien_d:
                x_tien_min = xd
                y_tien_min = yd

            # Nội dung câu hỏi
            noidungcauhoi = ('''Người ta định dùng hai loại nguyên liệu để chiết xuất ít nhất $%s$ kg hóa chất $A$ và $%s$ kg hóa chất $B$. Từ mỗi tấn nguyên liệu loại $I$ có thể chiết xuất được $%s$ kg chất $A$ và $%s$ kg chất $B$. Từ mỗi tấn nguyên liệu loại $II$ có thể chiết xuất được $%s$ chất $A$ và $%s$ kg chất $B$. Biết rằng cơ sở cung cấp nguyên liệu chỉ có thể cung cấp không quá $%s$ tấn nguyên liệu loại $I$ và $%s$ tấn nguyên liệu loại $II$, giá tiền mỗi tấn nguyên liệu loại $I$ là $%s$ triệu đồng, mỗi tấn nguyên liệu loại $II$ là $%s$ triệu đồng. Tính chi phí mua nguyên liệu loại I và loại II ít nhất. \n'''
                            %(latex(a),latex(b),latex(c),latex(d),latex(e),latex(f),latex(xb),latex(yb),latex(i),latex(k)
                                )
                                )

                # Nội dung lời giải
            hinhve = ('\\begin{center} \n'
                      '\\begin{tikzpicture}[>=stealth, scale=1, line width=1pt] \n'
                      '\\draw[->] (-2.5,0) -- (5.5,0) node[below]{$x$}; \n'
                      '\\draw[->] (0,-2.5) -- (0,5.5) node[left]{$y$}; \n'
                      '\\node at (0,0) [below left] {$O$}; \n'
                      '\\clip (-2.5,-2.5) rectangle (5.4,5.4); \n'
                      '\\fill[pattern=north east lines, pattern color=black] (-2.5,-2.5) rectangle (5.4,5.4); \n'
                      '\\fill[white] (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- cycle; \n'
                      '\\draw[black, smooth, domain=-3:6] plot(\\x,{%s*\\x+%s}); \n'
                      '\\draw[black, smooth, domain=-3:6] plot(\\x,{%s*\\x+%s}); \n'
                      '\\draw[black, smooth, domain=-3:6] plot(\\x,{%s}); \n'
                      '\\draw[black] (%s,-3) -- (%s,6); \n'
                      '\\coordinate (A) at (%s,%s); \n'
                      '\\coordinate (B) at (%s,%s); \n'
                      '\\coordinate (C) at (%s,%s); \n'
                      '\\coordinate (D) at (%s,%s); \n'
                      '\\fill (A) circle (0.5pt) node[below left] {$A$}; \n'
                      '\\fill (B) circle (0.5pt) node[below right] {$B$}; \n'
                      '\\fill (C) circle (0.5pt) node[above right] {$C$}; \n'
                      '\\fill (D) circle (0.5pt) node[above left] {$D$}; \n'
                      '\\end{tikzpicture} \n'
                      '\\end{center} \n'
                      %(latex(xa),latex(ya), latex(xb),latex(yb), latex(xc),latex(yc), latex(xd),latex(yd),
                        latex(-2), latex(ya+2*xa),
                        latex((yc-yd)/(xc-xd)), latex(yc-xc*(yc-yd)/(xc-xd)),
                        latex(yb),
                        latex(xb), latex(xb),
                        latex(xa),latex(ya), latex(xb),latex(yb), latex(xc),latex(yc), latex(xd),latex(yd)))

            # Nội dung lời giải
            loigiai=('Gọi số tấn nguyên liệu loại $I$ là $x$ tấn; Số tấn nguyên liệu loại $II$ là $y$ tấn, với $0 \\le x \\le %s$ và $0 \\le y \\le %s$. \\\\ \n'
                    'Khi đó số chất $A$ thu được là $%s$. \\\\ \n'
                    'Số chất $B$ thu được là $%s$. \\\\ \n'
                    'Ta có hệ phương trình: $\\heva{& 0 \\le x \\le %s \\\\& 0 \\le y \\le %s\\\\& %s\\\\& %s} \\Leftrightarrow  \\heva{& 0 \\le x \\le %s \\\\& 0 \\le y \\le %s\\\\& %s\\\\& %s.}$\\\\ \n'
                    'Vẽ các đường thẳng sau trên cùng hệ trục tọa độ $(Oxy)$: \\\\ \n'
                    '$d_1: x=%s$.\\\\ \n'
                    '$d_2: y=%s$.\\\\ \n'
                    '$d_3: %s$.\\\\ \n'
                    '$d_4: %s$.\\\\ \n'
                    'Ta được miền nghiệm của hệ bất phương trình là phần tô đậm trong hình vẽ sau: \\\\ \n'
                    '%s' #hinhve
                    'Miền nghiệm là đa giác $ABCD$ với $A \\left( %s;%s \\right), B \\left( %s;%s \\right), C \\left( %s;%s \\right)$ và $D \\left( %s;%s \\right)$. \\\\ \n'
                    'Số tiền bỏ ra là $F(x;y)=%s$ nghìn đồng. Ta có \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    'Ta thấy $F(x;y)$ đạt giá trị nhỏ nhất tại điểm $\\left( %s;%s \\right)$. \\\\ \n'
                    'Vậy chi phí ít nhất để mua nguyên liệu là $%s$ triệu đồng.'

                    %(latex(xb),latex(yb),
                        latex(pt111),
                        latex(pt222),
                        latex(xb),latex(yb),
                        latex(pt11),
                        latex(pt22),
                        latex(xb),latex(yb),
                        latex(bpt1),latex(bpt2),
                        latex(xb),
                        latex(yb),
                        latex(pt1),
                        latex(pt2),
                        str(hinhve),
                        latex(xa),latex(ya),
                        latex(xb),latex(yb),
                        latex(xc),latex(yc),
                        latex(xd),latex(yd),
                        latex(tien),
                        latex(xa),latex(ya), latex(tien_a),
                        latex(xb),latex(yb), latex(tien_b),
                        latex(xc),latex(yc), latex(tien_c),
                        latex(xd),latex(yd), latex(tien_d),
                        latex(x_tien_min),latex(y_tien_min),latex(tien_min),
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac'). replace('1x','x').replace('-1x','-x'). replace('1y','y'). replace('.0',''). replace('+-','-')
            return content

