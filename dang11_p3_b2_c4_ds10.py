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


def bt_dang11_p3_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên cho bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tham số m dương để hàm số có GTNN (parabol quay bề lõm lên trên)
                # Ta chọn m sao cho y_min = -4m - 2 (dựa trên cấu trúc y = mx^2 - 2mx - 3m - 2)
                # Để số liệu đẹp, ta random m là số nguyên dương
                m_val = random.randint(1, 10)

                # Tính GTNN dựa trên công thức từ ảnh: y = -4m - 2
                gtnn_val = -4 * m_val - 2

                # Biến số cho sympy
                m_sym = symbols('m')

                # Đáp án đúng
                da = '$m = %s$' % (m_val)

                # Tạo các đáp án sai (không trùng với đáp án đúng)
                s = []
                while len(s) < 3:
                    sai = random.randint(1, 15)
                    if sai != m_val:
                        s_val = '$m = %s$' % (sai)
                        if s_val not in s:
                            s.append(s_val)

                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi: Thay các giá trị vào đề bài
                # Hàm số: y = m*x^2 - 2*m*x - 3*m - 2
                noidungcauhoi = ('''Giá trị thực của tham số $m \\neq 0$ để hàm số $y = %sx^2 - %smx - %sm - 2$ có giá trị nhỏ nhất bằng $%s$ trên $\\mathbb{R}$ bằng bao nhiêu?'''
                                 % (latex(m_sym), latex(2*m_sym), latex(3*m_sym), latex(gtnn_val)))

                # Lưu ý: Trong chuỗi trên dùng latex(m_sym) để giữ nguyên chữ m trong đề bài tổng quát 
                # Hoặc nếu muốn đề bài hiện số cụ thể thì dùng latex(m_val). Ở đây tôi giữ chữ 'm' theo đúng ảnh mẫu.
                noidungcauhoi = ('''Giá trị thực của tham số $m \\neq 0$ để hàm số $y = mx^2 - 2mx - 3m - 2$ có giá trị nhỏ nhất bằng $%s$ trên $\\mathbb{R}$ bằng bao nhiêu?'''
                                 % (latex(gtnn_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt cấu trúc trong ảnh)
                loigiai = ('''Ta có $x = -\\frac{b}{2a} = \\frac{2m}{2m} = 1$, suy ra $y = -4m - 2$. \\\\
                          Để hàm số có giá trị nhỏ nhất bằng $%s$ khi và chỉ khi \\\\
                          $\\frac{m}{2} > 0 \\Leftrightarrow m > 0 \\Leftrightarrow \\begin{cases} m > 0 \\\\ -4m - 2 = %s \\end{cases} \\Leftrightarrow m = %s$.'''
                          % (latex(gtnn_val), latex(gtnn_val), latex(m_val)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(m_val))
            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

