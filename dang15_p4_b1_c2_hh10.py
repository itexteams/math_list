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


def bt_dang15_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Cố định tên điểm theo chuẩn mẫu (không random điểm)
        D1, D2, D3, D4, D5, D6 = "A", "B", "C", "D", "E", "F"
        tam_O, diem_M = "O", "M"
        
        # Random độ dài cạnh lục giác đều là số chẵn để tính toán đẹp
        canh_a = randint(1, 5) * 2
        nua_canh = Rational(canh_a, 2)
        
        # Tính AM^2 = AF^2 + FM^2 - 2*AF*FM*cos(120) = a^2 + a^2/4 + a^2/2 = 7a^2/4
        AM_binh = Rational(7 * canh_a**2, 4)
        AM_val = sp.sqrt(AM_binh)
        
        # Tính BM^2 = BF^2 + FM^2 = 3a^2 + a^2/4 = 13a^2/4
        BM_binh = Rational(13 * canh_a**2, 4)
        BM_val = sp.sqrt(BM_binh)
        
        # Random câu hỏi tính tổng |AM| + |BM| để ra một con số cụ thể cho dạng trả lời ngắn
        tong_val = AM_val + BM_val
        number = Decimal(float(tong_val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Cho lục giác đều $%s %s %s %s %s %s$ cạnh bằng $%s$ có tâm $%s$. Gọi $%s$ là trung điểm của $%s %s$. Tính tổng độ dài $|\\overrightarrow{%s %s}| + |\\overrightarrow{%s %s}|$ (kết quả làm tròn đến hàng phần trăm).'
                         %(D1, D2, D3, D4, D5, D6, str(canh_a), tam_O, diem_M, D5, D6, D1, diem_M, D2, diem_M))
        
        # Nội dung lời giải
        loigiai = ('\\begin{itemize} \n'
                   '\\item Trong lục giác đều cạnh $%s$, ta có $\\widehat{%s %s %s} = 120^\\circ$, $%s %s = %s$, $%s %s = %s$. \\\\ \n'
                   '\\item Áp dụng định lí Côsin trong $\\triangle %s %s %s$: \\\\ \n'
                   '$%s %s^2 = %s %s^2 + %s %s^2 - 2 \\cdot %s %s \\cdot %s %s \\cdot \\cos 120^\\circ = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(-\\dfrac{1}{2}\\right) = %s \\Rightarrow |\\overrightarrow{%s %s}| = %s$. \\\\ \n'
                   '\\item Vì $%s %s \\perp %s %s$ và $%s %s = %s$, áp dụng định lí Pytago trong $\\triangle %s %s %s$ vuông tại $%s$: \\\\ \n'
                   '$|\\overrightarrow{%s %s}| = %s %s = \\sqrt{%s %s^2 + %s %s^2} = \\sqrt{%s + %s} = %s$. \\\\ \n'
                   '\\item Vậy $|\\overrightarrow{%s %s}| + |\\overrightarrow{%s %s}| = %s + %s = %s \\approx %s$. \n'
                   '\\end{itemize}'
                   %(str(canh_a), D1, D6, D5, D1, D6, str(canh_a), D6, diem_M, latex(nua_canh),
                     D1, D6, diem_M, D1, diem_M, D1, D6, D6, diem_M, D1, D6, D6, diem_M, str(canh_a), latex(nua_canh), str(canh_a), latex(nua_canh), latex(AM_binh), D1, diem_M, latex(AM_val),
                     D2, D6, D5, D6, D2, D6, latex(canh_a * sp.sqrt(3)), D2, D6, diem_M, D6, D2, diem_M, D2, diem_M, D2, D6, D6, diem_M, str(3 * canh_a**2), latex(nua_canh**2), latex(BM_val),
                     D1, diem_M, D2, diem_M, latex(AM_val), latex(BM_val), latex(tong_val), kq_str))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

