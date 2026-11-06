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


def bt_dang30_p4_b6_c2_hh11(self):
            # Khai báo biến
            # k=1 sẽ cho bài toán y hệt trong ảnh
            lis_k = [1, 2, 3, 4]
            k = random.choice(lis_k)

            # Khai báo biến ký hiệu cho a
            a = symbols('a')
            canh_day = k * a

            # Tính diện tích đáy tam giác đều: S = (cạnh^2 * sqrt(3)) / 4
            dien_tich_day_sym = Rational(k**2, 4) * sqrt(3) * a**2
            dien_tich_day_tex = "\\frac{" + latex(k**2) + "a^2\\sqrt{3}}{4}" if k % 2 != 0 else latex(sp.simplify(dien_tich_day_sym))

            # Chiều cao h = cạnh_day * tan(60) = k*a * sqrt(3)
            chieu_cao_sym = k * sqrt(3) * a
            chieu_cao_tex = latex(chieu_cao_sym)

            # Thể tích V = S * h = [(k^2 * sqrt(3) * a^2) / 4] * [k * sqrt(3) * a] = (3 * k^3 * a^3) / 4
            tu_so_v = 3 * (k**3)
            mau_so_v = 4
            the_tich_sym = Rational(tu_so_v, mau_so_v) * a**3
            the_tich_tex = "\\frac{" + latex(tu_so_v) + "a^3}{" + latex(mau_so_v) + "}"
            if tu_so_v % mau_so_v == 0:
                the_tich_tex = latex(sp.simplify(the_tich_sym))

            # --- BƯỚC 4: ĐIỀU CHỈNH CÁC PHƯƠNG ÁN SAI ---
            # Đáp án đúng
            da_dung = "$" + the_tich_tex + "$"

            # Tạo các phương án nhiễu dựa trên logic bài toán (sai diện tích hoặc sai chiều cao)
            s1 = "$" + latex(Rational(tu_so_v, 2) * a**3) + "$" # Sai mẫu số (chia 2 thay vì chia 4)
            s2 = "$" + latex(Rational(k**3, 4) * a**3) + "$"    # Quên nhân 3 (do sqrt(3)*sqrt(3))
            s3 = "$" + latex(Rational(tu_so_v, 8) * a**3) + "$" # Sai diện tích đáy (chia 8)

            # Đảm bảo không trùng lặp
            list_wrong = list(set([s1, s2, s3]))
            while len(list_wrong) < 3:
                list_wrong.append("$" + latex(Rational(random.randint(1, 10), 4) * a**3) + "$")
            random.shuffle(list_wrong)

            da_d = "\\True " + da_dung
            da_s1 = list_wrong[0]
            da_s2 = list_wrong[1]
            da_s3 = list_wrong[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- BƯỚC 2: VIẾT LỜI GIẢI VÀ NỘI DUNG ---
            # Chuẩn bị chuỗi cạnh đáy cho đề bài
            str_canh = "a" if k == 1 else latex(k) + "a"

            noidungcauhoi = ("Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy là tam giác đều cạnh $" + str_canh + "$, $A'B$ tạo với mặt phẳng đáy một góc $60^\\circ$. Tính thể tích khối lăng trụ $ABC.A'B'C'$.")

            # Vẽ hình TikZ giống 100% ảnh (độ dày 1pt)
            ve_hinh = ("\\begin{center}\n"
                       "\\begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm, scale=0.8, line width=1pt]\n"
                       "\\coordinate (A) at (0,0);\n"
                       "\\coordinate (B) at (2.5,-1.5);\n"
                       "\\coordinate (C) at (5,0);\n"
                       "\\coordinate (A1) at (0,4);\n"
                       "\\coordinate (B1) at (2.5,2.5);\n"
                       "\\coordinate (C1) at (5,4);\n"
                       "\\draw (A1)--(B1)--(C1)--(A1) (A)--(B)--(C) (A)--(A1) (B)--(B1) (C)--(C1) (A1)--(B);\n"
                       "\\draw [dashed] (A)--(C);\n"
                       "\\draw (1.8,-0.6) node {\\small $60^\\circ$};\n"
                       "\\draw (A) node[left] {$A$};\n"
                       "\\draw (B) node[below] {$B$};\n"
                       "\\draw (C) node[right] {$C$};\n"
                       "\\draw (A1) node[left] {$A'$};\n"
                       "\\draw (B1) node[right] {$B'$};\n"
                       "\\draw (C1) node[right] {$C'$};\n"
                       "\\end{tikzpicture}\n"
                       "\\end{center}")

            loigiai = ("Đáy là tam giác đều cạnh $" + str_canh + "$, có diện tích: $S_{\\triangle ABC} = " + dien_tich_day_tex + "$. \\\\\n"
                       "Vì $AA' \\perp \\left( ABC \\right) \\Rightarrow \\widehat{A'BA} = \\left( A'B, \\left( ABC \\right) \\right) = 60^\\circ$, suy ra: $AA' = AB \\tan 60^\\circ = " + chieu_cao_tex + "$. \\\\\n"
                       "Vậy thể tích khối lăng trụ: \\\\\n"
                       "$V_{ABC.A'B'C'} = S_{\\triangle ABC} \\cdot AA' = " + dien_tich_day_tex + " \\cdot " + chieu_cao_tex + " = " + the_tich_tex + "$.")

            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ("\\begin{minipage}{\\textwidth} \n"
                       "\\begin{ex}\n" + str(noidungcauhoi) + 
                       "\\loigiai{" +str(ve_hinh)+ str(loigiai) + "}\n"
                       "\\end{ex}\n \\end{minipage} \n\n")
            return content

