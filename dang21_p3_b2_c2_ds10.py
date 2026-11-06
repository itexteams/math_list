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


def bt_dang21_p3_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp random để đảm bảo sinh ra miền nghiệm giới hạn và nghiệm tối ưu rơi vào giao điểm có tọa độ nguyên
                while True:
                    # Chọn trước điểm tối ưu nguyên
                    x0 = random.randint(1, 5)
                    y0 = random.randint(1, 5)

                    Xa = random.randint(8, 12)
                    Ya = random.randint(2, 5)
                    Xb = random.randint(3, 7)
                    Yb = random.randint(15, 20)

                    # Ép (x0, y0) là giao điểm của hai đường thẳng đầu tiên (điều kiện >=)
                    A_req = Xa * x0 + Ya * y0
                    B_req = Xb * x0 + Yb * y0

                    Xc = random.randint(12, 18)
                    Yc = random.randint(18, 24)
                    # Đảm bảo đường C_max chặn phía trên tạo thành đa giác kín
                    C_max = Xc * x0 + Yc * y0 + random.randint(20, 50)

                    Cx = random.randint(30, 45)
                    Cy = random.randint(40, 55)

                    M = random.randint(5, 15)

                    # Tính toán tọa độ các đỉnh của đa giác miền nghiệm bằng sympy
                    x_sym, y_sym = sp.symbols('x_sym y_sym')
                    L1 = Xa*x_sym + Ya*y_sym - A_req
                    L2 = Xb*x_sym + Yb*y_sym - B_req
                    L3 = Xc*x_sym + Yc*y_sym - C_max
                    L4 = x_sym
                    L5 = y_sym

                    lines = [L1, L2, L3, L4, L5]
                    vertices = []

                    # Tìm giao điểm của từng cặp đường thẳng
                    for i in range(len(lines)):
                        for j in range(i+1, len(lines)):
                            sol = sp.solve((lines[i], lines[j]), (x_sym, y_sym))
                            if sol and isinstance(sol, dict) and x_sym in sol and y_sym in sol:
                                vx = sol[x_sym]
                                vy = sol[y_sym]

                                # Kiểm tra xem giao điểm có thỏa mãn toàn bộ hệ bất phương trình không
                                try:
                                    c1 = float(Xa*vx + Ya*vy) >= A_req - 1e-5
                                    c2 = float(Xb*vx + Yb*vy) >= B_req - 1e-5
                                    c3 = float(Xc*vx + Yc*vy) <= C_max + 1e-5
                                    c4 = float(vx) >= -1e-5
                                    c5 = float(vy) >= -1e-5

                                    if c1 and c2 and c3 and c4 and c5:
                                        # Loại bỏ các đỉnh trùng lặp
                                        is_dup = False
                                        for (ex_x, ex_y) in vertices:
                                            if abs(float(vx) - float(ex_x)) < 1e-4 and abs(float(vy) - float(ex_y)) < 1e-4:
                                                is_dup = True
                                                break
                                        if not is_dup:
                                            vertices.append((vx, vy))
                                except:
                                    pass

                    # Phải có ít nhất 3 đỉnh tạo thành đa giác và nghiệm nhỏ nhất trùng với x0, y0
                    if len(vertices) >= 3:
                        min_cost = float('inf')
                        best_v = None
                        for vx, vy in vertices:
                            cost = float(Cx*vx + Cy*vy)
                            if cost < min_cost:
                                min_cost = cost
                                best_v = (vx, vy)

                        # Kiểm tra xem đỉnh tối ưu có đúng là điểm nguyên (x0, y0) không
                        if abs(float(best_v[0]) - x0) < 1e-4 and abs(float(best_v[1]) - y0) < 1e-4:
                            min_cost_val = Cx * x0 + Cy * y0
                            break

                kq_int = M * min_cost_val
                kq = str(kq_int)

                # Tạo chuỗi đánh giá từng điểm cho lời giải
                points_eval_str = ""
                for idx, (vx, vy) in enumerate(vertices):
                    vx_sp = sp.simplify(vx)
                    vy_sp = sp.simplify(vy)
                    cost_sp = sp.simplify(Cx*vx_sp + Cy*vy_sp)
                    points_eval_str += ("Điểm $M_{%s}\\left(%s; %s\\right) \\Rightarrow T = %s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right) = %s$. \\\\ \n             " 
                                        % (idx + 1, latex(vx_sp), latex(vy_sp), latex(Cx), latex(vx_sp), latex(Cy), latex(vy_sp), latex(cost_sp)))

                # Tính toán kích thước tự động cho khung hình TikZ
                max_x = int(math.ceil(max([float(v[0]) for v in vertices]))) + 2
                max_y = int(math.ceil(max([float(v[1]) for v in vertices]))) + 2

                # Xây dựng chuỗi TikZ dựa trên mẫu vẽ miền nghiệm
                tikz_str = ('''
            \\begin{center}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=0.6]
            \\draw[->] (-1,0)--(%s,0) node[below]{$x$};
            \\draw[->] (0,-1)--(0,%s) node[left]{$y$};
            \\draw (0,0) node[below left]{$O$};
            \\clip (-1,-1) rectangle (%s,%s);
            \\fill[pattern=north west lines] (-1,-1) rectangle (0,%s);
            \\fill[pattern=north west lines] (-1,-1) rectangle (%s,0);
            \\draw[domain=-1:%s,smooth,variable=\\x] plot (\\x,{(%s - %s*\\x)/%s});
            \\fill[pattern=north west lines] plot[domain=-1:%s](\\x,{(%s - %s*\\x)/%s})--(%s,-1)--(-1,-1)--cycle;
            \\draw[domain=-1:%s,smooth,variable=\\x] plot (\\x,{(%s - %s*\\x)/%s});
            \\fill[pattern=north west lines] plot[domain=-1:%s](\\x,{(%s - %s*\\x)/%s})--(%s,-1)--(-1,-1)--cycle;
            \\draw[domain=-1:%s,smooth,variable=\\x] plot (\\x,{(%s - %s*\\x)/%s});
            \\fill[pattern=north west lines] plot[domain=-1:%s](\\x,{(%s - %s*\\x)/%s})--(%s,%s)--(-1,%s)--cycle;
            \\end{tikzpicture}
            \\end{center}''' % (max_x, max_y, max_x, max_y, max_y, max_x, 
                                max_x, A_req, Xa, Ya, max_x, A_req, Xa, Ya, max_x,
                                max_x, B_req, Xb, Yb, max_x, B_req, Xb, Yb, max_x,
                                max_x, C_max, Xc, Yc, max_x, C_max, Xc, Yc, max_x, max_y+1, max_y+1))

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên, loại bỏ trùng lặp với đáp án đúng
                s_pool = [
                    kq_int + M * 10,
                    kq_int - M * 10,
                    kq_int + M * Cx,
                    kq_int - M * Cy,
                    M * (min_cost_val + 5),
                    M * (min_cost_val - 5)
                ]
                s_pool = list(set([val for val in s_pool if val > 0 and val != kq_int]))

                # Bổ sung nếu thiếu để đủ 3 phương án sai
                while len(s_pool) < 3:
                    s_pool.append(kq_int + random.randint(1, 20) * M)
                    s_pool = list(set(s_pool))

                s = ['$%s$'%(latex(s_pool[0])),
                     '$%s$'%(latex(s_pool[1])),
                     '$%s$'%(latex(s_pool[2]))]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Công ty vận tải nhận một đơn hàng vận chuyển ít nhất $%s$ tấn hàng loại $A$, ít nhất $%s$ tấn hàng loại $B$ và không quá $%s$ tấn hàng loại $C$. Công ty vận tải sử dụng hai loại xe $X$ và $Y$ để chở số hàng đó. Mỗi xe loại $X$ đều chở $%s$ tấn hàng loại $A$, $%s$ tấn hàng loại $B$ và $%s$ tấn hàng loại $C$. Mỗi xe loại $Y$ đều chở $%s$ tấn hàng loại $A$, $%s$ tấn hàng loại $B$ và $%s$ tấn hàng loại $C$. Chi phí cho $1$ xe loại $X$ là $%s$ triệu đồng và cho $1$ xe loại $Y$ là $%s$ triệu đồng. Gọi $T$ (triệu đồng) là chi phí nhỏ nhất để công ty hoàn thành đơn hàng. Giá trị của $%s T$ bằng bao nhiêu?'''
                                 %(latex(A_req), latex(B_req), latex(C_max), 
                                   latex(Xa), latex(Xb), latex(Xc), 
                                   latex(Ya), latex(Yb), latex(Yc), 
                                   latex(Cx), latex(Cy), latex(M)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi $x, y$ lần lượt là số xe loại $X$ và loại $Y$ được công ty sử dụng ($x \\ge 0, y \\ge 0$). \\\\
                         Tổng số hàng loại $A$ chở được là: $%s x + %s y$ (tấn). \\\\
                         Tổng số hàng loại $B$ chở được là: $%s x + %s y$ (tấn). \\\\
                         Tổng số hàng loại $C$ chở được là: $%s x + %s y$ (tấn). \\\\
                         Theo đề bài, ta có hệ bất phương trình: \\\\
                         $$ \\begin{cases} %s x + %s y \\ge %s \\\\ %s x + %s y \\ge %s \\\\ %s x + %s y \\le %s \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases} $$
                         Tổng chi phí vận chuyển là: $T(x, y) = %s x + %s y$ (triệu đồng). \\\\
                         Biểu diễn miền đa giác nghiệm của hệ bất phương trình trên mặt phẳng tọa độ (phần không bị gạch):
                         %s
                         Tọa độ các đỉnh của đa giác miền nghiệm là giao điểm của các đường thẳng giới hạn miền nghiệm. Thay tọa độ các đỉnh này vào biểu thức $T(x, y)$, ta có: \\\\
                         %s
                         Từ các kết quả trên, ta thấy chi phí nhỏ nhất là $T = %s$ (triệu đồng) đạt được tại $x = %s$ và $y = %s$ (thỏa mãn điều kiện thực tế $x, y \\in \\mathbb{N}$). \\\\
                         Vậy giá trị cần tìm là $%s T = %s \\cdot %s = %s$.'''
                         %(latex(Xa), latex(Ya), 
                           latex(Xb), latex(Yb), 
                           latex(Xc), latex(Yc),
                           latex(Xa), latex(Ya), latex(A_req),
                           latex(Xb), latex(Yb), latex(B_req),
                           latex(Xc), latex(Yc), latex(C_max),
                           latex(Cx), latex(Cy),
                           tikz_str,
                           points_eval_str,
                           latex(min_cost_val), latex(x0), latex(y0),
                           latex(M), latex(M), latex(min_cost_val), latex(kq_int)
                         ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_int))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' + dapan +
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

