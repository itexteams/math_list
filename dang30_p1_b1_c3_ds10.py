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


def bt_dang30_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Chọn một số nguyên dương không phải số chính phương
        ds_so = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 19]
        n = random.choice(ds_so)
        
        # Tính căn bậc hai với độ chính xác cao
        val_sqrt = math.sqrt(n)
        
        # Lấy chuỗi xấp xỉ hiển thị trên máy tính (7 chữ số thập phân)
        str_full = f"{val_sqrt:.7f}"
        phan_nguyen, phan_thap_phan = str_full.split('.')
        chu_so_thu_4 = int(phan_thap_phan[3])
        chu_so_thu_3 = int(phan_thap_phan[2])
        
        # Làm tròn đến 3 chữ số thập phân dùng Decimal và ROUND_HALF_UP
        d = Decimal(str(val_sqrt))
        res_rounded = d.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
        da_val_str = f"{res_rounded:.3f}".replace('.', ',')
        
        # Tạo các đáp án gây nhiễu
        da_num = float(res_rounded)
        sai_1 = f"{da_num - 0.001:.3f}".replace('.', ',')
        sai_2 = f"{da_num + 0.001:.3f}".replace('.', ',')
        # Một đáp án làm tròn đến chữ số khác hoặc cộng trừ 0.004
        sai_3 = f"{da_num + 0.004:.3f}".replace('.', ',') if da_num <= 5 else f"{da_num - 0.004:.3f}".replace('.', ',')
        
        # Đáp án đúng và đáp án sai
        da = '$%s$' % da_val_str
        s1 = '$%s$' % sai_1
        s2 = '$%s$' % sai_2
        s3 = '$%s$' % sai_3
        
        # Chuỗi xấp xỉ 7 chữ số thập phân dùng dấu phẩy
        str_xapxi = str_full.replace('.', ',')
        
        # Câu hỏi
        noidungcauhoi = ('''Dùng máy tính để tìm giá trị gần đúng của $\\sqrt{%s}$ và làm tròn đến ba chữ số thập phân. Kết quả là'''
                         % latex(n)
                         )
        
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(s1)
        da_s2 = str(s2)
        da_s3 = str(s3)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        # Giải thích bước làm tròn
        if chu_so_thu_4 < 5:
            giai_thich_buoc = 'chữ số thứ tư sau dấu phẩy là $%s < 5$, nên giữ nguyên chữ số thứ ba.' % chu_so_thu_4
        else:
            giai_thich_buoc = 'chữ số thứ tư sau dấu phẩy là $%s \\ge 5$, nên cộng thêm $1$ đơn vị vào chữ số thứ ba.' % chu_so_thu_4
            
        # Nội dung lời giải
        loigiai = ('''Dùng máy tính được $\\sqrt{%s} \\approx %s$.\\\\
    Làm tròn đến ba chữ số thập phân, %s\\\\
    Suy ra $\\sqrt{%s} \\approx %s$.'''
                   % (latex(n), str_xapxi, giai_thich_buoc, latex(n), da_val_str)
                   )
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    