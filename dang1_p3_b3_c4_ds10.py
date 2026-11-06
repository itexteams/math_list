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


def bt_dang1_p3_b3_c4_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                m=symbols('m')

                a1=randint(1,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                a2=randint(1,9)
                b2=randint(-9,9)
                c2=randint(-9,9)
                k=randint(1,10)
                while b1**2-4*b2<=b1**2-4*b2-k or k==0:
                    a1=randint(1,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)
                    a2=randint(1,9)
                    b2=randint(-9,9)
                    c2=randint(-9,9)
                    k=randint(1,10)
                m1=Rational((b1**2-4*b2),(4*a2))
                m2=Rational((b1**2-4*b2-k**2),(4*a2))


                f1=x**2+b1*x
                fm=a2*m+b2

                # Tạo phân số từ số thực
                frac = Fraction(m2).limit_denominator()

                # Lấy tử số và mẫu số
                numerator = frac.numerator
                denominator = frac.denominator

                kq2=numerator+denominator
                # Câu hỏi
                noidungcauhoi = ('Giá trị của tham số $m$ để tập nghiệm của bất phương trình $%s+%s\\le0$ có độ dài bằng $%s$. Biết rằng $m=\\dfrac{a}{b}$ với $\\dfrac{a}{b}$ tối giản, $a, b$ là các số nguyên và $b>0$. Tổng $a+b$ bằng bao nhiêu?'
                                %(latex(f1),latex(fm),latex(k),)
                                )


                # Nội dung lời giải
                loigiai=( 'Đặt $f(x)=%s+%s$ vì $a=1>0$ nên để thỏa mãn yêu cầu bài toán thì phương trình $%s+%s=0$ có hai nghiệm $x_1;x_2$ thỏa mãn $|x_1-x_2|=%s$. Với $\\heva{& x_1+x_2=%s\\\\ & x_1x_2=%s}$\\\\ \n'
                        ' Hay $\\heva{&\\Delta >0\\\\ & (x_1-x_2)^2=%s} \\Leftrightarrow \\heva{&(%s)^2-4\\cdot 1\\cdot (%s) >0\\\\ & (x_1+x_2)^2-4x_1x_2-%s=0} \\Leftrightarrow \\heva{& m <%s\\\\ & (%s)^2-4(%s)-%s=0}$.\\\\ \n'
                        '$\\Leftrightarrow \\heva{&m <%s\\\\ & m=%s}\\Leftrightarrow m=%s$. Khi đó $a=%s;b=%s$. Vậy $a+b=%s$. '

                        %(latex(f1),latex(fm),latex(f1),latex(fm),latex(k),latex(-b1),latex(fm),
                        latex(k**2),latex(b1),latex(fm),latex(k**2),latex(m1),latex(-b1),latex(fm),latex(k**2),
                        latex(m1),latex(m2),latex(m2),latex(numerator),latex(denominator),latex(kq2),)
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq2))

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                m=symbols('m')

                a1=randint(1,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                a2=randint(1,9)
                b2=randint(-9,9)
                c2=randint(-9,9)
                k=randint(1,10)
                while b1**2-4*b2<=b1**2-4*b2-k or k==0:
                    a1=randint(1,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)
                    a2=randint(1,9)
                    b2=randint(-9,9)
                    c2=randint(-9,9)
                    k=randint(1,10)
                m1=Rational((b1**2-4*b2),(4*a2))
                m2=Rational((b1**2-4*b2-k**2),(4*a2))


                f1=-x**2+b1*x
                fm=-a2*m-b2

                # Tạo phân số từ số thực
                frac = Fraction(m2).limit_denominator()

                # Lấy tử số và mẫu số
                numerator = frac.numerator
                denominator = frac.denominator

                kq2=numerator+denominator
                # Câu hỏi
                noidungcauhoi = ('Giá trị của tham số $m$ để tập nghiệm của bất phương trình $%s+%s\\ge0$ có độ dài bằng $%s$. Biết rằng $m=\\dfrac{a}{b}$ với $\\dfrac{a}{b}$ tối giản, $a, b$ là các số nguyên và $b>0$. Tổng $a+b$ bằng bao nhiêu?'
                                %(latex(f1),latex(fm),latex(k),)
                                )


                # Nội dung lời giải
                loigiai=( 'Đặt $f(x)=%s+%s$ vì $a=-1<0$ nên để thỏa mãn yêu cầu bài toán thì phương trình $%s+%s=0$ có hai nghiệm $x_1;x_2$ thỏa mãn $|x_1-x_2|=%s$. Với $\\heva{& x_1+x_2=%s\\\\ & x_1x_2=%s}$.\\\\ \n'
                        ' Hay $\\heva{&\\Delta >0\\\\ & (x_1-x_2)^2=%s} \\Leftrightarrow \\heva{&(%s)^2-4\\cdot (-1)\\cdot (%s) >0\\\\ & (x_1+x_2)^2-4x_1x_2-%s=0} \\Leftrightarrow \\heva{& m <%s\\\\ & (%s)^2-4(%s)-%s=0}$.\\\\ \n'
                        '$\\Leftrightarrow \\heva{&m <%s\\\\ & m=%s}\\Leftrightarrow m=%s$. Khi đó $a=%s;b=%s$. Vậy $a+b=%s$.'

                        %(latex(f1),latex(fm),latex(f1),latex(fm),latex(k),latex(b1),latex(-fm),
                        latex(k**2),latex(b1),latex(fm),latex(k**2),latex(m1),latex(b1),latex(-fm),latex(k**2),
                        latex(m1),latex(m2),latex(m2),latex(numerator),latex(denominator),latex(kq2),)
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq2))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+').replace('21\\vec', '21f\\vec').replace('51\\vec', '51f\\vec').replace('81\\vec', '81f\\vec').replace('1\\vec', '\\vec').replace('21f\\vec', '21\\vec').replace('51f\\vec', '51\\vec').replace('81f\\vec', '81\\vec')
            return content

