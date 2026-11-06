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


def bt_dang48_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số cho bài toán
                ab = random.randint(1, 4)
                bc = random.randint(1, 5)
                angle = random.choice([30, 45, 60])

                # Biểu diễn biến dưới dạng sympy để lấy LaTeX chuẩn
                ab_sym = sp.Integer(ab)
                bc_sym = sp.Integer(bc)

                if angle == 30:
                    tan_sym = sp.sqrt(3)/3
                elif angle == 45:
                    tan_sym = sp.Integer(1)
                else:
                    tan_sym = sp.sqrt(3)

                # Tính toán chính xác các giá trị
                sa_sym = ab_sym * tan_sym
                area_sym = sp.Rational(1, 2) * ab_sym * bc_sym
                v_exact_sym = sp.Rational(1, 3) * area_sym * sa_sym

                # Tính giá trị thập phân và làm tròn
                v_exact_float = float(v_exact_sym)
                v_dec = Decimal(str(v_exact_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(v_dec).replace('.', ',')

                # Chuỗi LaTeX
                tan_latex = sp.latex(tan_sym)
                sa_latex = sp.latex(sa_sym)
                area_latex = sp.latex(area_sym)
                v_exact_latex = sp.latex(v_exact_sym)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq)

                # Tạo các phương án nhiễu hợp lý (nhầm công thức 1/3, 1/2, v.v...)
                s_set = set()
                multipliers = [2, 3, 6, 1.5, 4, 0.5, 1/3, 1/2]
                for m in multipliers:
                    val = v_exact_float * m
                    val_dec = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    val_str = '$%s$' % str(val_dec).replace('.', ',')
                    if val_str != da:
                        s_set.add(val_str)
                    if len(s_set) == 3:
                        break

                # Dự phòng nếu các hệ số nhân không đủ tạo 3 đáp án phân biệt
                offset = 0.1
                while len(s_set) < 3:
                    v_temp = v_exact_float + offset
                    val_dec = Decimal(str(v_temp)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    val_str = '$%s$' % str(val_dec).replace('.', ',')
                    if val_str != da:
                        s_set.add(val_str)
                    offset += 0.1

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp tam giác $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$, cạnh bên $SA$ vuông góc với mặt phẳng đáy. Biết rằng $AB = %s$, góc nhị diện $[S,BC,A] = %s^\\circ$ và khoảng cách từ $C$ đến mặt phẳng $(SAB)$ bằng $%s$. Thể tích của khối chóp $S.ABC$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).'''
                                 % (ab, angle, bc))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (1.5,-2);
            \\coordinate (C) at (4,0);
            \\coordinate (S) at (0,3);
            \\draw (S) -- (A) -- (B) -- (C) -- (S);
            \\draw (S) -- (B);
            \\draw[dashed] (A) -- (C);
            \\node[left] at (A) {$A$};
            \\node[below] at (B) {$B$};
            \\node[right] at (C) {$C$};
            \\node[above] at (S) {$S$};
            \\end{tikzpicture}
            \\end{center}
            Ta có $\\begin{cases} (SBC) \\cap (ABC) = BC \\\\ BC \\perp SB, SB \\subset (SBC) \\\\ BC \\perp AB, AB \\subset (ABC) \\end{cases} \\Rightarrow [S,BC,A] = \\widehat{SBA} = %s^\\circ$.\\\\
            Tam giác $SAB$ vuông tại $A$ có $\\tan \\widehat{SBA} = \\frac{SA}{AB} \\Rightarrow SA = AB \\cdot \\tan %s^\\circ = %s \\cdot %s = %s = h$.\\\\
            Mặt khác, $BC \\perp (SAB), B \\in (SAB)$ nên $d(C,(SAB)) = BC = %s$.\\\\
            Từ đó, ta có diện tích mặt phẳng đáy là $S = \\frac{1}{2}AB \\cdot BC = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.\\\\
            Vậy thể tích khối chóp đã cho bằng $V = \\frac{1}{3}Sh = \\frac{1}{3} \\cdot %s \\cdot %s = %s \\approx %s$.'''
                           % (angle, angle, ab, tan_latex, sa_latex, bc, ab, bc, area_latex, area_latex, sa_latex, v_exact_latex, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

