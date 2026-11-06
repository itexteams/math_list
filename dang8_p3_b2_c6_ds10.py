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


def bt_dang8_p3_b2_c6_ds10(self):
            # Khai báo biến
            a=randint(5,20)
            b=randint(5,20)
            c=randint(5,20)
            kq1=a*b*math.comb(c,2)
            kq2=a*c*math.comb(b,2)
            kq3=c*b*math.comb(a,2)
            kgm=math.comb(a+b+c,4)
            kq=Rational(kq1+kq2+kq3,kgm)
            kqs1=Rational(kq1+kq2+kq3+1,kgm)
            kqs2=Rational(kq1+kq2+kq3+2,kgm)
            kqs3=Rational(kq1+kq2+kq3-1,kgm)
            # Câu hỏi
            noidungcauhoi='''Có $%s$ bông hoa màu trắng, $%s$ bông hoa màu vàng và $%s$ bông hoa màu đỏ. Người ta chọn ra $4$ bông hoa từ các bông hoa trên. Xác suất của biến cố “Bốn bông hoa chọn ra có cả ba màu” bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''%(latex(a),latex(b),latex(c))
            # Các đáp án
            da_d = '\\True $%s$'%(latex(kq)) 
            da_s1 = '$%s$'%(latex(kqs1))   
            da_s2 = '$%s$'%(latex(kqs2)) 
            da_s3 = '$%s$'%(latex(kqs3)) 
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            h1=kq
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')
            loigiai=( 'Tổng số bông hoa là $%s+%s+%s=%s$. \\\\ \n' 
                    'Mỗi lần chọn $4$ bông hoa từ $%s$ bông hoa là một tổ hợp chập $4$ của $%s$ phần tử.\\\\ \n'
                    'Do đó, $n(\\Omega)=\\mathrm{C}_{%s}^4=%s$.  \\\\ \n'         
                    'Gọi $A$ là biến cố “Bốn bông hoa chọn ra có cả ba màu”. \\\\ \n'
                    'Khi đó xảy ra ba trường hợp sau: \\\\ \n'
                    '\\begin{itemize}  \n'
                    '\\item TH1. Chọn ra $1$ bông hoa màu trắng, $1$ bông hoa màu vàng và $2$ bông hoa màu đỏ. \\\\ \n '
                    'Có $%s$ cách chọn $1$ bông hoa màu trắng. \\\\ \n'
                    'Có $%s$ cách chọn $1$ bông hoa màu vàng.\\\\ \n'
                    'Có $\\mathrm{C}_{%s}^2$ cách chọn $2$ bông hoa màu đỏ.\\\\ \n'
                    'Theo quy tắc nhân, số cách chọn ra $1$ bông hoa màu trắng, $1$ bông hoa màu vàng và $2$ bông hoa màu đỏ là $%s \\cdot %s \\cdot \\mathrm{C}_{%s}^2=%s$. \\\\ \n'
                    '\\item TH2. Chọn ra $1$ bông hoa màu trắng, $2$ bông hoa màu vàng và $1$ bông hoa màu đỏ. \\\\ \n'
                    'Có $%s$ cách chọn $1$ bông hoa màu trắng. \\\\ \n'         
                    'Có $\\mathrm{C}_{%s}^2$ cách chọn $2$ bông hoa màu vàng.\\\\ \n'
                    'Có $%s$ cách chọn $1$ bông hoa màu đỏ.\\\\ \n'
                    'Theo quy tắc nhân, số cách chọn ra $1$ bông hoa màu trắng, $2$ bông hoa màu vàng và $1$ bông hoa màu đỏ là $%s \\cdot \\mathrm{C}_{%s}^2 \\cdot %s=%s$. \\\\ \n'
                    '\\item TH3. Chọn ra $2$ bông hoa màu trắng, $1$ bông hoa màu vàng và $1$ bông hoa màu đỏ. \\\\ \n'
                    'Có $\\mathrm{C}_{%s}^2$ cách chọn $2$ bông hoa màu trắng.\\\\ \n'
                    'Có $%s$ cách chọn $1$ bông hoa màu vàng. \\\\ \n'
                    'Có $%s$ cách chọn $1$ bông hoa màu đỏ.\\\\ \n'
                    'Theo quy tắc nhân, số cách chọn ra $2$ bông hoa màu trắng, $1$ bông hoa màu vàng và $1$ bông hoa màu đỏ là $\\mathrm{C}_{%s}^2 \\cdot %s \\cdot %s=%s$.\\\\ \n'
                    '\\end{itemize}  \n'
                    'Theo quy tắc cộng, số cách chọn $4$ bông hoa đủ cả ba màu là $%s+%s+%s=%s$.\\\\ \n'
                    'Do đó, số phần tử của biến cố $A$ là $n(A)=%s$. \\\\ \n'
                    'Vậy xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{n(A)}{n(\\Omega)}=%s \\approx %s$.'
                    %(latex(a),latex(b),latex(c),latex(a+b+c), #dòng 1
                    latex(a+b+c),latex(a+b+c),latex(a+b+c),latex(kgm), #dòng 2
                    latex(a),latex(b), #dòng 4, 5
                    latex(c),
                    latex(a),latex(b),latex(c),latex(kq1), #dòng 9
                    latex(a),latex(b),latex(c),
                    latex(a),latex(b),latex(c),latex(kq2),
                    latex(a),latex(b),latex(c),
                    latex(a),latex(b),latex(c),latex(kq3),
                    latex(kq1),latex(kq2),latex(kq3),latex(kq1+kq2+kq3),
                    latex(kq1+kq2+kq3),latex(kq),kqz
                        )
                    )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

