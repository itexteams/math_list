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


def bt_dang47_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các số liệu trong bài toán
                while True:
                    N = random.choice([80, 90, 100, 110, 120])
                    S = random.choice([300, 400, 500])
                    p = random.choice([2, 3, 4])
                    E = random.choice([700, 800, 900])
                    C = random.choice([5000, 6000, 8000, 10000])
                    R = random.choice([30000, 40000, 50000])

                    S100 = S // 100
                    a = S100 * p
                    # Đảm bảo nghiệm k_opt không phải là số nguyên để xuất hiện việc so sánh 2 giá trị
                    if E % (2 * a) != 0:
                        k_opt = E / (2 * a)
                        # Giới hạn số người tăng ca ở mức thực tế (>10 và <N-10)
                        if 10 < k_opt < N - 10:
                            break

                # Tính toán các hệ số
                k_frac = Rational(E, 2*a)
                k_exact_latex = latex(k_frac) + " \\notin \\mathbb{N}"

                k1 = int(k_opt)
                k2 = k1 + 1

                # Hàm tính lợi nhuận để so sánh
                def T_val(k):
                    return R + E*k - (S*k + a*(k**2)) - C - S*(N - k)

                T1 = T_val(k1)
                T2 = T_val(k2)
                T_const = R - C - S * N

                if T1 > T2:
                    k_max = k1
                    k_min = k2
                else:
                    k_max = k2
                    k_min = k1

                ans = N - k_max

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (ans)]
                da = random.choice(du)

                # Khởi tạo phương án nhiễu đảm bảo không trùng lặp
                s_set = set()
                s_set.add(k_max)         # Nhiễu 1: Nhầm lấy số người tăng ca
                s_set.add(N - k1)        # Nhiễu 2: Lấy số người không tăng ca tại k1 (nếu k2 là max)
                s_set.add(N - k2)        # Nhiễu 3: Lấy số người không tăng ca tại k2 (nếu k1 là max)
                s_set.add(ans + 1)
                s_set.add(ans - 1)
                s_set.add(ans + 2)
                s_set.add(ans - 2)

                if ans in s_set:
                    s_set.remove(ans)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = '$%s$' % (s_list[0])
                das2 = '$%s$' % (s_list[1])
                das3 = '$%s$' % (s_list[2])

                # Câu hỏi
                noidungcauhoi = ('''Một nhà hàng có tổng cộng $%s$ nhân viên và chi trả mức lương cố định cho mỗi nhân viên thường xuyên tăng ca là $%s$ USD/tháng. Vì nhà hàng liên tục đón những đoàn khách với số lượng lớn nhưng không thể thuê thêm nhân viên nên chủ nhà hàng muốn khuyến khích nhân viên của mình tăng ca. Ông chủ quyết định cứ một nhân viên quyết định tăng ca thì mức lương của tất cả nhân viên tăng ca trong nhà hàng đều được tăng thêm $%s$\\%%. Tương tự nếu $k$ nhân viên tăng ca thì lương cho mỗi người trong số $k$ người đó sẽ tăng $%sk$(\\%%). Bên cạnh tiền lương cho nhân viên thì tiền điện nước và duy trì cơ sở vật chất là cố định $%s$ USD/tháng. Doanh thu trung bình từ khách hàng là $%s$ USD/tháng và mỗi nhân viên tăng ca trung bình sẽ được khách hàng tip $%s$ USD/tháng (tiền tip phải nộp lại cho chủ cửa hàng và tính vào doanh thu). Xác định số nhân viên còn lại không tăng ca cần có để lợi nhuận của nhà hàng đạt giá trị lớn nhất?'''
                                 % (latex(N), latex(S), latex(p), latex(p), latex(C), latex(R), latex(E)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Xét với $k$ là số nhân viên tăng ca thì lương mỗi nhân viên sau tăng ca là: $%s(1 + %sk)$ USD.\\\\
                Tổng lương cho $k$ nhân viên là: $%sk(1 + %sk) = %sk(100 + %sk)$.\\\\
                Với $%s - k$ nhân viên còn lại thì mức lương vẫn $%s$ USD nên tổng sẽ là: $%s(%s - k)$ USD.\\\\
                Cứ $k$ nhân viên tăng ca doanh thu tăng $%sk$ USD nên doanh thu tổng là: $%s + %sk$ USD.\\\\
                Suy ra lợi nhuận tổng của nhà hàng là:\\\\
                $T(k) = %s + %sk - %sk(100 + %sk) - %s - %s(%s - k) = %s + %sk - %sk^2$.\\\\
                Xét hàm số $T(k)$, ta có: $T'(k) = %s - %sk$. Giải $T'(k) = 0 \\Leftrightarrow k = %s \\Rightarrow \\left[ \\begin{array}{l} k = %s \\\\ k = %s \\end{array} \\right.$\\\\
                Xét $T(%s) = %s; T(%s) = %s \\rightarrow T(%s) > T(%s) \\Rightarrow T_{\\max} = T(%s)$ tức lợi nhuận max là khi số nhân viên tăng ca là $%s$ tức số nhân viên còn lại không tăng ca là $%s - %s = %s$.'''
                % (
                    latex(S), str(p/100).replace('.', ','),
                    latex(S), str(p/100).replace('.', ','), latex(S100), latex(p),
                    latex(N), latex(S), latex(S), latex(N),
                    latex(E), latex(R), latex(E),
                    latex(R), latex(E), latex(S100), latex(p), latex(C), latex(S), latex(N), latex(T_const), latex(E), latex(a),
                    latex(E), latex(2*a), k_exact_latex, latex(k1), latex(k2),
                    latex(k1), latex(T1), latex(k2), latex(T2), latex(k_max), latex(k_min), latex(k_max), latex(k_max), latex(N), latex(k_max), latex(ans)
                ))
                dapan='\\shortans[0]{$%s$}\n'%(ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

