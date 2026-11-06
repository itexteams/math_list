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


def bt_dang18_p2_b1_c3_hh10(self):
            # Khai báo các ký hiệu Sympy
            x, y = symbols('x y')

            # 1. Khởi tạo dữ liệu bài toán (Random tọa độ)
            while True:
                xD, yD = random.randint(-3, 3), random.randint(-3, 3)
                xE, yE = random.randint(-3, 5), random.randint(-3, 5)
                xF, yF = random.randint(1, 6), random.randint(1, 7)

                # Kiểm tra không thẳng hàng
                if (xE-xD)*(yF-yD) != (xF-xD)*(yE-yD):
                    break

            # --- HÀM HỖ TRỢ LÀM ĐẸP PHƯƠNG TRÌNH ---
            def get_pretty_equation(A_val, B_val, x0, y0):
                """Trả về phương trình tối giản Ax + By + C = 0 từ VTPT(A,B) và điểm (x0,y0)"""
                C_val = -(A_val * x0 + B_val * y0)
                # Quy đồng mẫu số (lấy LCM của các mẫu số)
                denoms = [sp.denom(A_val), sp.denom(B_val), sp.denom(C_val)]
                lcm_val = sp.lcm(denoms)
                A_i, B_i, C_i = A_val * lcm_val, B_val * lcm_val, C_val * lcm_val
                # Chia cho GCD để tối giản
                common = sp.gcd_list([A_i, B_i, C_i])
                A_f, B_f, C_f = A_i / common, B_i / common, C_i / common
                # Đảm bảo hệ số đầu tiên dương
                if A_f < 0 or (A_f == 0 and B_f < 0):
                    A_f, B_f, C_f = -A_f, -B_f, -C_f
                return A_f * x + B_f * y + C_f

            # Nội dung câu hỏi
            noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho tam giác $DEF$ có $D\\left(%s; %s\\right)$, $E\\left(%s; %s\\right)$, $F\\left(%s; %s\\right)$.' 
                             % (latex(xD), latex(yD), latex(xE), latex(yE), latex(xF), latex(yF)))

            # --- Mệnh đề a: Vectơ chỉ phương/pháp tuyến ---
            vecEF = (xF - xE, yF - yE)
            da_a_d = '\\True Đường thẳng vuông góc với $EF$ nhận $\\vec{EF}=\\left(%s; %s\\right)$ làm vectơ pháp tuyến' % (latex(vecEF[0]), latex(vecEF[1]))
            da_a_s = 'Đường thẳng vuông góc với $EF$ nhận $\\vec{EF}=\\left(%s; %s\\right)$ làm vectơ chỉ phương' % (latex(vecEF[0]), latex(vecEF[1]))
            list_da_a = [da_a_d, da_a_s]
            loigiai_a = ('Đường thẳng vuông góc với $EF$ sẽ nhận vectơ chỉ phương của $EF$ là $\\vec{EF} = \\left(%s; %s\\right)$ làm vectơ pháp tuyến.' % (latex(vecEF[0]), latex(vecEF[1])))

            # --- Mệnh đề b: Phương trình đường cao kẻ từ D ---
            # Đường cao kẻ từ D vuông góc EF => Nhận vecEF làm VTPT
            pt_duongcao = get_pretty_equation(vecEF[0], vecEF[1], xD, yD)
            da_b_d = '\\True Phương trình đường cao kẻ từ $D$ là: $%s = 0$' % (latex(pt_duongcao))
            da_b_s = 'Phương trình đường cao kẻ từ $D$ là: $%s = 0$' % (latex(pt_duongcao + random.randint(1,2)))
            list_da_b = [da_b_d, da_b_s]
            loigiai_b = ('Đường cao kẻ từ $D$ vuông góc với cạnh $EF$ nên nhận $\\vec{EF} = \\left(%s; %s\\right)$ làm vectơ pháp tuyến. '
                         'Phương trình: $%s = 0$.' % (latex(vecEF[0]), latex(vecEF[1]), latex(pt_duongcao)))

            # --- Mệnh đề c: Tọa độ trung điểm I của DF ---
            midI_x, midI_y = Rational(xD + xF, 2), Rational(yD + yF, 2)
            da_c_d = '\\True Gọi $I$ là trung điểm $DF$. Tọa độ của $I$ là $\\left(%s; %s\\right)$' % (latex(midI_x), latex(midI_y))
            da_c_s = 'Gọi $I$ là trung điểm $DF$. Tọa độ của $I$ là $\\left(%s; %s\\right)$' % (latex(midI_x + 1), latex(midI_y))
            list_da_c = [da_c_d, da_c_s]
            loigiai_c = ('Tọa độ trung điểm $I$ của $DF$: $x_I = \\frac{x_D + x_F}{2} = %s$; $y_I = \\frac{y_D + y_F}{2} = %s$.' % (latex(midI_x), latex(midI_y)))

            # --- Mệnh đề d: Phương trình đường trung tuyến kẻ từ E ---
            # VTCP EI = (midI_x - xE, midI_y - yE) -> VTPT = (-(yI-yE), xI-xE)
            val_A = -(midI_y - yE)
            val_B = midI_x - xE
            pt_trungtuyen = get_pretty_equation(val_A, val_B, xE, yE)

            da_d_d = '\\True Đường trung tuyến kẻ từ $E$ là: $%s = 0$' % (latex(pt_trungtuyen))
            da_d_s = 'Đường trung tuyến kẻ từ $E$ là: $%s = 0$' % (latex(pt_trungtuyen + 1))
            list_da_d = [da_d_d, da_d_s]
            loigiai_d = ('Đường trung tuyến $EI$ đi qua $E\\left(%s; %s\\right)$ và $I\\left(%s; %s\\right)$. '
                         'Vectơ chỉ phương $\\vec{EI} = \\left(%s; %s\\right)$. '
                         'Phương trình: $%s = 0$.' % (latex(xE), latex(yE), latex(midI_x), latex(midI_y), 
                                                    latex(midI_x - xE), latex(midI_y - yE), latex(pt_trungtuyen)))

            # --- Chọn ngẫu nhiên đúng/sai (Đảm bảo 1-3 câu đúng) ---
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                ans_a = random.choice(list_da_a)
                ans_b = random.choice(list_da_b)
                ans_c = random.choice(list_da_c)
                ans_d = random.choice(list_da_d)
                if 1 <= count_true([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

