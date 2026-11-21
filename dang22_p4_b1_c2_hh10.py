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


def bt_dang22_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Cố định tên điểm theo chuẩn mẫu (không random điểm)
        diem_O, diem_A, diem_B = "O", "A", "B"
        
        # Random cặp góc phụ nhau để tạo góc vuông 90 độ tại A
        cap_goc = [(30, 60), (60, 30), (45, 45), (20, 70), (70, 20), (35, 55), (55, 35)]
        goc_bac, goc_nam = random.choice(cap_goc)
        
        # Random bộ 3 Pytago cho quãng đường OA, AB và độ dịch chuyển OB (km)
        bo_quang_duong = [(4, 3, 5), (3, 4, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13), (8, 15, 17), (15, 8, 17)]
        c_OA, c_AB, c_OB = random.choice(bo_quang_duong)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Một người đi bộ xuất phát từ trạm kiểm lâm $%s$, đi theo hướng Đông Bắc (hợp với hướng Bắc một góc $%s^\\circ$) được $%s\\,\\mathrm{km}$ đến trạm $%s$, sau đó chuyển hướng đi về phía Đông Nam (hợp với hướng Nam một góc $%s^\\circ$) được $%s\\,\\mathrm{km}$ đến trạm $%s$. Tính độ lớn vectơ độ dịch chuyển $\\overrightarrow{%s %s}$ của người đó.'
                         %(diem_O, str(goc_bac), str(c_OA), diem_A, str(goc_nam), str(c_AB), diem_B, diem_O, diem_B))
        
        # Nội dung lời giải
        loigiai = ('\\begin{itemize} \n'
                   '\\item Vẽ hệ trục tọa độ địa lý Đông - Tây - Nam - Bắc tại điểm $%s$. \n'
                   '\\item Tia $%s %s$ hợp với hướng Nam một góc $%s^\\circ$ về phía Tây; tia $%s %s$ hợp với hướng Nam một góc $%s^\\circ$ về phía Đông. \n'
                   '\\item Suy ra $\\widehat{%s %s %s} = %s^\\circ + %s^\\circ = 90^\\circ$, tức $\\triangle %s %s %s$ vuông tại $%s$. \n'
                   '\\item Độ lớn độ dịch chuyển: $|\\overrightarrow{%s %s}| = %s %s = \\sqrt{%s %s^2 + %s %s^2} = \\sqrt{%s^2 + %s^2} = %s\\,\\mathrm{km}$. \n'
                   '\\end{itemize}'
                   %(diem_A,
                     diem_A, diem_O, str(goc_bac), diem_A, diem_B, str(goc_nam),
                     diem_O, diem_A, diem_B, str(goc_bac), str(goc_nam), diem_O, diem_A, diem_B, diem_A,
                     diem_O, diem_B, diem_O, diem_B, diem_O, diem_A, diem_A, diem_B, str(c_OA), str(c_AB), str(c_OB)))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\loigiai{ \n' +str(loigiai)+'\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

