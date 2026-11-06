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


def bt_dang24_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Giới hạn: Giờ bắt đầu (g_start) từ 1 đến 5; Giờ kết thúc (g_end) từ 8 đến 12
            g_start = randint(1, 5)
            g_end = randint(8, 12)
            if g_start >= g_end: # Đảm bảo giờ kết thúc lớn hơn giờ bắt đầu
                g_end = g_start + randint(4, 7)
                if g_end > 12: g_end = 12

            # Số chuông đánh lúc giờ rưỡi (luôn là 1 trong bài toán gốc, nhưng có thể random để mở rộng)
            chuong_30 = 1 

            # --- TÍNH TOÁN KẾT QUẢ ---

            # 1. Tổng chuông Giờ Đúng (S1): Tổng cấp số cộng từ g_start đến g_end
            # Số lượng giờ đúng: n = g_end - g_start + 1
            # S1 = (g_start + g_end) * n / 2
            s1 = (g_start + g_end) * (g_end - g_start + 1) / 2

            # 2. Tổng chuông Giờ Rưỡi (S2):
            # Số lần giờ rưỡi (từ g_start:30 đến g_end-1:30): n_30 = g_end - g_start
            s2_so_lan = g_end - g_start
            s2 = s2_so_lan * chuong_30

            # Tổng số chuông: S = S1 + S2
            kq_so = int(s1 + s2)
            kq = str(kq_so)

            # --- TẠO ĐÁP ÁN TRẮC NGHIỆM ---
            da = '$%s$'%(kq)

            # Tạo các đáp án sai
            s = []
            sai_so = [-3, -2, -1, 1, 2, 3] # Sai số là số nguyên do kết quả là số nguyên
            for ss in sai_so:
                s.append('$%s$'%(kq_so + ss))

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            # --- NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---

            noidungcauhoi = ('''Chuông đồng hồ ở một toà tháp đánh số tiếng chuông đúng bằng số giờ và cứ mỗi $%s$ phút không phải là giờ đúng thì đánh $%s$ tiếng chuông. Hỏi bắt đầu từ lúc $%s$ giờ đến $%s$ giờ, chuông đồng hồ đó đã đánh tất cả bao nhiêu tiếng?'''
                              %(latex(30), latex(chuong_30), latex(g_start), latex(g_end)
                              ))

            # Các đáp án
            da_d = ('\\True ' +str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)

            # Lời giải
            loigiai=('''1. Số chuông Giờ Đúng ($S_1$): \\\\
                          Lúc $%s$ giờ, toà tháp đánh $%s$ tiếng chuông; lúc $%s$ giờ, toà tháp đánh $%s$ tiếng chuông. \\\\
                          Tổng chuông cho giờ đúng là tổng cấp số cộng từ $%s$ đến $%s$: \\\\
                          $S_1 = %s + %s + \\dots + %s = \\frac{(%s + %s) \\cdot %s}{2} = %s$ tiếng. \\\\
                          2. Số chuông Giờ Rưỡi ($S_2$): \\\\
                          Mỗi $%s$ phút không phải giờ đúng thì đánh $%s$ tiếng chuông. \\\\
                          Từ $%s$ giờ đến $%s$ giờ có $%s$ lần giờ rưỡi (ví dụ: $%s:30, \\dots, %s:30$). \\\\
                          $S_2 = %s \\cdot %s = %s$ tiếng. \\\\
                          Vậy tổng số chuông là: $S = S_1 + S_2 = %s + %s = %s$ tiếng.'''

                    %(latex(g_start), latex(g_start), latex(g_end), latex(g_end),
                      latex(g_start), latex(g_end), 
                      latex(g_start), latex(g_start+1), latex(g_end), 
                      latex(g_start), latex(g_end), latex(g_end-g_start+1), latex(int(s1)),
                      latex(30), latex(chuong_30),
                      latex(g_start), latex(g_end), latex(s2_so_lan), latex(g_start), latex(g_end-1),
                      latex(s2_so_lan), latex(chuong_30), latex(int(s2)),
                      latex(int(s1)), latex(int(s2)), latex(kq)
                    ))
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

