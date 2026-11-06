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


def bt_dang57_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Hàm định dạng số hiển thị dấu phẩy cho số thập phân
            def fmt(num):
                if isinstance(num, (int, float)):
                    if int(num) == num:
                        return str(int(num))
                    return str(num).replace('.', ',')
                return str(num).replace('.', ',')

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Lặp để tìm bộ số ngẫu nhiên hợp lý
                while True:
                    p1 = random.randint(10, 15)      # Giá bán năm đầu tiên
                    b = random.randint(1, 4)         # Hệ số bậc 1 của chi phí
                    c = random.randint(4, 10)        # Chi phí cố định
                    k = random.randint(4, 7)         # Số năm để hoàn vốn (kết quả bài toán)

                    p1_minus_1 = p1 - 1
                    M = p1_minus_1 - b               # Tham số gom cho gọn biểu thức: M = p1 - 1 - b

                    # Đảm bảo lợi nhuận năm đầu phải > 0 và số lượng sản xuất x > 0
                    P1 = 0.5 * (1 + M)**2 - c
                    if P1 > 0 and M > 0:
                        break

                # Tính lợi nhuận từng năm và tổng chi phí đầu tư ban đầu C0
                sum_profit = 0
                sum_str_list = []
                year_profits_str_percent = ""
                for i in range(1, k+1):
                    Pi = 0.5 * (i + M)**2 - c
                    sum_profit += Pi
                    sum_str_list.append(fmt(Pi))
                    year_profits_str_percent += "Năm %s: $P_{%s} = 0,5(%s + %s)^2 - %s = %s$. \\\\    " % (i, i, i, M, c, fmt(Pi))

                C0 = sum_profit
                sum_str = " + ".join(sum_str_list)

                kq = str(k)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da= random.choice(du)

                # Tạo các phương án nhiễu sai khác với đáp án đúng
                s_list = [k-2, k-1, k+1, k+2, k+3]
                s = []
                for val in s_list:
                    if val > 0:
                        s.append('$%s$'%(val))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một công ty xây dựng một nhà máy mới có chi phí $%s$ tỷ đồng. Chi phí sản xuất $x$ nghìn sản phẩm mỗi năm tại nhà máy này là $0,5x^2 + %sx + %s$ tỷ đồng. Khi nhà máy đã được xây dựng, công ty sẽ sản xuất sản phẩm ở số lượng sao cho lợi nhuận lớn nhất. Giá bán sản phẩm trong năm đầu là $%s$ triệu đồng, và mỗi năm tiếp theo, giá tăng thêm $1$ triệu đồng so với năm ngay trước đó. Hỏi sau bao nhiêu năm việc xây dựng nhà máy mới, công ty sẽ hoàn vốn?'''
                                 %(fmt(C0), fmt(b), fmt(c), fmt(p1)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $n$ là năm thứ $n$ kể từ khi nhà máy bắt đầu hoạt động ($n \\in \\mathbb{N}^*$). \\\\
                Giá bán sản phẩm trong năm thứ $n$ là $p_n = %s + (n-1) \\cdot 1 = n + %s$ (triệu đồng/sản phẩm) $= n + %s$ (tỷ đồng/nghìn sản phẩm). \\\\
                Doanh thu khi bán $x$ nghìn sản phẩm trong năm thứ $n$ là: $R_n(x) = (n + %s)x$ (tỷ đồng). \\\\
                Lợi nhuận công ty thu được trong năm thứ $n$ là: \\\\
                $L_n(x) = R_n(x) - C(x) = (n + %s)x - (0,5x^2 + %sx + %s) = -0,5x^2 + (n + %s)x - %s$. \\\\
                Xét hàm số $L_n(x) = -0,5x^2 + (n + %s)x - %s$ với $x > 0$. \\\\
                Ta có đạo hàm: $L_n'(x) = -x + n + %s$. \\\\
                Cho $L_n'(x) = 0 \\Leftrightarrow x = n + %s$. \\\\
                Bảng biến thiên:
                \\begin{center}
                \\begin{tikzpicture}
                \\tkzTabInit[lgt=2,espcl=3,deltacl=0.5]{$x$ / 1, $L_n'(x)$ / 1, $L_n(x)$ / 2}{$0$, $n+%s$, $+\\infty$}
                \\tkzTabLine{,+,0,-,}
                \\tkzTabVar{-/ $-%s$, +/ $P_{\\max}$, -/ $-\\infty$}
                \\end{tikzpicture}
                \\end{center}
                Từ bảng biến thiên, lợi nhuận lớn nhất đạt được khi sản xuất $x = n + %s$ (nghìn sản phẩm). \\\\
                Khi đó, lợi nhuận tối đa trong năm thứ $n$ là: \\\\
                $P_n = L_n(n + %s) = -0,5(n + %s)^2 + (n + %s)(n + %s) - %s = 0,5(n + %s)^2 - %s$. \\\\
                Tổng lợi nhuận sau $k$ năm là $S_k = P_1 + P_2 + \\dots + P_k$. \\\\
                Ta tính mức lợi nhuận lớn nhất đạt được từng năm: \\\\
                %s
                Tổng lợi nhuận sau $%s$ năm hoạt động là: $S_{%s} = %s = %s$ (tỷ đồng). \\\\
                Vì chi phí xây dựng nhà máy là $%s$ tỷ đồng, nên tổng lợi nhuận sau $%s$ năm thu được vừa đủ để bù đắp chi phí đầu tư ban đầu. \\\\
                Vậy công ty sẽ hoàn vốn sau đúng $%s$ năm.'''
                % (fmt(p1), fmt(p1_minus_1), fmt(p1_minus_1),
                   fmt(p1_minus_1),
                   fmt(p1_minus_1), fmt(b), fmt(c), fmt(M), fmt(c),
                   fmt(M), fmt(c),
                   fmt(M),
                   fmt(M),
                   fmt(M),
                   fmt(c),
                   fmt(M),
                   fmt(M), fmt(M), fmt(M), fmt(M), fmt(c), fmt(M), fmt(c),
                   year_profits_str_percent, fmt(k), fmt(k), sum_str, fmt(sum_profit),
                   fmt(C0), fmt(k), fmt(k)))
                dapan='\\shortans[0]{$%s$}\n'%(fmt(k))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

