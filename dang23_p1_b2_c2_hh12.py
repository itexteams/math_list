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


def bt_dang23_p1_b2_c2_hh12(self):
            # --- BƯỚC 1: SINH DỮ LIỆU ---
            # 1. Khởi tạo dữ liệu ngẫu nhiên
            Ax, Ay, Az = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            Bx, By, Bz = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            Cx, Cy, Cz = randint(-5, 5), randint(-5, 5), randint(-5, 5)

            # 2. Tính toán trung điểm M và Vectơ AM
            Mx, My, Mz = Rational(Bx + Cx, 2), Rational(By + Cy, 2), Rational(Bz + Cz, 2)
            ux, uy, uz = Mx - Ax, My - Ay, Mz - Az

            # Đảm bảo vectơ chỉ phương khác vectơ không
            while ux == 0 and uy == 0 and uz == 0:
                Cx += 1
                Mx, My, Mz = Rational(Bx + Cx, 2), Rational(By + Cy, 2), Rational(Bz + Cz, 2)
                ux, uy, uz = Mx - Ax, My - Ay, Mz - Az

            def format_fraction_coord(num, den=2):
                """Tạo chuỗi latex phân số cho tọa độ trung điểm"""
                return f"\\frac{{{num}}}{{{den}}}"

            def format_component(p, u):
                """Định dạng thành phần x = x0 + at"""
                p_tex = latex(p)
                if u == 0: return f"{p_tex}"

                if u == 1: u_tex = "+ t"
                elif u == -1: u_tex = "- t"
                elif u > 0: u_tex = f"+ {latex(u)}t"
                else: u_tex = f"{latex(u)}t"

                if p == 0: return u_tex.lstrip("+ ").strip()
                return f"{p_tex} {u_tex}"

            def make_system(p0, v_dir):
                """Tạo hệ phương trình tham số"""
                x_line = f"x = {format_component(p0[0], v_dir[0])}"
                y_line = f"y = {format_component(p0[1], v_dir[1])}"
                z_line = f"z = {format_component(p0[2], v_dir[2])}"
                return f"\\begin{{cases}}{x_line}\\\\{y_line}\\\\{z_line}\\end{{cases}}".replace("+ -", "-")

            # 3. Tạo các phương án trắc nghiệm
            da_dung_latex = make_system((Ax, Ay, Az), (ux, uy, uz))
            list_ans = []
            list_ans.append(f"\\True ${da_dung_latex}$")

            # Tạo phương án nhiễu
            potential_distractors = [
                ((Mx, My, Mz), (ux, uy, uz)), 
                ((Ax, Ay, Az), (Bx-Ax, By-Ay, Bz-Az)), 
                ((Ax, Ay, Az), (ux, uy, 0)), 
                ((Bx, By, Bz), (ux, uy, uz))
            ]

            for p_pt, v_pt in potential_distractors:
                dist_latex = f"${make_system(p_pt, v_pt)}$"
                if dist_latex not in [a.replace("\\True ", "") for a in list_ans]:
                    list_ans.append(dist_latex)
                if len(list_ans) == 4: break

            random.shuffle(list_ans)

            # 4. Nội dung câu hỏi và Lời giải (Đã sửa \left( \right))
            noidungcauhoi = (
                f"Trong không gian với hệ tọa độ $Oxyz$, cho tam giác $ABC$ có "
                f"$A\\left({Ax};{Ay};{Az}\\right)$, $B\\left({Bx};{By};{Bz}\\right)$ và $C\\left({Cx};{Cy};{Cz}\\right)$. "
                f"Phương trình tham số của đường trung tuyến $AM$ của tam giác $ABC$ là"
            )

            # Sử dụng \left( \right) cho tọa độ điểm M
            buoc_tinh_M = (
                f"M\\left("
                f"{format_fraction_coord(f'{Bx} + {Cx}')}; "
                f"{format_fraction_coord(f'{By} + {Cy}')}; "
                f"{format_fraction_coord(f'{Bz} + {Cz}')}"
                f"\\right) \\Rightarrow M\\left({latex(Mx)}; {latex(My)}; {latex(Mz)}\\right)"
            )

            # Sử dụng \left( \right) cho tọa độ vectơ
            buoc_tinh_vec = f"\\vec{{AM}} = \\left({latex(ux)}; {latex(uy)}; {latex(uz)}\\right)"

            loigiai = (
                f"Gọi $M$ là trung điểm của cạnh $BC$. Ta có tọa độ điểm $M$ là:\\\\"
                f"${buoc_tinh_M}$.\\\\ "
                f"Đường trung tuyến $AM$ đi qua điểm $A\\left({Ax}; {Ay}; {Az}\\right)$ và nhận "
                f"${buoc_tinh_vec}$ làm vectơ chỉ phương.\\\\"
                f"Vậy phương trình tham số của đường trung tuyến $AM$ là: "
                f"${da_dung_latex}$."
            ).replace("+ -", "-")

            # 5. Xuất kết quả
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choice \n'
                '{' + list_ans[0] + '}\n'
                '{' + list_ans[1] + '}\n'
                '{' + list_ans[2] + '}\n'
                '{' + list_ans[3] + '}\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

