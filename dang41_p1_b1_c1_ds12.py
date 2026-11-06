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


def bt_dang41_p1_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng cực trị (số giao điểm cắt xuyên qua trục hoành của f'(x))
                # số giao điểm thực tế có thể là 1, 2, hoặc 3 cực trị
                so_cuc_tri = random.choice([1, 2, 3])

                # Định nghĩa cấu trúc đồ thị tương ứng bằng TikZ (đường cong bezier mềm mại nét 1pt)
                if so_cuc_tri == 1:
                    # Đồ thị f'(x) chỉ cắt trục hoành tại 1 điểm duy nhất bên phải (như hình gốc)
                    tikz_do_thi = (
                        "\\begin{center}\n"
                        "\\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]\n"
                        "\\draw[->] (-1.5,0) -- (4,0) node[below] {$x$};\n"
                        "\\draw[->] (0,-1.5) -- (0,3.5) node[left] {$y$};\n"
                        "\\draw (0,0) node[below left] {$O$};\n"
                        "\\draw[domain=-0.3:3.5, samples=100] plot (\\x, {-0.4*(\\x)*(\\x)*(\\x) + 1.8*(\\x)*(\\x) - 2.2*\\x + 2.5});\n"
                        "\\end{tikzpicture}\n"
                        "\\end{center}"
                    )
                    giai_thich_giao_diem = "cắt đường thẳng $y = 0$ tại $1$ điểm đơn duy nhất"
                    ket_luan_nghiem = "có $1$ nghiệm đơn"
                    dap_an_dung = "1"

                elif so_cuc_tri == 2:
                    # Đồ thị f'(x) tiếp xúc trục hoành tại điểm cực tiểu và cắt tại 1 điểm khác (hoặc ngược lại)
                    tikz_do_thi = (
                        "\\begin{center}\n"
                        "\\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]\n"
                        "\\draw[->] (-1.5,0) -- (4,0) node[below] {$x$};\n"
                        "\\draw[->] (0,-1.5) -- (0,3.5) node[left] {$y$};\n"
                        "\\draw (0,0) node[below left] {$O$};\n"
                        "\\draw[domain=-0.3:3.5, samples=100] plot (\\x, {-0.4*(\\x)*(\\x)*(\\x) + 1.8*(\\x)*(\\x) - 2.4*\\x + 0.8});\n"
                        "\\end{tikzpicture}\n"
                        "\\end{center}"
                    )
                    giai_thich_giao_diem = "tiếp xúc với đường thẳng $y = 0$ tại $1$ điểm và cắt xuyên qua tại $1$ điểm khác"
                    ket_luan_nghiem = "có $1$ nghiệm kép và $1$ nghiệm đơn"
                    dap_an_dung = "1" # Nghiệm kép không làm đạo hàm đổi dấu nên chỉ có 1 cực trị

                else:  # so_cuc_tri == 3
                    # Đồ thị f'(x) cắt trục hoành tại 3 điểm phân biệt
                    tikz_do_thi = (
                        "\\begin{center}\n"
                        "\\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]\n"
                        "\\draw[->] (-1.5,0) -- (4,0) node[below] {$x$};\n"
                        "\\draw[->] (0,-2) -- (0,3.5) node[left] {$y$};\n"
                        "\\draw (0,0) node[below left] {$O$};\n"
                        "\\draw[domain=-0.3:3.5, samples=100] plot (\\x, {-0.4*(\\x)*(\\x)*(\\x) + 1.8*(\\x)*(\\x) - 2.1*\\x + 0.5});\n"
                        "\\end{tikzpicture}\n"
                        "\\end{center}"
                    )
                    giai_thich_giao_diem = "cắt đường thẳng $y = 0$ tại $3$ điểm phân biệt"
                    ket_luan_nghiem = "có $3$ nghiệm đơn phân biệt"
                    dap_an_dung = "3"

                # Định nghĩa đáp án đúng
                da = "$%s$" % dap_an_dung

                # Tạo danh sách các phương án nhiễu (không trùng với đáp án đúng)
                s_candidates = ["0", "1", "2", "3", "4"]
                s = ["$%s$" % item for item in s_candidates if item != dap_an_dung]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = (
                    "Cho hàm số $f(x) = ax^4 + bx^3 + cx^2 + dx + e$. Hàm số $y = f'(x)$ có đồ thị như hình vẽ sau."
                    "%s"
                    "Đồ thị hàm số $y = f(x)$ có tất cả bao nhiêu điểm cực trị?"
                    % (tikz_do_thi)
                )

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên các phương án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo từng trường hợp cực trị ngẫu nhiên
                loigiai = (
                    "Ta có $y = f(x) \\Rightarrow y' = f'(x)$.\\\\\n"
                    "Ta thấy đồ thị hàm số $y = f'(x)$ %s suy ra phương trình $f'(x) = 0$ %s.\\\\\n"
                    "Vậy hàm số $y = f(x)$ có $%s$ điểm cực trị."
                    % (giai_thich_giao_diem, ket_luan_nghiem, dap_an_dung)
                )

            # Xuất câu trắc nghiệm đúng định dạng
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choice \n"
                "{" + str(list_1[0]) + "}\n"
                "{" + str(list_1[1]) + "}\n"
                "{" + str(list_1[2]) + "}\n"
                "{" + str(list_1[3]) + "}\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content 

