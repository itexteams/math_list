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


def bt_dang15_p4_b2_c4_ds12(self):
            # Khai báo biến
            a=randint(3,5)
            b=a-1
            l=2*b
            t1=a
            v1=b
            t2=randint(3,7)
            v2=randint(2,6)
            n=t2+v2+l
            n1=t1+v1
            n2=t2+v2
            p1=nsimplify(l/n)
            p2=nsimplify(1-l/n)
            q1=nsimplify(v1/n1)
            q2=nsimplify(v2/n2)
            pb=p1*q1+p2*q2
            number = Decimal(float(pb))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            lisdang1=['trắng','xanh','đỏ']
            m1=random.choice(lisdang1)
            lisdang2=['đen','vàng','cam']
            m2=random.choice(lisdang2)
            # Nội dung câu hỏi
            noidungcauhoi = ('Có hai hộp bóng bàn, các quả bóng bàn có cùng kích thước và hình dạng như nhau$zz$ hộp thứ nhất có $%s$ quả bóng màu %s và $%s$ quả bóng màu %s$zz$ '
                            'Hộp hai có $%s$ quả bóng bàn màu %s và $%s$ quả bóng màu %s$zz$ Lấy ngẫu nhiên $%s$ quả bóng bàn ở hộp thứ nhất bỏ vào hộp thứ hai rồi lấy ngẫu nhiên một quả bóng bàn '
                            'ở hộp thứ hai ra$zz$ Tính xác suất để lấy được quả bóng bàn màu %s từ hộp thứ hai (làm tròn kết quả đến hàng phần trăm)$zz$'
                            %(latex(t1),m1,latex(v1),m2,latex(t2),m1,latex(v2),m2,latex(l),m2
                            )
                            )
            # Nội dung lời giải
            loigiai = ('Xét các biến cố:\\\\ \n'
                        '\\hspace*{1cm} $A$: "Lấy được quả bóng bàn màu %s từ hộp thứ hai"\\\\ \n'
                    '\\hspace*{1cm} $H_{1}$: "Quả bóng lấy ra ở hộp thứ hai có nguồn gốc từ hộp thứ nhất";\\\\ \n'
                    '\\hspace*{1cm} $H_{2}$: "Quả bóng lấy ra ở hộp thứ hai có nguồn gốc từ hộp thứ hai"$zz$\\\\ \n'
                        'Ta có\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(H_{1})=\\dfrac{%s}{%s}$; $\\mathrm{P}(H_{2})=\\dfrac{%s}{%s}$; $\\mathrm{P}(A|H_{1})=\\dfrac{%s}{%s}$; $\\mathrm{P}(A|H_{2})=\\dfrac{%s}{%s}$$zz$\\\\ \n'
                        'Vậy xác suất để lấy được quả bóng bàn màu %s từ hộp thứ hai là\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(A)=\\mathrm{P}(H_{1})\\cdot\\mathrm{P}(A|H_{1})+\\mathrm{P}(H_{2})\\cdot\\mathrm{P}(A|H_{2})=\\dfrac{%s}{%s}\\cdot \\dfrac{%s}{%s}+\\dfrac{%s}{%s}\\cdot \\dfrac{%s}{%s}\\approx %s$$zz$'
                        %(m2,latex(l),latex(n),latex(n2),latex(n),latex(v1),latex(n1),latex(v2),latex(n2),m2,
                        latex(l),latex(n),latex(v1),latex(n1),latex(n2),latex(n),latex(v2),latex(n2),latex(kq)
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.').replace('pht','\\%')
            return content 

