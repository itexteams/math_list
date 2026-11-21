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


def bt_dang5_p3_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Random số điểm từ 4 đến 8
        n = randint(4, 8)
        
        # Tạo danh sách các điểm bằng các chữ cái in hoa
        points = [chr(65 + i) for i in range(n)]
        points_str = ", ".join(points)
        
        # Chọn ngẫu nhiên 2 điểm đầu tiên để làm vectơ hướng
        p1 = points[0]
        p2 = points[1]
        
        # Số lượng các vectơ cùng hướng = nC2
        ans = n * (n - 1) // 2
        
        # Liệt kê các vectơ thỏa mãn
        vector_list = []
        for i in range(n):
            for j in range(i + 1, n):
                vector_list.append(f"\\overrightarrow{{{points[i]}{points[j]}}}")
        
        vector_str = ", ".join(vector_list)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Cho $%s$ điểm phân biệt thẳng hàng theo thứ tự $%s$. Có tất cả bao nhiêu vectơ khác $\\overrightarrow{0}$ cùng hướng với vectơ $\\overrightarrow{%s%s}$ và có điểm đầu, điểm cuối lấy từ $%s$ điểm đã cho?'
                         %(str(n), points_str, p1, p2, str(n)))
        
        # Nội dung lời giải
        loigiai = ('Vì $%s$ điểm đã cho cùng nằm trên một đường thẳng và được xếp theo một thứ tự cố định, nên các vectơ cùng hướng với $\\overrightarrow{%s%s}$ là các vectơ có điểm đầu đứng trước điểm cuối trong dãy thứ tự đã cho. \\\\'
                   'Số lượng vectơ như vậy bằng số cách chọn ra $2$ điểm bất kỳ từ $%s$ điểm đã cho, vì với mỗi $2$ điểm chọn ra, chỉ có duy nhất một cách ghép chúng lại để tạo thành vectơ cùng hướng với $\\overrightarrow{%s%s}$. \\\\'
                   'Do đó, số vectơ thỏa mãn là tổ hợp chập $2$ của $%s$ phần tử: $C_{%s}^2 = %s$. \\\\'
                   'Các vectơ đó là: $%s$.'
                   %(str(n), p1, p2, str(n), p1, p2, str(n), str(n), str(ans), vector_str))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(str(ans))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

