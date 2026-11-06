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


def bt_dang7_p3_b2_c6_ds10(self):
            # Khai báo biến
            a=randint(5,20)
            b=randint(5,20)
            c=math.comb(a+b,2)
            kq=Rational(a*b,c)
            kqs1=Rational(a*b,c+2)
            kqs2=Rational(a*b,c+1)
            kqs3=Rational(a*b,c+3)
            # Câu hỏi
            noidungcauhoi='''Trong một hội thảo quốc tế có $%s$ chuyên gia đến từ các nước ở châu Á, $%s$ chuyên gia đến từ các nước ở châu Âu. Chọn ngẫu nhiên $2$ chuyên gia vào ban tổ chức. Xác suất của biến cố “Chọn được $2$ chuyên gia ở hai châu lục khác nhau vào ban tổ chức” bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''%(latex(a),latex(b))
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
            loigiai=( 'Tổng số chuyên gia trong hội thảo đến từ các nước ở châu Á và châu Âu là $%s+%s=%s$ chuyên gia. \\\\ \n' 
                    'Mỗi cách chọn ngẫu nhiên $2$ chuyên gia vào ban tổ chức là một tổ hợp chập $2$ của $%s$ phần tử.  \\\\ \n'         
                    'Vậy không gian mẫu là số các tổ hợp chập $2$ của $%s$ phần tử, nên $n(\\Omega)=\\mathrm{C}_{%s}^2=%s$. \\\\ \n'
                    'Gọi $A$ là biến cố "Chọn được $2$ chuyên gia ở hai châu lục khác nhau vào ban tổ chức". \\\\ \n'
                    'Để chọn được $2$ chuyên gia ở $2$ châu lục khác nhau, ta chọn $1$ chuyên gia đến từ các nước ở châu Á và $1$ chuyên gia đến từ các nước ở châu Âu. Ta có: \\\\ \n '
                    'Chọn $1$ chuyên gia đến từ các nước ở châu Á trong $%s$ chuyên gia, có $%s$ cách chọn. \\\\ \n'
                    'Chọn $1$ chuyên gia đến từ các nước ở châu Âu trong $%s$ chuyên gia, có $%s$ cách chọn.\\\\ \n'
                    'Theo quy tắc nhân, ta có $%s \\cdot %s=%s$ cách chọn $2$ chuyên gia ở hai châu lục khác nhau. Do đó $n(A) =%s$.\\\\ \n'
                    'Vậy xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{n(A)}{n(\\Omega)}=%s \\approx %s$.'
                    %(latex(a),latex(b),latex(a+b),
                    latex(a+b),
                    latex(a+b),latex(a+b),latex(c),
                    latex(a),latex(a),
                    latex(b),latex(b),
                    latex(a),latex(b),latex(a*b),latex(a*b),
                    latex(kq),kqz)
                    )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

