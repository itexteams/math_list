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

def bt_dang21_p3_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sử dụng bộ ba số Pytago để kết quả là số nguyên
        pythagorean_triples = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41)]
        triple = random.choice(pythagorean_triples)
        he_so = randint(1, 3)
        
        # Số ô di chuyển sang phải (hoặc trái)
        x_move = triple[0] * he_so
        
        # Số ô di chuyển lên trên (hoặc xuống)
        y_move = triple[1] * he_so
        
        # Tính độ dài vectơ dịch chuyển
        distance = triple[2] * he_so
        
        # Random hướng di chuyển để bài toán đa dạng hơn
        huong_x = random.choice(["sang phải", "sang trái"])
        huong_y = random.choice(["đi lên trên", "đi xuống dưới"])
        
        # Kết quả
        kq_str = str(distance)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Trong một game chiến thuật, nhân vật xuất phát từ tọa độ gốc, di chuyển %s $%s$ ô rồi %s $%s$ ô để nhặt vật phẩm. Nếu mỗi ô vuông có cạnh bằng $1$ đơn vị, độ dài vectơ dịch chuyển của nhân vật bằng bao nhiêu đơn vị?'
                         %(huong_x, str(x_move), huong_y, str(y_move)))
        
        # Nội dung lời giải
        loigiai = ('Giả sử vị trí xuất phát của nhân vật là gốc tọa độ $O(0; 0)$ trên mặt phẳng tọa độ $Oxy$. \\\\'
                   'Nhân vật di chuyển %s $%s$ ô, tức là di chuyển dọc theo trục $Ox$ một đoạn có độ dài là $%s$ đơn vị. \\\\'
                   'Sau đó nhân vật %s $%s$ ô, tức là di chuyển song song với trục $Oy$ một đoạn có độ dài là $%s$ đơn vị. \\\\'
                   'Vị trí cuối cùng của nhân vật là điểm $A$. \\\\'
                   'Quãng đường di chuyển theo trục $Ox$ và $Oy$ tạo thành hai cạnh góc vuông của một tam giác vuông với cạnh huyền là đoạn thẳng $OA$. \\\\'
                   'Áp dụng định lý Pytago, độ dài vectơ dịch chuyển của nhân vật là độ dài đoạn thẳng $OA$: \\\\'
                   '$|\\overrightarrow{OA}| = OA = \\sqrt{%s^2 + %s^2} = \\sqrt{%s + %s} = \\sqrt{%s} = %s$ (đơn vị).'
                   %(huong_x, str(x_move), str(x_move), huong_y, str(y_move), str(y_move), str(x_move), str(y_move), str(x_move**2), str(y_move**2), str(x_move**2 + y_move**2), kq_str))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

