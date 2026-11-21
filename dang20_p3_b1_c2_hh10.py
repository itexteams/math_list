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

def bt_dang20_p3_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Random các thông số sao cho kết quả căn bậc 2 là số nguyên
        # Sử dụng các bộ số x, y, z sao cho x^2 + y^2 + z^2 là một số chính phương
        # Một số bộ quen thuộc: (3, 4, 12) -> 13; (2, 3, 6) -> 7; (1, 2, 2) -> 3; (4, 12, 3) -> 13
        bo_so = random.choice([(3, 4, 12), (2, 3, 6), (1, 2, 2), (4, 12, 3), (6, 8, 24), (20, 15, 60)])
        he_so = randint(1, 10) * 10
        
        # Khoảng cách thẳng đứng (trục z)
        h = bo_so[0] * he_so
        
        # Khoảng cách ngang hướng Đông (trục x)
        d_dong = bo_so[1] * he_so
        
        # Khoảng cách ngang hướng Bắc (trục y)
        d_bac = bo_so[2] * he_so
        
        # Tính độ lớn độ dịch chuyển (đường chéo hình hộp chữ nhật)
        s = int(math.sqrt(h**2 + d_dong**2 + d_bac**2))
        
        # Kết quả
        kq_str = str(s)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Một drone xuất phát từ mặt đất, bay thẳng lên cao $%s \\text{ m}$, sau đó bay ngang về hướng Đông $%s \\text{ m}$ rồi tiếp tục bay ngang về hướng Bắc $%s \\text{ m}$. Độ lớn vectơ độ dịch chuyển của drone so với vị trí xuất phát bằng bao nhiêu? (đơn vị: $\\text{m}$).'
                         %(str(h), str(d_dong), str(d_bac)))
        
        # Nội dung lời giải
        loigiai = ('Giả sử vị trí xuất phát của drone trên mặt đất là gốc tọa độ $O(0; 0; 0)$. \\\\'
                   'Chọn hệ trục tọa độ $O x y z$ với trục $O z$ hướng thẳng đứng lên trên, trục $O x$ chỉ hướng Đông, trục $O y$ chỉ hướng Bắc. \\\\'
                   'Khi drone bay thẳng lên cao $%s \\text{ m}$, tọa độ của nó là $(0; 0; %s)$. \\\\'
                   'Sau đó drone bay ngang về hướng Đông $%s \\text{ m}$, tọa độ mới là $(%s; 0; %s)$. \\\\'
                   'Cuối cùng drone tiếp tục bay ngang về hướng Bắc $%s \\text{ m}$, vị trí cuối cùng của drone có tọa độ là $A(%s; %s; %s)$. \\\\'
                   'Vectơ độ dịch chuyển của drone so với vị trí xuất phát là $\\overrightarrow{O A} = (%s; %s; %s)$. \\\\'
                   'Độ lớn của vectơ độ dịch chuyển là $|\\overrightarrow{O A}| = \\sqrt{%s^2 + %s^2 + %s^2} = \\sqrt{%s + %s + %s} = \\sqrt{%s} = %s$ (m).'
                   %(str(h), str(h), str(d_dong), str(d_dong), str(h), str(d_bac), str(d_dong), str(d_bac), str(h), str(d_dong), str(d_bac), str(h), str(d_dong), str(d_bac), str(h), str(d_dong**2), str(d_bac**2), str(h**2), str(d_dong**2 + d_bac**2 + h**2), kq_str))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
               '\\loigiai{ \n' +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

