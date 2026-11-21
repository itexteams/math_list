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


def bt_dang18_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Cố định tên điểm theo chuẩn mẫu (không random điểm)
        tam_O, D1, D2, diem_C, diem_H = "O", "A", "B", "C", "H"
        
        # Random độ dài dây cung AB (ví dụ: R*sqrt(3), R*sqrt(2), R)
        R = sp.Symbol('R', positive=True)
        cac_day_cung = [R * sp.sqrt(3), R * sp.sqrt(2), R]
        AB_expr = random.choice(cac_day_cung)
        
        # Tính toán các đại lượng bằng sympy
        AH_expr = AB_expr / 2
        AH_binh = AH_expr**2
        OH_binh = R**2 - AH_binh
        OH_expr = sp.sqrt(OH_binh)
        
        CH_expr = R + OH_expr
        CH_binh = sp.expand(CH_expr**2)
        CA_binh = sp.simplify(CH_binh + AH_binh)
        CA_expr = sp.sqrt(CA_binh)
        
        # Chuyển sang chuỗi LaTeX
        str_AB = latex(AB_expr)
        str_AH = latex(AH_expr)
        str_AH_binh = latex(AH_binh)
        str_OH = latex(OH_expr)
        str_CH = latex(CH_expr)
        str_CH_binh = latex(CH_binh)
        str_CA = latex(CA_expr)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Cho đường tròn $(%s; R)$ và dây cung $%s %s = %s$. Gọi $%s$ là điểm chính giữa cung lớn $%s %s$. Tính độ dài vectơ $\\overrightarrow{%s %s}$ và $\\overrightarrow{%s %s}$.'
                         %(tam_O, D1, D2, str_AB, diem_C, D1, D2, diem_C, D1, diem_C, tam_O))
        
        # Nội dung lời giải
        loigiai = ('\\begin{itemize} \n'
                   '\\item Dễ thấy $|\\overrightarrow{%s %s}| = %s %s = R$. \n'
                   '\\item Gọi $%s$ là trung điểm $%s %s \\Rightarrow %s %s \\perp %s %s$ và $%s %s = %s$. \n'
                   '\\item Tính $%s %s = \\sqrt{%s %s^2 - %s %s^2} = \\sqrt{R^2 - %s} = %s$. \n'
                   '\\item Vì $%s$ là điểm chính giữa cung lớn $%s %s$ nên $%s, %s, %s$ thẳng hàng theo thứ tự đó $\\Rightarrow %s %s = %s %s + %s %s = %s$. \n'
                   '\\item Trong $\\triangle %s %s %s$ vuông tại $%s$: $|\\overrightarrow{%s %s}| = %s %s = \\sqrt{%s %s^2 + %s %s^2} = \\sqrt{%s + %s} = %s$. \n'
                   '\\end{itemize}'
                   %(diem_C, tam_O, diem_C, tam_O,
                     diem_H, D1, D2, tam_O, diem_H, D1, D2, D1, diem_H, str_AH,
                     tam_O, diem_H, tam_O, D1, D1, diem_H, str_AH_binh, str_OH,
                     diem_C, D1, D2, diem_C, tam_O, diem_H, diem_C, diem_H, diem_C, tam_O, tam_O, diem_H, str_CH,
                     D1, diem_H, diem_C, diem_H, diem_C, D1, diem_C, D1, diem_C, diem_H, D1, diem_H, str_CH_binh, str_AH_binh, str_CA))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\loigiai{ \n' +str(loigiai)+'\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

