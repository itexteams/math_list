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


def bt_dang21_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Random vận tốc riêng của máy bay (km/h) và vận tốc gió (km/h)
        v_mb = randint(20, 60) * 10
        v_gio = randint(3, 12) * 10
        
        # Góc hợp bởi hướng Bắc và hướng Tây Nam (hợp với hướng Nam 45 độ) là 180 - 45 = 135 độ
        goc_hop = 135
        
        # Tính toán bằng sympy
        v_mb_binh = v_mb**2
        v_gio_binh = v_gio**2
        # v^2 = v_mb^2 + v_gio^2 + 2 * v_mb * v_gio * cos(135)
        tich_cos = 2 * v_mb * v_gio * sp.cos(sp.rad(goc_hop))
        v_binh_expr = v_mb_binh + v_gio_binh + tich_cos
        v_val_expr = sp.sqrt(v_binh_expr)
        
        # Làm tròn v^2 đến hàng phần trăm và v đến hàng phần mười theo chuẩn Decimal
        num_v_binh = Decimal(str(float(v_binh_expr.evalf())))
        kq_v_binh = num_v_binh.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        str_v_binh = str(kq_v_binh).replace('.', ',')
        
        num_v = Decimal(str(float(v_val_expr.evalf())))
        kq_v = num_v.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        str_v = str(kq_v).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Một máy bay bay theo hướng Bắc với vận tốc riêng $%s\\,\\mathrm{km/h}$. Gió thổi theo hướng Tây Nam (hợp với hướng Nam một góc $45^\\circ$) với vận tốc $%s\\,\\mathrm{km/h}$. Tính độ lớn vectơ vận tốc thực tế của máy bay so với mặt đất (làm tròn đến hàng phần mười).'
                         %(str(v_mb), str(v_gio)))
        
        # Nội dung lời giải
        loigiai = ('\\begin{itemize} \n'
                   '\\item Góc hợp bởi hai vectơ vận tốc máy bay (hướng Bắc) và vận tốc gió (hướng Tây Nam) là $%s^\\circ$. \n'
                   '\\item Áp dụng định lí Côsin cho hình bình hành vận tốc: $v^2 = %s^2 + %s^2 + 2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ = %s + %s %s \\approx %s$. \n'
                   '\\item Suy ra $v \\approx %s\\,\\mathrm{km/h}$. \n'
                   '\\end{itemize}'
                   %(str(goc_hop),
                     str(v_mb), str(v_gio), str(v_mb), str(v_gio), str(goc_hop), str(v_mb_binh), str(v_gio_binh), latex(tich_cos), str_v_binh,
                     str_v))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\loigiai{ \n' +str(loigiai)+'\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

