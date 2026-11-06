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


def bt_dang9_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Bước 1 & 2: Thiết lập thông số bài toán (Random hóa các hệ số)
            # Phương trình mẫu: sqrt(ax^2 + bx + c) - |dx + e| = f
            # Để đảm bảo có nghiệm, ta chọn các thông số gần với đề gốc
            a = 1
            b = random.randint(-6, -2) # Gốc là -4
            c = random.randint(-2, 0)  # Gốc là -1
            d = random.randint(1, 3)   # Gốc là 2
            e = random.randint(1, 2)   # Gốc là 1
            f = random.randint(1, 1)   # Gốc là 1

            # Biểu thức trong căn và trong trị tuyệt đối
            expr_sqrt = a*x**2 + b*x + c
            expr_abs = d*x + e

            # Bước 3: Giải chi tiết để tìm số nghiệm thực tế
            # Điều kiện xác định: expr_sqrt >= 0 (Sẽ được kiểm tra khi thay vào pt gốc)

            # Trường hợp 1: dx + e >= 0 <=> x >= -e/d
            cond1_val = Rational(-e, d)
            # PT: sqrt(expr_sqrt) - (dx + e) = f  => sqrt(expr_sqrt) = dx + e + f
            rhs1 = d*x + e + f
            # Bình phương: expr_sqrt = rhs1^2
            eq1 = sp.Eq(expr_sqrt, rhs1**2)
            sol1_raw = solve(eq1, x)
            sol1_final = []
            for s in sol1_raw:
                # Kiểm tra điều kiện: x >= cond1_val VÀ vế phải sau khi chuyển vế >= 0
                if s >= cond1_val and (d*s + e + f) >= 0:
                    # Thay lại vào pt gốc để kiểm tra tính đúng đắn (loại nghiệm ngoại lai do bình phương)
                    val_sqrt = expr_sqrt.subs(x, s)
                    if val_sqrt >= 0 and sp.simplify(sqrt(val_sqrt) - abs(d*s + e) - f) == 0:
                        sol1_final.append(s)

            # Trường hợp 2: dx + e < 0 <=> x < -e/d
            # PT: sqrt(expr_sqrt) - (-(dx + e)) = f => sqrt(expr_sqrt) = f - (dx + e)
            rhs2 = f - (d*x + e)
            eq2 = sp.Eq(expr_sqrt, rhs2**2)
            sol2_raw = solve(eq2, x)
            sol2_final = []
            for s in sol2_raw:
                if s < cond1_val and (f - (d*s + e)) >= 0:
                    val_sqrt = expr_sqrt.subs(x, s)
                    if val_sqrt >= 0 and sp.simplify(sqrt(val_sqrt) - abs(d*s + e) - f) == 0:
                        sol2_final.append(s)

            # Tổng hợp nghiệm
            all_solutions = sol1_final + sol2_final
            so_nghiem = len(all_solutions)

            # Bước 4: Tạo các phương án trắc nghiệm (không trùng đáp án đúng)
            da_dung = '$' + str(so_nghiem) + '$'
            cac_lua_chon_sai = []
            possible_wrong = [0, 1, 2, 3, 4]
            if so_nghiem in possible_wrong:
                possible_wrong.remove(so_nghiem)
            random.shuffle(possible_wrong)

            da_s1 = '$' + str(possible_wrong[0]) + '$'
            da_s2 = '$' + str(possible_wrong[1]) + '$'
            da_s3 = '$' + str(possible_wrong[2]) + '$'

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình sau: $\\sqrt{%s} - |%s| = %s$. Số nghiệm của phương trình là bao nhiêu?'''
                             % (latex(expr_sqrt), latex(expr_abs), latex(f)))

            # Danh sách đáp án
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            # Lấy các bước trung gian để trình bày
            tp1_pt = sp.Eq(sqrt(expr_sqrt), d*x + e + f)
            tp2_pt = sp.Eq(sqrt(expr_sqrt), -d*x + f - e)

            loigiai = ('''Trường hợp 1: Với $%s \\geq 0$ hay $x \\geq %s$, phương trình đã cho trở thành: \\\\
                         $%s \\Leftrightarrow \\sqrt{%s} = %s$ (1) \\\\
                         Bình phương hai vế của phương trình (1), ta được: \\\\
                         $%s = %s \\Rightarrow %s = 0$ \\\\
                         Tìm được nghiệm và đối chiếu điều kiện $x \\geq %s$, ta nhận các giá trị thỏa mãn. \\\\
                         Trường hợp 2: Với $%s < 0$ hay $x < %s$, phương trình đã cho trở thành: \\\\
                         $\\sqrt{%s} + (%s) = %s \\Leftrightarrow \\sqrt{%s} = %s$ (2) \\\\
                         Bình phương hai vế của phương trình (2), ta được: \\\\
                         $%s = %s \\Rightarrow %s = 0$ \\\\
                         Tìm được nghiệm và đối chiếu điều kiện $x < %s$, ta nhận các giá trị thỏa mãn. \\\\
                         Vậy phương trình đã cho có %s nghiệm.''' 
                         % (latex(expr_abs), latex(cond1_val), 
                            latex(sp.Eq(sqrt(expr_sqrt) - expr_abs, f)), latex(expr_sqrt), latex(rhs1),
                            latex(expr_sqrt), latex(rhs1**2), latex(sp.simplify(expr_sqrt - rhs1**2)), latex(cond1_val),
                            latex(expr_abs), latex(cond1_val),
                            latex(expr_sqrt), latex(expr_abs), latex(f), latex(expr_sqrt), latex(rhs2),
                            latex(expr_sqrt), latex(rhs2**2), latex(sp.simplify(expr_sqrt - rhs2**2)), latex(cond1_val),
                            str(so_nghiem)
                           ))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(so_nghiem))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

