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

def bt_dang13_p3_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sử dụng bộ ba số Pytago để kết quả là số nguyên
        # (ví dụ 3, 4, 5 nhân với một hệ số)
        he_so = randint(2, 6)
        
        # Khoảng cách về hướng Bắc
        ab = 3 * he_so
        
        # Khoảng cách về hướng Đông
        bc = 4 * he_so
        
        # Tính độ dài độ dịch chuyển AC bằng định lý Pytago
        ac = math.sqrt(ab**2 + bc**2)
        
        # Xử lý chuỗi kết quả (bỏ .0)
        kq_str = str(int(ac))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Một tàu thủy xuất phát từ cảng $A$, chạy thẳng $%s \\text{ km}$ về hướng Bắc đến điểm $B$, sau đó rẽ vuông góc chạy thẳng $%s \\text{ km}$ về hướng Đông đến đảo $C$. Độ lớn vectơ độ dịch chuyển $\\overrightarrow{A C}$ của tàu bằng bao nhiêu? (đơn vị: $\\text{km}$).'
                         %(str(ab), str(bc)))
        
        # Nội dung lời giải
        loigiai = ('Quãng đường tàu chạy từ cảng $A$ đến điểm $B$ được biểu diễn bởi vectơ $\\overrightarrow{A B}$ có độ dài $|\\overrightarrow{A B}| = A B = %s \\text{ km}$. \\\\'
                   'Quãng đường tàu chạy từ điểm $B$ đến đảo $C$ được biểu diễn bởi vectơ $\\overrightarrow{B C}$ có độ dài $|\\overrightarrow{B C}| = B C = %s \\text{ km}$. \\\\'
                   'Vì hướng Bắc vuông góc với hướng Đông nên $\\Delta A B C$ vuông tại $B$. \\\\'
                   'Áp dụng định lý Pytago trong tam giác vuông $A B C$, ta có: \\\\'
                   '$A C^2 = A B^2 + B C^2 = %s^2 + %s^2 = %s$. \\\\'
                   'Suy ra độ lớn vectơ độ dịch chuyển của tàu là $|\\overrightarrow{A C}| = A C = \\sqrt{%s} = %s \\text{ km}$.'
                   %(str(ab), str(bc), str(ab), str(bc), str(int(ab**2 + bc**2)), str(int(ab**2 + bc**2)), kq_str))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

