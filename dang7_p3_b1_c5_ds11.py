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


def bt_dang7_p3_b1_c5_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a = symbols('a')
                b = symbols('b')
                x = symbols('x')

                n=randint(2,9)
                m1=n
                m=n*m1
                xk=randint(-50,50)

                k=randint(2,7)
                p=randint(4,11)
                p1=randint(1,3)
                q=p-p1
                p2=randint(4,11)
                p3=randint(1,3)
                q2=p2-p3
                while p==p1 or p2==p3 or p % q==0 or q2 %p2==0 or m%(n+1)==0:
                    n=randint(2,9)
                    m1=n
                    m=n*m1
                    xk=randint(-50,50)

                    k=randint(2,7)
                    p=randint(4,11)
                    p1=randint(1,3)
                    q=p-p1
                    p2=randint(4,11)
                    p3=randint(1,3)
                    q2=p2-p3
                bmu=Rational(p,q)
                bmu1=Rational(q2,p2)
                fx=m**x+n
                f0=Rational(1,n+1)
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho $a>0,b>0$ và hàm số $f(x)=\\dfrac{%s^x}{%s}$. Biết $m,n$ là các số thực thỏa mãn \\\\ \n'
                                '$\\sqrt{a}\\cdot\\sqrt[%s]{a^%s\\sqrt{a}}=a^m;\\dfrac{b^{%s}\\left( b^{%s}+b^{%s}\\right)}{b^{%s}\\left( b^{%s}+b^{%s}\\right)}=b^n$ và $f(m-a)+f(n-b)=%s$. Khi đó $f(a^m)+f(b^n)$ bằng bao nhiêu?'
                                %(latex(m),latex(fx),
                                latex(2*k+1),latex(k),latex(bmu),latex(1-bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(-bmu1),latex(xk),))

                # Nội dung lời giải
                loigiai = (
                    'Ta có $\\sqrt{a}\\cdot\\sqrt[%s]{a^%s\\sqrt{a}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^%s a^\\frac{1}{2}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^{%s+\\frac{1}{2}}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^{%s}}=a^\\frac{1}{2}\\cdot a^\\frac{1}{2}=a=a^m$.\\\\ \n'
                    'Vậy $m=1$.\\\\ \n'
                    '$\\dfrac{b^{%s}\\left( b^{%s}+b^{%s}\\right)}{b^{%s}\\left( b^{%s}+b^{%s}\\right)}=$'
                    '$\\dfrac{b^{%s}\\cdot b^{%s}+b^{%s}\\cdot b^{%s}}{b^{%s}\\cdot b^{%s}+b^{%s}\\cdot b^{%s}}=$'
                    '$\\dfrac{b+b^{2}}{b+1}=\\dfrac{b(1+b)}{b+1}=b=b^n$.\\\\ \n'
                    'Vậy $n=1$.\\\\ \n'
                    '$f(m-a)=f(1-a)=\\dfrac{%s^{1-a}}{%s^{1-a}+%s}=\\dfrac{%s^{1-a}%s^{a}}{\\left(%s^{1-a}+%s\\right)%s^{a}}=\\dfrac{%s}{%s+%s\\cdot %s^{a}}=\\dfrac{%s}{%s+ %s^{a}}$.\\\\ \n'
                    '$f(n-b)=f(1-b)=\\dfrac{%s^{1-b}}{%s^{1-b}+%s}=\\dfrac{%s^{1-b}%s^{b}}{\\left(%s^{1-b}+%s\\right)%s^{b}}=\\dfrac{%s}{%s+%s\\cdot %s^{b}}=\\dfrac{%s}{%s+ %s^{b}}$.\\\\ \n'
                    'Theo giả thiết $f(m-a)+f(n-b)=%s \\Rightarrow \\dfrac{%s}{%s+ %s^{a}}+\\dfrac{%s}{%s+ %s^{b}}=%s$  $(1)$.\\\\ \n'
                    'Ta lại có \\\\ \n'
                    '$f(a^m)=f(a)=\\dfrac{%s^a}{%s^a+%s}=\\dfrac{%s^a+%s-%s}{%s^a+%s}=1-\\dfrac{%s}{%s^a+%s}$.\\\\ \n'
                    '$f(b^n)=f(b)=\\dfrac{%s^b}{%s^b+%s}=\\dfrac{%s^b+%s-%s}{%s^b+%s}=1-\\dfrac{%s}{%s^b+%s}$.\\\\ \n'
                    'Khi đó  $f(a^m)+f(b^n)=1-\\dfrac{%s}{%s^a+%s}+1-\\dfrac{%s}{%s^b+%s}=2-\\left(\\dfrac{%s}{%s^a+%s}+\\dfrac{%s}{%s^b+%s}\\right)$  $(2)$. \\\\ \n'
                    'Thay $(1)$ vào $(2)$ ta có $f(a^m)+f(b^n)=2-%s=%s$.'



                %(latex(2*k+1),latex(k),latex(2*k+1),latex(k),latex(2*k+1),latex(k),latex(2*k+1),latex(Rational(2*k+1,2)),
                latex(bmu),latex(1-bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(-bmu1),
                    latex(bmu),latex(1-bmu),latex(bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(bmu1),latex(-bmu1),
                    latex(m),latex(m),latex(n), latex(m),latex(m),latex(m),latex(n),latex(m), latex(m),latex(m),latex(n),latex(m),latex(m1),latex(m1),latex(m),
                    latex(m),latex(m),latex(n), latex(m),latex(m),latex(m),latex(n),latex(m), latex(m),latex(m),latex(n),latex(m),latex(m1),latex(m1),latex(m),
                    latex(xk),latex(m1),latex(m1),latex(m),latex(m1),latex(m1),latex(m), latex(xk),
                    latex(m),latex(m),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n), latex(n),latex(m),latex(n),
                    latex(m),latex(m),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n), latex(n),latex(m),latex(n),
                    latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n), latex(xk), latex(2-xk),
                )
                )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(2-xk))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

