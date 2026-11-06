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


def bt_dang5_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                t = symbols('t')
                a = randint(1,25)
                while a==1 or a==4 or a==9 or a==16 or a==25:
                    a = randint(1,25)
                t1 = sqrt(a)
                t0 = t1
                c=t/(t**2+a)
                cmax =t1/(t1**2+a)

                number = Decimal(float(t0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Một loại thuốc được dùng cho một bệnh nhân và nồng độ thuốc trong máu của bệnh nhân được giám sát bởi bác sĩ$zz$'
                                '  Biết rằng nồng độ thuốc trong máu của bệnh nhân sau khi tiêm vào cơ thể trong $t$ giờ được cho bởi công thức $c\\left(t\\right)=\\dfrac{t}{{{t}^{2}}+%s}$(mg/L)$zz$'
                                ' Hỏi sau khi tiêm thuốc bao lâu thì nồng độ thuốc trong máu của bệnh nhân cao nhất? (kết quả làm tròn đến hàng phần trăm)$zz$ \n'%(latex(a)))
                # Nội dung lời giải
                loigiai = ('''Xét hàm số $c\\left(t\\right)=\\dfrac{t}{{{t}^{2}}+%s},(t>0)$$zz$\\\\ \n'''
                        '''\\hspace*{1cm}${c}'\\left(t\\right)=\\dfrac{%s-{{t}^{2}}}{{{\\left( {{t}^{2}}+%s\\right)}^{2}}}$$zz$ \\\\ \n'''
                        '''\\hspace*{1cm}${c}'\\left(t\\right)=0 \\Leftrightarrow \\hoac{& t=%s \\\\& t=%s$zz$}$\\\\ \n'''
                        '''Bảng biến thiên \\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5]   \n'
                        '{$t$/1,$c\'(t)$/0$zz$7,$c(t)$/2$zz$1}   \n'
                        '{$0$,$%s$,$+\\infty$}   \n'
                        '\\tkzTabLine{,+,0,-,}   \n'
                        '\\tkzTabVar{-/0,+/$%s$,-/$0$}   \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        'Với $t=%s\\approx%s$ giờ thì nồng độ thuốc trong máu của bệnh nhân cao nhất$zz$'
                        %(latex(a),latex(a),latex(a),
                            latex(t1),latex(-t1),
                            latex(t1),
                            latex(cmax),latex(t1),latex(kq)))
            #Đáp án


            if dang=='1':
                t = symbols('t')
                a = random.choice([1,4,9,16,25])
                t1 = sqrt(a)
                t0 = t1
                c=t/(t**2+a)
                cmax =t1/(t1**2+a)

                number = Decimal(float(t0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Một loại thuốc được dùng cho một bệnh nhân và nồng độ thuốc trong máu của bệnh nhân được giám sát bởi bác sĩ$zz$'
                                '  Biết rằng nồng độ thuốc trong máu của bệnh nhân sau khi tiêm vào cơ thể trong $t$ giờ được cho bởi công thức $c\\left(t\\right)=\\dfrac{t}{{{t}^{2}}+%s}$(mg/L)$zz$'
                                ' Hỏi sau khi tiêm thuốc bao lâu thì nồng độ thuốc trong máu của bệnh nhân cao nhất? (kết quả làm tròn đến hàng phần trăm)$zz$ \n'%(latex(a)))
                # Nội dung lời giải
                loigiai = ('''Xét hàm số $c\\left(t\\right)=\\dfrac{t}{{{t}^{2}}+%s},(t>0)$$zz$\\\\ \n'''
                        '''\\hspace*{1cm}${c}'\\left(t\\right)=\\dfrac{%s-{{t}^{2}}}{{{\\left( {{t}^{2}}+%s\\right)}^{2}}}$$zz$ \\\\ \n'''
                        '''\\hspace*{1cm}${c}'\\left(t\\right)=0 \\Leftrightarrow \\hoac{& t=%s \\\\& t=%s$zz$}$\\\\ \n'''
                        '''Bảng biến thiên \\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5]   \n'
                        '{$t$/1,$c\'(t)$/0$zz$7,$c(t)$/2$zz$1}   \n'
                        '{$0$,$%s$,$+\\infty$}   \n'
                        '\\tkzTabLine{,+,0,-,}   \n'
                        '\\tkzTabVar{-/0,+/$%s$,-/$0$}   \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        'Với $t=%s,00$ giờ thì nồng độ thuốc trong máu của bệnh nhân cao nhất$zz$'
                        %(latex(a),latex(a),latex(a),
                            latex(t1),latex(-t1),
                            latex(t1),
                            latex(cmax),latex(kq)))
            #Đáp án

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

