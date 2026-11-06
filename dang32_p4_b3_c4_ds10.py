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


def bt_dang32_p4_b3_c4_ds10(self):
            # Khai báo biến
            # ==========================================
            m = symbols('m')

            # Random các hệ số a, b sao cho phương trình (m+a)x^2 - 2mx + m-b = 0
            # Ví dụ dựa trên ảnh mới: a=4, b=9, k=4
            a = random.randint(2, 5)
            b = random.randint(6, 10)
            k = random.randint(3, 5)

            # ==========================================
            # GIẢI TOÁN TỰ ĐỘNG
            # ==========================================

            # 1. Điều kiện để có 2 nghiệm phân biệt khác 0 (I)
            root_delta = Rational(-a*b, b-a)
            cond_I_expr = (m > root_delta) & sp.Ne(m, -a) & sp.Ne(m, b)
            cond_I_set = cond_I_expr.as_set()

            # 2. Điều kiện 1/x1 + 1/x2 < k (II)
            expr_vieta = (2*m) / (m - b)
            sol_ineq_set = solve_univariate_inequality(expr_vieta < k, m, relational=False)

            # 3. Kết hợp điều kiện (Giao các tập hợp)
            final_sol_set = Intersection(cond_I_set, sol_ineq_set)

            # ==========================================
            # HÀM ĐỊNH DẠNG ĐÁP ÁN THEO YÊU CẦU
            # ==========================================
            def format_set_to_latex(s):
                # Lấy chuỗi latex chuẩn từ sympy
                res = latex(s)

                # 1. Sửa lỗi dương vô cực (thêm dấu +)
                res = res.replace(r'\infty', r'+\infty')

                # 2. Sửa định dạng loại trừ điểm: \setminus {a, b} thành \setminus {a; b}
                if r'\setminus' in res:
                    parts = res.split(r'\setminus')
                    left_side = parts[0]
                    # Xử lý phần tập hợp bị loại trừ phía sau dấu \
                    right_side = parts[1].replace(',', ';')
                    # Đảm bảo có dấu ngoặc nhọn đúng kiểu
                    right_side = right_side.replace(r'\left\{', r'\{').replace(r'\right\}', r'\}')
                    res = f"{left_side} \\setminus {right_side}"

                # 3. Thay đổi dấu phẩy ngăn cách khoảng thành dấu chấm phẩy nếu cần (tùy sở thích)
                # Ở đây giữ nguyên dấu phẩy cho khoảng (a, b) theo chuẩn SGK, chỉ đổi trong tập hợp { }

                return res

            da_dung = f"${format_set_to_latex(final_sol_set)}$"

            # ==========================================
            # TẠO ĐÁP ÁN NHIỄU
            # ==========================================
            distractors = [
                f"$m < {b} \\vee m > {latex(Rational(k*b, k-2))}$",
                f"$-{a} < m < {b}$",
                f"$m > {b}$",
                f"$m \\in ({latex(root_delta)}; {b})$",
                f"$m > {latex(Rational(k*b, k-2))}$"
            ]
            random.shuffle(distractors)
            das1, das2, das3 = distractors[:3]

            # ==========================================
            # NỘI DUNG CÂU HỎI VÀ LỜI GIẢI
            # ==========================================
            noidungcauhoi = (f"Tìm giá trị thực của tham số $m$ để phương trình $(m+{a})x^2 - 2mx + m - {b} = 0$ "
                             f"có hai nghiệm phân biệt $x_1, x_2$ khác $0$ thỏa mãn $\\frac{{1}}{{x_1}} + \\frac{{1}}{{x_2}} < {k}$.")

            loigiai = (f"Xét phương trình $(m+{a})x^2 - 2mx + m - {b} = 0 \\ (*)$. \\\\"
                       f"Phương trình $(*)$ có hai nghiệm phân biệt khác $0$ khi và chỉ khi: \\\\"
                       f"$\\begin{{cases}} a \\neq 0 \\\\ \\Delta' > 0 \\\\ P \\neq 0 \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} m + {a} \\neq 0 \\\\ m^2 - (m+{a})(m-{b}) > 0 \\\\ m - {b} \\neq 0 \\end{{cases}} \\\\"
                       f"\\Leftrightarrow \\begin{{cases}} m \\neq -{a} \\\\ {b-a}m + {a*b} > 0 \\\\ m \\neq {b} \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} m > {latex(root_delta)} \\\\ m \\neq -{a} \\\\ m \\neq  {b} \\end{{cases}} \\ (I)$. \\\\"
                       f"Theo hệ thức Vi-ét: $x_1+x_2 = \\frac{{2m}}{{m+{a}}}; x_1x_2 = \\frac{{m-{b}}}{{m+{a}}}$. \\\\"
                       f"Ta có: $\\frac{{1}}{{x_1}} + \\frac{{1}}{{x_2}} < {k} \\Leftrightarrow \\frac{{x_1+x_2}}{{x_1x_2}} < {k} "
                       f"\\Leftrightarrow \\frac{{2m}}{{m-{b}}} < {k} \\Leftrightarrow \\frac{{{2-k}m + {k*b}}}{{m-{b}}} < 0$. \\\\"
                       f"Giải bất phương trình trên ta được $m \\in {format_set_to_latex(sol_ineq_set)}$. \\\\"
                       f"Kết hợp với điều kiện $(I)$, ta chọn được $m \\in {format_set_to_latex(final_sol_set)}$.")

            # ==========================================
            # XUẤT KẾT QUẢ
            # ==========================================
            list_ans = ['\\True ' + da_dung, das1, das2, das3]
            random.shuffle(list_ans)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('-+','-')
            return content

