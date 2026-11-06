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


def bt_dang42_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo các ký hiệu toán học
            x, y = symbols('x y')

            # ---------------------------------------------------------
            # BƯỚC 1 & 3: NGHIÊN CỨU VÀ TẠO DỮ LIỆU NGẪU NHIÊN
            # ---------------------------------------------------------
            while True:
                # Random tọa độ 3 điểm A, B, C trong khoảng [-5, 8]
                xA, yA = random.randint(-5, 5), random.randint(-5, 8)
                xB, yB = random.randint(-5, 8), random.randint(-5, 5)
                xC, yC = random.randint(-5, 5), random.randint(-5, 5)

                # Kiểm tra 3 điểm không thẳng hàng (diện tích tam giác != 0)
                S = 0.5 * abs(xA*(yB - yC) + xB*(yC - yA) + xC*(yA - yB))
                if S > 2: # Đảm bảo tam giác không quá dẹt để tọa độ H đẹp

                    # Vectơ BC = (xC - xB; yC - yB)
                    u_BC, v_BC = xC - xB, yC - yB
                    # Vectơ AC = (xC - xA; yC - yA)
                    u_AC, v_AC = xC - xA, yC - yA

                    # Vectơ AH = (x - xA; y - yA)
                    # Vectơ BH = (x - xB; y - yB)

                    # Hệ phương trình trực tâm: AH.BC = 0 và BH.AC = 0
                    eq1 = sp.Eq(u_BC*(x - xA) + v_BC*(y - yA), 0)
                    eq2 = sp.Eq(u_AC*(x - xB) + v_AC*(y - yB), 0)

                    sol = solve((eq1, eq2), (x, y))

                    # Chỉ lấy bài toán nếu tọa độ H là số nguyên hoặc phân số đẹp
                    if sol:
                        xH_val = sol[x]
                        yH_val = sol[y]
                        if isinstance(xH_val, (sp.Integer, sp.Rational)) and xH_val.q < 5 and yH_val.q < 5:
                            break

            # ---------------------------------------------------------
            # BƯỚC 2: VIẾT LẠI LỜI GIẢI CHI TIẾT
            # ---------------------------------------------------------

            # Chuẩn bị các thành phần vectơ để đưa vào lời giải
            vec_AH = (x - xA, y - yA)
            vec_BC = (u_BC, v_BC)
            vec_BH = (x - xB, y - yB)
            vec_AC = (u_AC, v_AC)

            noidungcauhoi = ("Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có $A(%s; %s), B(%s; %s)$ và $C(%s; %s)$. Tọa độ trực tâm $H$ của tam giác là" 
                             % (latex(xA), latex(yA), latex(xB), latex(yB), latex(xC), latex(yC)))

            loigiai = ("Gọi $H(x; y)$ là trực tâm của tam giác $ABC$. \\\\ "
                       "Ta có $\\overrightarrow{AH} = (x %s; y %s), \\overrightarrow{BC} = (%s; %s), \\overrightarrow{BH} = (x %s; y %s), \\overrightarrow{AC} = (%s; %s)$. \\\\ "
                       "Do $H$ là trực tâm nên ta được: \\\\ "
                       "$\\begin{cases} \\overrightarrow{AH} \\cdot \\overrightarrow{BC} = 0 \\\\ \\overrightarrow{BH} \\cdot \\overrightarrow{AC} = 0 \\end{cases} "
                       "\\Leftrightarrow \\begin{cases} (%s) \\cdot (x %s) + (%s) \\cdot (y %s) = 0 \\\\ (%s) \\cdot (x %s) + (%s) \\cdot (y %s) = 0 \\end{cases} "
                       "\\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\ "
                       "Vậy $H(%s; %s)$."
                       % (latex(-xA) if xA <= 0 else "-" + latex(xA), latex(-yA) if yA <= 0 else "-" + latex(yA), 
                          latex(u_BC), latex(v_BC),
                          latex(-xB) if xB <= 0 else "-" + latex(xB), latex(-yB) if yB <= 0 else "-" + latex(yB), 
                          latex(u_AC), latex(v_AC),
                          latex(u_BC), latex(-xA) if xA <= 0 else "-" + latex(xA), latex(v_BC), latex(-yA) if yA <= 0 else "-" + latex(yA),
                          latex(u_AC), latex(-xB) if xB <= 0 else "-" + latex(xB), latex(v_AC), latex(-yB) if yB <= 0 else "-" + latex(yB),
                          latex(xH_val), latex(yH_val), latex(xH_val), latex(yH_val)))

            # ---------------------------------------------------------
            # BƯỚC 4: TẠO PHƯƠNG ÁN SAI KHÔNG TRÙNG ĐÁP ÁN ĐÚNG
            # ---------------------------------------------------------
            da_dung = "$H(%s; %s)$" % (latex(xH_val), latex(yH_val))

            ds_sai = set()
            while len(ds_sai) < 3:
                # Tạo các biến thể sai từ tọa độ đúng
                sai_x = xH_val + random.choice([-2, -1, 1, 2, sp.Rational(1, 2)])
                sai_y = yH_val + random.choice([-2, -1, 1, 2, sp.Rational(1, 2)])
                pa_sai = "$H(%s; %s)$" % (latex(sai_x), latex(sai_y))
                if pa_sai != da_dung:
                    ds_sai.add(pa_sai)

            list_ans = ["\\True " + da_dung] + list(ds_sai)
            random.shuffle(list_ans)

            # ---------------------------------------------------------
            # XUẤT NỘI DUNG (CONTENT)
            # ---------------------------------------------------------
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

