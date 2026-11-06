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


def bt_dang1_p3_b3_c2_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lish=['Đông','Tây','Nam','Bắc']
                hg1=random.choice(lish)
                lish.remove(hg1)
                hg2=random.choice(lish)

                lisv=[30,35,40,45,50,55,60,65]
                v1=random.choice(lisv)
                lisv.remove(v1)
                v2=random.choice(lisv)

                lis1=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                m=random.choice(lis1)
                lis1.remove(m)
                n=random.choice(lis1)

                # Tử số và mẫu số
                numerator = v2
                denominator = v1

                # Tìm ước chung lớn nhất (GCD)
                gcd = math.gcd(numerator, denominator)

                # Chia cả tử số và mẫu số cho GCD
                simplified_numerator = numerator // gcd
                simplified_denominator = denominator // gcd

                simplified_fraction = (simplified_numerator, simplified_denominator)

                a=simplified_numerator
                b=simplified_denominator

                p=m*a+n*b

                h1=p        
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một người đi xe máy từ hướng %s sang hướng %s với vận tốc $%s$ km/h được biểu thị bởi vectơ $\\vec{v_1}$, một người khác đi xe máy từ hướng %s sang hướng %s với vận tốc $%s$ km/h được biểu thị bởi vectơ $\\vec{v_2}$. Biết $\\vec{v_2}=-\\dfrac{a}{b} \\vec{v_1}$ với $a, b \\in \\mathbb{Z}, b \\ne 0$ và $\\dfrac{a}{b}$ là phân số tối giản. '
                                'Giá trị của biểu thức $P=%sa+%sb$ bằng bao nhiêu?'
                                %(str(hg1),str(hg2),latex(v1),str(hg2),str(hg1),latex(v2),latex(m),latex(n)
                                ))

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} Vectơ $\\vec{v_2}$ ngược hướng với vectơ $\\vec{v_1}$ và có độ lớn bằng $\\dfrac{%s}{%s}=%s$ vectơ $\\vec{v_1}$. \\\\ \n'
                        '\\hspace*{1cm} Do đó $\\vec{v_2}=-%s \\vec{v_1}$.\\\\ \n'
                        '\\hspace*{1cm} Suy ra $a=%s$ và $b=%s$. \\\\ \n' 
                        'Vậy $P=%s a+%s b=%s \\cdot %s+%s \\cdot %s=%s$.'
                        %(latex(v2),latex(v1),latex(Rational(a,b)),
                            latex(Rational(v2,v1)),
                            latex(a),latex(b),
                            latex(m),latex(n),
                            latex(m),latex(a),latex(n),latex(b),latex(p)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(p))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

