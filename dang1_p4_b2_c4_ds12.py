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


def bt_dang1_p4_b2_c4_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                d1=randint(4,10)
                v1=randint(4,10)
                d2=randint(4,10)
                v2=randint(3,10)

                d21=d2+1
                v21=v2

                d22=d2
                v22=v2+1

                pa=Rational(d1,d1+v1)
                pb1=Rational(d21,d21+v21)
                pb2=Rational(d22,d22+v22)
                pc=Rational(1,d2+1)

                mau=pb1*pa+pb2*(1-pa)
                tu=pc*pb1*pa

                xs=tu/mau

                h1=xs

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Có hai chiếc hộp, hộp I có $%s$ quả bóng màu đỏ và $%s$ quả bóng màu vàng, hộp II có $%s$ quả '
                                'bóng màu đỏ và $%s$ quả bóng màu vàng, các quả bóng có cùng kích thước và khối lượng. Lấy ngẫu '
                                'nhiên một quả bóng từ hộp I bỏ vào hộp II. Sau đó, lấy ra ngẫu nhiên một quả bóng từ hộp II. Tính '
                                'xác suất để quả bóng được lấy ra từ hộp II là quả bóng được chuyển từ hộp I sang, biết rằng quả '
                                'bóng đó có màu đỏ (làm tròn kết quả đến hàng phần trăm).  \n'
                                %(latex(d1),latex(v1),latex(d2),latex(v2)
                                ))

                # Nội dung lời giải
                loigiai = ('Gọi biến cố A: Quả bóng lấy ra từ hộp I màu đỏ. \\\\ \n'
                        'Khi đó \\\\'
                        '\\hspace*{1cm} $P(A)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $P(\\bar{A})=1-P(A)=%s$. \\\\ \n'
                        'Gọi biến cố B: Quả bóng lấy ra từ hộp II màu đỏ, sau khi bỏ quả bóng từ hộp I vào. \\\\ \n'
                            'Trường hợp 1: Quả bóng lấy từ hộp I sang hộp II màu đỏ. \\\\'
                            '\\hspace*{1cm} $P(B|A)=%s$. \\\\ \n'
                            '\\hspace*{1cm} $P(\\bar{B}|A)=1-P(B|A)=%s$. \\\\ \n'
                            'Trường hợp 2: Quả bóng lấy từ hộp I sang hộp II không phải màu đỏ. \\\\'
                            '\\hspace*{1cm} $P(B|\\bar{A})=%s$. \\\\ \n'
                            '\\hspace*{1cm} $P(\\bar{B}|\\bar{A})=1-P(B|\\bar{A})=%s$. \\\\ \n'
                            'Gọi biến cố C: Quả bóng lấy ra từ hộp II là quả bóng từ một I và có màu đỏ. \\\\ \n'
                            'Khi đó \\\\'
                            '\\hspace*{1cm} $P(C|AB)=%s$. \\\\ \n'
                            '\\hspace*{1cm} $P(\\bar{C}|AB)=1-P(C|AB)=%s$. \\\\ \n'
                            'Gọi biến cố M: Quả bóng lấy ra từ hộp II là quả bóng được lấy từ hộp I. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $P(M|B)=\\dfrac{P(C|AB) \\cdot P(AB)}{P(B)}$. \\\\ \n'
                            'Trong đó \\\\ \n'
                            '\\hspace*{1cm} $P(B)=P(B|A) \\cdot P(A)+P(B|\\bar{A}) \\cdot P(\\bar{A})$. \\\\ \n'
                            '\\hspace*{2.1cm} $=%s \\cdot %s +%s \\cdot %s=%s$. \\\\ \n'
                            'Và \\\\ \n'
                            '\\hspace*{1cm} $P(C|AB) \\cdot P(AB)=P(C|AB) \\cdot P(B|A) \\cdot P(A)$. \\\\ \n'
                            '\\hspace*{4.45cm} $=%s \\cdot %s \\cdot %s =%s$. \\\\ \n'
                            'Suy ra \\\\ \n'
                            '\\hspace*{1cm} $P(M|B)=\\dfrac{%s}{%s}=%s \\approx %s$. \\\\ \n'
                            'Vậy xác suất thỏa mãn yêu cầu bài toán là $%s$.'

                        %(latex(pa),
                            latex(1-pa),
                            latex(pb1),
                            latex(1-pb1),
                            latex(pb2),
                                latex(1-pb2),
                            latex(pc),
                            latex(1-pc),
                            latex(pb1),latex(pa),latex(pb2),latex(1-pa),latex(mau),
                            latex(pc),latex(pb1),latex(pa),latex(tu),
                            latex(tu),latex(mau),latex(xs),latex(kq),
                            latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

