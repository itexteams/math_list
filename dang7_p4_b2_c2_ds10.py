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


def bt_dang7_p4_b2_c2_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo hệ số phóng to/thu nhỏ k và p để thay đổi biên độ M của tham số m
                k = random.randint(1, 3) 
                p = random.randint(5, 15)
                M = 10 * k + p

                # Tọa độ các đỉnh A, B, C, D thay đổi theo hệ số k (Xử lý âm dương trực tiếp trên biến số)
                Ax, Ay = -1 * k, 0
                Bx, By = 5 * k, 0
                Cx, Cy = 2 * k, 3 * k
                Dx, Dy = 0, 2 * k

                # Tính giá trị F(x, y) = -2x + y tại các đỉnh
                FA = -2 * Ax + Ay
                FB = -2 * Bx + By
                FC = -2 * Cx + Cy
                FD = -2 * Dx + Dy

                # Tìm giá trị nhỏ nhất của F
                min_F = min(FA, FB, FC, FD) # min_F luôn đạt tại FB = -10k

                # Số lượng giá trị m nguyên thỏa mãn m <= min_F trong đoạn [-M, M]
                kq_num = min_F - (-M) + 1
                kq = str(kq_num)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = du[0]

                # Tạo các đáp án sai ngẫu nhiên (Cộng trừ thêm các giá trị gần đúng)
                s_nums = [kq_num + 1, kq_num + 2, kq_num - 1, kq_num - 2, kq_num + 3, kq_num - 3]
                s = ['$%s$' % (val) for val in s_nums] # Sửa bỏ latex() nếu chưa import thư viện tương ứng, hoặc giữ nguyên nếu hàm latex đã được định nghĩa

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tìm số các giá trị $m$ nguyên thuộc $[-%s; %s]$ để $m \\le -2x + y$ với mọi cặp số $(x;y)$ thoả mãn hệ bất phương trình sau: 
            $\\begin{cases} -2x + y \\le %s \\\\ -x + 2y \\le %s \\\\ x + y \\le %s \\\\ y \\ge 0 \\end{cases}$.''' 
                % (M, M, 2*k, 4*k, 5*k))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Khởi tạo tỉ lệ scale cho hình vẽ
                scale_val = round(1.2 / k, 2)

                # Xác định các giới hạn của đồ thị để clip và vẽ nền gạch sọc
                xmin, xmax = -2.5 * k, 6.5 * k
                ymin, ymax = -1.5 * k, 5.5 * k

                # Đoạn mã vẽ hình TikZ bằng code, tọa độ co giãn linh hoạt theo phong cách gạch sọc
                khoanh_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=%s, line width=1pt]
                \\clip (%s,%s) rectangle (%s,%s);
                \\fill[pattern=north east lines, pattern color=black] (%s,%s) rectangle (%s,%s);
                \\fill[white] (%s,0) -- (%s,0) -- (%s,%s) -- (0,%s) -- cycle;
                \\draw[black] (%s,%s) -- (%s,%s); %% Đường thẳng y = 2x + 2k (qua AD)
                \\draw[black] (%s,%s) -- (%s,%s); %% Đường thẳng y = 0.5x + 2k (qua DC)
                \\draw[black] (%s,%s) -- (%s,%s); %% Đường thẳng y = -x + 5k (qua CB)
                \\coordinate (A) at (%s,0);
                \\coordinate (B) at (%s,0);
                \\coordinate (C) at (%s,%s);
                \\coordinate (D) at (0,%s);
                \\fill (A) circle (0.5pt) node[above left] {$A(%s;0)$};
                \\fill (B) circle (0.5pt) node[above right] {$B(%s;0)$};
                \\fill (C) circle (0.5pt) node[above right] {$C(%s;%s)$};
                \\fill (D) circle (0.5pt) node[left] {$D(0;%s)$};
                \\draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
                \\draw[->] (%s,0) -- (%s,0) node[below] {$x$};
                \\draw[->] (0,%s) -- (0,%s) node[left] {$y$};
                \\node at (0,0) [below left] {$O$};
            \\end{tikzpicture}
            \\end{center}''' % (
                    scale_val,
                    xmin, ymin, xmax, ymax,                     # Giới hạn Clip
                    xmin, ymin, xmax, ymax,                     # Khu vực fill gạch sọc
                    Ax, Bx, Cx, Cy, Dy,                         # Vùng fill trắng (Tứ giác ABCD)
                    -2.5*k, -3*k, 2.5*k, 7*k,                   # Tọa độ vẽ đường AD (y = 2x + 2k)
                    -2.5*k, 0.75*k, 6.5*k, 5.25*k,              # Tọa độ vẽ đường DC (y = 0.5x + 2k)
                    -1.5*k, 6.5*k, 6.5*k, -1.5*k,               # Tọa độ vẽ đường CB (y = -x + 5k)
                    Ax, Bx, Cx, Cy, Dy,                         # Khai báo coordinate
                    Ax, Bx, Cx, Cy, Dy,                         # Gắn nhãn các điểm
                    Cx, Cx, Cy, Cy,                              # Nét đứt C
                    xmin, xmax, ymin, ymax,                     # Trục Ox, Oy                        
                ))

                # Xây dựng nội dung lời giải, nhúng hình vẽ TikZ
                loigiai = ('''Miền nghiệm của hệ bất phương trình là miền tứ giác $ABCD$ với $A(%s;0), B(%s;0), C(%s;%s), D(0;%s)$.\n''' 
                           % (Ax, Bx, Cx, Cy, Dy))

                loigiai += khoanh_hinh + '\n'

                loigiai += ('''Ở đó $A(%s;0)$ có tọa độ là nghiệm của hệ phương trình $\\begin{cases} -2x + y = %s \\\\ y = 0 \\end{cases}$.\\\\
            Điểm $B(%s;0)$ có tọa độ là nghiệm của hệ phương trình $\\begin{cases} x + y = %s \\\\ y = 0 \\end{cases}$.\\\\
            Điểm $C(%s;%s)$ có tọa độ là nghiệm của hệ phương trình $\\begin{cases} -x + 2y = %s \\\\ x + y = %s \\end{cases}$.\\\\
            Điểm $D(0;%s)$ có tọa độ là nghiệm của hệ phương trình $\\begin{cases} -2x + y = %s \\\\ -x + 2y = %s \\end{cases}$.\\\\
            Đặt $F = -2x + y$. Tính giá trị của $F = -2x + y$ tại các cặp số $(x;y)$ là tọa độ của các đỉnh tứ giác $ABCD$ rồi so sánh:
            \\begin{center}
            \\begin{tabular}{|c|c|c|c|c|}
            \\hline
            Đỉnh & $A(%s;0)$ & $B(%s;0)$ & $C(%s;%s)$ & $D(0;%s)$ \\\\
            \\hline
            $F = -2x + y$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Ta có: $m \\le -2x + y$ với mọi cặp số $(x;y)$ thoả mãn hệ bất phương trình khi và chỉ khi $m \\le \\min F \\Leftrightarrow m \\le %s$.\\\\
            Do $m$ nguyên thuộc $[-%s; %s]$ nên $m \\in \\{-%s; -%s; \\dots ; %s\\}$.\\\\
            Nên có $%s$ giá trị thỏa mãn.''' % (
                    Ax, 2*k,
                    Bx, 5*k,
                    Cx, Cy, 4*k, 5*k,
                    Dy, 2*k, 4*k,
                    Ax, Bx, Cx, Cy, Dy,
                    FA, FB, FC, FD,
                    min_F,
                    M, M, M, M-1, min_F,
                    kq
                ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

