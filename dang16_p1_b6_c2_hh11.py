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


def bt_dang16_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Bộ số: [cạnh góc vuông 1, cạnh góc vuông 2, cạnh huyền]
            triples = [[3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 12, 15], [8, 15, 17]]
            selected_triple = random.choice(triples)

            # Xáo trộn hai cạnh góc vuông để tạo sự ngẫu nhiên cho AB và AC
            cạnh_gv = [selected_triple[0], selected_triple[1]]
            random.shuffle(cạnh_gv)

            ab_val = cạnh_gv[0]
            ac_val = cạnh_gv[1]
            bc_val = selected_triple[2]
            sa_val = random.randint(3, 9) # Chiều cao SA ngẫu nhiên từ 3 đến 9

            # B2: Tính toán các giá trị
            # Diện tích đáy S_ABC = 1/2 * AB * AC
            s_day = Rational(1, 2) * ab_val * ac_val
            # Thể tích V = 1/3 * S_day * SA
            v_val = Rational(1, 3) * s_day * sa_val

            # B3: Tạo các phương án sai (không trùng đáp án đúng)
            kq = v_val
            da_dung = '$V = %s$' % (latex(kq))

            wrong_options = set()
            while len(wrong_options) < 3:
                # Các lỗi sai thường gặp: quên 1/3, nhầm diện tích, hoặc số ngẫu nhiên
                wa1 = s_day * sa_val # Quên 1/3
                wa2 = 2 * v_val # Nhầm công thức
                wa3 = Rational(ab_val * ac_val * bc_val, 10) # Số ngẫu nhiên logic
                wa4 = v_val + random.randint(2, 10)

                for val in [wa1, wa2, wa3, wa4]:
                    val_str = '$V = %s$' % (latex(val))
                    if val != kq and len(wrong_options) < 3:
                        wrong_options.add(val_str)

            list_wrong = list(wrong_options)

            # B4: Viết nội dung câu hỏi và lời giải chi tiết
            noidungcauhoi = (
                'Cho khối chóp $S.ABC$ có $SA$ vuông góc với đáy, $SA = %s$, $AB = %s$, $BC = %s$ và $CA = %s$. '
                'Thể tích $V$ của khối chóp $S.ABC$ là'
                % (latex(sa_val), latex(ab_val), latex(bc_val), latex(ac_val))
            )

            # Mã TikZ vẽ hình (độ dày nét 1pt, nét đứt cho AC)
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, line width=1pt]\n'
                '  \\coordinate (A) at (0,0);\n'
                '  \\coordinate (B) at (1.5,-1.5);\n'
                '  \\coordinate (C) at (4,0.5);\n'
                '  \\coordinate (S) at (0,3.5);\n'
                '  \\draw [dashed] (A)--(C);\n'
                '  \\draw (S)--(A)--(B)--(C)--(S)--(B);\n'
                '  \\draw (A) node [left] {$A$};\n'
                '  \\draw (B) node [below] {$B$};\n'
                '  \\draw (C) node [right] {$C$};\n'
                '  \\draw (S) node [above] {$S$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            loigiai = (
                'Ta có $%s^2 = %s^2 + %s^2$ suy ra tam giác $ABC$ vuông tại $A$. \\\\'
                'Diện tích tam giác đáy $ABC$ là: $S_{ABC} = \\frac{1}{2} \\cdot AB \\cdot AC = \\frac{1}{2} \\cdot %s \\cdot %s = %s$. \\\\'
                'Thể tích của khối chóp $S.ABC$ là: $V = \\frac{1}{3} S_{ABC} \\cdot SA = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.'
                % (latex(bc_val), latex(ab_val), latex(ac_val), latex(ab_val), latex(ac_val), latex(s_day), latex(s_day), latex(sa_val), latex(v_val))
            )

            # Đưa vào danh sách và xáo trộn
            da_d = '\\True ' + da_dung
            list_1 = [da_d, list_wrong[0], list_wrong[1], list_wrong[2]]
            random.shuffle(list_1)

            # Xuất kết quả theo cấu trúc mẫu (không dùng tiền tố r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n' + tikz_code + '\n'
                '\\choice \n'
                '{' + list_1[0] + '}\n'
                '{' + list_1[1] + '}\n'
                '{' + list_1[2] + '}\n'
                '{' + list_1[3] + '}\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

