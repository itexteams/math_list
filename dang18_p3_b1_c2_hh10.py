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
from decimal import Decimal, ROUND_HALF_UP

def bt_dang18_p3_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sử dụng bộ ba số Pytago để kết quả là số nguyên
        pythagorean_triples = [(5, 12, 13), (3, 4, 5), (8, 15, 17), (7, 24, 25)]
        triple = random.choice(pythagorean_triples)
        he_so = randint(1, 3)
        
        # Khoảng cách thẳng đứng
        h1 = triple[1] * he_so
        
        # Khoảng cách ngang
        h2 = triple[0] * he_so
        
        # Khối lượng bê tông (random số thập phân)
        m = round(random.uniform(1.0, 5.0), 1)
        m_str = str(m).replace('.', ',')
        
        # Tính độ lớn độ dịch chuyển tổng cộng (định lý Pytago)
        d = triple[2] * he_so
        
        # Kết quả
        kq_str = str(d)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Một cần cẩu nâng một khối bê tông nặng $%s \\text{ tấn}$ theo phương thẳng đứng lên cao $%s \\text{ m}$, sau đó quay ngang để dịch chuyển khối bê tông theo phương ngang một đoạn $%s \\text{ m}$. Độ lớn vectơ độ dịch chuyển tổng cộng của khối bê tông từ vị trí ban đầu đến vị trí cuối cùng bằng bao nhiêu? (đơn vị: $\\text{m}$).'
                         %(m_str, str(h1), str(h2)))
        
        # Nội dung lời giải
        loigiai = ('Gọi $A$ là vị trí ban đầu của khối bê tông. \\\\'
                   'Quá trình nâng khối bê tông theo phương thẳng đứng lên cao $%s \\text{ m}$ được biểu diễn bởi vectơ $\\overrightarrow{A B}$ có độ dài $A B = %s \\text{ m}$. \\\\'
                   'Quá trình dịch chuyển khối bê tông theo phương ngang một đoạn $%s \\text{ m}$ được biểu diễn bởi vectơ $\\overrightarrow{B C}$ có độ dài $B C = %s \\text{ m}$. \\\\'
                   'Vectơ độ dịch chuyển tổng cộng của khối bê tông từ vị trí ban đầu đến vị trí cuối cùng là $\\overrightarrow{A C}$. \\\\'
                   'Vì phương thẳng đứng vuông góc với phương ngang nên tam giác $A B C$ vuông tại $B$. \\\\'
                   'Áp dụng định lý Pytago trong tam giác vuông $A B C$, ta có: \\\\'
                   '$A C = \\sqrt{A B^2 + B C^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s + %s} = \\sqrt{%s} = %s \\text{ (m)}$.'
                   %(str(h1), str(h1), str(h2), str(h2), str(h1), str(h2), str(h1**2), str(h2**2), str(h1**2 + h2**2), kq_str))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

