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


def bt_dang22_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán bằng cách thay đổi hệ số k của cạnh đáy a
                k = random.randint(2, 5)
                a = symbols('a')

                if k == 1:
                    canh_day_tex = "a"
                    canh_day_sym = a
                else:
                    canh_day_tex = f"{k}"
                    canh_day_sym = k

                # Bước 1 & 2: Tính toán dựa trên đề bài
                # Diện tích đáy S = (ka)^2
                S_ABCD = canh_day_sym**2

                # Đường chéo AC = ka * sqrt(2)
                AC = canh_day_sym * sqrt(2)

                # Vì tam giác ASC vuông tại S và H là trung điểm AC nên SH = AC / 2
                SH = AC / 2

                # Thể tích V = 1/3 * S_ABCD * SH
                V_chinh_xac = Rational(1, 3) * S_ABCD * SH

                # CHUYỂN ĐỔI SANG SỐ THẬP PHÂN LÀM TRÒN ĐẾN HÀNG PHẦN CHỤC
                # Tính toán giá trị số (coefficient) đi kèm với a^3
                # V = (k^3 * sqrt(2) / 6) * a^3
                v_numeric = float((k**3 * sqrt(2) / 6).evalf())
                v_rounded = round(v_numeric, 1)

                # Định dạng hiển thị (Ví dụ: 1.9a^3)
                v_final_tex = f"{v_rounded}"

                # Bước 4: Tạo các phương án sai (số thập phân)
                # s1: Quên 1/3, s2: Quên chia 2 ở SH, s3: Nhầm hệ số khác
                s1_val = round(float((k**3 * sqrt(2) / 2).evalf()), 1)
                s2_val = round(float((k**3 * sqrt(2) / 3).evalf()), 1)
                s3_val = round(float((k**3 / 6.0)), 1)

                # Đảm bảo các phương án sai không trùng đáp án đúng
                if s1_val == v_rounded: s1_val += 0.5
                if s2_val == v_rounded: s2_val += 0.7

                da_dung = f"$V \\approx {v_final_tex}$"
                das1 = f"$V \\approx {s1_val}$"
                das2 = f"$V \\approx {s2_val}$"
                das3 = f"$V \\approx {s3_val}$"

                # Câu hỏi
                noidungcauhoi = (
                    f"Cho khối chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng ${canh_day_tex}$. "
                    f"Biết $\\widehat{{ASC}} = 90^\\circ$, thể tích $V$ của khối chóp đó bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                )

                # Vẽ hình TikZ
                tikz_code = (
                    "\\begin{center}\n"
                    "\\begin{tikzpicture}[scale=0.8, line width=1pt, font=\\footnotesize]\n"
                    "\\coordinate (A) at (0,0);\n"
                    "\\coordinate (B) at (3.5,-1.2);\n"
                    "\\coordinate (C) at (6,0.5);\n"
                    "\\coordinate (D) at (2.5,1.7);\n"
                    "\\coordinate (H) at (3,0.25);\n"
                    "\\coordinate (S) at (3,4.5);\n"
                    "\\draw[dashed, line width=1pt] (D) -- (A) (D) -- (C) (D) -- (S) (A) -- (C) (B) -- (D) (S) -- (H);\n"
                    "\\draw[line width=1pt] (S) -- (A) (S) -- (B) (S) -- (C) (A) -- (B) (B) -- (C);\n"
                    "\\node at (S) [above] {$S$};\n"
                    "\\node at (A) [left] {$A$};\n"
                    "\\node at (B) [below] {$B$};\n"
                    "\\node at (C) [right] {$C$};\n"
                    "\\node at (D) [above left] {$D$};\n"
                    "\\node at (H) [below] {$H$};\n"
                    "\\end{tikzpicture}\n"
                    "\\end{center}"
                )

                # Lời giải chi tiết
                loigiai = (
                    f"Ta có: $S_{{ABCD}} = {latex(S_ABCD)}$.\\\\\n"
                    f"Gọi $H$ là tâm của hình vuông $ABCD$. Vì $S.ABCD$ là chóp đều nên $SH \\perp \\left(ABCD\\right)$.\\\\\n"
                    f"Xét tam giác $ASC$ vuông tại $S$ (theo giả thiết), có $H$ là trung điểm của $AC$.\\\\\n"
                    f"Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: $SH = \\frac{{AC}}{{2}}$.\\\\\n"
                    f"Ta có $AC = {canh_day_tex}\\sqrt{2} \\Rightarrow SH = \\frac{{{latex(AC)}}}{{2}} = {latex(SH)}$.\\\\\n"
                    f"Thể tích khối chóp là: $V = \\frac{{1}}{{3}} S_{{ABCD}} \\cdot SH = \\frac{{1}}{{3}} \\cdot {latex(S_ABCD)} \\cdot {latex(SH)} = {latex(V_chinh_xac)}$.\\\\\n"
                    f"Giá trị xấp xỉ: $V \\approx {v_final_tex}$."
                )

                # Sửa lỗi kqz thành v_final_tex
                dapan='\\shortans[0]{$%s$}\n'%(str(v_final_tex).replace('.',','))
                # Format các ký tự theo yêu cầu đặc biệt
                # Thay ( bằng \left( và ) bằng \right) (đã làm trong loigiai), thay . bằng ,


                # Các đáp án
                da_d = "\\True " + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + str(dapan)+
                "\\loigiai{" + tikz_code+ str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

