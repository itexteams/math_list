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


def bt_dang6_p3_b1_c4_ds11(self):
            # Khai báo biến
            def round_SA(a): 
                # Kiểm tra nếu a là số nguyên
                if a == int(a):
                    return "", int(a)

                # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                # Xác định cách làm tròn
                if len(integer_part) > 2:
                    number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng đơn vị)."
                elif len(integer_part) == 2 and len(decimal_part) > 1:
                    number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần chục)."
                elif len(decimal_part) <= 2:
                    number = str_a  # Không cần làm tròn thêm
                    cirle = ""
                else:
                    number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần trăm)."

                # Chuyển dấu chấm thành dấu phẩy (nếu có)
                return cirle, str(number).replace('.', ',')

            # ------------------------------------------------------------------------------BÀI TOÁN
            # Sinh ngẫu nhiên các đối số đầu vào một cách hợp lý và tính toán giải bài toán
            # 1. Phân tích đại lượng thay đổi: Cạnh hình vuông ban đầu (a1)
            a1_val = random.randint(2, 12) # Chọn cạnh ban đầu từ 2 đến 12

            # 2. Tư duy ngược và Tính toán
            # Diện tích A1
            A1_val = a1_val**2

            # Cạnh a2 = sqrt((a1/2)^2 + (a1/2)^2) = a1 / sqrt(2)
            # Diện tích A2 = (a1 / sqrt(2))^2 = a1^2 / 2 = A1 / 2
            A2_val = S(A1_val) / 2

            # Diện tích A3 = A2 / 2 = A1 / 4
            A3_val = S(A1_val) / 4

            # Dãy diện tích là CSN lùi vô hạn với u1 = A1 và q = 1/2
            q_val = S(1) / 2

            # Tổng S = u1 / (1 - q) = A1 / (1 - 1/2) = A1 / (1/2) = 2 * A1
            tong_dien_tich_val = 2 * A1_val

            # 3. Viết đề bài (bao gồm hình minh họa TikZ)
            # Hình TikZ chỉ mang tính minh họa, không cần thay đổi theo a1_val
            tikz_code = f"""\\begin{{tikzpicture}}[scale=0.5]
                    \\coordinate (A1) at (0,0);
                    \\coordinate (B1) at (6,0);
                    \\coordinate (C1) at (6,6);
                    \\coordinate (D1) at (0,6);
                    \\draw (A1) -- (B1) -- (C1) -- (D1) -- cycle; % Square 1
                    \\coordinate (A2) at (3,0);
                    \\coordinate (B2) at (6,3);
                    \\coordinate (C2) at (3,6);
                    \\coordinate (D2) at (0,3);
                    \\draw (A2) -- (B2) -- (C2) -- (D2) -- cycle; % Square 2
                    \\coordinate (A3) at (4.5,1.5);
                    \\coordinate (B3) at (4.5,4.5);
                    \\coordinate (C3) at (1.5,4.5);
                    \\coordinate (D3) at (1.5,1.5);
                    \\draw (A3) -- (B3) -- (C3) -- (D3) -- cycle; % Square 3
                \\end{{tikzpicture}}"""

            de_bai = f""" \\immini{{
            Cho hình vuông $S_1$ có cạnh dài ${latex(a1_val)}$ cm. Nối các trung điểm của các cạnh của $S_1$ để tạo thành hình vuông $S_2$. Tiếp tục nối các trung điểm của các cạnh của $S_2$ để tạo thành hình vuông $S_3$, và cứ thế tiếp tục vô hạn các hình vuông. (Xem hình minh họa)
            }}{{{tikz_code}}}"""

            # 4. Viết các ý hỏi và lời giải (theo cấu trúc SA)
            # Tuân thủ quy tắc escaping: \\, {{, }}
            loi_giai_chi_tiet = f"""\\begin{{itemize}}
                \\item \\textbf{{Diện tích hình vuông $S_1$:}}
                Cạnh của $S_1$ là $a_1 = {latex(a1_val)}$ cm.
                Diện tích $A_1 = a_1^2 = ({latex(a1_val)})^2 = {latex(A1_val)}$ cm$^2$.
                \\item \\textbf{{Diện tích hình vuông $S_2$:}}
                Cạnh của $S_2$ (gọi là $a_2$) được tạo thành bằng cách nối các trung điểm của $S_1$.
                Cạnh $a_2$ là cạnh huyền của tam giác vuông cân có cạnh góc vuông bằng $\\dfrac{{a_1}}{{2}} = \\dfrac{{{latex(a1_val)}}}{{2}}$.
                Theo định lý Pitago, cạnh của $S_2$ là:
                $$ a_2 = \\sqrt{{ \\left(\\dfrac{{a_1}}{{2}}\\right)^2 + \\left(\\dfrac{{a_1}}{{2}}\\right)^2 }} = \\sqrt{{ 2 \\cdot \\left(\\dfrac{{a_1}}{{2}}\\right)^2 }} = \\dfrac{{a_1}}{{\\sqrt{{2}}}} $$
                Diện tích $A_2 = a_2^2 = \\left(\\dfrac{{a_1}}{{\\sqrt{{2}}}}\\right)^2 = \\dfrac{{a_1^2}}{{2}} = \\dfrac{{{latex(A1_val)}}}{{2}} = {latex(A2_val)}$ cm$^2$.
                \\item \\textbf{{Diện tích hình vuông $S_3$:}}
                Tương tự, $A_3 = \\dfrac{{A_2}}{{2}} = \\dfrac{{{latex(A1_val)}}}{{4}} = {latex(A3_val)}$ cm$^2$.
                \\item \\textbf{{Tính tổng diện tích:}}
                Các diện tích của các hình vuông $S_1, S_2, S_3, \\dots$ tạo thành một cấp số nhân (CSN) lùi vô hạn:
                $$ {latex(A1_val)}, {latex(A2_val)}, {latex(A3_val)}, \\dots $$
                Đây là CSN lùi vô hạn với:
                \\begin{{itemize}}
                    \\item Số hạng đầu $u_1 = A_1 = {latex(A1_val)}$.
                    \\item Công bội $q = \\dfrac{{A_2}}{{A_1}} = \\dfrac{{{latex(A2_val)}}}{{{latex(A1_val)}}} = {latex(q_val)}$.
                \\end{{itemize}}
                Vì $\\left|q\\right| = \\left|{latex(q_val)}\\right| < 1$, nên tổng $S_A$ của CSN lùi vô hạn này là:
                \\allowdisplaybreaks
                \\begin{{eqnarray*}}
                    S_A &=& \\dfrac{{u_1}}{{1 - q}} \\\\
                    S_A &=& \\dfrac{{{latex(A1_val)}}}{{1 - {latex(q_val)}}} \\\\
                    S_A &=& \\dfrac{{{latex(A1_val)}}}{{\\dfrac{{1}}{{2}}}} \\\\
                    S_A &=& {latex(tong_dien_tich_val)}
                \\end{{eqnarray*}}
                Vậy, tổng diện tích của tất cả các hình vuông được tạo thành là ${latex(tong_dien_tich_val)}$ cm$^2$.
            \\end{{itemize}} """

            ds_abcd = [
                (f"""Tính tổng diện tích của tất cả các hình vuông được tạo thành (đơn vị cm$^2$).""",
                 loi_giai_chi_tiet,
                 tong_dien_tich_val # Đáp án là một số nguyên nên không cần dùng round
                )
            ]

            # ########### CODE BÊN DƯỚI GIỮ NGUYÊN ====================
            hoi, loigiai, ket_qua = random.choice(ds_abcd)
            #Đáp án
            dapan='\n\\begin{flushright} \\shortans[0]{$%s$} \\end{flushright} \n'%(round_SA(ket_qua)[1])              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(de_bai) + str(hoi) +str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content 

