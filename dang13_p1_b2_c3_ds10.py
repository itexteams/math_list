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


def bt_dang13_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng người của 3 nhóm
                n1 = random.randint(8, 15)
                n2 = random.randint(12, 20)
                n3 = random.randint(18, 30)

                # Random cân nặng trung bình từng nhóm
                m1 = random.randint(45, 55)
                m2 = random.randint(35, 45)
                m3 = random.randint(38, 50)

                # Tính tổng số người N và tổng khối lượng S
                N = n1 + n2 + n3
                S = n1*m1 + n2*m2 + n3*m3

                # ==========================================
                # XỬ LÝ KẾT QUẢ VÀ TẠO ĐÁP ÁN NHIỄU
                # ==========================================
                tb_exact = Rational(S, N)
                s_vals_str = set()

                # Bẫy phổ biến: Lấy trung bình cộng của 3 số trung bình mà không nhân trọng số
                unweighted = (m1 + m2 + m3) / 3
                if float(unweighted).is_integer():
                    s_vals_str.add(str(int(unweighted)))
                else:
                    s_vals_str.add(str(round(unweighted, 1)).replace('.', ','))

                # Xử lý kết quả đúng (nguyên / thập phân hữu hạn / phân số vô hạn)
                if tb_exact.q == 1:
                    tb_str = str(tb_exact.p)
                    while len(s_vals_str) < 4:
                        s_vals_str.add(str(tb_exact.p + random.randint(-5, 5)))

                elif 100000 % tb_exact.q == 0:  
                    tb_float = S / N
                    tb_str = str(tb_float).replace('.', ',')
                    while len(s_vals_str) < 4:
                        cand = tb_float + random.choice([-2.5, -1.5, -0.5, 0.5, 1.5, 2.5])
                        if cand.is_integer():
                            s_vals_str.add(str(int(cand)))
                        else:
                            s_vals_str.add(str(round(cand, 2)).replace('.', ','))

                else:
                    tb_str = f"\\frac{{{tb_exact.p}}}{{{tb_exact.q}}}"
                    while len(s_vals_str) < 4:
                        p_new = tb_exact.p + random.choice([-2, -1, 1, 2, 3]) * tb_exact.q
                        s_vals_str.add(f"\\frac{{{p_new}}}{{{tb_exact.q}}}")

                # Đảm bảo danh sách nhiễu không trùng đáp án đúng
                if tb_str in s_vals_str:
                    s_vals_str.remove(tb_str)

                # Lấy chính xác 3 đáp án nhiễu
                s_vals_list = list(s_vals_str)[:3]

                da = f"${tb_str}$ kg"
                s = [f"${val}$ kg" for val in s_vals_list]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = f"Ba nhóm học sinh gồm ${n1}$ người, ${n2}$ người, ${n3}$ người. Cân nặng trung bình của mỗi nhóm lần lượt là ${m1}$ kg, ${m2}$ kg, ${m3}$ kg. Khối lượng trung bình của ba nhóm học sinh đó là"

                # Gán đáp án vào danh sách
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = f"Khối lượng trung bình của ba nhóm học sinh là\\\\ \n$$ \\frac{{1}}{{{n1} + {n2} + {n3}}} \\cdot ({n1} \\cdot {m1} + {n2} \\cdot {m2} + {n3} \\cdot {m3}) = {tb_str} \\text{{ kg}}. $$"

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

