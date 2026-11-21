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


def bt_dang19_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Cố định tên điểm theo chuẩn mẫu (không random điểm)
        diem_O, diem_A, diem_B = "O", "A", "B"
        diem_A1, diem_P1, diem_B1 = "A'", "P'", "B'"
        
        # Random trọng lượng P (chọn số chẵn chia hết cho 2 để kết quả đẹp)
        P_val = randint(2, 20) * 10
        
        # Random góc hợp bởi dây OA và phương ngang (30, 45, 60 độ)
        cac_goc = [30, 45, 60]
        goc_ngang = random.choice(cac_goc)
        goc_thang_dung = 90 - goc_ngang
        
        # Tính toán bằng sympy
        goc_rad = sp.rad(goc_thang_dung)
        cos_val = sp.cos(goc_rad)
        sin_val = sp.sin(goc_rad)
        
        T1_val = P_val * cos_val
        T2_val = P_val * sin_val
        
        # Hình vẽ TikZ biểu diễn các vectơ lực tác dụng lên vật (nét 1pt, điểm 1pt, màu black)
        hinh_ve = ('\\begin{center}\n'
                   '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                   '\\coordinate (O) at (0,0);\n'
                   '\\coordinate (A) at (-2.5,1.44);\n'
                   '\\coordinate (B) at (1.5,2.6);\n'
                   '\\coordinate (P1) at (0,-2.5);\n'
                   '\\coordinate (A1) at (-1.25,0.72);\n'
                   '\\coordinate (B1) at (1.25,2.16);\n'
                   '\\coordinate (H1) at (-2.5,0);\n'
                   '\\coordinate (H2) at (2.5,0);\n'
                   '\\draw[line width=1pt] (A)--(O)--(B);\n'
                   '\\draw[line width=1pt, dashed] (H1)--(H2) (A1)--(0,2.88)--(B1);\n'
                   '\\draw[line width=1pt, ->] (O)--(A1) node[below left] {$\\overrightarrow{T_1}$};\n'
                   '\\draw[line width=1pt, ->] (O)--(B1) node[below right] {$\\overrightarrow{T_2}$};\n'
                   '\\draw[line width=1pt, ->] (O)--(P1) node[below] {$\\overrightarrow{P}$};\n'
                   '\\draw[line width=1pt, ->] (O)--(0,2.88) node[above] {$\\overrightarrow{F}_{hl}$};\n'
                   '\\fill (O) circle (1pt) node[below left] {$O$};\n'
                   '\\fill (A) circle (1pt) node[above left] {$A$};\n'
                   '\\fill (B) circle (1pt) node[above right] {$B$};\n'
                   '\\fill (A1) circle (1pt) node[above left] {$A\'$};\n'
                   '\\fill (B1) circle (1pt) node[right] {$B\'$};\n'
                   '\\fill (P1) circle (1pt) node[left] {$P\'$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Một vật có trọng lượng $P = %s\\,\\mathrm{N}$ được treo đứng yên bởi hai sợi dây nhẹ $%s %s$ và $%s %s$ buộc vào trần nhà sao cho $\\widehat{%s %s %s} = 90^\\circ$ và dây $%s %s$ hợp với phương ngang một góc $%s^\\circ$. Vẽ hình biểu diễn các vectơ lực tác dụng lên vật và tính độ lớn của các vectơ lực căng dây $\\overrightarrow{T_1}$ (trên $%s %s$) và $\\overrightarrow{T_2}$ (trên $%s %s$).'
                         %(str(P_val), diem_O, diem_A, diem_O, diem_B, diem_A, diem_O, diem_B, diem_O, diem_A, str(goc_ngang), diem_O, diem_A, diem_O, diem_B))
        
        # Nội dung lời giải
        loigiai = ('%s'
                   '\\begin{itemize} \n'
                   '\\item Vật đứng yên nên hợp lực của $\\overrightarrow{T_1}$ và $\\overrightarrow{T_2}$ cân bằng với trọng lực $\\overrightarrow{P}$ (có độ lớn $%s\\,\\mathrm{N}$, hướng thẳng đứng xuống dưới). \n'
                   '\\item Dựng hình chữ nhật lực $%s %s %s %s$ với đường chéo $%s %s = P = %s\\,\\mathrm{N}$. \n'
                   '\\item Góc giữa $%s %s$ và phương thẳng đứng là $90^\\circ - %s^\\circ = %s^\\circ$. \n'
                   '\\item Tính được: $T_1 = P \\cdot \\cos %s^\\circ = %s \\cdot %s = %s\\,\\mathrm{N}$; $T_2 = P \\cdot \\sin %s^\\circ = %s \\cdot %s = %s\\,\\mathrm{N}$. \n'
                   '\\end{itemize}'
                   %(hinh_ve,
                     str(P_val),
                     diem_O, diem_A1, diem_P1, diem_B1, diem_O, diem_P1, str(P_val),
                     diem_O, diem_A, str(goc_ngang), str(goc_thang_dung),
                     str(goc_thang_dung), str(P_val), latex(cos_val), latex(T1_val),
                     str(goc_thang_dung), str(P_val), latex(sin_val), latex(T2_val)))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\loigiai{ \n' +str(loigiai)+'\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

