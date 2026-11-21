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


def bt_dang16_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Cố định tên điểm theo chuẩn mẫu (không random điểm)
        T1, T2, T3 = "A", "B", "C"
        diem_G, diem_M = "G", "M"
        
        # Random độ dài 2 cạnh AB, AC và góc BAC (chọn bộ số sao cho BC nguyên)
        bo_canh_60 = [(5, 8, 7), (3, 8, 7), (7, 8, 13), (5, 7, 13), (8, 15, 13), (7, 15, 13)]
        c_AB, c_AC, c_BC = random.choice(bo_canh_60)
        
        # Tính công thức đường trung tuyến: AM^2 = (2(AB^2 + AC^2) - BC^2) / 4
        tu_so = 2 * (c_AB**2 + c_AC**2) - c_BC**2
        AM_binh = Rational(tu_so, 4)
        AM_val = sp.sqrt(AM_binh)
        
        # Tính độ dài AG = 2/3 AM
        AG_val = Rational(2, 3) * AM_val
        
        # Làm tròn kết quả đến hàng phần trăm
        number = Decimal(float(AG_val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Cho tam giác $%s %s %s$ có $%s %s = %s, %s %s = %s, \\widehat{%s %s %s} = 60^\\circ$. Gọi $%s$ là trọng tâm của tam giác $%s %s %s$. Tính độ dài vectơ $\\overrightarrow{%s %s}$ (kết quả làm tròn đến hàng phần trăm).'
                         %(T1, T2, T3, T1, T2, str(c_AB), T1, T3, str(c_AC), T2, T1, T3, diem_G, T1, T2, T3, T1, diem_G))
        
        # Nội dung lời giải
        loigiai = ('\\begin{itemize} \n'
                   '\\item Gọi $%s$ là trung điểm $%s %s$. Áp dụng định lí Côsin trong $\\triangle %s %s %s$: \\\\ \n'
                   '$%s %s^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos 60^\\circ = %s + %s - %s = %s \\Rightarrow %s %s = %s$. \\\\ \n'
                   '\\item Công thức đường trung tuyến: \\\\ \n'
                   '$%s %s^2 = \\dfrac{2(%s %s^2 + %s %s^2) - %s %s^2}{4} = \\dfrac{2(%s + %s) - %s}{4} = %s \\Rightarrow %s %s = %s$. \\\\ \n'
                   '\\item Độ dài $|\\overrightarrow{%s %s}| = %s %s = \\dfrac{2}{3} %s %s = %s \\approx %s$. \n'
                   '\\end{itemize}'
                   %(diem_M, T2, T3, T1, T2, T3, 
                     T2, T3, str(c_AB), str(c_AC), str(c_AB), str(c_AC), str(c_AB**2), str(c_AC**2), str(c_AB * c_AC), str(c_BC**2), T2, T3, str(c_BC),
                     T1, diem_M, T1, T2, T1, T3, T2, T3, str(c_AB**2), str(c_AC**2), str(c_BC**2), latex(AM_binh), T1, diem_M, latex(AM_val),
                     T1, diem_G, T1, diem_G, T1, diem_M, latex(AG_val), kq_str))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

