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


def bt_dang9_p3_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random số lượng thẻ n (từ 12 đến 20)
                n_total = random.randint(12, 20)
                # Random số chia k cho biến cố B (thường là 3, 4 hoặc 5 để bài toán hay)
                k_div = random.choice([3, 4])

                # Tập hợp không gian mẫu
                omega = list(range(1, n_total + 1))
                n_omega = len(omega)

                # Biến cố A: Số chẵn
                set_A = [i for i in omega if i % 2 == 0]
                n_A = len(set_A)

                # Biến cố B: Số chia hết cho k_div
                set_B = [i for i in omega if i % k_div == 0]
                n_B = len(set_B)

                # Biến cố giao AB: Số chẵn và chia hết cho k_div
                set_AB = [i for i in set_A if i in set_B]
                n_AB = len(set_AB)

                # Tính toán xác suất bằng Sympy để giữ phân số chính xác
                prob_A = Rational(n_A, n_omega)
                prob_B = Rational(n_B, n_omega)
                prob_AB = Rational(n_AB, n_omega)

                # Tính p = P(A).P(B) - P(AB)
                p_val_exact = prob_A * prob_B - prob_AB

                # Chuyển sang số thập phân và làm tròn đến hàng phần trăm
                p_float = float(p_val_exact)
                p_rounded = Decimal(str(p_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(p_rounded).replace('.', ',')

                # Tạo các phương án sai
                # Đảm bảo các phương án không trùng nhau và không trùng đáp án đúng
                s_options = set()
                while len(s_options) < 3:
                    # Tạo sai số ngẫu nhiên từ -0.05 đến 0.05
                    offset = random.choice([-0.03, -0.02, -0.01, 0.01, 0.02, 0.03, 0.04])
                    wrong_val = p_rounded + Decimal(str(offset))
                    wrong_str = str(wrong_val).replace('.', ',')
                    if wrong_str != kq:
                        s_options.add('$%s$' % wrong_str)

                list_wrong = list(s_options)
                da_d = '\\True $%s$' % kq

                # Trộn các đáp án
                list_1 = [da_d, list_wrong[0], list_wrong[1], list_wrong[2]]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một hộp chứa $%s$ tấm thẻ cùng loại được đánh số từ $1$ đến $%s$. Chọn ngẫu nhiên $1$ thẻ từ hộp. Gọi $A$ là biến cố "Số ghi trên thẻ được chọn là số chẵn" và $B$ là biến cố "Số ghi trên thẻ được chọn chia hết cho $%s$". Đặt $p = P\\left( A \\right) \\cdot P\\left( B \\right) - P\\left( AB \\right)$, thì $p$ bằng bao nhiêu? (làm tròn đến hàng phần chục).'''
                                 % (latex(n_total), latex(n_total), latex(k_div)))

                # Nội dung lời giải chi tiết
                # Format danh sách tập hợp cho lời giải
                str_A = ', '.join(map(str, set_A))
                str_B = ', '.join(map(str, set_B))
                str_AB = ', '.join(map(str, set_AB))

                loigiai = ('''Ta có $A = \\left\\{ %s \\right\\} \\Rightarrow n\\left( A \\right) = %s$; \\\\
                           $B = \\left\\{ %s \\right\\} \\Rightarrow n\\left( B \\right) = %s$; \\\\
                           $AB = \\left\\{ %s \\right\\} \\Rightarrow n\\left( AB \\right) = %s$; $n\\left( \\Omega \\right) = %s$. \\\\
                           $P\\left( A \\right) = \\frac{%s}{%s}$, $P\\left( B \\right) = \\frac{%s}{%s}$ suy ra $P\\left( A \\right) \\cdot P\\left( B \\right) = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = %s$; \\\\
                           $P\\left( AB \\right) = \\frac{%s}{%s}$. \\\\
                           Do đó $p = P\\left( A \\right) \\cdot P\\left( B \\right) - P\\left( AB \\right) = %s - \\frac{%s}{%s} = %s \\approx %s$.'''
                           % (str_A, latex(n_A), 
                              str_B, latex(n_B), 
                              str_AB, latex(n_AB), latex(n_omega),
                              latex(n_A), latex(n_omega), latex(n_B), latex(n_omega),
                              latex(n_A), latex(n_omega), latex(n_B), latex(n_omega), latex(prob_A * prob_B),
                              latex(n_AB), latex(n_omega),
                              latex(prob_A * prob_B), latex(n_AB), latex(n_omega), latex(p_val_exact), kq))
                dapan=' \\shortans[0]{$%s$} '%(kq) 
            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

