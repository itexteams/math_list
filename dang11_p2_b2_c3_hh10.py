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


def bt_dang11_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Hàm bổ trợ: Làm tròn và đổi dấu phẩy thập phân
            def fix_dec(number, precision=1):
                num_rounded = round(float(number), precision)
                return str(num_rounded).replace('.', ',')

            # 1. Khai báo dữ liệu bài toán (Bám sát đề bài gốc để đúng bước B2)
            A = Point(2, -1)
            B = Point(2, -2)
            C = Point(0, 1)

            xA, yA = A.x, A.y
            xB, yB = B.x, B.y
            xC, yC = C.x, C.y

            # 2. Tính toán các thông số hình học
            vec_BC = (xC - xB, yC - yB) # (-2, 3)
            dist_BC = B.distance(C)      # sqrt(13)
            dist_AB = A.distance(B)      # 1
            dist_AC = A.distance(C)      # sqrt(8)

            # Phương trình tổng quát BC: 3x + 2y - 2 = 0
            line_BC = Line(B, C)
            h_A = line_BC.distance(A)    # 2/sqrt(13)
            S_ABC = Rational(1, 2) * dist_BC * h_A # S = 1

            p = (dist_AB + dist_BC + dist_AC) / 2
            r_in = S_ABC / p

            cosC = (dist_AC**2 + dist_BC**2 - dist_AB**2) / (2 * dist_AC * dist_BC)
            angleC_deg = float(deg(acos(cosC)))

            # 3. Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có các đỉnh $A(%s; %s), B(%s; %s)$ và $C(%s; %s)$.''' 
                             %(xA, yA, xB, yB, xC, yC))

            ########################################################################
            # a) Độ dài đường cao (Nhận biết)
            ha_val = fix_dec(h_A)
            ha_true = '\\True Độ dài đường cao kẻ từ $A$ đến cạnh $BC$ của tam giác là $h_A \\approx %s$' % ha_val
            ha_false = 'Độ dài đường cao kẻ từ $A$ đến cạnh $BC$ của tam giác là $h_A \\approx %s$' % fix_dec(float(h_A) + 0.5)
            list_ha = [ha_true, ha_false]

            loigiai_ha = ('''Ta có $\\vec{BC} = (%s; %s)$. Suy ra đường thẳng $BC$ nhận $\\vec{n}=(3; 2)$ làm vectơ pháp tuyến.\\\\
                          Phương trình đường thẳng $BC$ là: $3(x - %s) + 2(y - %s) = 0 \\Leftrightarrow 3x + 2y - 2 = 0$.\\\\
                          Độ dài đường cao $h_A = d(A, BC) = \\frac{|3 \\cdot %s + 2 \\cdot (%s) - 2|}{\\sqrt{3^2 + 2^2}} = \\frac{2}{\\sqrt{13}} \\approx %s$.''' 
                          % (xC-xB, yC-yB, xC, yC, xA, yA, ha_val))

            ########################################################################
            # b) Diện tích (Thông hiểu)
            S_val = fix_dec(S_ABC)
            S_true = '\\True Diện tích tam giác $ABC$ bằng %s' % S_val
            S_false = 'Diện tích tam giác $ABC$ bằng %s' % fix_dec(float(S_ABC) + 1.5)
            list_S = [S_true, S_false]

            loigiai_S = ('''Độ dài cạnh $BC = \\sqrt{(%s - %s)^2 + (%s - %s)^2} = \\sqrt{13} \\approx %s$.\\\\
                          Diện tích tam giác $ABC$ được tính theo công thức:\\\\
                          $S_{ABC} = \\frac{1}{2} BC \\cdot h_A = \\frac{1}{2} \\cdot \\sqrt{13} \\cdot \\frac{2}{\\sqrt{13}} = %s$.'''
                          % (xC, xB, yC, yB, fix_dec(dist_BC), S_val))

            ########################################################################
            # c) Bán kính nội tiếp (Vận dụng) - Làm tròn 1 chữ số, dấu phẩy
            r_val = fix_dec(r_in)
            r_true = '\\True Bán kính đường tròn nội tiếp $r$ của tam giác xấp xỉ %s' % r_val
            r_false = 'Bán kính đường tròn nội tiếp $r$ của tam giác xấp xỉ %s' % fix_dec(float(r_in) + 0.3)
            list_r = [r_true, r_false]

            loigiai_r = ('''Ta tính độ dài các cạnh còn lại của tam giác:\\\\
                         $AB = \\sqrt{(2-2)^2 + (-2 - (-1))^2} = 1$.\\\\
                         $AC = \\sqrt{(0-2)^2 + (1 - (-1))^2} = \\sqrt{8} \\approx %s$.\\\\
                         Nửa chu vi tam giác: $p = \\frac{AB + BC + AC}{2} \\approx \\frac{1 + %s + %s}{2} \\approx %s$.\\\\
                         Bán kính đường tròn nội tiếp: $r = \\frac{S}{p} \\approx \\frac{1}{%s} \\approx %s$.'''
                         % (fix_dec(dist_AC), fix_dec(dist_BC), fix_dec(dist_AC), fix_dec(p), fix_dec(p), r_val))

            ########################################################################
            # d) Góc C (Vận dụng cao)
            angle_val = fix_dec(angleC_deg)
            angle_true = '\\True Số đo góc $\\widehat{C}$ của tam giác xấp xỉ $%s^\\circ$' % angle_val
            angle_false = 'Số đo góc $\\widehat{C}$ của tam giác xấp xỉ $%s^\\circ$' % fix_dec(angleC_deg + 4.2)
            list_angle = [angle_true, angle_false]

            loigiai_angle = ('''Áp dụng hệ quả của định lý côsin trong tam giác $ABC$ cho góc $C$:\\\\
                             $\\cos C = \\frac{AC^2 + BC^2 - AB^2}{2 \\cdot AC \\cdot BC} = \\frac{(\\sqrt{8})^2 + (\\sqrt{13})^2 - 1^2}{2 \\cdot \\sqrt{8} \\cdot \\sqrt{13}} = \\frac{20}{2\\sqrt{104}} = \\frac{10}{\\sqrt{104}}$.\\\\
                             Suy ra $\\widehat{C} \\approx %s^\\circ$.''' % angle_val)

            # 4. Logic chọn đáp án Đúng/Sai (1-3 câu đúng)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_ha)
                ans_b = random.choice(list_S)
                ans_c = random.choice(list_r)
                ans_d = random.choice(list_angle)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # 5. Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(ans_a)+'}\n'
                '{'+str(ans_b)+'}\n'
                '{'+str(ans_c)+'}\n'
                '{'+str(ans_d)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_ha)+'\n'
                '\\item '+str(loigiai_S)+'\n'
                '\\item '+str(loigiai_r)+'\n'
                '\\item '+str(loigiai_angle)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

