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


def bt_dang30_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến k (hệ số cạnh đáy)
            lis_k = [1, 2, 3, 4, 5, 6]
            k = random.choice(lis_k)

            # Cạnh đáy (đã bỏ ký hiệu a)
            canh_day = k

            # Diện tích đáy tam giác đều: S = (cạnh^2 * sqrt(3)) / 4
            dien_tich_day_val = (k**2 * math.sqrt(3)) / 4

            # Chiều cao h = cạnh_day * tan(60) = k * sqrt(3)
            chieu_cao_val = k * math.sqrt(3)

            # Thể tích V = S * h = [(k^2 * sqrt(3)) / 4] * [k * sqrt(3)] = (3 * k^3) / 4
            the_tich_val = (3 * k**3) / 4.0
            # Làm tròn đến hàng phần chục
            the_tich_final = round(the_tich_val, 1)

            # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI (Dạng số thập phân) ---
            da_dung = f"{the_tich_final}"

            # Tạo nhiễu
            s1 = round(the_tich_val / 3, 1)  # Quên nhân 3 hoặc nhầm sang khối chóp
            s2 = round((k**3 * math.sqrt(3)) / 4, 1) # Sai do không nhân tan(60)
            s3 = round(the_tich_val * 2, 1) # Nhầm công thức

            # Đảm bảo không trùng lặp và không trùng đáp án đúng
            list_wrong = set()
            for s in [s1, s2, s3]:
                if s != the_tich_final:
                    list_wrong.add(f"{s}")

            while len(list_wrong) < 3:
                random_val = round(random.uniform(1, 100), 1)
                if f"{random_val}" != da_dung:
                    list_wrong.add(f"{random_val}")

            list_wrong = list(list_wrong)
            random.shuffle(list_wrong)

            da_d = "\\True " + da_dung
            da_s1 = list_wrong[0]
            da_s2 = list_wrong[1]
            da_s3 = list_wrong[2]

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # --- BƯỚC 2: VIẾT LỜI GIẢI VÀ NỘI DUNG ---
            noidungcauhoi = (f"Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy là tam giác đều cạnh ${k}$, "
                             f"$A'B$ tạo với mặt phẳng đáy một góc $60^\\circ$. Thể tích khối lăng trụ $ABC.A'B'C'$ "
                             f"bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười).")

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

            loigiai = (f"Đáy là tam giác đều cạnh ${k}$, có diện tích: $S_{{\\triangle ABC}} = \\frac{{{k}^2\\sqrt{3}}}{{4}} \\approx {dien_tich_day_val:.1f}$. \\\\\n"
                       f"Vì $AA' \\perp \\left( ABC \\right) \\Rightarrow \\widehat{{A'BA}} = \\left( A'B, \\left( ABC \\right) \\right) = 60^\\circ$, "
                       f"suy ra: $AA' = AB \\cdot \\tan 60^\\circ = {k} \\cdot \\sqrt{3} \\approx {chieu_cao_val:.1f}$. \\\\\n"
                       f"Vậy thể tích khối lăng trụ: \\\\\n"
                       f"$V_{{ABC.A'B'C'}} = S_{{\\triangle ABC}} \\cdot AA' = \\frac{{3 \\cdot {k}^3}}{{4}} = {the_tich_final}$.")
            dapan='\\shortans[0]{$%s$}\n'%(str(the_tich_final).replace('.',','))
            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ("\\begin{minipage}{\\textwidth} \n"
                       "\\begin{ex}\n" + str(noidungcauhoi) + str(dapan)+
                       "\\loigiai{" +str(ve_hinh)+ str(loigiai) + "}\n"
                       "\\end{ex}\n \\end{minipage} \n\n")
            return content

