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


def bt_dang33_p3_b2_c1_ds12(self):
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
            x = symbols('x') # là chiều dài AD
            dien_tich = 100 * random.randint(3, 9) # m^2
            gia_moi_met = random.randint(60, 80) if dien_tich < 700 else  random.randint(40, 60) # nghìn VND/m
            so_hinh_chu_nhat_chia = random.randint(2, 5)

            ham_chieu_dai_rao = 2 * x + dien_tich * (so_hinh_chu_nhat_chia + 1) / x
            diff_ham_chieu_dai_rao = diff(ham_chieu_dai_rao, x)
            sol = solve(diff_ham_chieu_dai_rao, x)
            chieu_dai_toi_uu = max(sol)
            pham_vi_chieu_dai = random.randint(int(chieu_dai_toi_uu) - 2, int(chieu_dai_toi_uu) + 10)

            ham_chi_phi = gia_moi_met * ham_chieu_dai_rao
            chi_phi_toi_uu = ham_chi_phi.subs(x, min(chieu_dai_toi_uu, pham_vi_chieu_dai))

            ket_qua = chi_phi_toi_uu

            # 3. Mã TikZ để vẽ hình minh họa
            tikz_code = f"""  \\begin{{tikzpicture}}[scale=0.9,line width=1pt,line cap=round,line join=round,font=\\footnotesize]
              \\def\\x{{6}} % Length AD (horizontal)
              \\def\\y{{4}} % Width AB (vertical, dien_tich/x)
              \\def\\n{{{so_hinh_chu_nhat_chia}}} % Number of small rectangles (so_hinh_chu_nhat_chia)
              \\draw[thick] (0,0) coordinate (A) -- (0,\\y) coordinate (B) -- (\\x,\\y) coordinate (C) -- (\\x,0) coordinate (D) -- cycle;
              \\node[below left] at (A) {{$A$}};
              \\node[above left] at (B) {{$B$}};
              \\node[above right] at (C) {{$C$}};
              \\node[below right] at (D) {{$D$}};
              \\foreach \\i in {{1,...,\\the\\numexpr\\n-1\\relax}} {{
                \\draw[dashed] ({{\\x*\\i/\\n}},0) -- ({{\\x*\\i/\\n}},\\y);  }}
                \\end{{tikzpicture}}  """

            noidungcauhoi = f"""\\immini{{  Người ta cần rào một mảnh đất hình chữ nhật $ABCD $ có diện tích là ${dien_tich}$ m². 
                        Trên mảnh đất này, người ta chia làm ${so_hinh_chu_nhat_chia}$ miếng đất hình chữ nhật có diện tích bằng nhau 
                        bằng cách sử dụng ${so_hinh_chu_nhat_chia - 1}$ hàng rào ngăn cách song song với cạnh rộng $AB$. 
                        Giá tiền để xây dựng hàng rào bên trong và bao bên ngoài là ${gia_moi_met}$ nghìn đồng mỗi mét, 
                        biết rằng chiều dài $AD$ của hình chữ nhật $ABCD$ không vượt quá ${pham_vi_chieu_dai} $ m. 
                        Chi phí thấp nhất để xây dựng hàng rào là bao nhiêu nghìn đồng? {round_SA(chi_phi_toi_uu)[0]}
            }}{{{tikz_code}}}"""
            loigiai = f"""  Gọi chiều dài của mảnh đất là $x$ (mét) thì chiều rộng là $\\frac{{{dien_tich}}}{{x}}$ m, với $0 < x \\le {pham_vi_chieu_dai}$. \\\\
                         Mảnh đất được chia thành ${so_hinh_chu_nhat_chia}$ phần bằng nhau bởi ${so_hinh_chu_nhat_chia - 1} $ hàng rào song song với cạnh rộng, nên tổng chiều dài hàng rào là: $L(x) = 2x + {so_hinh_chu_nhat_chia + 1} \\cdot \\dfrac{{{dien_tich}}}{{x}} = {latex(ham_chieu_dai_rao)}$.\\\\
                         Đạo hàm $L'(x) = {latex(diff(ham_chieu_dai_rao, x))}$.\\\\
                         Giải phương trình $L'(x) = 0$ ta được nghiệm $x = {latex(nsimplify(chieu_dai_toi_uu))}$.\\\\
                         Vì $ x = {latex(nsimplify(chieu_dai_toi_uu))}$ {'không' if chieu_dai_toi_uu > pham_vi_chieu_dai else ''} thoả điều kiện $0 < x \\le {pham_vi_chieu_dai}$ nên để chi phí làm hàng rào thấp nhất thì chiều dài hình chữ nhật phải là ${latex(min(chieu_dai_toi_uu, pham_vi_chieu_dai))}$.\\\\
                         Khi đó chi phí tối ưu là ${gia_moi_met} \\times L\\left({latex(min(chieu_dai_toi_uu, pham_vi_chieu_dai))}\\right) = {latex(ket_qua)} {'' if len(str(ket_qua)) < 5 else f'\\approx {round_SA(ket_qua)[1]}'} $. """
            #Đáp án
            dapan='\\shortans[0]{$%s$} '%(round_SA(ket_qua)[1])              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content

