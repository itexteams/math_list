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


def bt_dang11_p1_b4_c3_hh10(self):
            # Khai báo biến
            x = symbols("x")
            y = symbols('y')

            k = randint(1,9)
            c = 5*k
            b1 = [3*k,4*k]
            b = random.choice(b1)
            if b==3*k:
                a=4*k
            else:
                a=3*k

            list_tieudiem = [c,-c]
            tieudiem = random.choice(list_tieudiem)

            pt = Eq(x**2/a**2-y**2/b**2,1)
            pt1 = Eq(x**2/(a+1)**2-y**2/b**2,1)
            pt2 = Eq(x**2/a**2-y**2/(b+1)**2,1)
            pt3 = Eq(x**2/(a+2)**2-y**2/b**2,1)

            list_xm = [c,-c,a,-a]
            x_m = random.choice(list_xm)
            y1 = Rational(b*sqrt(x_m**2-a**2),a)
            list_ym = [y1,-y1]
            y_m = random.choice(list_ym)
            # Câu hỏi
            noidungcauhoi='''Trong mặt phẳng tọa độ $(Oxy)$, cho hypebol có một tiêu điểm $F(%s;0)$ và đi qua điểm $M(%s;%s)$. Phương trình chính tắc của hypebol là''' %(latex(tieudiem), latex(x_m), latex(y_m))
            # Các đáp án
            da_d = '\\True $(H):%s$' %(latex(pt))
            da_s1 = '$(H):%s$' %(latex(pt1))
            da_s2 = '$(H):%s$' %(latex(pt2))
            da_s3 = '$(H):%s$' %(latex(pt3))  

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=( 'Tiêu điểm của hypebol là $F(%s;0)$ nên suy ra $c=%s$. \\\\'
                    'Phương trình chính tắc của hypebol có dạng $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1$ với $b^2=c^2-a^2=%s-a^2$.\\\\'
                    'Và vì hypebol đi qua điểm $M(%s;%s)$ nên thay $x=%s$ và $y=%s$ vào phương trình ta có \\\\'
                    '$\\dfrac{%s}{a^2}-\\dfrac{%s}{%s-a^2}=1$. \\\\'
                    'Giải phương trình trên với điều kiện $0<a^2<%s$ ta được $a^2=%s$. \\\\'
                    'Suy ra $b^2=c^2-a^2=%s-%s=%s$.\\\\'
                    'Vậy phương trình chính tắc của hypebol là $(H):%s$.'
                    ) %(latex(tieudiem), latex(c), latex(c**2), latex(x_m), latex(y_m), latex(x_m), latex(y_m), latex(x_m**2), latex(y_m**2), latex(c**2), latex(c**2), latex(a**2), latex(c**2), latex(a**2), latex(b**2), latex(pt))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('+-','-').replace('--','+').replace('-+','-')
            return content 

