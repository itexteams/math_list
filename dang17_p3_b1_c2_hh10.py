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

def bt_dang17_p3_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sử dụng bộ ba số Pytago (3, 4, 5) nhân với một hệ số để số liệu đẹp (tròn trăm)
        he_so = randint(1, 4) * 100
        
        # Vận tốc máy bay 1 (Tây)
        v1 = 3 * he_so
        
        # Vận tốc máy bay 2 (Nam)
        v2 = 4 * he_so
        
        # Thời gian bay (từ 1 đến 3 giờ)
        t = randint(1, 3)
        
        # Quãng đường máy bay 1 đi được
        s1 = v1 * t
        
        # Quãng đường máy bay 2 đi được
        s2 = v2 * t
        
        # Khoảng cách giữa hai máy bay sau t giờ (định lý Pytago)
        khoang_cach = int(math.sqrt(s1**2 + s2**2))
        
        # Kết quả
        kq_str = str(khoang_cach)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Hai máy bay cùng cất cánh từ sân bay $O$: máy bay thứ nhất bay thẳng về hướng Tây với vận tốc $%s \\text{ km/h}$, máy bay thứ hai bay thẳng về hướng Nam với vận tốc $%s \\text{ km/h}$. Sau $%s$ giờ bay, khoảng cách giữa hai máy bay (chính là độ dài vectơ nối vị trí hai máy bay) là bao nhiêu $\\text{km}$?'
                         %(str(v1), str(v2), str(t)))
        
        # Nội dung lời giải
        loigiai = ('Giả sử sau $%s$ giờ, máy bay thứ nhất đến vị trí $A$, máy bay thứ hai đến vị trí $B$. \\\\'
                   'Quãng đường máy bay thứ nhất đi được là: $O A = %s \\cdot %s = %s \\text{ (km)}$. \\\\'
                   'Quãng đường máy bay thứ hai đi được là: $O B = %s \\cdot %s = %s \\text{ (km)}$. \\\\'
                   'Vì hướng Tây và hướng Nam vuông góc với nhau nên $\\Delta O A B$ vuông tại $O$. \\\\'
                   'Khoảng cách giữa hai máy bay sau $%s$ giờ chính là độ dài đoạn thẳng $A B$. \\\\'
                   'Áp dụng định lý Pytago trong tam giác vuông $O A B$, ta có: \\\\'
                   '$A B = \\sqrt{O A^2 + O B^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s + %s} = \\sqrt{%s} = %s \\text{ (km)}$.'
                   %(str(t), str(v1), str(t), str(s1), str(v2), str(t), str(s2), str(t), str(s1), str(s2), str(s1**2), str(s2**2), str(s1**2 + s2**2), kq_str))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

