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


def bt_dang17_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                lis=[100000,150000,200000,250000,300000,350000,400000,450000,500000]
                k=random.choice(lis)
                n1=randint(100,300)
                a=randint(301,600)
                n2=randint(601,1000)
                f=2*x**3-2*(n1+n2)*x**2+n1*n2*x+k
                g=(n1+n2)*x-5*n1*n2-k/x
                h=expand(f-x*g, x)
                daoham=6*x**2-6*(n1+n2)*x+6*n1*n2
                x1=n1
                x2=n2
                l=2*x**3-2*(n1+n2)*x**2+n1*n2*x+k-x*((n1+n2)*x-5*n1*n2-k/x)
                l1=2*1**3-2*(n1+n2)*1**2+n1*n2*1+k-1*((n1+n2)*1-5*n1*n2-k/1)
                la=2*a**3-2*(n1+n2)*a**2+n1*n2*a+k-a*((n1+n2)*a-5*n1*n2-k/a)
                l2=2*x1**3-2*(n1+n2)*x1**2+n1*n2*x1+k-x1*((n1+n2)*x1-5*n1*n2-k/x1)
                maxl=max(l1,l2,la)
                h1=x1

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một doanh nghiệp dự định sản xuất không quá $%s$ sản phẩm. Nếu doanh nghiệp sản xuất $x$ sản phẩm $(1 \\le x \\le %s)$ thì $F(x)=%s$ (đồng) là hàm biểu thị doanh thu nhận được khi bán hết số sản phẩm đó, trong khi chi phí sản suất bình quân cho một sản phẩm là $G(x)=%s$ (đồng). Doanh nghiệp cần sản xuất bao nhiêu sản phẩm để lợi nhuận thu được là lớn nhất?'
                                %(latex(a),latex(a),latex(f),latex(g)
                                ))

                # Nội dung lời giải
                loigiai = ('Lợi nhuận của doanh nghiệp khi sản suất $x$ sản phẩm là \\\\ \n'
                        '\\hspace*{1cm} $L(x)=F(x)-xG(x)$ \\\\ \n'
                        '\\hspace*{1.95cm} $=%s-x\\left( %s \\right)$ \\\\ \n'
                        '\\hspace*{1.95cm} $=%s$. \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $L\'(x)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $L\'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Trên đoạn $[1;%s]$, ta có \\\\ \n'
                        '\\hspace*{1cm} $L(1)=%s$.\\\\ \n'
                        '\\hspace*{1cm} $L(%s)=%s$.\\\\ \n'
                        '\\hspace*{1cm} $L\\left(%s \\right)=%s$.\\\\ \n'
                        'Suy ra $\\max L(x)=%s$ đạt được khi $x=%s$. \\\\ \n'
                        'Vậy doanh nghiệp cần sản xuất $%s$ sản phẩm để lợi nhuận thu được là lớn nhất.'

                        %(latex(f),latex(g),
                            latex(h),
                            latex(daoham),
                            latex(daoham), latex(x1),latex(x2),
                            latex(a),
                            latex(l1),
                            latex(a),latex(la),
                            latex(x1),latex(l2),
                            latex(maxl),latex(x1),
                            latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')
            return content

